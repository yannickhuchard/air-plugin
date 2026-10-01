"""Build the AIR skills plugin without copying a checkout, runtime or credentials."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
# Explicit inventory: untracked notes, credentials and future files are never swept in.
TEXT_FILES = (
    '.codex-plugin/plugin.json', 'plugin.json', 'README.md', 'LICENSE', 'NOTICE',
    'skills/air-local-setup/SKILL.md',
    'skills/air-local-setup/references/connection.md',
    'skills/air-local-design/SKILL.md',
)
BINARY_FILES = ('assets/logo.png',)
FILES = TEXT_FILES + BINARY_FILES


def build(source: Path, output: Path, variant: str = 'mcp') -> dict:
    source = source.resolve()
    if variant not in ('mcp', 'cli'):
        raise ValueError('Unknown variant')
    files = FILES + (('skills/air-local-design/scripts/air_cli.py',) if variant == 'cli' else ())
    payloads = {}
    for name in files:
        path = source / name
        if path.is_symlink() or not path.resolve().is_relative_to(source):
            raise ValueError('Plugin source must not contain redirected files')
        # Only text is normalized: PNG bytes must survive packaging unchanged.
        payloads[name] = (path.read_text(encoding='utf-8').replace('\r\n', '\n').encode('utf-8')
                          if name not in BINARY_FILES else path.read_bytes())
        if name in BINARY_FILES and (not payloads[name].startswith(b'\x89PNG\r\n\x1a\n')
                                    or len(payloads[name]) > 5 * 1024 * 1024):
            raise ValueError('Plugin branding requires a PNG up to 5 MiB')
    portable = json.loads(payloads['plugin.json'])
    compat = json.loads(payloads['.codex-plugin/plugin.json'])
    for key in ('name', 'version', 'description', 'author', 'homepage', 'repository', 'keywords', 'license'):
        if portable[key] != compat[key]:
            raise ValueError('Plugin manifests disagree: ' + key)
    if portable['name'] != 'air-local' or not re.fullmatch(r'\d+\.\d+\.\d+', portable['version']):
        raise ValueError('Unexpected plugin identity or version')
    if portable['author']['name'] != 'Yannick Huchard' or compat['interface']['developerName'] != 'Yannick Huchard':
        raise ValueError('Official developer metadata is inconsistent')
    if portable['license'] != 'Apache-2.0' or b'END OF TERMS AND CONDITIONS' not in payloads['LICENSE']:
        raise ValueError('Plugin license assignment or license text is missing')
    for field in ('logo', 'composerIcon'):
        if compat['interface'].get(field) != './assets/logo.png':
            raise ValueError('Plugin branding must reference its packaged logo')
    # This distribution is deliberately project-bound, not a global MCP connection.
    if any(k in manifest for manifest in (compat, portable) for k in ('mcpServers', 'apps')):
        raise ValueError('AIR Local must use the project connection')
    if variant == 'cli' and any(p.name in ('mcp.json', '.mcp.json') for p in source.rglob('*')):
        raise ValueError('CLI variant cannot contain MCP configuration')
    if variant == 'cli':
        interface = compat['interface']
        overlay = portable.get('extensions', {}).get('com.openai', {})
        if overlay.get('interface') != interface:
            raise ValueError('CLI listing metadata must agree across package formats')
        for field, limit in (('displayName', 30), ('shortDescription', 30), ('longDescription', 4000)):
            value = interface.get(field)
            if not isinstance(value, str) or not value.strip() or len(value) > limit:
                raise ValueError('Public listing field invalid: ' + field)
    output = output.resolve()
    if output == source or output.is_relative_to(source):
        raise ValueError('Write artifacts outside the plugin source')
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"air-local-{portable['version']}{'-cli' if variant == 'cli' else ''}.zip"
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_STORED) as bundle:
        for name, content in sorted(payloads.items()):
            info = zipfile.ZipInfo('air-local/' + name, (2020, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, content)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    report = {'schema': 'air.plugin-package/1', 'name': portable['name'],
              'version': portable['version'], 'developer': portable['author']['name'], 'license': portable['license'],
              'archive': archive.name, 'sha256': digest,
              'files': {name: hashlib.sha256(data).hexdigest() for name, data in sorted(payloads.items())}}
    (output / 'plugin-package.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'dist' / 'plugin')
    parser.add_argument('--variant', choices=('mcp', 'cli'), default='mcp')
    args = parser.parse_args()
    source = ROOT / ('variants/air-local-cli' if args.variant == 'cli' else 'plugins/air-local')
    print(json.dumps(build(source, args.output_dir, args.variant), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
