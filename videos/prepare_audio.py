"""Generate local Kokoro narration with measured per-paragraph timings."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
CONTENT = json.loads((ROOT / "video-content.json").read_text(encoding="utf-8"))

def generate(job):
    project, scene, index, text = job
    assets = project / "assets"
    assets.mkdir(exist_ok=True)
    stem = f"{scene['id']}-{index:02}"
    script = assets / (stem + ".txt")
    wav = assets / (stem + ".wav")
    script.write_text(text, encoding="utf-8")
    digest = hashlib.sha256(text.encode()).hexdigest()
    marker = assets / (stem + ".sha256")
    if not wav.exists() or not marker.exists() or marker.read_text() != digest:
        result = subprocess.run(["npx.cmd", "--yes", "hyperframes@0.8.95", "tts", str(script),
            "--voice", "ff_siwis", "--lang", "fr-fr", "--speed", "0.85", "-o", str(wav)],
            capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode:
            raise RuntimeError(f"TTS failed {stem}: {result.stderr} {result.stdout}")
        marker.write_text(digest)
    duration = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=nw=1:nk=1", str(wav)], text=True).strip())
    print(f"{stem}: {duration:.2f}s", flush=True)
    return {"scene":scene["id"], "paragraph":index, "text":text,
            "path":f"assets/{stem}.wav", "duration":duration, "script_sha256":digest}

if __name__ == "__main__":
    for name, scenes in CONTENT.items():
        project = ROOT / f"air-{name}-fr"
        jobs = [(project, scene, i, text) for scene in scenes for i,text in enumerate(scene["lines"])]
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(generate, jobs))
        (project / "audio-meta.json").write_text(json.dumps({"provider":"local Kokoro",
            "voice":"ff_siwis", "speed":0.85, "paragraphs":results}, ensure_ascii=False, indent=2), encoding="utf-8")
