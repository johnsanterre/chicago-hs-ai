#!/usr/bin/env python3
"""Course 2 — Code with an AI Partner: animated lesson videos.
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_course2.py [slug]"""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from vidlib import (s_title, s_bullets, s_browser, s_code, s_loop, s_chat,
                    build_all)

L = {}

L["chsai-web-1"] = [
 (s_title("Code with an AI Partner · Lesson 1", "A website is a text file",
          "and your browser knows how to draw it."),
  "Welcome to Code with an AI Partner. Here is the secret hiding in plain sight: right-click any website and view the page source. That wall of text IS the site. A website is just a text file the browser knows how to draw — and today you write one."),
 (s_browser("The first file", "hello.html, from nothing",
   ["<h1>Hello, Chicago</h1>", "<p>My first page.</p>"],
   [(0, "h1", "Hello, Chicago"), (1, "p", "My first page.")],
   note="Saved. Opened. That is a website."),
  "Open vscode dev in your browser — it works on any Chromebook, nothing to install. Make a folder called my-site, and a new file: hello dot h t m l. Type two lines: an h one tag with your headline, a p tag with a sentence. Save it, open the file in a new tab — and there it is. Yours."),
 (s_loop("The loop", "Where you will live", ["edit", "save", "refresh"],
         note="Two seconds around. That loop is all of web development."),
  "Now the loop that is all of web development: edit, save, refresh. Change the text, save, refresh the tab, watch the page change. Two seconds around. Every site you have ever visited was built by someone going around this exact loop, thousands of times."),
 (s_bullets("This lesson", "Your move", [
   "Open vscode.dev, make my-site, write hello.html",
   "Run the edit-save-refresh loop until it is boring",
   "The course rule starts now: read everything the AI writes"], closing=True),
  "Your AI pair can write HTML fast — and this course's rule stands from day one: you read everything it writes. That is what makes you the programmer and not the passenger. Go make your file, run the loop until it feels boring, and bring the page to the lesson."),
]

L["chsai-web-2"] = [
 (s_title("Code with an AI Partner · Lesson 2", "Six tags build the web",
          "headline, paragraph, link, image, list."),
  "Look at almost any page on the internet and squint: it is a headline, some paragraphs, links, pictures, and lists. Six tags. This lesson you build a real page about you — and everything on it is those six tags."),
 (s_browser("The build", "An about-me page, live",
   ["<h1>Amara Johnson</h1>",
    '<p>Junior at Kenwood. I build things.</p>',
    '<a href="...">my robotics team</a>',
    '<img src="me.jpg">',
    "<ul>", "  <li>deep-dish, obviously</li>", "  <li>house music</li>", "</ul>"],
   [(0, "h1", "Amara Johnson"), (1, "p", "Junior at Kenwood. I build things."),
    (2, "a", "my robotics team"), (3, "img", ""), (5, "li", "deep-dish, obviously"),
    (6, "li", "house music")],
   url="my-site/about.html"),
  "Watch the page assemble. H one for the name. P for a sentence. The a tag makes a link — the tag that makes the web a web. I m g drops in a picture. And u l with l i items makes a list. Notice how the list items live INSIDE the list — tags nest, parents and children, and your indents show the structure."),
 (s_chat("The AI beat", "Ask for the skeleton",
   [("you", "Give me a page skeleton with DOCTYPE, head, and body — and explain what head and body are each FOR."),
    ("ai", "The head is information ABOUT the page — its title, its styles. The body is what people actually see. Here is the skeleton…")],
   note="Then put YOUR six tags in the body."),
  "Now use your pair the right way. Ask it for the standard page skeleton — doctype, head, body — and make it explain what head and body are each for, not just hand you the code. Then put your six tags inside the body yourself. It scaffolds; you build."),
 (s_bullets("This lesson", "Build the page you'd want seen", [
   "Your name, your sentence, a real link, a picture, a list",
   "Indent the nesting so the structure shows",
   "Publish day is lesson 8 — today's page ships then"], closing=True),
  "Your build: the about-me page you would actually want the internet to see. Real name, real link, a picture, a list of favorites. Keep the nesting indented so the structure shows at a glance. And know where this is going — lesson eight is publish day, and today's page is what ships."),
]

L["chsai-web-3"] = [
 (s_title("Code with an AI Partner · Lesson 3", "Predict, then run",
          "the habit that keeps you the programmer."),
  "Your AI pair just generated forty lines of HTML. The tempting move is paste it and move on. This lesson installs the professional move instead — and it is the single most important habit in this course."),
 (s_loop("The method", "For every line", ["read", "predict", "run", "check"],
         note="Wrong prediction? That line just taught you something."),
  "The method: read a line. Say out loud what it will do — before you run it. Then run it and check. If you were wrong, that line just taught you something real. If you were right, that is confidence — earned, not assumed. Around the loop, line by line."),
 (s_chat("The unknown", "When you hit a mystery line",
   [("you", "Explain this line like I've never seen a div before."),
    ("ai", "A div is a plain container — an invisible box for grouping things so you can style or move them together. This one wraps your header…")],
   note="Not sure what a line does? Delete it, refresh, see what breaks."),
  "You will hit lines you cannot predict — good. Ask your pair to explain the mystery like you have never seen it, because you haven't. And there is a second tool: the deletion test. Not sure what a line does? Delete it, refresh, and see what breaks. The browser forgives everything, and undo brings it back."),
 (s_bullets("This lesson", "The mystery page", [
   "A full AI-generated page, read line by line",
   "Prediction before execution, every line",
   "This habit separates people who use AI from people AI uses"], closing=True),
  "Your build is a full mystery page: AI-generated, unfamiliar, and yours to read line by line with predictions on the record. Prediction before execution — that habit is what separates people who use AI from people AI uses. Go read some code."),
]

L["chsai-web-4"] = [
 (s_title("Code with an AI Partner · Lesson 4", "Style is a second language",
          "selector, property, value — that's CSS."),
  "Your about-me page is honest. It is also plain. This lesson adds the second language of the web: CSS. Three rules in, your page will look designed — and you will know exactly why."),
 (s_browser("The transform", "Three rules, live",
   ["<style>", "body { background: #FCFBF8;", "       font-family: system-ui; }",
    "h1   { color: #174A6C; }", "p    { line-height: 1.6; }", "</style>"],
   [(0, "h1", "Amara Johnson"), (1, "p", "Junior at Kenwood. I build things."),
    (2, "p", "Chicago, IL")],
   url="my-site/about.html", style_at=4,
   note="Refresh. Different page. selector { property: value; }"),
  "Add a style block in the head and write three rules. Body gets a background and a real font. H one gets a color — that navy is Chicago flag navy. P gets breathing room between lines. Refresh: different page. Every CSS rule is the same shape — selector, property, value — a sentence in the second language."),
 (s_chat("The AI beat", "Options, then taste",
   [("you", "Give me three different looks for this page — one calm, one bold, one weird — as complete style blocks."),
    ("ai", "Look one, calm: warm paper background, navy headings, generous spacing… Look two, bold: black background, huge type… Look three…")],
   note="The AI generates looks. YOU have taste. Choosing is the design act."),
  "Now the move you learned in How AI Works: ask for options. Three complete looks — one calm, one bold, one weird. Paste each one, look at your page wearing it, and choose. The AI generates looks; you have taste. Choosing is the design act, and it cannot be delegated."),
 (s_bullets("This lesson", "Readable beats flashy", [
   "Line length, contrast, spacing — the big three",
   "Restyle your page until it looks intentional",
   "Keep the style block where you can read every rule"], closing=True),
  "One designer's secret before you go: readable beats flashy, every time. Watch your line lengths, your contrast, your spacing — those three carry most of good design. Your build: restyle your about-me page until it looks intentional, with every rule in the style block one you can explain."),
]

L["chsai-web-5"] = [
 (s_title("Code with an AI Partner · Lesson 5", "The page comes alive",
          "find an element, attach a behavior."),
  "So far your pages just sit there. Today they act. JavaScript is the third language of the web — the one that makes pages DO things — and your first ten lines of it are this lesson."),
 (s_code("The wire-up", "A button that answers",
   ['<button id="hi">Say hi</button>', "<script>",
    "document.getElementById('hi').onclick = () => {",
    "  alert('Hi Chicago!');", "};", "</script>"],
   console=[("(click)  >  Hi Chicago!", (140, 200, 160))],
   note="Find an element. Attach a behavior. That is JavaScript."),
  "Here is the whole pattern. A button with an i d. A script that finds that element and attaches a behavior to its click. Press the button — the page acts. Level it up to a counter that displays the click count and you have written real interactive code. Read every line aloud."),
 (s_code("The console", "Where JavaScript talks back",
   ["document.getElementByld('hi')  // typo!"],
   console=[("Uncaught TypeError: document.getElementByld", (230, 120, 110)),
            ("    is not a function      (line 3)", (230, 120, 110)),
            ("console.log('made it here')  >  made it here", (140, 200, 160))],
   err_line=0,
   note="Press F12. Errors name the exact line. Errors are reports."),
  "Press F twelve and meet the console — where JavaScript talks back. Plant a typo on purpose and watch: the console names the error AND the exact line. You learned this in the Python course and it holds here: errors are not accusations, they are reports. The console is where you read them."),
 (s_bullets("This lesson", "Your build", [
   "Wire a button, then a counter — read every line",
   'AI beat: "add a dark-mode toggle and explain every line"',
   "Predict, run, check — the lesson-3 habit, now with behavior"], closing=True),
  "Your build: wire up the button, then the counter. Then the AI beat — ask your pair for a dark-mode toggle for your page, with every line explained. Read it, predict it, test it. The lesson-three habit does not retire just because the code got more interesting."),
]

L["chsai-web-6"] = [
 (s_title("Code with an AI Partner · Lesson 6", "Debugging is a process",
          "symptom, hypothesis, experiment, fix."),
  "A button that does nothing. No error on screen. This is the moment that separates panic from process — and this lesson hands you the process. Professionals do not debug by staring harder; they run a loop."),
 (s_loop("The loop", "Four steps, repeated",
         ["symptom", "hypothesis", "experiment", "fix"],
         note="The smallest test that checks the idea — that's the skill."),
  "The loop: symptom — what exactly is wrong, stated precisely. Hypothesis — what could cause that? Experiment — the smallest test that checks the idea. Fix, and run again. The skill is in the experiment step: shrink the place a bug can hide until it has nowhere left."),
 (s_code("Bug one, live", "The silent button",
   ["document.getElementById('hii').onclick = ...",
    "        // the button's id is 'hi' — one letter off"],
   console=[("Uncaught TypeError: Cannot read properties", (230, 120, 110)),
            ("    of null  (reading 'onclick')", (230, 120, 110))],
   err_line=0,
   note="The console had the answer the whole time."),
  "Bug one, live. The button does nothing — but open the console and there is the report: cannot read properties of null. Null means the script FOUND nothing — so the i d must be wrong. One look, hypothesis confirmed: it is misspelled by one letter. Fix it, click, works. The console had the answer the whole time."),
 (s_bullets("This lesson", "Isolation, and the hunt", [
   "Styles ignored? Replace the rule with background: red — does it run at all?",
   "Half-rendered page? View source: find the unclosed tag",
   "Your build: three planted bugs, hunted with the loop on paper"], closing=True),
  "Two more bugs wait in the lesson: styles that get ignored, and a page that half-renders. Both fall to isolation — like replacing a whole rule with background red just to learn whether the rule runs at all. Your build: hunt three planted bugs with the loop written out. Symptom, hypothesis, experiment, fix."),
]

L["chsai-web-7"] = [
 (s_title("Code with an AI Partner · Lesson 7", "Save points, in public",
          "Git saves your work. GitHub shows it."),
  "You know save points from games: lose the boss fight, reload the save. Git is save points for your work — every version, forever. And GitHub is where those saves live in public, under your name. Today your code gets a permanent address."),
 (s_browser("The repo", "Made in the browser, no installs",
   ["github.com  >  New repository", "name: my-site", "visibility: public",
    "> Create repository", "", "Upload files: hello.html, about.html"],
   [(1, "h1", "my-site"), (2, "p", "Public repository"),
    (5, "li", "hello.html"), (5, "li", "about.html")],
   url="github.com/you/my-site"),
  "All in the browser, no installs: github dot com, new repository, name it my-site, make it public, create. Then drag your files in — hello and about. That is a repo: your code, versioned, at an address anyone can visit."),
 (s_bullets("The message", "Commits talk to future-you", [
   '"Add about page with styles and dark mode"  — a real message',
   '"stuff"  "asdf"  "final2"  — lies to your future self',
   "A commit message says WHAT changed and WHY"]),
  "One box matters more than it looks: the commit message. Add about page with styles and dark mode — that tells future-you what happened and why. Stuff, a s d f, final two — those are lies to your future self. Every commit from now on gets a real sentence."),
 (s_bullets("This lesson", "The public record", [
   "Colleges look. Employers look. Your repos answer.",
   "Twenty repos from these courses beats any resume line",
   "New rule: every build, in every course, ends with a commit"], closing=True),
  "Here is why this lesson sits in the middle of the course and not the end: from today, every build in every course ends with a commit. Twenty real repos under your name is a public record no resume line can match. Colleges look. Employers look. Start the record now."),
]

L["chsai-web-8"] = [
 (s_title("Code with an AI Partner · Lesson 8", "Ship it",
          "one switch, and your site is on the internet."),
  "Your repo is sitting there — visible, but not live. This lesson flips the one switch that changes that, and by the end, your page has a U R L that works on any phone on earth. This is publish day."),
 (s_browser("The switch", "Settings > Pages > Save",
   ["repo > Settings > Pages", "Source: main branch, / root", "> Save",
    "", "…ninety seconds…", "your site is live at:"],
   [(2, "p", "Building your site…"),
    (5, "h1", "you.github.io/my-site"), (5, "p", "Your site is live")],
   url="github.com/you/my-site/settings/pages",
   note="Open it on a phone. Your file. The internet. Anyone."),
  "Repo, settings, pages. Source: the main branch, root folder. Save. Wait about ninety seconds, refresh — and there is a U R L: your username dot github dot i o slash my-site. Open it on a phone. That is your file, served to anyone on earth who asks."),
 (s_loop("The loop, upgraded", "Now it ends on the live site",
         ["edit", "commit", "live"],
         note="Fix a typo, commit, watch the internet update."),
  "What just happened: GitHub runs computers that serve your repo's files to any browser that asks — free, for public repos. And this exact system serves the site you are taking this course on right now. Your loop upgrades: edit, commit, and the LIVE site updates. Fix a typo and watch the internet change."),
 (s_bullets("Course complete", "Send someone the URL", [
   "Ship the about page you're proud of",
   "Text the URL to someone who will actually open it",
   "You now build, read, style, debug, and ship — with a pair"], closing=True),
  "Your final build: ship the about page you are proud of, and text the U R L to someone who will actually open it. Course complete. You build pages, read code you did not write, style with taste, debug with a process, and ship to the real internet — with an AI pair, and with you as the programmer."),
]

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    build_all(L, "Code with an AI Partner", only)
