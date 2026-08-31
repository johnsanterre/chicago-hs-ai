#!/usr/bin/env python3
"""Course 8 — Document Pipelines: animated lesson videos.
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_course8.py [slug]"""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from vidlib import s_title, s_bullets, s_chat, s_loop, s_code, build_all

L = {}

L["chsai-docs-1"] = [
 (s_title("Document Pipelines · Lesson 1", "Documents in, answers out",
          "every organization has the drawer."),
  "Ask a food pantry how many families they served last year, and someone opens a drawer: monthly reports, some typed, some scanned, some in emails. The answer exists — spread across forty documents in forty formats. This course builds the machine that turns that drawer into answers."),
 (s_loop("The assembly line", "Seven stages, always", ["collect", "extract + clean", "structure + validate", "store + ask"],
         note="Each stage checkable. Each stage fixable alone."),
  "The professional move is an assembly line: collect the files, extract the text, clean the junk, structure the fields into rows, validate every row, store a clean table, and then ask — because questions against a table are cheap. Seven stages, the same every time."),
 (s_bullets("Why stages win", "Two properties", [
   "Small enough to check — you can see each stage's output",
   "Fixable alone — repair one stage, rerun, nothing else moves",
   "One giant 'read it all' step has neither"]),
  "Why not one giant step — computer, read all this and tell me the answer? Because you can't check it and you can't fix it. Stages have both properties: each is small enough to look at, and when page headers pollute your text you fix the clean stage and rerun — nothing else changes. That's the whole argument."),
 (s_bullets("This lesson", "Claim your drawer", [
   "Walk one document through all seven stages in the figure",
   "The notebook runs a whole pipeline in miniature",
   "Pick a real pile — it becomes your capstone"], closing=True),
  "In the figure, walk one pantry report through all seven stages. The notebook runs an entire pipeline in miniature — six documents, two of which fail in ways later lessons handle. Then claim your own drawer: a club's minutes, a team's reports, a nonprofit's newsletters. It becomes your lesson eight capstone, so pick a pile you actually care about."),
]

L["chsai-docs-2"] = [
 (s_title("Document Pipelines · Lesson 2", "Getting the text out",
          "a PDF is drawing instructions, not text."),
  "A PDF looks like text, but inside it is drawing instructions — place these characters at these coordinates. Extraction rebuilds lines from positions, and it mostly works. Mostly. Today you learn what gets lost, and the habit that catches it."),
 (s_code("The ladder", "Formats, easy to hostile",
   [".txt   already text - read and go", ".csv   already structured - even better", ".pdf   drawing instructions - extraction", "scan   just pixels - OCR guesses"],
   err_line=3, note="OCR is a prediction system. It makes prediction mistakes."),
  "Formats form a ladder. A text file: read it and go. A CSV: already structured. A PDF: extraction territory. And a scan is the hostile end — just pixels, so OCR has to guess the characters, and it guesses like a prediction system: mostly right, silently wrong. L becomes one. O becomes zero. A donation of eighteen forty-seven becomes something that is not a number at all."),
 (s_bullets("The classic damage", "What extraction loses", [
   "Headers and footers landing mid-sentence",
   "Spacing collapsed: served212families",
   "Characters swapped silently by OCR",
   "None of it announces itself"]),
  "The classic casualties: page headers interleaved mid-sentence, spacing collapsed until words fuse, characters swapped without a sound. None of it announces itself — and all of it poisons every later stage if it gets through. So the rule that runs this whole course: extraction is lossy. Inspect what survived, before building on it."),
 (s_bullets("This lesson", "Build a PDF by hand", [
   "700 bytes, written from scratch in the notebook",
   "Then pypdf pulls your text back out",
   "Then the inspection checklist — use it forever"], closing=True),
  "In the notebook you build a real PDF from raw bytes — about seven hundred of them, and the format stops being magic. Then you extract your own text back out, and run the inspection checklist you will use on every document for the rest of the course. Two minutes of inspection saves hours downstream."),
]

L["chsai-docs-3"] = [
 (s_title("Document Pipelines · Lesson 3", "Cleaning at scale",
          "small functions, composed in order, logged."),
  "One messy document, you would fix by hand. You have forty this month and forty more next month. So you write cleaning functions — and you follow three rules that make cleaning trustworthy at scale."),
 (s_loop("The rules", "Three of them", ["one fix per function", "compose in order", "log every change"],
         note="strip_headers, then fix_spacing, then dates. Order matters."),
  "Rule one: one fix per function. Strip headers does that and nothing else — small functions are checkable. Rule two: compose them in order, because order matters: headers out before spacing gets fixed, or the leftovers survive. Rule three: log every change. Removed three header lines. Rewrote two dates. Every run, on the record."),
 (s_bullets("The log", "Your alibi", [
   "“Did processing alter our documents?” — a record, not a shrug",
   "A wrong number later? The log says if cleaning touched it",
   "Organizations that trust you with documents deserve this"]),
  "The log is your alibi. When a number in the final table looks wrong, the log tells you whether cleaning touched it. And when the organization asks — did processing alter our documents? — you have a record instead of a shrug. Groups that hand you their documents are trusting you. The log is what that trust stands on."),
 (s_bullets("This lesson", "Compose, then extend", [
   "Toggle the four cleaners in the figure, watch the log",
   "The notebook has a mystery document — new junk",
   "You write the fifth cleaner yourself"], closing=True),
  "In the figure, toggle four cleaners and watch the text and the log change together. The notebook builds them for real, runs the pile — and then hands you a mystery document with junk none of the four handle. Diagnose it, write the fifth cleaner, slot it into the right position. That add-a-function move is the whole job, forever."),
]

L["chsai-docs-4"] = [
 (s_title("Document Pipelines · Lesson 4", "Fields from rules",
          "sharp where formats are fixed. Blind where they aren't."),
  "Clean text still is not data. Rules — patterns that match shapes — pull the fields out: dates, amounts, emails. They are unbeatable exactly where formats are fixed, and blind exactly where humans got creative. Today you measure both halves."),
 (s_code("The workhorses", "Three patterns, most documents",
   ["amounts:  $ digits , cents", "dates:    YYYY-MM-DD  (cleaning made them one shape)", "emails:   thing @ thing . thing"],
   note="Fast, free, consistent - and they never invent."),
  "Three workhorse patterns cover most organizational documents. Amounts: a dollar sign and digits. Dates: one pattern — because lesson three standardized them into one shape; this is why cleaning came first. Emails practically extract themselves. Rules are fast, free, perfectly consistent — and they can never invent, because a rule can only find what is literally there."),
 (s_chat("The boundary", "Where rules go blind",
   [("you", "Extract the amount: 'we raised around two grand at youth night'"),
    ("ai", "amount: None - no dollar sign, no digits, nothing matches")],
   note="Rules match shapes. That sentence has meaning, not shape."),
  "Then the boundary. We raised around two grand. Due next Tuesday. Contact Rosa — she knows. No pattern matches meaning; rules match shapes, and these have the wrong shape. You can keep adding rules for a while — and then the rulebook becomes the mess. Knowing where the boundary sits is the skill."),
 (s_bullets("This lesson", "Measure both halves", [
   "Sweep a document with three patterns in the figure",
   "The notebook: twenty reports, find-rates per rule",
   "Quote the three failures — lesson 5's shopping list"], closing=True),
  "In the figure, sweep a document and watch the matches light up — then read the last paragraph, written by a human, where nothing lights up at all. The notebook extracts a pile of twenty reports and scores every rule honestly: found in eighteen of twenty. The failures you quote are not embarrassments. They are lesson five's shopping list."),
]

L["chsai-docs-5"] = [
 (s_title("Document Pipelines · Lesson 5", "Fields from an LLM",
          "reads meaning. Can also invent. Both true."),
  "On the far side of the rules boundary: documents where every author formatted things their own way. An LLM reads meaning, so it extracts what no pattern can reach — and it can invent, so nothing it returns skips validation. Both halves of that sentence run this lesson."),
 (s_code("The schema", "The contract, per document",
   ["Extract as JSON with EXACTLY these keys:", "  date (YYYY-MM-DD or null),", "  donations (number or null),", "  donations_approximate (true/false)", "Use null for anything not stated. Do not guess."],
   note="Null is permission to be honest."),
  "You do not ask, what does this say. You demand the exact row: these keys, null for anything not stated, JSON only. The schema is the contract — every document gets the same one, so every answer lands in the same table. And the null option is doing ethical work: around fifteen hundred dollars becomes a flagged estimate, not fake precision. A schema without null forces inventions."),
 (s_bullets("The trade", "Stated honestly", [
   "Rules never invent — but they quit when format varies",
   "LLMs never quit — but they can invent",
   "Route by format; validate everything from both"]),
  "The two-sided trade, with no varnish. Rules never invent — a rule cannot produce what is not there — but they quit the moment format varies. LLMs never quit — they will return a confident row for anything — but they can invent: a plausible date the document never gives. Neither extractor is trustworthy alone. Route by format. Validate everything."),
 (s_bullets("This lesson", "Extract, then audit", [
   "Route three documents in the figure — rules or LLM",
   "The notebook: schema prompt + the JSON retry loop",
   "The invention hunt: stated, inferred, or invented?"], closing=True),
  "In the figure, route three documents and read what each choice cost. The notebook builds the schema prompt and the retry loop, runs the documents that defeated lesson four — and then comes the invention hunt: audit every field as stated, inferred, or invented. At least one invention hides in the batch. Finding it is the lesson."),
]

L["chsai-docs-6"] = [
 (s_title("Document Pipelines · Lesson 6", "Trust but verify",
          "the gate before the table."),
  "Everything upstream can lie to you politely. OCR swaps characters. Rules match the wrong thing. LLMs invent. The validate stage is the gate where the lying stops — and the error rate you measure there is the number that makes your whole pipeline credible."),
 (s_code("The checks", "Four families",
   ["types:     is $l,847 a number? no.", "ranges:    21,200 families? a comma moved.", "required:  a row with no date can't sort.", "cross:     63 donations totaling $0.00?"],
   err_line=0, note="Each check catches a specific upstream lie."),
  "Four families of check, each catching a specific lie. Types: is the amount actually a number — this is where lesson two's OCR casualty finally dies. Ranges: twenty-one thousand families at one pantry means a comma moved. Required: a row with no date cannot join a time-sorted table. And cross-checks: sixty-three donations totaling zero dollars is a contradiction wearing a straight face."),
 (s_bullets("Quarantine + the numbers", "Not deleted — quarantined", [
   "Failing rows keep their reason and their source",
   "Error rate: measured, reported with the table",
   "Spot-check five PASSING rows — the gate isn't proof"]),
  "A failing row is not deleted — deletion hides problems. It goes to quarantine with its reason and its source document attached: a to-do list for human eyes, and where the interesting stories live. Then two numbers make you credible. The error rate, measured and reported with the table. And the spot-check: five random rows that passed, verified against the originals by hand — because a gate only catches what it was built to catch."),
 (s_bullets("This lesson", "Run the gate", [
   "Toggle checks off in the figure — watch lies get hall passes",
   "The notebook: four validators, seeded errors, error rate",
   "A table without these numbers is a rumor with columns"], closing=True),
  "In the figure, toggle checks off and watch specific lies walk into the table with hall passes. The notebook builds the four validators and runs a pile with seeded errors — your gate should catch all four. A table with a measured error rate and a passed spot-check is data. Anything else is a rumor with columns."),
]

L["chsai-docs-7"] = [
 (s_title("Document Pipelines · Lesson 7", "Store and ask",
          "the payoff: questions are cheap now."),
  "The pile is a validated table now. Store it where other people's tools can read it, and the questions that took an afternoon of drawer-digging take one line each — with every answer showing its work."),
 (s_code("Store", "Two formats, three lines each",
   ["pantry_2026.csv   -> opens in Excel and Sheets", "pantry_2026.json  -> keeps nulls for the next program", "+ quarantine file and cleaning log, alongside"],
   note="The organization can use the CSV without you. That's the point."),
  "Two formats cover nearly everything. CSV opens in Excel and Google Sheets — which means the organization can use it without you, and that independence is most of the point. JSON keeps the nulls and nesting for the next program. And the quarantine file and cleaning log travel with the table — the paperwork is part of the product."),
 (s_bullets("Ask", "Code computes; the model converses", [
   "Filter, sum, group: one line each, rows named",
   "LLM at the edges: vague question in, sentence out",
   "The number ALWAYS comes from the table"]),
  "Questions against structured rows are one line each — filter, sum, group — and the answer names the rows it used, reproducible by anyone. Where does the LLM fit? Not in the arithmetic — code sums perfectly and for free. It earns its place at the edges: turning a board member's vague question into the right filter, and a computed number into a newsletter sentence. The number always comes from the table."),
 (s_bullets("This lesson", "The board packet", [
   "Question the table in the figure — answers point at rows",
   "The notebook: CSV, JSON, and a board meeting's questions",
   "One newsletter paragraph, every number traced"], closing=True),
  "In the figure, put four board-meeting questions to a year of pantry data and watch every answer highlight its rows. The notebook stores the table both ways and answers questions in code — then uses the model only for phrasing. Your turn-in is a board packet where every number can be traced to the line that computed it."),
]

L["chsai-docs-8"] = [
 (s_title("Document Pipelines · Lesson 8", "Your pile",
          "every stage, your documents, one honest report."),
  "The capstone. The drawer you claimed in lesson one meets the pipeline you built in lessons two through seven — and you ship the table, the answers, and the report that lets a stranger decide how far to trust it."),
 (s_bullets("Privacy first", "Before anything runs", [
   "Permission from whoever owns the documents",
   "Real names and addresses? Rules locally, or a public pile",
   "Anything sent to an LLM leaves your machine"]),
  "Before anything runs: privacy. If the pile holds real people's information, you need permission from whoever owns it — and anything sent to an LLM leaves your machine. When in doubt, use local rules for the sensitive fields, or choose a public pile. A pipeline that leaks its documents has failed at the only stage that cannot be rerun."),
 (s_bullets("The four deliverables", "What shipping means", [
   "The table — CSV and JSON, with quarantine and log",
   "Three answered questions, each naming its rows",
   "The pipeline report — routing, error rate, spot-check",
   "The handoff note: three sentences a non-programmer can follow"]),
  "You ship four things. The table, with its paperwork. The three questions you promised in lesson one, answered with rows named. The pipeline report: what went in, what each stage did, which documents went to rules and which to the LLM and why, the measured error rate, and the spot-check verdict. And the handoff note — three sentences a non-programmer can follow, including what the table must not be used for."),
 (s_bullets("The finish", "Why the report is the grade", [
   "Anyone can produce a table",
   "The report is what makes it trustworthy to a stranger",
   "Deliver a real organization's CSV — that's the practicum, in miniature"], closing=True),
  "The report is the grade, because the report is the professional artifact. Anyone can produce a table; the report is what lets a stranger decide how far to trust it — the difference between data and a rumor with columns. And if your pile came from a real organization, deliver them the CSV and the handoff note. That delivery is the practicum, in miniature. Go ship."),
]

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    build_all(L, "Document Pipelines", only)
