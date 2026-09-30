"""Build an explicit, credential-free video delivery kit after verification."""
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/"dist"/"videos"/"20260930"
OUT.mkdir(parents=True,exist_ok=True)
validation=json.loads((ROOT/"validation.json").read_text(encoding="utf-8"))
assert len(validation["videos"])==2
assert all(v["visual_review"]=="PASS_CHAPTER_FRAMES" for v in validation["videos"])
inputs=[(ROOT/p,f"videos/{p}") for p in ("README.md","video-content.json","prepare_audio.py","build_videos.py","verify_videos.py","package_videos.py","validation.json")]
for filename in ("LICENSE","NOTICE"):
    inputs.append((ROOT.parent/filename,filename))
for item in validation["videos"]:
    name=f"air-{item['name']}-fr"
    project=ROOT/name
    video=project/"renders"/item["file"]
    assert hashlib.sha256(video.read_bytes()).hexdigest()==item["sha256"]
    shutil.copy2(video,OUT/f"{name}-20260930.mp4")
    for filename in ("BRIEF.md","SCRIPT.md","STORYBOARD.md","design.md","index.html","hyperframes.json","package.json","meta.json","audio-meta.json","asset-provenance.json","chapters.json","check.json","subtitles.fr.srt","subtitles.fr.vtt"):
        inputs.append((project/filename,f"videos/{name}/{filename}"))
    for folder in ("assets","compositions"):
        for path in sorted((project/folder).rglob('*')):
            if path.is_file() and path.suffix in {".html",".json",".png",".txt",".wav",".sha256"}:
                inputs.append((path,f"videos/{name}/{path.relative_to(project).as_posix()}"))
    inputs.append((video,f"videos/{name}/renders/{video.name}"))
    inputs.append((project/"renders/verified-contact-sheet.jpg",f"videos/{name}/renders/verified-contact-sheet.jpg"))
manifest={"schema":"air.video-kit/1","date":"2026-09-30","scope":"French editorial presentation and local narrated capture montage, not public ChatGPT acceptance","files":[{"path":name,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()} for path,name in inputs]}
archive=OUT/"air-videos-kit-20260930.zip"
with zipfile.ZipFile(archive,"w",zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for path,name in inputs: z.write(path,name)
    z.writestr("manifest.json",json.dumps(manifest,ensure_ascii=False,indent=2))
shutil.copy2(ROOT/"validation.json",OUT/"videos-validation-20260930.json")
assets=[p for p in sorted(OUT.iterdir()) if p.suffix in {".mp4",".zip",".json"}]
(OUT/"SHA256SUMS.txt").write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.name+"\n" for p in assets),encoding="utf-8")
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for f in manifest["files"]:
        assert hashlib.sha256(z.read(f["path"])).hexdigest()==f["sha256"]
print(json.dumps({"files":len(inputs),"artifacts":[{"file":p.name,"bytes":p.stat().st_size} for p in assets]},indent=2))
