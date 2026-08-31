#!/usr/bin/env python3
"""Course 7 — Build a Tiny Language Model: listen-segment narrations.
Run: /Users/john/Dropbox/_/tts/venv/bin/python audio_course7.py"""
import os, subprocess
import numpy as np
import soundfile as sf

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = "/tmp/chsai-anim"
os.makedirs(WORK, exist_ok=True)

T = {}

T[1] = ("Two minutes before you read. This course builds a language model, and "
 "version one is pure counting. Walk through text one letter at a time and "
 "tally what follows what: after t, how often h? After q, how often u? The "
 "finished table can answer a question no program you have written could "
 "answer: given this letter, what probably comes next. That table is a real "
 "language model — a bigram model — and it knows nothing about meaning or "
 "grammar. It knows what follows what, because it counted. Two things to "
 "watch for as you build it. First, the table only knows what its text "
 "taught it — count a different paragraph, get a different model. Second, "
 "any letter pair the text never contained is a zero in the table, and "
 "zeros matter enormously next lesson, when the table starts writing. "
 "Predict your three next-letters by hand before the machine counts. Being "
 "wrong there is the fun part.")

T[2] = ("Two minutes before you read. Today the table writes. Move one: divide "
 "every row by its total, so counts become betting odds that sum to one "
 "hundred percent. Move two: roll the dice. Start with a letter, look up "
 "its row, pick the next letter weighted by the odds, then look up the new "
 "letter's row and roll again. A hundred rolls later you have a line of "
 "text that has never existed anywhere. It will be gibberish — read it "
 "closely anyway. Word lengths look right. Vowels arrive on schedule. Q "
 "finds u every single time. It is wrong the way English is wrong, not the "
 "way static is wrong, because every roll is weighted by patterns counted "
 "from real text. And hold on to this: the loop you are about to build — "
 "look up, roll, append, repeat — is the same loop running inside every "
 "model you have ever talked to. Only the look-up step gets smarter from "
 "here.")

T[3] = ("Two minutes before you read. First, a failure worth having: skip the "
 "dice and always pick the most likely next letter. It's called greedy "
 "generation, and it gets stuck — if e's favorite leads to space, and "
 "space's favorite leads to t, and t's favorite leads back to e, the "
 "machine writes the the the forever. Deterministic plus a cycle equals "
 "stuck. The fix is the dice you already have, plus a dial called "
 "temperature. Cold — below one — makes favorites even more favored: safe, "
 "repetitive, loop-prone. Warm — exactly one — plays the odds as counted. "
 "Hot — above one — flattens everything toward equal, until pattern "
 "dissolves into static. This dial is not a toy: it is the temperature "
 "setting in real model dashboards, and you are about to build it. Low for "
 "facts and code. Higher for brainstorms. Find your machine's greedy loop "
 "in the notebook and catch it red-handed.")

T[4] = ("Two minutes before you read. Your machine forgets everything but the "
 "current letter, and that one-letter memory is why its output dissolves. "
 "The upgrade is obvious: condition on the last two letters, or three. It "
 "works — real words surface, then phrases. Now count the cost. One letter "
 "of context needs twenty-seven rows. Two letters: seven hundred "
 "twenty-nine. Three: nineteen thousand. Ten letters: two hundred six "
 "trillion rows, for a corpus of a few thousand characters. Almost every "
 "row would be empty — the model would know nothing, very precisely. This "
 "is the wall, and it stopped the whole field for decades: most long "
 "contexts have never occurred anywhere, so a counting model has nothing "
 "to look up. The sentence you are hearing right now has never existed "
 "before, and you understand it fine. That gap — between looking up and "
 "understanding — is exactly what the next lesson closes.")

T[5] = ("Two minutes before you read. This is the best idea in the course. "
 "Instead of a table of counts, give the model a grid of adjustable "
 "numbers — weights — that start random. Then loop: show it one real "
 "example from the corpus. Score its bet with a single number called the "
 "loss — big when the model was surprised by the truth. Nudge every weight "
 "a tiny step in the direction that would have made the loss smaller. "
 "Repeat, thousands of times. No single nudge does much; together they "
 "drag the loss down, and a falling loss means the bets are getting "
 "sharper. Why this beats counting: a table can only look up contexts it "
 "has literally seen, but learned weights generalize — similar contexts "
 "share weights, so the model bets sensibly even on combinations it never "
 "met. That property, scaled up a billionfold, is the models you talk to. "
 "The figure trains seven hundred fifty-six real weights in your browser. "
 "Nothing in it is faked. Watch the number fall.")

T[6] = ("Two minutes before you read. Models don't read letters, and they "
 "don't read words — they read tokens, and today you build the machine "
 "that invents them. Byte-pair encoding: split text into characters, count "
 "every adjacent pair, merge the most frequent one everywhere, and repeat. "
 "T plus h becomes one token. Then t-h plus e becomes the. Nobody chooses "
 "the vocabulary — frequency does, which means common words end up as "
 "single tokens and rare words stay shattered into pieces. And that "
 "explains course one's oddities mechanically: a model can miscount the "
 "letters in strawberry because it never sees letters — it sees chunks. "
 "Your own name might shatter into three pieces, and the way it splits "
 "tells you how common your name was in the training text. The whole "
 "algorithm is about forty lines. You have written harder things already.")

T[7] = ("Two minutes before you read. Today's experiment: train two identical "
 "machines on different text. The one fed formal prose writes long words "
 "and careful rhythms. The one fed chat messages writes l-o-l and drops "
 "its capitals. Same code, run twice — every difference came from the "
 "data. Now scale that up. The models you use daily were trained on a "
 "giant slice of the internet, so their voice, their assumptions, their "
 "blind spots, and their biases are the internet's, averaged. Course one "
 "said that as a warning; you can now say it as an engineer: whatever is "
 "over-represented in the data is over-represented in the odds. Two more "
 "consequences worth carrying. Data quality is model quality — feed it "
 "typos and it learns typos, faithfully. And a machine trained on your "
 "own writing picks up your voice, which you will meet personally in the "
 "capstone. Most students find that slightly unsettling. Correct.")

T[8] = ("Two minutes before you read — and before you build. The capstone: "
 "curate a corpus, train your machine, tune it, generate a page, and "
 "write the honest model card. The corpus rule is firm: your words, or "
 "words old enough to belong to everyone. Your essays and journals are "
 "perfect. Public-domain books are fine. Your group chat is not only your "
 "words, and copyrighted books are not yours to train on. Tune the "
 "context length and temperature until the output sounds most like you, "
 "mark the best and worst passages, and then write the card: what went "
 "in, what you left out, what works, what fails, and one thing the model "
 "believes that is really a fact about your corpus. Last, the ladder. "
 "Your model: a few thousand numbers. GPT-2, which stunned the field in "
 "2019: one and a half billion. Today's frontier: undisclosed, and far "
 "beyond. Same idea at every rung — look at context, place bets. You "
 "built the real thing, small.")

def main():
    from kokoro import KPipeline
    pipe = KPipeline(lang_code="a")
    for n, text in sorted(T.items()):
        chunks = [a for _, _, a in pipe(text, voice="af_heart")]
        audio = np.concatenate(chunks)
        audio = np.concatenate([audio, np.zeros(int(24000 * 0.5), dtype=audio.dtype)])
        wav = f"{WORK}/tiny-{n}-listen.wav"
        sf.write(wav, audio, 24000)
        out = f"{SITE}/audio/chsai-tiny-{n}-listen.m4a"
        subprocess.run(["ffmpeg", "-y", "-i", wav, "-c:a", "aac", "-b:a", "96k", out],
                       capture_output=True, check=True)
        print(f"{out}  ({len(audio)/24000/60:.1f} min)", flush=True)
    print("AUDIO DONE", flush=True)

if __name__ == "__main__":
    main()
