"""Verify finished exports and create one contact sheet per encoded video.

Requires ffmpeg/ffprobe and Pillow, only for authoring videos (not AIR runtime).
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from PIL import Image, ImageDraw, ImageOps

ROOT=Path(__file__).resolve().parent
results=[]
for name in (sys.argv[1:] or ("presentation", "parcours-local")):
    project=ROOT/f"air-{name}-fr"
    video=project/"renders"/f"air-{name}-fr.mp4"
    meta=json.loads((project/"chapters.json").read_text(encoding="utf-8"))
    probe=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_format","-show_streams","-of","json",str(video)],text=True))
    vs=next(s for s in probe["streams"] if s["codec_type"]=="video")
    aus=next(s for s in probe["streams"] if s["codec_type"]=="audio")
    duration=float(probe["format"]["duration"])
    assert abs(duration-meta["duration"])<0.15,(duration,meta["duration"])
    assert (vs["width"],vs["height"])==(1920,1080)
    assert vs["codec_name"]=="h264" and aus["codec_name"]=="aac"
    assert video.stat().st_size>100000
    decode=subprocess.run(["ffmpeg","-v","error","-i",str(video),"-f","null","-"],capture_output=True,text=True)
    assert decode.returncode==0 and not decode.stderr.strip(),decode.stderr
    volume=subprocess.run(["ffmpeg","-hide_banner","-i",str(video),"-vn","-af","volumedetect","-f","null","-"],capture_output=True,text=True).stderr
    mean=float(re.search(r'mean_volume: ([\d.-]+)',volume)[1]); peak=float(re.search(r'max_volume: ([\d.-]+)',volume)[1])
    assert mean>-40 and peak<0,(mean,peak)
    frame_dir=project/"verification-frames"; frame_dir.mkdir(exist_ok=True)
    sheet=Image.new("RGB",(1440,1308),"#e2edf0"); draw=ImageDraw.Draw(sheet)
    for i,c in enumerate(meta["chapters"]):
        frame=frame_dir/f"{c['id']}.png"
        subprocess.run(["ffmpeg","-v","error","-ss",str(c["midpoint"]),"-i",str(video),"-frames:v","1","-y",str(frame)],check=True)
        shot=Image.open(frame).convert("RGB")
        assert sum(ImageOps.grayscale(shot).getextrema())>40,"Dark frame"
        sheet.paste(ImageOps.contain(shot,(700,394)),((i%2)*720,(i//2)*436))
        draw.text(((i%2)*720+12,(i//2)*436+400),f"{c['id']} | {c['midpoint']:.2f}s | MP4",fill="#153653")
    sheet.save(project/"renders"/"verified-contact-sheet.jpg",quality=92)
    results.append({"name":name,"file":video.name,"duration_seconds":duration,"width":vs["width"],"height":vs["height"],"fps":vs["r_frame_rate"],"video_codec":vs["codec_name"],"audio_codec":aus["codec_name"],"bytes":video.stat().st_size,"sha256":hashlib.sha256(video.read_bytes()).hexdigest(),"full_decode":"PASS","mean_audio_db":mean,"peak_audio_db":peak,"chapter_frames":6,"visual_review":"PENDING","caption_timing":meta["caption_timing"]})
    print(name,duration,mean,peak,flush=True)
(ROOT/"validation.json").write_text(json.dumps({"schema":"air.video-validation/1","date":"2026-09-30","hyperframes":"0.8.95","synthetic_narration":"Kokoro ff_siwis, fr-fr, speed 0.85","videos":results,"evidence_scope":"Editorial presentation and narrated montage of real local generated views; not a native client or public ChatGPT acceptance recording","engine_version":"0.34.0rc9","plugin_version":"0.1.4","engine_changed":False,"ci_executed":False},ensure_ascii=False,indent=2),encoding="utf-8")
