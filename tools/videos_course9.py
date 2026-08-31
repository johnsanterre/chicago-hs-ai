#!/usr/bin/env python3
"""Course 9 — Research Agents: animated lesson videos.
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_course9.py [slug]"""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from vidlib import s_title, s_bullets, s_chat, s_loop, s_code, build_all

L = {}

L["chsai-agent-1"] = [
 (s_title("Research Agents · Lesson 1", "A model in a loop",
          "a chatbot remembers. An agent goes and looks."),
  "Ask a chatbot how many plots the Riverside Community Garden has, and it answers from training data — which may be nothing, or stale, or a confident guess. It cannot go look. An agent can, and an agent is not a different kind of model. It is the same model, placed in a loop."),
 (s_loop("The loop", "Four words", ["plan", "act", "observe", "repeat"],
         note="Model proposes. Code executes. Evidence returns."),
  "The loop has four words. Plan: the model reads the question and says what action it needs. Act: your code runs that action and gets a real result. Observe: the result goes back into the conversation. Repeat: the model reads the new evidence and either asks for the next action, or answers. Everything else in this course is a refinement of those four words."),
 (s_chat("Who does what", "The safety property",
   [("ai", 'ACTION: search("riverside garden plots")'),
    ("you", "CODE: search ran - 3 results, urls attached")],
   note="The model writes requests. Your dispatch decides what runs."),
  "Notice who does what. The model never touches the world — it only writes requests, in text. Your dispatch code looks the request up in a dictionary of functions and runs the real thing. An agent with search and fetch can search and fetch. It cannot delete files or send email, because you gave it no such hands. That property is yours to keep, all course long."),
 (s_bullets("This lesson", "Build the loop", [
   "Step through a five-turn run in the figure",
   "The notebook: a scripted planner over a bundled mini-web",
   "Turn-in: a transcript annotated M or C, every line"], closing=True),
  "In the figure, step through one five-turn run and watch which lines come from the model and which from your code. The notebook builds the loop with a scripted planner over a bundled mini-web — nine pages, small enough to read whole. Then annotate a transcript line by line: model or code. If you can mark every line correctly, you understand agents better than most people using them."),
]

L["chsai-agent-2"] = [
 (s_title("Research Agents · Lesson 2", "Tools",
          "described functions the model can request by name."),
  "Lesson one's planner was a script we wrote. A real model needs to be told what actions exist. That is a tool: a name, what it does, what arguments it takes — described in plain language, sent along with the question."),
 (s_chat("The handshake", "Request, dispatch, result",
   [("ai", '{"tool": "search", "query": "riverside garden founding"}'),
    ("you", 'TOOLS["search"](...) -> results, back into the conversation')],
   note="JSON request in, real result out. Five lines of dispatch."),
  "The handshake is simple. You send the question plus the tool descriptions. If the model wants an action, it replies with the tool's name and arguments as JSON. Your dispatch code looks the name up, runs the function, and sends the result back as the next message. Nothing here is magic — a dictionary lookup does the work."),
 (s_bullets("What deserves a tool", "Memory versus hands", [
   "Things the model can't know: today's facts, your files, live pages",
   "Things it can't do reliably: arithmetic - give it a calculator",
   "Things it knows cold: no tool - tools cost time and money"]),
  "What deserves a tool? Things the model cannot know: today's facts, your private files, live pages. And things it cannot do reliably — arithmetic is the classic, because models predict text, and text-shaped arithmetic fails quietly. Give it a calculator. But defining a word needs no tool at all, and tools cost time and money per call. A good agent uses them only where memory fails."),
 (s_bullets("This lesson", "Wire real tools", [
   "Watch the model choose tools for three tasks in the figure",
   "The notebook runs lesson 1's loop with the model planning",
   "Turn-in: a tool set you designed - and the tool you withheld"], closing=True),
  "In the figure, three tasks get three different calls — a search, a calculator, and no tool at all. The notebook describes search and fetch to the real model and reruns lesson one's loop with the model doing the planning. Then design a tool set for an agent that would help someone you know — and name the tool you deliberately withheld. Deciding what hands to give an agent is a real design decision. Make it on purpose."),
]

L["chsai-agent-3"] = [
 (s_title("Research Agents · Lesson 3", "One question, five searches",
          "coverage beats luck."),
  "Type one search and you get one keyhole view — and no way to know what you missed, because missing things is silent. A research agent's first real move is not searching. It is decomposition."),
 (s_loop("Angles", "Each one a bet", ["plot history", "membership", "funding", "coverage"],
         note="Each angle: where might evidence live?"),
  "Decomposition turns the question into four to six angles, each one a separate search aimed at a different part of the answer. Is the garden growing? Plot history. Membership. Funding. Outside coverage. Each angle is a small bet about where evidence might live — and together they cover the question the way one query never can."),
 (s_bullets("The trade", "Angles aren't free", [
   "Every angle costs searches, fetches, reading time",
   "Past coverage, new angles just re-find the same pages",
   "Professionals land near five"]),
  "One honest caution: more angles is not free. Every angle costs searches, fetches, and reading time — and past a point, new angles just re-find the same pages. The skill is enough angles to cover, few enough to afford. Professionals usually land near five. And writing good angles is meaning-work, which is why the model earns its seat at this stage."),
 (s_bullets("This lesson", "Measure the coverage", [
   "Toggle angles in the figure - watch facts light up",
   "The notebook: model-written angles, measured coverage",
   "Turn-in: two questions decomposed by hand AND by model"], closing=True),
  "In the figure, toggle four angles and watch which of six facts become reachable — and notice no single angle finds them alone. The notebook has the model write angles as JSON, runs each as a search, and measures coverage as a number. Then decompose two real questions yourself, by hand and by model, and compare. Which angles did the model find that you missed? Which of yours beat the model's?"),
]

L["chsai-agent-4"] = [
 (s_title("Research Agents · Lesson 4", "Gather, with receipts",
          "every note carries its source. From the start."),
  "Now the agent does the legwork. Angles become searches, searches become fetched pages, pages become notes. Two mechanical habits and one law make this stage professional."),
 (s_code("The habits", "Dedupe, then notes",
   ["seen = set()  # before every fetch", "if url in seen: skip", "notes: small, quotable pieces - not whole pages"],
   note="One source must not masquerade as two."),
  "Habit one: dedupe before fetching. Different angles find the same pages, and fetching twice wastes a call — worse, it makes one source look like two independent ones later, when agreement starts to mean something. A set of seen URLs fixes it in three lines. Habit two: notes, not pages. A fetched page is mostly noise; extract the sentences that bear on the question."),
 (s_chat("The law", "Receipts at gather time",
   [("you", '{"note": "60 plots", "source": "cityparks.gov/report-2026", "date": "2026-03-14"}'),
    ("ai", "an hour later, without that source field: which page said 60?")],
   note="Cheap now. Impossible to reconstruct later."),
  "The law: every note carries its receipt — the URL it came from and the date on the page. Do it at gather time and it costs nothing; the URL is right there in your hand. Skip it, and it is gone forever: an hour later, nobody can say which of seven pages a number came from. Every later stage — checking claims, resolving contradictions, citing the report — reads that source field."),
 (s_bullets("This lesson", "Feel the difference", [
   "The figure: same notes, receipts stripped - try to reason",
   "The notebook gathers the full mini-web run, offline",
   "Turn-in: three notes traced to their exact source sentences"], closing=True),
  "In the figure, toggle the receipts off and try to answer a simple question about independence — you can't, and that stuck feeling is the lesson. The notebook runs the full gather stage: all angles, deduped, fetched once, notes with sources. Then trace three notes back to their exact source sentences. One of them says slightly more than its page does. Find it."),
]

L["chsai-agent-5"] = [
 (s_title("Research Agents · Lesson 5", "From pages to claims",
          "falsifiable, sourced, quoted."),
  "Notes are evidence, but evidence is not yet a report. The next compression is claims — and the word has a precise meaning: a statement specific enough that a source could prove it wrong."),
 (s_bullets("Claim or vibe", "The test", [
   "'The garden has 60 plots (2026)' - a source can contradict it. Claim",
   "'The garden is thriving' - pins nothing down. Vibe",
   "Rewrite the vibe with numbers and it becomes a claim"]),
  "The garden has sixty plots — that's a claim; the census either says it or it doesn't. The garden is thriving — that's not a claim; no source can contradict it, because it pins nothing down. Feel-good sentences are where sloppy research hides. A research agent's report is built only from the checkable kind."),
 (s_code("The claim record", "Statement, source, quote",
   ['{"claim": "60 plots in 2026",', ' "source": "cityparks.gov/report-2026",', ' "quote": "Riverside Community Garden: 60 plots"}'],
   note="The quote is checkable on sight. Memory is not."),
  "Each claim keeps three things: the statement, the source, and the exact quote that backs it. The quote matters most — it is the difference between 'the source supports this' and 'I remember the source supporting this.' If you took Document Pipelines, this is the schema prompt again: same JSON contract, same null rule, aimed at sentences instead of form fields."),
 (s_bullets("This lesson", "Audit the extraction", [
   "Sort six statements in the figure: claim or vibe",
   "The notebook: model extracts, the quote-audit checks",
   "Turn-in: every claim marked backed, stretched, or unbacked"], closing=True),
  "In the figure, sort six statements: could a source prove this wrong? The notebook has the model extract a claim table from the mini-web, then runs the audit: is every quote really on its page, and does the quote actually say what the claim says? One claim in the table stretches — a real quote, a claim that quietly says more. Finding it is the assignment, and the habit."),
]

L["chsai-agent-6"] = [
 (s_title("Research Agents · Lesson 6", "Verification",
          "try to kill every claim. Keep what survives."),
  "Everything upstream can lie politely. Pages go stale — the garden's own site still says 48. Pages are wrong — one blog says 600 plots, a typo with no editor. And the extracting model can invent. This stage is where the lying stops."),
 (s_chat("The adversarial move", "Refute, don't confirm",
   [("you", "Here are the sources. Find evidence that CONTRADICTS this claim."),
    ("ai", "cityparks census states 60 plots - the 600 claim is refuted")],
   note="Models like to agree. So ask them to attack."),
  "Asking a model 'is this right?' invites agreement — models like to say yes. So the verifier is prompted the opposite way: here is the claim, here are the sources, find what contradicts it. Trying to kill the claim and failing — that is what support means. This one prompt-design choice is most of what makes verification real."),
 (s_loop("The vote", "Three passes, majority", ["pass 1", "pass 2", "pass 3", "verdict"],
         note="One pass can be wrong. Two agreeing sources beat one blog."),
  "One verification pass can itself be wrong, so each claim gets three, and the majority decides. Sources get weighed along the way: two independent pages agreeing beat one blog post, a 2026 census beats a 2023 sign, and a source that copied another counts once. Claims leave labeled confirmed, plausible, or refuted — and refuted claims are quarantined with their reason, never deleted."),
 (s_bullets("This lesson", "Break it to learn it", [
   "Run the three-verdict vote in the figure",
   "The notebook catches the 600-plot typo mechanically",
   "Turn-in: plant a lie, rerun the pipeline, report what happened"], closing=True),
  "In the figure, run the vote and watch one claim die, one get hedged, one survive clean. The notebook builds the verifier both ways — scripted, so you see the vote mechanics, and with the model prompted to refute. Then the best assignment on this site: plant your own lie in the mini-web, rerun everything, and report whether the vote caught it. If it slipped through, explaining why is worth more than catching it."),
]

L["chsai-agent-7"] = [
 (s_title("Research Agents · Lesson 7", "The report shows its work",
          "every number cited. Every gap admitted."),
  "The last stage is the one readers see, and it is mostly discipline about who does what. Code merges and ranks. The model writes prose. And the facts come from the table — nothing else."),
 (s_code("Code's half", "Merge, then rank",
   ["'60 plots (census)' + 'now 60 (news)' -> one claim, two sources", "confirmed first, plausible after", "refuted -> quarantine file, with reasons"],
   note="Two sources agreeing is evidence. Twice-counted is decoration."),
  "Code merges duplicates: sixty plots from the census and sixty from the news story are one fact with two supporting sources — which is stronger than either alone. Then claims sort by verdict: confirmed first, plausible after, refuted nowhere except the quarantine file, where they sit with their reasons for anyone who asks."),
 (s_chat("The model's half", "Prose from the table only",
   [("you", "Use ONLY these claims. Cite after every fact. Hedge the plausible ones. Name the gaps."),
    ("ai", "The garden reached 60 plots in 2026 [cityparks.gov]...")],
   note="The model turns rows into paragraphs. It does not get to add facts."),
  "The writing prompt is strict: use only these claims, cite the source after every factual sentence, hedge anything labeled plausible, and if the claims don't answer part of the question, say so. The model is good at turning rows into readable paragraphs. It does not get to add facts, remember things, or round numbers. Every number traces to a row, every row to a quote, every quote to a URL."),
 (s_bullets("This lesson", "The limits section", [
   "Toggle citations and hedges in the figure - watch trust move",
   "The notebook diffs the report's numbers against the table",
   "Turn-in: the number-to-row list, complete"], closing=True),
  "The limits section is not optional. No source states the budget; the lease claim rests on one page — two sentences like that do more for credibility than any confident prose, because they prove somebody checked. In the figure, strip the citations and hedges and watch the same true sentences become untrustworthy. The notebook ends with the number diff: every number in the report, matched to its row. A number with no row is an invention — and now you can catch it."),
]

L["chsai-agent-8"] = [
 (s_title("Research Agents · Lesson 8", "Your question",
          "the whole machine, pointed at something you care about."),
  "Everything is built. This lesson points it at a question you choose, and adds the two pieces that make it real: the live web, and the rules for using it."),
 (s_code("Real search", "One line, same shape",
   ['tools=[{"type": "web_search_20260209",', '        "name": "web_search"}]', "# the model searches the live web during its turn"],
   note="Search is still a requested tool - it just runs on the provider's side."),
  "For real questions, search becomes a server-side tool: include it in the request, and the model searches the live web during its turn, returning answers with the URLs it used. Your loop doesn't change shape — search is still a tool the model requests, exactly like lesson two. The notebook shows both paths: the mini-web, free and deterministic, and the live web with the class key."),
 (s_bullets("The rules", "Before anything runs", [
   "What you send to a model leaves your machine",
   "The live web is wrong at scale - verification is the working stage",
   "The report is a draft for a human. Verify before you repeat"]),
  "Three rules before anything runs. What you send to the model — your question, your angles — leaves your machine; other people's private situations are theirs. The live web contains stale, wrong, and copied pages at a scale the mini-web only simulates — out there, verification is the stage doing the most work. And the one to carry for life: the agent's report is a draft for a human. Before you repeat a claim to another person, follow the citation and read the source. Thirty seconds. You built the receipts so a human could spend them."),
 (s_bullets("The capstone", "Four deliverables", [
   "The cited, hedged report - with a Limits section",
   "The claim table and the quarantine, receipts intact",
   "The run report: angles, fetches, and your own trust paragraph"], closing=True),
  "Ship four things: the report, cited and hedged, with its limits section. The claim table. The quarantine — what the agent refused to believe, and why. And the run report, ending with your own trust paragraph: what you'd repeat from this report, and what you'd verify by hand first. Pick a question with stakes — one where you care whether the answer is right. Caring is what makes verification feel necessary instead of ceremonial. Go find something out."),
]

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    build_all(L, "Research Agents", only)
