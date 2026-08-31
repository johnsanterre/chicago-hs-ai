#!/usr/bin/env python3
"""The lesson-page template for adding a course to this site.

Used to build courses 6-8 (2026-08-30). The per-course content
generators were session scratchpad and are gone; the HTML pages in the
repo are the source of truth and are edited in place. This file keeps
the TEMPLATE durable so course 9 starts here instead of from scratch.

How to add a course
===================
1. Pick a short key (e.g. "docs"). Pages: lesson-<key>-1..8.html.
   localStorage key: chsai-<key>-N. Media: video/chsai-<key>-N-watch.mp4
   and audio/chsai-<key>-N-listen.m4a. Notebooks: <key>N-<slug>.ipynb.
2. PAGE below is the CODE-course variant (segment 4 = Code, with the
   Colab button block). For a NO-CODE course: replace the code section
   with a "try" section (see lesson-think-1.html for the exact shape)
   and change SEGS in the page script from
   ['watch','listen','read','code','check','build','done'] to
   ['watch','listen','read','try','check','build','done'].
3. Every lesson needs, per tools/lesson-checklist.md: an animated video
   (tools/videos_courseN.py, built on vidlib), a listen narration
   (tools/audio_courseN.py), at least one interactive figure that
   operates the lesson's claim, a 3-question check with one
   spaced-retrieval item, and a build turn-in.
4. Site wiring (ALL of it, or the site disagrees with itself):
   - index.html: course card + the h1 course count
   - "N independent courses" footer: index.html AND every course page
   - README.md: the count (twice) + the course list entry
   - teacher-guide.html: a rubric section for the course
5. Verify before pushing: node --check every script block,
   driven-click screenshots of every figure (iframe + negative-margin
   harness), 390px spot checks, and EXECUTE notebook algorithms
   offline - parsing is not verification.
6. LLM-using lessons copy the course-5 ceremony verbatim (pip install
   anthropic, getpass class key, MODEL cell, ask/get_json retry)
   and include precomputed outputs for keyless study.

Fill PAGE with .format(): title, lede, n, ckey, nb, coursepage,
coursetitle, watch_h2, watch_note, listen_line, read_h2, read_html,
code_h2, code_intro, quiz_html, build_h2, build_html, fig_js,
prevlink, nextlink. quiz() turns question tuples into quiz_html.
"""


def quiz(qs):
    """qs = [(question, [(choice_text, is_correct), ...]), ...] -> HTML."""
    out = []
    for i, (q, choices) in enumerate(qs, 1):
        attr = '' if i == 1 else ' style="margin-top:1.2em"'
        out.append(f'  <p{attr}><b>{i}. {q}</b></p>')
        out.append(f'  <div data-q="{i}">')
        for text, ok in choices:
            out.append(f'    <button class="choice" data-ok="{1 if ok else 0}">{text}</button>')
        out.append('  </div>')
        out.append(f'  <p class="feedback" id="fb{i}"></p>')
    return '\n'.join(out)


PAGE = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<title>{title} · Chicago HS AI</title>\n<link rel="stylesheet" href="style.css">\n</head>\n<body>\n<header class="site"><div class="wrap">\n  <a class="brand" href="index.html">Chicago HS AI <span class="star">&#x2739;</span></a>\n  <span class="crumb"><a href="index.html">Catalog</a> / <a href="{coursepage}">{coursetitle}</a> / Lesson {n}</span>\n</div></header>\n\n<div class="wrap">\n<p class="kicker">{coursetitle} · Lesson {n} of 8 · about 2–4 hours</p>\n<h1>{title}</h1>\n<p class="lede">{lede}</p>\n\n<div class="progresswrap">\n  <div class="progressbar"><div id="pbar"></div></div>\n  <div class="plabel"><span id="pdone">0</span> of 7 segments complete</div>\n</div>\n\n<section class="seg" data-seg="watch">\n  <div class="stype">1 · Watch</div>\n  <h2>{watch_h2}</h2>\n  <video controls preload="metadata" style="width:100%;border-radius:8px;background:#000"\n    src="video/chsai-{ckey}-{n}-watch.mp4"></video>\n  <p style="font-size:13px;color:var(--ink2);margin:6px 0 0">{watch_note}\n  <span style="color:var(--ink2)">(Animated explainer with narration; a recorded version can replace it later.)</span></p>\n  <button class="mark" data-for="watch">Mark complete</button>\n</section>\n\n<section class="seg" data-seg="listen">\n  <div class="stype">2 · Listen</div>\n  <h2>Listen: two minutes before you go on</h2>\n  <p>{listen_line}</p>\n  <audio controls preload="none" style="width:100%" src="audio/chsai-{ckey}-{n}-listen.m4a"></audio>\n  <button class="mark" data-for="listen">Mark complete</button>\n</section>\n\n<section class="seg" data-seg="read">\n  <div class="stype">3 · Read &amp; play</div>\n  <h2>{read_h2}</h2>\n\n{read_html}\n  <button class="mark" data-for="read">Mark complete</button>\n</section>\n\n<section class="seg" data-seg="code">\n  <div class="stype">4 · Code</div>\n  <h2>{code_h2}</h2>\n  <p>{code_intro}</p>\n  <p style="margin:14px 0 6px">\n    <a class="colab-btn" href="https://colab.research.google.com/github/johnsanterre/chicago-hs-ai/blob/main/notebooks/{nb}.ipynb" target="_blank" rel="noopener">&#9654;&nbsp;Open in Colab</a>\n    <a href="notebooks/{nb}.ipynb" download style="font-size:13.5px">or download the .ipynb</a>\n  </p>\n  <details style="margin-top:6px"><summary style="cursor:pointer;font-weight:600">First time in Colab?</summary>\n    <ol style="font-size:14.5px">\n      <li>The button opens the notebook directly in Colab — sign in with your school Google account.</li>\n      <li><b>File &rarr; Save a copy in Drive</b> right away, so your work is yours.</li>\n      <li>Run cells top to bottom with the ▶ button or <b>Shift+Enter</b>.</li>\n    </ol>\n  </details>\n  <button class="mark" data-for="code">Mark complete</button>\n</section>\n\n<section class="seg" data-seg="check">\n  <div class="stype">5 · Quick check</div>\n  <h2>Check yourself</h2>\n{quiz_html}\n</section>\n\n<section class="seg" data-seg="build">\n  <div class="stype">6 · Build</div>\n  <h2>{build_h2}</h2>\n  <div class="buildtask">\n\n{build_html}\n  </div>\n  <button class="mark" data-for="build">Mark complete</button>\n</section>\n\n<section class="seg" data-seg="done">\n  <div class="stype">7 · Done</div>\n  <h2 id="doneHead">Finish the lesson</h2>\n  <p id="doneMsg">Complete the segments above, then claim the finish here.</p>\n  <p style="font-size:14.5px;color:var(--ink2)">Pace: one lesson a week when you\'re\n  locked in finishes this course in two months. One every two weeks still finishes it\n  in a semester. Both count.</p>\n  <button class="mark" id="finishBtn" data-for="done" disabled>Complete lesson {n}</button>\n</section>\n\n<p style="margin:30px 0;display:flex;justify-content:space-between">{prevlink} {nextlink}</p>\n</div>\n\n<footer class="site"><div class="wrap">Chicago HS AI &middot; a Free Focus program &middot; {coursetitle}, lesson {n} of 8\n&middot; watch &rarr; listen &rarr; read &rarr; code &rarr; check &rarr; build &rarr; done.</div></footer>\n\n<script>\n(function(){{\n  const KEY=\'chsai-{ckey}-{n}\';\n  const SEGS=[\'watch\',\'listen\',\'read\',\'code\',\'check\',\'build\',\'done\'];\n  let state={{}};\n  try{{state=JSON.parse(localStorage.getItem(KEY)||\'{{}}\')}}catch(e){{state={{}}}}\n  function save(){{try{{localStorage.setItem(KEY,JSON.stringify(state))}}catch(e){{}}}}\n  function segEl(id){{return document.querySelector(\'.seg[data-seg="\'+id+\'"]\')}}\n  function render(){{\n    let n=0;\n    for(const s of SEGS){{\n      const done=!!state[s]; if(done)n++;\n      const el=segEl(s); el.classList.toggle(\'done\',done);\n      const b=el.querySelector(\'button.mark[data-for="\'+s+\'"]\');\n      if(b&&s!==\'done\'){{b.disabled=false;b.textContent=done?\'✓ Complete — undo\':\'Mark complete\'}}\n    }}\n    document.getElementById(\'pbar\').style.width=(n/SEGS.length*100)+\'%\';\n    document.getElementById(\'pdone\').textContent=n;\n    const others=SEGS.slice(0,-1).every(s=>state[s]);\n    const fin=document.getElementById(\'finishBtn\');\n    if(state.done){{fin.disabled=false;fin.textContent=\'✓ Lesson {n} complete — undo\';\n      document.getElementById(\'doneHead\').textContent=\'Lesson {n} complete\';\n      document.getElementById(\'doneMsg\').textContent=\'Nice work. The next lesson is waiting when you are.\';}}\n    else{{fin.disabled=!others;fin.textContent=\'Complete lesson {n}\';\n      document.getElementById(\'doneHead\').textContent=\'Finish the lesson\';\n      document.getElementById(\'doneMsg\').textContent=others?\n        \'Everything above is done — claim it.\':\'Complete the segments above, then claim the finish here.\'}}\n  }}\n  document.querySelectorAll(\'button.mark\').forEach(b=>{{\n    b.addEventListener(\'click\',()=>{{\n      const sg=b.dataset.for;state[sg]=!state[sg];save();render();\n      if(sg===\'done\'&&state.done&&!state._counted){{state._counted=true;save();\n        if(window.goatcounter&&window.goatcounter.count){{\n          window.goatcounter.count({{path:\'complete/\'+KEY,event:true}});}}}}}})\n  }});\n  const groups=[...document.querySelectorAll(\'[data-q]\')];\n  const right={{}};\n  groups.forEach(g=>{{\n    const q=g.dataset.q;\n    g.querySelectorAll(\'.choice\').forEach(c=>{{\n      c.addEventListener(\'click\',()=>{{\n        const ok=c.dataset.ok===\'1\';\n        g.querySelectorAll(\'.choice\').forEach(x=>x.classList.remove(\'right\',\'wrong\'));\n        c.classList.add(ok?\'right\':\'wrong\');\n        document.getElementById(\'fb\'+q).textContent=ok?\n          \'Right.\':\'Not quite — the Read segment has what you need. Try again.\';\n        right[q]=ok;\n        if(groups.every(x=>right[x.dataset.q])){{state.check=true;save();render()}}\n      }})\n    }})\n  }});\n  render();\n}})();\n</script>\n<script>\n\n/* ---- Lesson {n} figure ---- */\n{fig_js}\n</script>\n<script data-goatcounter="https://johnsanterre.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>\n</body>\n</html>\n'
