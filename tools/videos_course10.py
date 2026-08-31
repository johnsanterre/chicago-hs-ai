#!/usr/bin/env python3
"""Course 10 — Ask Your Documents: animated lesson videos.
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_course10.py [slug]"""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from vidlib import s_title, s_bullets, s_chat, s_loop, s_code, build_all

L = {}

L["chsai-ask-1"] = [
 (s_title("Ask Your Documents · Lesson 1", "The model never read your stuff",
          "your handbook was not in the training data."),
  "Ask a model about your school's retake policy and it has nothing to work with. Your handbook, your club's minutes, your notes — none of it was in the training data. Models that answer anyway are guessing from what other schools' documents tend to say. Fluent, specific, and unanchored."),
 (s_bullets("The obvious fix fails", "Paste it all in?", [
   "Context is working memory - small, and you pay per word",
   "Real piles don't fit; a 200-page handbook is ~400,000 characters",
   "One relevant paragraph under 199 pages of noise answers worse"]),
  "The obvious fix: paste the handbook into the chat. For one page, that works — the model answers well from text you put in front of it, and that fact powers this whole course. What breaks is scale. The context window is working memory, not a library: real piles don't fit, you pay for every word, and burying the relevant paragraph under two hundred irrelevant pages makes answers worse, not better."),
 (s_loop("The architecture", "Three verbs", ["store", "retrieve", "ask"],
         note="The pile stays outside. Only the relevant pieces go in."),
  "So the architecture that works keeps the pile outside the model and moves only the relevant pieces in, per question. Store: your documents, split into pieces, in your own storage. Retrieve: for each question, find the few pieces most likely to hold the answer. Ask: hand the model those pieces plus the question, with orders to answer only from them. Steps one and two are plain code. Only step three touches a model at all."),
 (s_bullets("This lesson", "Feel the problem", [
   "The figure: one question, three strategies, one context meter",
   "The notebook: guess, paste-everything, and hand-picked context",
   "Turn-in: your pile, inventoried, plus three real questions"], closing=True),
  "In the figure, watch the context meter under three strategies — memory only, paste everything, retrieve first. The notebook lets you feel all three against a bundled school pile. Then choose your own pile — a handbook, club documents, a rulebook, notes — and write three questions you genuinely want answered. That pile is your capstone. Pick one you'll actually use."),
]

L["chsai-ask-2"] = [
 (s_title("Ask Your Documents · Lesson 2", "Chunking",
          "the chunk is the unit of retrieval."),
  "Retrieval finds pieces, so the pile must become pieces first. Chunks are the atoms of this system: what gets scored, what gets found, what lands in front of the model. Cut badly, and every later stage inherits it."),
 (s_code("Two failures", "Small and large",
   ["too small: 'one retake per semester' - retake of WHAT?", "  (the condition was two sentences up, other chunk)", "too big: the answer, buried at line 41 of 60"],
   err_line=0, note="Orphaned meaning, or buried meaning."),
  "Cut too small and meaning gets orphaned: the chunk that says one retake per semester no longer says it applies to finals only — that was two sentences up, in a different chunk now. True and useless. Cut too big and you're back to paste-everything in miniature: the answer is in there, buried in forty paragraphs of noise, scoring poorly and spending your context on padding."),
 (s_bullets("The working answer", "Cut on structure", [
   "Documents have seams: headings, sections, paragraph breaks",
   "A few hundred words, aligned to sections, with overlap at cuts",
   "Every chunk keeps its receipt: which document, which section"]),
  "The working answer: cut on structure, not just length. Documents come with seams — headings, sections, paragraph breaks — and those seams are where meaning already separates. A few hundred words per chunk, aligned to sections, with a sentence of overlap at each cut so a rule and its condition never end up strangers. And every chunk keeps its receipt, because the citation in the final answer starts here."),
 (s_bullets("This lesson", "Measure the knife", [
   "Three cuts of the same pile in the figure",
   "The notebook counts which answers survive each knife",
   "Turn-in: your pile chunked - two good cuts, one casualty, your fix"], closing=True),
  "In the figure, the same question meets three chunkings and only one hands the model the whole rule. The notebook cuts the pile three ways and counts which known answers survive each knife intact — the trade-off as numbers. Then chunk your own pile, read ten random chunks, and report two well-cut ones and one the knife hurt. Every retrieval system you ever build starts with this decision."),
]

L["chsai-ask-3"] = [
 (s_title("Ask Your Documents · Lesson 3", "Search by words",
          "rare words shout. And words still aren't meanings."),
  "The first retriever is honest arithmetic: score every chunk by the words it shares with the question, and return the top few. Built in an afternoon, visible all the way down — and it powered real search engines for decades."),
 (s_code("Rarity weighting", "Not all shared words vote equally",
   ["sharing 'the'     - every chunk has it. Silence.", "sharing 'retake'  - one section in the pile. A shout.", "score = sum of 1/df for each shared word"],
   note="df = how many chunks contain the word."),
  "The one idea that makes word search work: weight rare words most. Sharing 'the' with a chunk means nothing. Sharing 'retake' means nearly everything — one section in the whole pile uses it. So each word votes with weight one over its document frequency: common words whisper, rare words shout. The notebook builds it from scratch, every number printable."),
 (s_chat("The break", "Same meaning, different words",
   [("you", "when do we get to leave early midweek?"),
    ("ai", "best chunk: 'dismissal at 1:30 PM every Wednesday' - ranked 6th. Not retrieved.")],
   note="No error. No warning. Silent."),
  "Now the break. When do we get to leave early midweek — the answering chunk says dismissal at one thirty every Wednesday. Same idea, different words, and word arithmetic has no idea. The chunk ranks sixth; top-three retrieval never sees it; the model downstream answers from noise or refuses. And notice the kind of failure: silent. No error appears. You just get worse answers, and unless you're measuring, you won't know."),
 (s_bullets("This lesson", "Measure the failure honestly", [
   "The figure: two queries, four chunks, scores visible",
   "The notebook: ten questions, hit or miss, diagnosed",
   "Turn-in: your ten-question set - it measures everything after"], closing=True),
  "In the figure, watch the scoring succeed on a fair fight and fail silently on a synonym. The notebook runs a ten-question set and measures the failure rate — then you diagnose every miss: absent, or present in different words? Build the same set for your pile and keep it. From here on, every improvement gets measured against those ten questions. That habit is worth more than any single technique."),
]

L["chsai-ask-4"] = [
 (s_title("Ask Your Documents · Lesson 4", "Meaning as numbers",
          "similar meanings, nearby vectors."),
  "Lesson three died on a fact: words are not meanings. The repair is one of the best ideas in modern AI. An embedding model turns text into a list of numbers — with one trained-in property: similar meanings land close together."),
 (s_bullets("The map", "Position is meaning", [
   "Every chunk becomes a point; clusters form by topic, unsorted",
   "The question becomes a point on the same map",
   "Retrieval = return the nearest chunks. Geometry."]),
  "Picture a map. Every chunk gets a point: schedule chunks cluster here, grading rules there, club minutes in a third region — not because anyone sorted them, but because meaning determines position. A question becomes a point on the same map, and retrieval becomes geometry: return the chunks nearest the question. Closeness is one small formula — cosine similarity — and the notebook builds it in three lines."),
 (s_code("The control experiment", "Vectors alone don't do it",
   ["word-count cosine: still ranks the dismissal chunk low", "the trained model: ranks it FIRST", "the difference is what training on billions of sentences buys"],
   err_line=0, note="It learned that 'leave early' and 'dismissal' share contexts."),
  "The notebook runs a control experiment first: cosine similarity over word-count vectors — real vector math — still misses the synonym question, because counting spelling is still spelling. Then the trained model, small and free, downloaded in seconds: it learned from billions of sentences that leave-early and dismissal live in the same contexts, and the miss closes. That knowledge is what the numbers encode."),
 (s_bullets("This lesson", "Before and after", [
   "Drop questions on the map in the figure",
   "The notebook: the full question set, words vs meaning, measured",
   "Turn-in: your before/after table, with diagnosis"], closing=True),
  "In the figure, drop three questions on the map and watch the nearest chunks light up — including the synonym question landing beside the dismissal chunk it shares no words with. The notebook reruns the whole question set both ways and prints the before-and-after table. Run it on your pile. Expect the synonym rows to flip. Anything that didn't flip goes in your pocket — it's lesson seven's raw material."),
]

L["chsai-ask-5"] = [
 (s_title("Ask Your Documents · Lesson 5", "Retrieve, then ask",
          "the pieces assemble. The prompt is a contract."),
  "Everything is built; today it clicks together. Embed the question. Take the nearest chunks. Build the prompt. Ask. Four moves — and the fourth one carries this lesson, because the prompt is not 'here's some stuff.' It is a contract."),
 (s_code("The contract", "Three clauses, three failures prevented",
   ["Answer using ONLY the provided sections.", "Cite the section after each fact.", "If they don't contain the answer, say exactly that."],
   note="Blending. Rumor-mode. Confident invention."),
  "Clause one: answer only from the provided sections — without it, the model blends your documents with training-data guesses, and you can't see the seam. Clause two: cite the section after each fact — the receipts traveled from chunking through retrieval precisely so the answer could carry them. Clause three, the hardest-working sentence: if the sections don't contain the answer, say exactly that."),
 (s_chat("The refusal is a feature", "Edges, honored",
   [("you", "What does the ski trip cost?"),
    ("ai", "That isn't in the provided documents. The sections cover retakes, appeals, and late work.")],
   note="A visible failure you can fix beats one you swallow."),
  "That third clause turns retrieval failure into an honest refusal instead of a plausible invention. A model handed the wrong chunks writes something reasonable-sounding anyway — that's what models do. Under the contract, the failure surfaces where you can see it and fix it. A system that knows the edge of its pile is trustworthy inside it."),
 (s_bullets("This lesson", "Run the whole system", [
   "Step through the four stations in the figure",
   "The notebook: ask() end to end over the school pile",
   "Turn-in: ten answers graded - right, cited, refusal-type"], closing=True),
  "In the figure, one question rides all four stations: embed, retrieve, contract, answer. The notebook wires it into one ask function and runs the question set end to end. Then grade ten answers on your own pile: right or wrong, cited or not — and for every refusal, was it correct, or a retrieval miss wearing honesty? The receipts let you tell. That distinction is lesson six's whole subject."),
]

L["chsai-ask-6"] = [
 (s_title("Ask Your Documents · Lesson 6", "Grounded or invented",
          "fluency is constant. Check the claims."),
  "Here is the uncomfortable truth at the center of every ask-your-documents system: the answer sounds exactly as good when retrieval failed. Handed the right chunk, the model writes a correct answer. Handed the wrong ones — it writes a fluent answer anyway."),
 (s_chat("The near miss", "The dangerous case",
   [("ai", "Permission forms are typically due one week before the trip."),
    ("you", "'typically' - no provided chunk says this. The real rule says five school days.")],
   note="Plausible, confident, and not from your documents."),
  "The dangerous case is the near miss: chunks close enough that the model answers, wrong enough that the answer is subtly off. Typically due one week before — plausible, confident, and drawn from what handbooks usually say, not from yours. Your school's rule says five school days. Nothing about the sentence's tone warns you."),
 (s_bullets("The grounding check", "Claim by claim", [
   "Find each claim in the provided chunks - present means grounded",
   "Absent means invented - even if it happens to be true",
   "'True but ungrounded' still fails: you'd be grading luck"]),
  "So professionals check claim by claim: take each factual claim in the answer and find it in the provided chunks. Present: grounded — you can point at its support. Absent: invented, no matter how reasonable, and no matter that it might even be true — because your system can't tell true-but-ungrounded from confident fiction, and grading luck is not grading. The check runs by eye, and it runs as a second model call: list every claim the sections don't support. A model checking text against text is reading, not remembering."),
 (s_bullets("This lesson", "Train your eye", [
   "The figure: two runs, click each claim to test it",
   "The notebook: sabotaged retrieval, then the checker catches it",
   "Turn-in: your ten answers audited at claim level"], closing=True),
  "In the figure, two runs of the same question — click each claim and test it against the chunks; one confident paragraph holds one real claim and one invention. The notebook sabotages retrieval on purpose, generates near-miss answers, and builds the checker that catches them. Then audit your own ten answers claim by claim, and trace every invention to its cause: wrong chunks arrived, or the contract got ignored. The fixes are different — and that's lesson seven."),
]

L["chsai-ask-7"] = [
 (s_title("Ask Your Documents · Lesson 7", "When retrieval fails",
          "four mechanisms. Four fixes. Zero vibes."),
  "Your question set has misses. Good — misses with receipts are diagnosable, and nearly all of them come from one of four mechanisms. This lesson is the repair manual."),
 (s_bullets("The catalog", "Four mechanisms", [
   "Straddle: rule in one chunk, condition in the next - re-chunk",
   "Cutoff: the answer ranked 4th, you kept 3 - raise k, watch cost",
   "Phrasing: slang lands in the wrong region - rewrite the query",
   "Absence: it isn't in the pile - add it, or let the refusal stand"]),
  "Mechanism one: the answer straddled a cut — fix the chunking. Two: the right chunk ranked fourth and your top-k kept three — found, then discarded at the cutoff; raise k, knowing every extra chunk spends context and adds noise. Three: the question's phrasing lands far from the answer's — one cheap model call rewrites 'when can we bail early' into 'what time is early dismissal' before embedding. Four: the answer isn't in the pile — and no retriever finds what isn't there."),
 (s_code("The discipline", "Never tune blind",
   ["change ONE stage", "rerun the FULL question set", "compare hit counts - fixes can break hits"],
   note="'It feels better now' is how systems drift worse."),
  "The discipline tying it together: never tune blind. One stage changed at a time, the full question set rerun after — not just the fixed questions, because a re-chunk that saves one answer can orphan another. Tuning by vibes is how systems drift worse while everyone nods. If you took Build with LLMs, this is the eval lesson again, with more stages to blame."),
 (s_bullets("This lesson", "Diagnose and repair", [
   "The figure: four misses - pick the mechanism, get the fix",
   "The notebook: engineered misses, repaired, measured",
   "Turn-in: your two worst misses, fixed, both tables shown"], closing=True),
  "In the figure, read four failed retrievals and pick the stage you'd fix — the fix follows the mechanism, every time. The notebook seeds all four failures over the school pile, walks each diagnosis, applies each fix, and shows the before-and-after numbers. Then repair your own two worst misses and report both full tables — including anything your fix broke. A repair manual beats a mystery. That's the lesson."),
]

L["chsai-ask-8"] = [
 (s_title("Ask Your Documents · Lesson 8", "Your pile, for real",
          "ship it with its edges labeled."),
  "Everything assembles today — and the assembly starts with questions that aren't technical. Whose documents are these? Who said you could use them? And what happens to a question after it's asked?"),
 (s_bullets("Privacy, first", "The data path", [
   "Chunking and embedding run local in your notebook",
   "Every question + its retrieved chunks go to the model provider",
   "Sensitive parts come out BEFORE the pile goes behind a system"]),
  "Know your system's data path. Chunking and embedding run local. But at answer time, every question — and every retrieved chunk sent with it — goes to the model's provider. A pile you wouldn't paste into a chat needs its sensitive parts removed before it goes behind an answering system. Documents with real people's names need permission from whoever owns them. When in doubt, run a public pile."),
 (s_code("The limits label", "From measurements, not hopes",
   ["Covers: academics, schedule, trips, clubs", "Measured: 100% on the 6-question eval", "A cited answer is checkable. An uncited one is a bug."],
   note="The label regenerates every time a dial changes."),
  "Real tools ship with their limits attached: what the pile covers and what it doesn't, the measured hit rate from your own eval, and the standing instruction — a cited answer is checkable; an uncited one is a bug; report it. Every dial you set this course — chunk size, k, the rewriting step, the refusal floor — now has a number defending it. The label is where those numbers face the user."),
 (s_bullets("The capstone", "Find your user", [
   "The working notebook, runnable by a stranger",
   "The eval table and the limits label",
   "The field report: who used it, and what their questions broke"], closing=True),
  "Ship four things: the working notebook with your pile and your dials. The eval table. The limits label. And the field report — because the point of this course is a user: a sibling who needs the team schedule, a club officer buried in old minutes, a parent facing a rulebook. Watch them ask real questions. Their third question — the one you never anticipated — will teach you more than any lesson on this site. Then check back in a week, and write down whether they're still using it. That's the realest number this course produces."),
]

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    build_all(L, "Ask Your Documents", only)
