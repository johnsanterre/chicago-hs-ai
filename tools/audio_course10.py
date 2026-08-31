#!/usr/bin/env python3
"""Course 10 — Ask Your Documents: listen-segment narrations.
Run: /Users/john/Dropbox/_/tts/venv/bin/python audio_course10.py"""
import os, subprocess
import numpy as np
import soundfile as sf

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = "/tmp/chsai-anim"
os.makedirs(WORK, exist_ok=True)

T = {}

T[1] = ("Two minutes before you read. Your handbook was never in the training "
 "data — neither were your club's minutes or your notes — so a model "
 "asked about them guesses from what other people's documents tend to "
 "say. Fluent, specific, and unanchored, which is the worst combination, "
 "because nothing in the answer's tone warns you. The obvious fix is "
 "pasting everything into the chat, and for one page it genuinely works: "
 "the model answers well from text you put in front of it. Hold onto "
 "that fact — it powers the whole course. What breaks is scale. The "
 "context window is working memory, not a library: real piles don't "
 "fit, you pay for every word you send, and one relevant paragraph "
 "buried under two hundred irrelevant pages answers worse, not better. "
 "So the architecture is three verbs. Store: your documents, cut into "
 "pieces, in your own storage. Retrieve: per question, find the few "
 "pieces likely to hold the answer. Ask: hand the model those pieces "
 "with orders to answer only from them. Two of the three verbs are "
 "plain code you'll own completely. As you read, pick your pile — it "
 "becomes your capstone, and the best pile is one you actually want "
 "answers from.")

T[2] = ("Two minutes before you read. A chunk is the atom of this whole "
 "system: it is what gets scored against your question, what gets "
 "retrieved, and what lands in front of the model. Cut badly and every "
 "later stage inherits it. Cut too small and meaning gets orphaned — "
 "the chunk that says one retake per semester no longer says finals "
 "only, because that condition was two sentences up and now lives in a "
 "different atom. The retrieved piece is true and useless. Cut too big "
 "and the answer gets buried — one relevant line inside forty "
 "paragraphs, scoring poorly because the chunk is mostly noise, and "
 "spending your context on padding when it is retrieved anyway. The "
 "working answer: cut on structure. Documents come with seams — "
 "headings, sections, paragraph breaks — where meaning already "
 "separates. A few hundred words per chunk, aligned to those seams, "
 "with a sentence of overlap at each cut so a rule and its condition "
 "never end up strangers. And every chunk keeps a receipt — which "
 "document, which section — because the citation in your final answer "
 "is born here. In the notebook the trade-off becomes numbers: three "
 "knives, five questions, count what survives.")

T[3] = ("Two minutes before you read. The first retriever is honest "
 "arithmetic: score every chunk by the words it shares with the "
 "question, return the top few. The one idea that makes it work is "
 "rarity weighting. Sharing 'the' with a chunk means nothing — every "
 "chunk has 'the'. Sharing 'retake' means nearly everything — one "
 "section in the whole pile uses it. So each shared word votes with "
 "weight one over its document frequency: common words whisper, rare "
 "words shout. That idea powered real search engines for decades, and "
 "you build it today from scratch, every number printable. Then the "
 "break. Ask when do we get to leave early midweek, and the answering "
 "chunk — dismissal at one thirty every Wednesday — shares no "
 "meaningful word with the question. Same idea, different words, and "
 "word arithmetic has no idea. The chunk ranks sixth. Top-three "
 "retrieval never sees it. And notice the shape of the failure: "
 "silent. No error, no warning — just a worse answer downstream, "
 "which is why the lesson ends with a ten-question set and a measured "
 "failure rate. Build the same set for your pile and keep it. "
 "Everything after this gets measured against it.")

T[4] = ("Two minutes before you read. An embedding model reads a piece of "
 "text and outputs a few hundred numbers — a vector — with one "
 "trained-in property: texts with similar meanings get vectors that "
 "are close together. Picture it as a map. Every chunk becomes a "
 "point; schedule chunks cluster in one region, grading rules in "
 "another — not because anyone sorted them, but because meaning "
 "determines position. A question becomes a point on the same map, "
 "and retrieval becomes geometry: return the nearest chunks. "
 "Closeness is one small formula, cosine similarity, three lines of "
 "code. The notebook runs a control experiment first: cosine over "
 "word-count vectors — real vector math — still misses the synonym "
 "question, because counting spelling is still spelling. Then the "
 "trained model, small, free, downloaded in seconds, no API key: it "
 "learned from billions of sentences that leave-early and dismissal "
 "live in the same contexts, and the miss closes. Two cautions "
 "before you read: embeddings can put things near each other for "
 "shallow reasons, and a fact that isn't in your pile is still not "
 "in your pile — nearness can't invent the answer chunk. Measure, "
 "don't trust. The before-and-after table is the point of the day.")

T[5] = ("Two minutes before you read. The runtime loop is four moves: embed "
 "the question, take the top-k nearest chunks, build the prompt, ask. "
 "The craft lives in move three, because the prompt is a contract "
 "with three clauses, and each one prevents a specific failure. "
 "Answer only from the provided sections — without it, the model "
 "blends your documents with training-data guesses, and you cannot "
 "see the seam. Cite the section after each fact — the receipts "
 "traveled from chunking through retrieval precisely so the answer "
 "could carry them; a cited answer is checkable in thirty seconds. "
 "And the hardest-working clause: if the sections don't contain the "
 "answer, say exactly that. A model handed the wrong chunks writes "
 "something plausible anyway — that is what models do. Under the "
 "contract, retrieval failure surfaces as an honest refusal you can "
 "see and fix, instead of a confident invention you swallow. Hold "
 "that reframe: the refusal is a feature. A system that knows the "
 "edges of its pile is the one you can trust inside them. In the "
 "build, you'll grade refusals into two kinds — correct, and "
 "retrieval-miss wearing honesty — and the receipts let you tell "
 "them apart.")

T[6] = ("Two minutes before you read. The uncomfortable truth at the center "
 "of this system: the model's answer sounds exactly as good when "
 "retrieval failed. The dangerous case is the near miss — chunks "
 "close enough that the model answers instead of refusing, wrong "
 "enough that the answer is subtly off, filled in from what such "
 "documents usually say. Typically due one week before the trip — "
 "plausible, confident, and not from your documents; your rule says "
 "five school days. So professionals run a grounding check, claim by "
 "claim: find each factual claim in the provided chunks. Present "
 "means grounded — you can point at its support. Absent means "
 "invented, no matter how reasonable it sounds, and no matter that "
 "it might even be true — because your system cannot tell "
 "true-but-ungrounded from confident fiction, and grading luck is "
 "not grading. The check runs by eye, and it runs as a second model "
 "call — a model checking text against text is reading, not "
 "remembering, and that is solid ground. One more reframe to carry: "
 "an invented claim traces to one of two causes — retrieval "
 "delivered the wrong chunks, or the model ignored the contract. "
 "The fixes are different. Sorting your failures by cause is the "
 "bridge to lesson seven.")

T[7] = ("Two minutes before you read. Nearly every retrieval miss comes "
 "from one of four mechanisms, and each has its own fix. The answer "
 "straddled a cut — rule in one chunk, condition in the next, "
 "neither scoring well alone: fix the chunking, wider pieces, more "
 "overlap. The cutoff — the right chunk ranked fourth and you kept "
 "three: found, then discarded; raise k, knowing every extra chunk "
 "spends context and adds noise. The phrasing — slang or missing "
 "key terms land the question in the wrong region of the map even "
 "for embeddings: rewrite the query first, one cheap model call "
 "that turns bail-early into early-dismissal before embedding. And "
 "absence — the answer simply isn't in the pile: no retriever finds "
 "what isn't there; add the document, or let the honest refusal "
 "stand. The discipline that ties it together: never tune blind. "
 "Change one stage, rerun the full question set, compare the "
 "numbers — the full set, because fixes can break existing hits. "
 "A re-chunk that saves one question can orphan another's answer. "
 "It-feels-better-now is how systems drift worse while everyone "
 "nods. Diagnose, fix, measure. The misses stop being mysteries "
 "today.")

T[8] = ("Two minutes before you read — and before anything runs, the "
 "questions that aren't technical. Whose documents are in your pile? "
 "If they mention real people, you need permission from whoever owns "
 "them — access is not permission. And know the data path: chunking "
 "and embedding run local, but every question and every retrieved "
 "chunk sent with it goes to the model's provider at answer time. A "
 "pile you wouldn't paste into a chat needs its sensitive parts "
 "removed before it goes behind an answering system. When in doubt, "
 "use a public pile. The engineering, you already own: cut on seams "
 "with overlap, embed and store, rewrite queries, retrieve top-k, "
 "ask under the contract, ground-check the answers. Every dial now "
 "has a number defending it, from your own question set. What makes "
 "it a real tool is the label: what the pile covers, the measured "
 "hit rate, and the standing rule that a cited answer is checkable "
 "and an uncited one is a bug. Then the point of the whole course: "
 "find your user. A sibling, a club officer, a parent facing a "
 "rulebook. Watch them ask real questions — their third one will "
 "teach you more than any lesson on this site — and check back in a "
 "week. Whether they're still using it is the realest number this "
 "course produces.")

def main():
    from kokoro import KPipeline
    pipe = KPipeline(lang_code="a")
    for n, text in sorted(T.items()):
        chunks = [a for _, _, a in pipe(text, voice="af_heart")]
        audio = np.concatenate(chunks)
        audio = np.concatenate([audio, np.zeros(int(24000 * 0.5), dtype=audio.dtype)])
        wav = f"{WORK}/ask-{n}-listen.wav"
        sf.write(wav, audio, 24000)
        out = f"{SITE}/audio/chsai-ask-{n}-listen.m4a"
        subprocess.run(["ffmpeg", "-y", "-i", wav, "-c:a", "aac", "-b:a", "96k", out],
                       capture_output=True, check=True)
        print(f"{out}  ({len(audio)/24000/60:.1f} min)", flush=True)
    print("AUDIO DONE", flush=True)

if __name__ == "__main__":
    main()
