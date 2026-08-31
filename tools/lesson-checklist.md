# Definition of done — lesson and course checks

The checks that must pass before a lesson, and then a course, is called
done. Started 2026-08-30 after the first student feedback round on the
sibling DATASCI 207 site; several checks exist because a real user hit
the gap.

## Per lesson

**Structure**
- [ ] All seven segments present and in order: watch, listen,
      read & play, try/code, check, build, done
- [ ] Progress bar counts correctly; every stage can be marked AND
      un-marked (toggle) — a misclick must not be permanent
- [ ] The completion event fires only on the first completion
- [ ] Prev/next lesson links and course-page link resolve

**Watch**
- [ ] Video file exists, loads, and plays (no TO FILL slot)
- [ ] Narration audible and synced; animation matches what it says
- [ ] The written video script remains on the page (future human
      recording can replace the generated video file-for-file)

**Listen**
- [ ] Audio file exists and loads; the on-page description matches it

**Read & play**
- [ ] At least one interactive figure where the concept benefits from
      direct manipulation (not decoration — if no figure earns its
      place, say so in the course notes rather than forcing one)
- [ ] Figure JS passes a syntax check (node --check on the extracted
      script block)
- [ ] Driven-click test in headless Chrome: every button/input
      exercised, end state screenshot-verified
- [ ] Works at 390px (iframe-in-wide-host technique — bare narrow
      windows clamp and lie)
- [ ] prefers-reduced-motion respected

**Check (quiz)**
- [ ] Three questions, real distractors, at least one spaced-retrieval
      question from an earlier lesson
- [ ] Every question answerable from THIS lesson's own content
      (the 207 audit standard: covered, not partial)

**Try / Code**
- [ ] Activities runnable with what a student actually has (the class
      chatbot, a browser, Colab)
- [ ] Demo-fragility escalation: where newer models pass a famous
      failure, the harder probe is included
- [ ] Notebook lessons: Colab loader URL resolves (raw file returns
      200), notebook is valid JSON, and runs top to bottom in Colab

**Build**
- [ ] Turn-in concretely defined (what, where)
- [ ] Matching rubric exists in the teacher guide

**Page hygiene**
- [ ] GoatCounter tag present
- [ ] No emojis, no self-invented jargon, high-schooler register
- [ ] No fake content — anything unfinished is an honest placeholder

## Per course

- [ ] All eight lessons pass the per-lesson checks
- [ ] Course page lists all lessons as live; pacing line present
- [ ] Teacher guide covers every lesson's turn-in
- [ ] Capstone genuinely integrates the course's skills
- [ ] Course-specific gates: Build with LLMs needs the teacher-set
      API key ceremony confirmed working before students start
- [ ] **The human gate: at least one real student has completed a
      lesson start-to-finish and their confusions are logged.** No
      course is done on internal checks alone — the 207 feedback
      round proved a first user finds what audits do not.

## Site-wide (checked on every push)

- [ ] All pages carry GoatCounter; completion events per lesson
- [ ] No page without a stylesheet; no bare-directory links
      (GitHub Pages returns 404 for those)
- [ ] Repo stays public (Colab loaders break the moment it is not)


## Adding a whole course — site-wiring checklist

(From courses 6–8. Page template + full instructions:
`tools/new_course_template.py`.)

- [ ] Course card on index.html, in course-number order
- [ ] index.html h1 count updated ("Nine courses. Start with any of them.")
- [ ] "N independent courses" footer updated on index.html AND every course page
- [ ] README.md: count in the opening line, count in the status line, course list entry
- [ ] teacher-guide.html: rubric section (turn-in / what good looks like / watch for, per lesson)
- [ ] Media present before push: 8 videos (chsai-<key>-N-watch.mp4) + 8 narrations (chsai-<key>-N-listen.m4a)
- [ ] Notebooks (code courses): 8 in notebooks/, algorithms EXECUTED offline, Colab links resolve
- [ ] Every figure driven-click verified + one 390px spot check
- [ ] LLM lessons: course-5 key ceremony + precomputed outputs for keyless study
