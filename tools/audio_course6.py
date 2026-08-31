#!/usr/bin/env python3
"""Course 6 — Think with AI: listen-segment narrations.
Run: /Users/john/Dropbox/_/tts/venv/bin/python audio_course6.py"""
import os, subprocess
import numpy as np
import soundfile as sf

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = "/tmp/chsai-anim"
os.makedirs(WORK, exist_ok=True)
os.makedirs(f"{SITE}/audio", exist_ok=True)

T = {}

T[1] = ("Two minutes before you read. This course starts with a sorting habit, "
 "and the habit has three buckets. Delegate: tasks you hand over completely — "
 "safe only when the stakes are low and you can check the result yourself in "
 "seconds. Brainstorms. Practice quizzes. Explanations. Collaborate: the work "
 "splits — the AI drafts and you decide, or you draft and it critiques. "
 "Anything that goes out under your name lives in this bucket. Never: graded "
 "work presented as yours, decisions about people, anything you could not "
 "verify or defend out loud. Two tests decide the bucket every time. Can I "
 "check the result? And does this carry my name? The reading walks the buckets, "
 "the figure makes you sort nine real tasks, and some of them are genuinely "
 "arguable — that is on purpose. Sorting is a judgment skill, and judgment "
 "needs practice on hard cases, not easy ones.")

T[2] = ("Two minutes before you read. The first answer is a first draft — from "
 "a machine that does not know your situation yet. This lesson is the three "
 "moves that come after. Steer: say what is wrong and what direction to go, "
 "with specifics. Not, make it better. Instead: too generic — I have four "
 "days, two are busy, the test is chapters three to five. Show an example: "
 "paste something in the style you want and say, match this. One example "
 "beats three sentences of description. And start clean: when a chat is "
 "built on a wrong assumption the AI keeps returning to, stop arguing. Open "
 "a fresh chat and write a better first ask with everything the wreck taught "
 "you. People who use AI well are not writing magic prompts. They are having "
 "better second exchanges. The figure puts you in a conversation going wrong "
 "and lets you fix it.")

T[3] = ("Two minutes before you read. Here is the uncomfortable fact about "
 "studying: rereading feels productive because the pages start to look "
 "familiar, and familiar is not known. Memory is built by retrieval — being "
 "forced to pull the answer out of your own head, struggling for a second, "
 "and finding out immediately whether you had it. The struggle is the "
 "mechanism, not a malfunction. So this lesson turns the AI into a "
 "quizmaster, with five settings: one question at a time. Wait for my "
 "answer. Tell me exactly what I missed. Get harder as I improve. And the "
 "non-negotiable one — quiz me only from the notes I pasted. That last "
 "setting exists because the model can invent facts with total confidence, "
 "and studying invented facts is worse than not studying. Your notes in, "
 "its inventions out. Configure the tutor in the figure, then run it on a "
 "real test this week.")

T[4] = ("Two minutes before you read. There are two ways to point an AI at "
 "your writing. The ghostwriter: rewrite this, make it good. What comes back "
 "is smooth, correct, and hollow — it sounds like the average of everything, "
 "because that is literally what the model is. The coach: critique this, do "
 "not rewrite it. Point at my three weakest sentences and say why. Argue "
 "against my thesis. Then you rewrite, and every word of the revision is "
 "yours. The line between them fits in one question: could you defend every "
 "sentence as yours, out loud, to the teacher who assigned it? Know your "
 "school's policy, and when AI help is allowed, one honest sentence covers "
 "you: I drafted this myself, used AI to critique it, and revised. The "
 "figure runs one paragraph down both paths so you can feel the difference "
 "before you try it on your own writing.")

T[5] = ("Two minutes before you read. Two facts, both true, and the workflow "
 "has to hold both. Fact one: for getting oriented in a new topic, the AI is "
 "the best tool ever built — the sides of the debate, the vocabulary, the "
 "questions worth asking, in thirty seconds. Fact two: it can hand you a "
 "wrong date, a wrong number, or a source that has never existed, in the "
 "same confident tone. So the workflow is two passes. Pass one, the map: "
 "use it freely. Pass two, the verify pass: anything with a number, a name, "
 "a date, or a quote gets checked against a source you can actually open "
 "before you repeat it. And know this about fabricated citations: the "
 "formatting is always perfect. Author, title, publisher, year — formatting "
 "proves nothing. The figure hands you a research brief with two wrong "
 "claims hiding in it. Find them.")

T[6] = ("Two minutes before you read. Big assignments do not stall because "
 "they are hard. They stall because they do not fit in a day — a four-week "
 "project sits in your head as one giant object, too big to start, so you "
 "don't. The fix is splitting: break the thing, then break the pieces, "
 "until every task passes two tests. It fits in one sitting. And it has a "
 "visible finish — you know when it is done. The AI is a strong splitting "
 "partner if you give it your real constraints, and then do the three "
 "things it cannot: push back on lazy splits — step two, do the research, "
 "is still three tasks. Add the steps it cannot know about, like the week "
 "your cousins visit. And put the dates on yourself, with the scary task "
 "early. The figure lets you split a science fair project down to green — "
 "every piece one sitting, every piece finishable.")

T[7] = ("Two minutes before you read. Look at a month of your AI use and the "
 "repeats jump out: the email that has to sound right, the long reading you "
 "need the short version of, practice questions before every test. The "
 "tenth time you type the same kind of prompt, you have a workflow — and a "
 "workflow is worth writing down as a template: a prompt with slots. The "
 "slots are the parts that change today. Everything outside the slots is "
 "judgment you wrote down once — the tone, the format, the limits that keep "
 "it honest. Keep your templates somewhere boring and permanent, like a "
 "phone note titled, my prompts. Five templates you actually reuse beat "
 "fifty screenshots you will never find. And improve them every time one "
 "comes back missing something. The figure has three working templates — "
 "two are yours to steal, and the lesson is finding the third one, the one "
 "that is actually yours.")

T[8] = ("Two minutes before you read — and this time, before you run the "
 "capstone. One real school week with your AI partner, documented. Sunday: "
 "split the week and sort every task into its bucket. All week: tutor "
 "sessions before tests, critique mode on anything you write, the verify "
 "pass on any fact before you repeat it, your templates for the repeats. "
 "The log is the assignment: what you asked, what came back, and the "
 "verdict — kept, fixed, or thrown out. Failures are required. A spotless "
 "log means light use, or no scrutiny. Friday, you write the playbook: one "
 "page, your voice — your buckets, your tutor prompt, your templates, your "
 "never-list, and the one rule you would give a friend starting out. That "
 "page is the product of this course. Present it, defend it, and expect it "
 "to change by spring.")

def main():
    from kokoro import KPipeline
    pipe = KPipeline(lang_code="a")
    for n, text in sorted(T.items()):
        chunks = [a for _, _, a in pipe(text, voice="af_heart")]
        audio = np.concatenate(chunks)
        audio = np.concatenate([audio, np.zeros(int(24000 * 0.5), dtype=audio.dtype)])
        wav = f"{WORK}/think-{n}-listen.wav"
        sf.write(wav, audio, 24000)
        out = f"{SITE}/audio/chsai-think-{n}-listen.m4a"
        subprocess.run(["ffmpeg", "-y", "-i", wav, "-c:a", "aac", "-b:a", "96k", out],
                       capture_output=True, check=True)
        print(f"{out}  ({len(audio)/24000/60:.1f} min)", flush=True)
    print("AUDIO DONE", flush=True)

if __name__ == "__main__":
    main()
