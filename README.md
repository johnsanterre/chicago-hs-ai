# Chicago HS AI

Five independent courses that teach Chicago high-schoolers to build
with AI — and then to put that skill to work for local nonprofits.

**Live site:** https://johnsanterre.github.io/chicago-hs-ai/

## The courses

Flat by design: every course starts from zero and stands alone. Pick
one and begin.

1. **How AI Works** — no coding required. What a language model
   actually is, how to talk to one well, how it fails, and when not
   to use it.
2. **Code with an AI Partner** — first real builds on the web:
   HTML, CSS, JavaScript with an AI pair, shipped live on GitHub
   Pages by lesson 8.
3. **Python in Colab** — Python from zero, in the browser, with an
   AI pair. Eight lessons, eight notebooks, ending in a working
   chore-bot project.
4. **Working with Data** — pandas, cleaning with a logged trail,
   honest charts (and how charts lie), live Chicago open data.
5. **Build with LLMs** — API calls, system prompts, JSON outputs,
   document Q&A, a chat app, evals, and a hand-built agent loop.

## How a lesson works

Each lesson is a short scroll-through sequence — watch → listen →
read → do → check → build — sized so a focused student finishes one
per week, and one every two weeks still completes a course in a
semester. Every lesson ends with something the student built.

- **Videos** are generated slide videos with narration; recorded
  versions can replace them file-for-file.
- **Audio** narration is machine-generated (Kokoro).
- **Notebooks** open directly in Google Colab from each lesson page.
- Progress is saved in the browser; graded work is the per-lesson
  turn-in, described on every lesson page and in the
  [teacher guide](teacher-guide.html).

## Structure

```
index.html            course catalog
<course>.html         one page per course, 8 lessons each
lesson-*.html         the lessons
notebooks/            Colab notebooks (Course 3)
audio/  video/        narrations and slide videos
teacher-guide.html    rubrics, pacing, platform notes for teachers
```

Plain static HTML — no build step; open `index.html` or serve the
folder anywhere.

## Status

Draft in active development (started 2026-08-30). All five courses
are built — 40 lessons, 24 notebooks. Feedback from real classrooms
is the next input.
