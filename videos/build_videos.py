"""Build two self-contained HyperFrames videos from recorded evidence and narration."""
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import urllib.request

ROOT = Path(__file__).resolve().parent
CONTENT = json.loads((ROOT / "video-content.json").read_text(encoding="utf-8"))
STYLE = """
*{box-sizing:border-box}body{margin:0}#root{position:absolute;inset:0;width:1920px;height:1080px;color:#153653;font-family:Montserrat,sans-serif;overflow:hidden}
.paper{position:absolute;inset:0;background:#f2f6fa}.top{position:absolute;left:64px;right:64px;top:42px;display:flex;justify-content:space-between;align-items:center}.brand{font-size:24px;font-weight:700;letter-spacing:3px}.edition{font-family:'IBM Plex Mono',monospace;font-size:22px;color:#52657a}.label{font-family:'IBM Plex Mono',monospace;font-size:22px;color:#067d80;letter-spacing:1px}.title{font-size:64px;line-height:1.1;letter-spacing:-2px;font-weight:700;margin:18px 0 0;max-width:1650px}.heading{position:absolute;top:126px;left:64px;right:64px}.main{position:absolute;left:64px;right:64px;top:295px;bottom:160px}.points{display:flex;flex-direction:column;gap:26px}.point{font-size:34px;line-height:1.3;font-weight:700;max-width:1450px}.number{font-family:'IBM Plex Mono',monospace;font-size:23px;color:#067d80;margin-bottom:10px}.rule{height:3px;width:100%;background:#153653;transform-origin:left}.footer{position:absolute;left:64px;right:64px;bottom:34px;display:flex;justify-content:space-between;color:#52657a;font-family:'IBM Plex Mono',monospace;font-size:19px}.progress{position:absolute;left:0;bottom:0;width:1920px;height:7px;background:#067d80;transform-origin:left}.caption{position:absolute;left:110px;right:110px;bottom:80px;min-height:66px;background:#153653;color:#f2f6fa;padding:15px 28px;font-size:27px;line-height:1.4;text-align:center;border-radius:6px}.hero{display:grid;grid-template-columns:1fr 420px;gap:90px;align-items:center;height:100%}.hero-logo{width:360px;height:360px;object-fit:contain}.hero-tag{font-size:46px;font-weight:700;line-height:1.2}.hero-sub{margin-top:34px;font-size:28px;line-height:1.5;color:#52657a;max-width:930px}.chain{display:flex;flex-direction:column;gap:18px;width:100%}.chain-row{display:flex;align-items:center;gap:38px;padding:15px 0;border-bottom:2px solid #ccdce7;font-size:38px;font-weight:700}.chain-row .idx{font-family:'IBM Plex Mono',monospace;color:#067d80;font-size:28px;width:75px}.results{display:flex;flex-direction:column;gap:30px}.result{display:grid;grid-template-columns:300px 1fr 240px;gap:32px;align-items:center;padding:30px 38px;background:#e2edf0}.result-name{font-size:38px;font-weight:700}.result-value{font-family:'IBM Plex Mono',monospace;font-size:42px;font-weight:700}.blocked{font-family:'IBM Plex Mono',monospace;font-size:28px;color:#a52839}.capture-layout{display:grid;grid-template-columns:425px 1fr;gap:35px;height:100%}.capture-notes{display:flex;flex-direction:column;gap:28px;justify-content:center}.capture-notes .point{font-size:29px}.capture-frame{position:relative;align-self:center;width:100%;height:625px;background:#e2edf0;border:2px solid #ccdce7;overflow:hidden}.capture-frame img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain}.capture-label{font-family:'IBM Plex Mono',monospace;font-size:20px;color:#52657a;margin-top:18px;line-height:1.4}.receipt{display:grid;grid-template-columns:1fr 1fr;gap:60px;height:100%}.receipt-pane{background:#153653;color:#f2f6fa;padding:36px 40px;font-family:'IBM Plex Mono',monospace;font-size:26px;line-height:1.65;white-space:pre-wrap;border-radius:8px}.receipt-note{font-size:30px;line-height:1.5}.topology{display:grid;grid-template-columns:1fr 1fr;gap:55px;height:100%;align-items:center}.local-box{border:3px solid #067d80;padding:45px;border-radius:12px}.local-box strong{display:block;font-size:46px;margin-bottom:30px}.local-box p{font-size:32px;margin:20px 0}.right-note{font-size:34px;line-height:1.5}.close-links{font-family:'IBM Plex Mono',monospace;font-size:35px;line-height:2}.badge{display:inline-block;background:#153653;color:#f2f6fa;font-size:28px;padding:12px 20px;margin-bottom:24px}.subtitle{font-size:30px;line-height:1.5;color:#52657a}.provenance{display:grid;grid-template-columns:1fr 1fr;gap:45px}.provenance img{width:100%;height:480px;object-fit:contain;background:#e2edf0;border:2px solid #ccdce7}
"""

def esc(s): return html.escape(str(s), quote=True)
def write(path, text): path.write_text(text, encoding="utf-8")
def stamp(seconds, comma=False):
    ms=round(seconds*1000); h,ms=divmod(ms,3600000); m,ms=divmod(ms,60000); s,ms=divmod(ms,1000)
    return f"{h:02}:{m:02}:{s:02}{',' if comma else '.'}{ms:03}"

def content(scene, duration, paragraphs):
    kind=scene["kind"]; pts=scene["points"]; sid=scene["id"]
    points=''.join(f'<div class="point">{esc(p)}</div>' for p in pts)
    if kind=="hero":
        return f'<div class="hero"><div><div class="points">{points}</div><p class="hero-sub">Conception, vérification et simulation des plans destinés aux équipes de réalisation.</p></div><img class="hero-logo" src="assets/logo.png" alt="Logo AIR"></div>', ''
    if kind=="chain":
        return '<div class="chain">'+''.join(f'<div class="chain-row"><span class="idx">0{i+1}</span><span>{esc(p)}</span></div>' for i,p in enumerate(pts))+'</div>', ''
    if kind=="results":
        rows=[('D01 / SAV','UNKNOWN'),('D02 / Atelier','VIOLATED'),('D03 / Identités','CONFLICTING')]
        return '<div class="results">'+''.join(f'<div class="result"><div class="result-name">{a}</div><div class="result-value">{b}</div><div class="blocked">BLOCKED</div></div>' for a,b in rows)+'</div>', ''
    if kind=="topology":
        return '<div class="topology"><div class="local-box"><strong>Poste architecte</strong><p>Agent + skills AIR</p><p>Moteur Python · SQLite</p><p>Registre local</p></div><div class="right-note">Une installation autonome par architecte ou entreprise.<p class="subtitle">Pas de fédération ou de synchronisation automatique annoncée.</p></div></div>', ''
    if kind=="receipt":
        return '<div class="receipt"><div class="receipt-pane">EXTRAIT DU REÇU PUBLIC\n\nstatus: PASS_SCOPED\nversion: 0.34.0rc9\nplatform: Windows\npython: 3.12.14\n\nsecond_physical_device:\n  NOT_ATTESTED\npublic_chatgpt_acceptance:\n  NOT_EXECUTED</div><div class="capture-notes">'+points+'<p class="capture-label">Recomposition éditoriale des champs du reçu, conservé dans assets/source/receipt.json.</p></div></div>', ''
    if kind=="capture":
        change=paragraphs[1]["start"] if len(paragraphs)>1 else duration/2
        body=f'<div class="capture-layout"><div class="capture-notes">{points}<p class="capture-label">À droite : capture de la vue générée, sans modification du contenu.<br>À gauche : commentaire du reçu et prochaine étape proposée.</p></div><div class="capture-frame"><img id="{sid}-shot1" src="assets/{scene["capture"]}-construction.png" alt="Vue de construction"><img id="{sid}-shot2" style="opacity:0" src="assets/{scene["capture"]}-reception.png" alt="Vue des critères de réception"></div></div>'
        return body, f'tl.set("#{sid}-shot1",{{opacity:0}},{change});tl.set("#{sid}-shot2",{{opacity:1}},{change});'
    if kind=="handoff":
        return '<div class="provenance"><div><div class="points">'+points+'</div><p class="capture-label">Capture réelle : registre, révisions et empreinte de la baseline.</p></div><img src="assets/d03-provenance.png" alt="Registre et empreinte"></div>', ''
    if kind=="close":
        return '<div><span class="badge">Apache-2.0</span><div class="close-links">'+esc(pts[0])+'<p>'+esc(pts[1])+'</p></div><p class="subtitle">Moteur 0.34.0rc9 · Plugin 0.1.4 · Périmètre local documenté</p></div>', ''
    return '<div class="points">'+points+'</div><p class="subtitle">La vidéo ne vaut pas approbation du plugin par OpenAI.</p>', ''

def build(name, scenes):
    project=ROOT/f"air-{name}-fr"; assets=project/"assets"; assets.mkdir(exist_ok=True)
    shutil.copy2(ROOT.parent/"plugins/air-local/assets/logo.png",assets/"logo.png")
    if not (assets/"gsap.min.js").exists():
        urllib.request.urlretrieve('https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js',assets/"gsap.min.js")
    (project/"compositions").mkdir(exist_ok=True)
    audio=json.loads((project/"audio-meta.json").read_text(encoding="utf-8"))["paragraphs"]
    write(project/"design.md", """# AIR video identity
Concept: an architecture dossier as a clear chain of decisions and evidence.
Palette: #f2f6fa paper, #153653 navy, #067d80 teal, #52657a muted text,
#ccdce7 separators, #e2edf0 panels, #a52839 blocked status.
Typography: Montserrat 400/700 headings/body; IBM Plex Mono 400/700 metadata.
No fabricated app UI. Existing AIR logo. Captures retain their original styling.
Flat editorial layout, 64px outer margins, 18–60px gaps, 6–12px corners, no shadows.
Capture panels are static for readability; chapter progress marks elapsed time.
Only editorial labels animate; no invented clicks, typing or success states.
""")
    offset=0; hosts=[]; sounds=[]; captions=[]; chapters=[]; storyboard=[]
    for index,scene in enumerate(scenes):
        sid=scene["id"]; paras=[dict(p) for p in audio if p["scene"]==sid]
        local=1.0
        for p in paras:
            p["start"]=local
            sounds.append(f'<audio id="audio-{sid}-{p["paragraph"]}" src="{p["path"]}" data-start="{offset+local:.3f}" data-duration="{p["duration"]:.3f}" data-track-index="10" data-volume="1"></audio>')
            # Paragraph duration measured from waveform; caption phrases distributed
            # proportionally by character count (not claimed as word-aligned ASR).
            pieces=re.findall(r'.{1,105}(?:\s+|$)',p["text"])
            if not pieces: pieces=[p["text"]]
            total=sum(len(x) for x in pieces); cursor=offset+local
            for piece in pieces:
                length=p["duration"]*len(piece)/total
                captions.append({"start":cursor,"end":cursor+length,"text":piece.strip()})
                cursor+=length
            local+=p["duration"]+0.6
        duration=round(local+1.1,3)
        body,extra=content(scene,duration,paras)
        note='MONTAGE COMMENTÉ · CAPTURES RC9' if name=='parcours-local' else 'PRÉSENTATION ÉDITORIALE'
        doc=f'''<template><style>{STYLE}</style><div id="root" data-composition-id="{sid}" data-width="1920" data-height="1080" data-duration="{duration}">
<div class="paper"></div><div class="top"><div class="brand">AIR</div><div class="edition">ARCHITECTURE WORKSPACE / {index+1:02}</div></div>
<div class="heading"><div class="label">{esc(scene['label'])}</div><h1 class="title" id="{sid}-title">{esc(scene['title'])}</h1></div>
<div class="main" id="{sid}-body">{body}</div><div class="footer"><span>{note}</span><span>Yannick Huchard · 2026</span></div><div id="{sid}-progress" class="progress"></div></div>
<script>window.__timelines=window.__timelines||{{}};var tl=gsap.timeline({{paused:true}});
tl.fromTo("#{sid}-title",{{y:48,opacity:0}},{{y:0,opacity:1,duration:0.45,ease:"power4.out"}},0);
tl.fromTo("#{sid}-body",{{y:22,opacity:0}},{{y:0,opacity:1,duration:0.45,ease:"power3.out"}},0.18);
tl.fromTo("#{sid}-progress",{{scaleX:0}},{{scaleX:1,duration:{duration},ease:"none"}},0);{extra}
window.__timelines["{sid}"]=tl;</script></template>'''
        write(project/"compositions"/f"{sid}.html",doc)
        write(project/"compositions"/f"{sid}.motion.json",json.dumps({"duration":duration,"assertions":[{"kind":"appearsBy","selector":f"#{sid}-title","bySec":1},{"kind":"staysInFrame","selector":f"#{sid}-title"}]}))
        hosts.append(f'<div id="host-{sid}" class="clip" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" data-start="{offset:.3f}" data-duration="{duration}" data-track-index="1" data-width="1920" data-height="1080" style="position:absolute;inset:0"></div>')
        chapters.append({"id":sid,"title":scene['title'],"start":offset,"duration":duration,"midpoint":round(offset+duration/2,3)})
        storyboard.append(f"## Frame {index+1} — {scene['title']}\n- status: animated\n- src: compositions/{sid}.html\n- duration: {duration}s\n- motion: short GSAP label arrival; stat-bars-and-fills progress\n- transition_in: cut\n\n{scene['title']}\n\n"+'\n\n'.join(scene['lines']))
        offset+=duration
    caption_html=''.join(f'<div id="caption-{i}" class="caption clip" data-start="{c["start"]:.3f}" data-duration="{c["end"]-c["start"]:.3f}" data-track-index="3">{esc(c["text"])}</div>' for i,c in enumerate(captions))
    write(project/"index.html",f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>AIR — {name}</title><script src="assets/gsap.min.js"></script><style>{STYLE}.caption{{position:absolute;font-family:Montserrat,sans-serif}}#film{{position:relative;width:1920px;height:1080px;overflow:hidden}}</style></head><body><div id="film" data-composition-id="air-{name}" data-width="1920" data-height="1080" data-duration="{offset:.3f}">{''.join(hosts)}{''.join(sounds)}{caption_html}</div><script>window.__timelines=window.__timelines||{{}};window.__timelines["air-{name}"]=gsap.timeline({{paused:true}});</script></body></html>''')
    write(project/"STORYBOARD.md",'---\nmode: autonomous\n---\n\n# AIR / '+name+'\n\n'+'\n\n'.join(storyboard))
    write(project/"SCRIPT.md",'\n\n'.join('# '+s['title']+'\n\n'+'\n\n'.join(s['lines']) for s in scenes))
    write(project/"chapters.json",json.dumps({"duration":round(offset,3),"chapters":chapters,"caption_timing":"Measured paragraph durations; proportional phrase timing, not word-level ASR"},ensure_ascii=False,indent=2))
    write(project/"subtitles.fr.srt",'\n\n'.join(f'{i+1}\n{stamp(c["start"],True)} --> {stamp(c["end"],True)}\n{c["text"]}' for i,c in enumerate(captions))+'\n')
    write(project/"subtitles.fr.vtt",'WEBVTT\n\n'+'\n\n'.join(f'{stamp(c["start"])} --> {stamp(c["end"])}\n{c["text"]}' for c in captions)+'\n')
    inventory=[{"path":p.relative_to(project).as_posix(),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(assets.rglob('*')) if p.is_file()]
    write(project/"asset-provenance.json",json.dumps({"logo":"AIR official plugin 0.1.4; Yannick Huchard; Apache-2.0","screenshots":"Browser captures of unmodified generated synthetic Asteria rc9 HTML on 2026-09-30","narration":"Local Kokoro ff_siwis; synthetic voice; no voice cloning","assets":inventory},indent=2))
    print(name,round(offset,3),'seconds; midpoints',','.join(str(c['midpoint']) for c in chapters))

if __name__=='__main__':
    for name,scenes in CONTENT.items(): build(name,scenes)
