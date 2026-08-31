#!/usr/bin/env python3
"""Course 8 — Document Pipelines: listen-segment narrations.
Run: /Users/john/Dropbox/_/tts/venv/bin/python audio_course8.py"""
import os, subprocess
import numpy as np
import soundfile as sf

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = "/tmp/chsai-anim"
os.makedirs(WORK, exist_ok=True)

T = {}

T[1] = ("Two minutes before you read. Every organization has the drawer — "
 "reports, forms, minutes, in every format — and somewhere in it is the "
 "answer to a question someone keeps asking. This course builds the "
 "assembly line that turns the drawer into answers, and the line has seven "
 "stages, the same every time: collect, extract, clean, structure, "
 "validate, store, ask. Why stages instead of one giant read-it-all step? "
 "Two properties. Each stage is small enough to check — you can look at "
 "its output and see if it's right. And each stage is fixable alone — when "
 "something breaks, you repair one stage and rerun, and nothing else "
 "moves. The giant step has neither. As you read, keep one eye on your own "
 "life: the figure asks you to claim a real pile of documents, and it "
 "becomes your capstone. Pick a drawer you actually want opened.")

T[2] = ("Two minutes before you read. A PDF is not text — it's a file format "
 "with text trapped inside, stored as drawing instructions: place these "
 "characters at these coordinates. Extraction rebuilds lines from "
 "positions, and it mostly works. The word to hold onto is mostly. "
 "Formats form a ladder: text files are free, CSVs are better than free, "
 "PDFs are extraction territory, and scans are the hostile end — just "
 "pixels, where OCR guesses the characters and guesses wrong silently: L "
 "becomes one, O becomes zero. The classic casualties to memorize: "
 "headers landing mid-sentence, spacing collapsing until words fuse, "
 "characters swapped without a sound. None of it announces itself, so "
 "the rule for the whole course is: inspect what survived, every time, "
 "before building on it. Today you also build a PDF yourself, from about "
 "seven hundred raw bytes — after which the format is never magic again.")

T[3] = ("Two minutes before you read. Extraction left junk in your text, and "
 "you have forty documents, so you write cleaning functions under three "
 "rules. One fix per function — strip headers does that and nothing else, "
 "so you can test it and trust it. Compose them in order — headers out "
 "before spacing gets repaired, because order changes results. And log "
 "every change — removed three header lines, rewrote two dates. The log "
 "is the part beginners skip and professionals never do, because it's "
 "your alibi: when a number looks wrong later, the log says whether "
 "cleaning touched it, and when the organization asks whether processing "
 "altered their documents, you answer with a record instead of a shrug. "
 "The notebook ends with a mystery document carrying junk none of your "
 "four cleaners handle. Diagnosing it and adding a fifth function is the "
 "actual job, in miniature.")

T[4] = ("Two minutes before you read. Rules are patterns that match shapes — "
 "a dollar sign followed by digits, a date in one standard form, "
 "something at something dot something. Where document formats are "
 "fixed, rules are unbeatable: fast, free, perfectly consistent, and "
 "constitutionally unable to invent, because a pattern can only find "
 "what is literally there. Notice the date pattern only works because "
 "lesson three standardized the dates first — the stages are load-"
 "bearing. Then the boundary: we raised around two grand. Due next "
 "Tuesday. Contact Rosa, she knows. Rules match shapes, and those "
 "sentences have meaning, not shape. You can add rules for a while, "
 "until the rulebook is the new mess. Today you measure both halves "
 "honestly — the find-rates where rules work, and the three quoted "
 "failures where they can't. Keep the failures. They're the shopping "
 "list for lesson five.")

T[5] = ("Two minutes before you read. For documents where every author did "
 "their own thing, the extractor is an LLM — it reads meaning, so "
 "around fifteen hundred dollars becomes a usable number where no "
 "pattern matched anything. The craft is the schema prompt: demand the "
 "exact row — these keys, null for anything not stated, JSON only. "
 "Null is the ethical part: it's permission to be honest, and a schema "
 "without it forces inventions. Then the trade, stated plainly. Rules "
 "never invent but quit when format varies. LLMs never quit but can "
 "invent — a plausible date the document never gave. Neither extractor "
 "is trustworthy alone, which is why everything from both goes through "
 "validation. Your assignment is an audit: mark every extracted field "
 "as stated, inferred, or invented. At least one invention is hiding in "
 "the batch. No class API key? The precomputed outputs teach the same "
 "pattern.")

T[6] = ("Two minutes before you read. Everything upstream can lie politely — "
 "OCR swaps characters, rules match the wrong thing, LLMs invent — and "
 "the validation gate is where the lying stops. Four families of check: "
 "types, is that amount actually a number. Ranges, is twenty-one "
 "thousand families plausible, or did a comma move. Required, can a row "
 "with no date join a time-sorted table. And cross-checks, sixty-three "
 "donations totaling zero dollars is a contradiction in a suit. Rows "
 "that fail are quarantined, never deleted — deletion hides problems; "
 "quarantine keeps the row, its reason, and its source for human eyes. "
 "Then the two numbers that make you credible: the error rate, measured "
 "and reported with the table, and the spot-check — five random rows "
 "that PASSED, verified by hand, because a gate only catches what it "
 "was built to catch. A table with those numbers is data. Without them, "
 "it's a rumor with columns.")

T[7] = ("Two minutes before you read. The payoff stage. Store the table twice: "
 "CSV, which opens in Excel and Sheets so the organization can use it "
 "without you — that independence is most of the point — and JSON for "
 "the next program. The quarantine file and cleaning log ship alongside; "
 "the paperwork is part of the product. Then ask. Against structured "
 "rows, questions cost one line each — filter, sum, group — and every "
 "answer names the rows it used, so anyone can rerun it. The LLM's place "
 "here is at the edges only: turning a board member's vague question "
 "into the right filter, and turning a computed number into a newsletter "
 "sentence. The arithmetic is never the model's job — code sums "
 "perfectly, for free. The moment a number comes from anywhere but the "
 "table, you've built a very polite rumor machine.")

T[8] = ("Two minutes before you read — and before anything runs, privacy. If "
 "your pile holds real people's names or addresses, you need permission "
 "from whoever owns the documents, and anything sent to an LLM leaves "
 "your machine. When in doubt: local rules for sensitive fields, or a "
 "public pile. Then the capstone ships four things. The table, CSV and "
 "JSON, with quarantine and log alongside. The three questions you "
 "promised in lesson one, each answer naming its rows. The pipeline "
 "report — what went in, what each stage did, the routing choices, the "
 "measured error rate, the spot-check verdict. And the handoff note: "
 "three sentences a non-programmer can follow, including what the table "
 "must not be used for. The report is the grade, because the report is "
 "what lets a stranger decide how far to trust the table. And if the "
 "pile came from a real organization, deliver the CSV and the note. "
 "That delivery is the practicum, in miniature.")

def main():
    from kokoro import KPipeline
    pipe = KPipeline(lang_code="a")
    for n, text in sorted(T.items()):
        chunks = [a for _, _, a in pipe(text, voice="af_heart")]
        audio = np.concatenate(chunks)
        audio = np.concatenate([audio, np.zeros(int(24000 * 0.5), dtype=audio.dtype)])
        wav = f"{WORK}/docs-{n}-listen.wav"
        sf.write(wav, audio, 24000)
        out = f"{SITE}/audio/chsai-docs-{n}-listen.m4a"
        subprocess.run(["ffmpeg", "-y", "-i", wav, "-c:a", "aac", "-b:a", "96k", out],
                       capture_output=True, check=True)
        print(f"{out}  ({len(audio)/24000/60:.1f} min)", flush=True)
    print("AUDIO DONE", flush=True)

if __name__ == "__main__":
    main()
