#!/usr/bin/env python3
"""Course 9 — Research Agents: listen-segment narrations.
Run: /Users/john/Dropbox/_/tts/venv/bin/python audio_course9.py"""
import os, subprocess
import numpy as np
import soundfile as sf

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = "/tmp/chsai-anim"
os.makedirs(WORK, exist_ok=True)

T = {}

T[1] = ("Two minutes before you read. An agent is not a smarter model — it is "
 "the same model placed in a loop, and the loop has four words: plan, act, "
 "observe, repeat. The model reads the question and writes a request; your "
 "code runs the request and returns the result; the model reads the "
 "evidence and either asks again or answers. Two things to hold onto as "
 "you read. First, the model never touches the world — your dispatch code "
 "is the hands, and only the functions you put in its table can ever run. "
 "An agent with search and fetch cannot delete a file, no matter what it "
 "writes. Second, the agent's answer is different in kind from a "
 "chatbot's: it can say where each fact came from, because the evidence "
 "arrived during the loop with its URL attached, instead of being half-"
 "remembered from training. This course builds one specific agent — a "
 "research agent, the kind that takes a question and returns a small "
 "cited report. Today you build the loop with a scripted planner, so "
 "every turn is visible. Watch which lines come from the model and which "
 "from your code. That boundary is the whole architecture.")

T[2] = ("Two minutes before you read. A tool is a function you describe to "
 "the model: a name, what it does, what arguments it takes. The model "
 "replies with the tool's name and JSON arguments; your dispatch code "
 "looks the name up in a dictionary and runs the real function; the "
 "result goes back as the next message. That handshake is how every real "
 "agent works, and none of it is magic. What deserves a tool? Things the "
 "model cannot know — today's facts, your files, live pages — and things "
 "it cannot do reliably. Arithmetic is the classic: models predict text, "
 "and text-shaped arithmetic goes wrong quietly, so professionals hand "
 "the model a calculator instead of trusting its multiplication. Things "
 "the model knows cold need no tool at all, and tools cost time and "
 "money per call. And the safety line from lesson one holds: the model "
 "can request anything; only the dispatch table decides what runs. "
 "Deciding what hands to give an agent is a real design decision — "
 "today you make it deliberately, and in the build you'll name the tool "
 "you chose to withhold, which is the more interesting half.")

T[3] = ("Two minutes before you read. One search gives you one keyhole view, "
 "and the things it missed are silent — nothing tells you they exist. So "
 "a research agent's first real move is not searching; it is "
 "decomposition: turning the question into four to six angles, each one "
 "a separate search aimed at a different part of the answer. Is the "
 "garden growing? Plot history is one angle. Membership is another. "
 "Funding. Outside coverage. Each angle is a bet about where evidence "
 "might live, and together they cover the question the way one lucky "
 "query never can. Writing good angles takes reading the question for "
 "what it actually asks — that is meaning-work, which is why the model "
 "earns its seat at this stage. But angles are not free: each one costs "
 "searches, fetches, and reading time, and past coverage they just "
 "re-find the same pages. Enough to cover, few enough to afford — "
 "professionals land near five. In the notebook the model writes the "
 "angles and you measure what they reach, because coverage is a number, "
 "not a feeling. Remember the missing-angle lesson: whatever evidence "
 "lived there is silently absent. Nothing marks the hole.")

T[4] = ("Two minutes before you read. The gather stage has two habits and one "
 "law. Habit one: dedupe before fetching. Different angles find the same "
 "pages, and a page fetched twice wastes a call — worse, it lets one "
 "source masquerade as two independent ones later, when agreement "
 "between sources starts to matter. A set of already-seen URLs fixes it "
 "in three lines. Habit two: notes, not pages. A fetched page is mostly "
 "noise; the agent keeps the sentences that bear on the question. And "
 "the law: every note carries its receipt — the URL it came from and "
 "the date on the page — attached at gather time, when the URL is right "
 "there in your hand. Skip it and it is gone: an hour later nobody, "
 "human or model, can say which of seven pages a number came from. "
 "Every later stage reads that source field — checking claims, "
 "weighing contradictions, citing the report. Notes without receipts "
 "are rumors with nice formatting. The figure lets you feel that: same "
 "notes, receipts stripped, and a simple question you suddenly cannot "
 "answer. Receipts now, or rumors forever.")

T[5] = ("Two minutes before you read. A claim, in this course, is a statement "
 "specific enough that a source could prove it wrong. The garden has "
 "sixty plots — a claim; the census either says it or it doesn't. The "
 "garden is thriving — not a claim; nothing pins it down, no source "
 "could contradict it, and feel-good sentences like it are where sloppy "
 "research hides. Each claim is stored with three things: the "
 "statement, its source, and the exact quote that backs it. The quote "
 "is the load-bearing part — checkable on sight, where 'the source "
 "supports this' without one is just a memory. The model does the "
 "extraction because turning a rambling sentence into a dated, "
 "two-number claim is meaning-work — and because the model can also "
 "invent, every claim faces the quote audit: is the quote really on "
 "the page, and does it actually say what the claim says? One claim in "
 "today's table stretches — a real quote, a claim that quietly says "
 "more. And one claim with a perfectly real quote is still wrong, "
 "because its page is wrong. The audit can't catch that one. Lesson "
 "six can.")

T[6] = ("Two minutes before you read. Everything upstream can lie politely — "
 "stale pages, wrong pages, an extractor that invents — and "
 "verification is where the lying stops. The design insight: don't ask "
 "a model whether a claim is right. Models lean toward yes. Prompt the "
 "verifier to refute — here are the sources, find what contradicts "
 "this claim — and support comes to mean something: the claim survived "
 "a hunt for its contradiction. One pass can itself be wrong, so each "
 "claim gets three, and the majority decides. Sources get weighed "
 "along the way: two independent pages beat one blog post, a fresh "
 "census beats an old sign, and thanks to lesson four's receipts, a "
 "copied source counts once instead of twice. Claims leave labeled "
 "confirmed, plausible, or refuted — and refuted ones are quarantined "
 "with their reasons, never deleted, because what the agent declined "
 "to believe is part of an honest report. In the notebook the vote "
 "catches a six-hundred-plot typo against two better sources. Then "
 "the best assignment on this site: plant your own lie and see "
 "whether the machine you built catches you.")

T[7] = ("Two minutes before you read. The report stage is a division of labor, "
 "and the division is the craft. Code merges duplicates — sixty plots "
 "from the census and sixty from the news story become one claim with "
 "two supporting sources, stronger than either alone — and ranks by "
 "verdict: confirmed first, plausible after, refuted only in the "
 "quarantine file. The model writes the prose, under strict orders: use "
 "only these claims, cite after every factual sentence, hedge anything "
 "plausible, and name what the claims don't cover. It turns rows into "
 "readable paragraphs, which it is good at. It does not get to add "
 "facts, remember things, or round numbers. Then the limits section — "
 "not optional. No source states the budget; the lease claim rests on "
 "one page. Two sentences like that buy more trust than any confident "
 "prose, because they prove somebody checked. The final check is the "
 "number diff: every number in the report, matched to its row in the "
 "table. A number with no row is an invention that slipped through. "
 "The notebook's report has none. Your capstone's might — and now "
 "you own the tool that catches it.")

T[8] = ("Two minutes before you read — and before anything runs, the rules. "
 "What you send to a model leaves your machine: your question, your "
 "angles, anything you paste. Researching someone else's private "
 "situation shares it. Second: the live web is stale, wrong, and "
 "copied at a scale the mini-web only simulates — out there, "
 "verification is the stage doing the most work. Third, the one to "
 "carry for life: the agent's report is a draft for a human, not an "
 "oracle. Before you repeat a claim to another person, follow its "
 "citation and read the source yourself — thirty seconds, and you "
 "built the receipts precisely so a human could spend them. The "
 "technical step is small: search becomes a server-side tool, the "
 "model searches the live web during its turn, and your loop keeps "
 "its shape — search is still just a requested tool. The capstone "
 "ships four things: the cited, hedged report with its limits "
 "section; the claim table; the quarantine with its reasons; and the "
 "run report ending in your own trust paragraph — what you'd repeat, "
 "and what you'd verify by hand first. Pick a question with stakes. "
 "Caring is what makes verification feel necessary instead of "
 "ceremonial.")

def main():
    from kokoro import KPipeline
    pipe = KPipeline(lang_code="a")
    for n, text in sorted(T.items()):
        chunks = [a for _, _, a in pipe(text, voice="af_heart")]
        audio = np.concatenate(chunks)
        audio = np.concatenate([audio, np.zeros(int(24000 * 0.5), dtype=audio.dtype)])
        wav = f"{WORK}/agent-{n}-listen.wav"
        sf.write(wav, audio, 24000)
        out = f"{SITE}/audio/chsai-agent-{n}-listen.m4a"
        subprocess.run(["ffmpeg", "-y", "-i", wav, "-c:a", "aac", "-b:a", "96k", out],
                       capture_output=True, check=True)
        print(f"{out}  ({len(audio)/24000/60:.1f} min)", flush=True)
    print("AUDIO DONE", flush=True)

if __name__ == "__main__":
    main()
