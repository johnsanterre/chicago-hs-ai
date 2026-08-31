#!/usr/bin/env python3
"""Course 7 — Build a Tiny Language Model: animated lesson videos.
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_course7.py [slug]"""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from vidlib import s_title, s_bullets, s_chat, s_loop, s_code, build_all

L = {}

L["chsai-tiny-1"] = [
 (s_title("Build a Tiny Language Model · Lesson 1", "A model you can count",
          "look at what came before, bet on what comes next."),
  "Welcome to the course where you build the thing. Course one told you a language model places bets on what comes next. This course makes you the builder — and version one needs no math beyond counting."),
 (s_loop("The move", "One pass, one tally at a time", ["read a pair", "add a tally", "next"],
         note="After t, how often h? After q, how often u? Count everything."),
  "Here is the entire method. Walk through some text one letter at a time and keep a tally: after t, how often does h come next? After q, how often u? Do that for every pair, and the finished table can answer a question no program you have written could answer before: given this letter, what probably comes next?"),
 (s_bullets("What you built", "That table is a model", [
   "A bigram model: two things in a row",
   "It knows nothing about meaning or grammar",
   "It knows what follows what — because it counted"]),
  "That table is a language model. Not a metaphor for one — an actual one, called a bigram model. It knows nothing about meaning, grammar, or the world. It knows what follows what, because it counted. Everything else in this course is upgrades to this one move."),
 (s_bullets("This lesson", "Count, then predict", [
   "Step the counting machine in the figure",
   "The notebook counts a full paragraph",
   "Predict three next-letters by hand, then check"], closing=True),
  "In the figure you step the counting machine through one sentence and watch the table fill. In the notebook, it counts a full paragraph — but first you predict three next-letters by hand, and then check yourself against the counts. The machine only ever knows what the text taught it. Go find out what one paragraph teaches."),
]

L["chsai-tiny-2"] = [
 (s_title("Build a Tiny Language Model · Lesson 2", "The bigram machine",
          "counts become dice, and the table starts writing."),
  "Your table can predict one next letter. Today it writes. Two small moves get you there — and the text it produces has never existed anywhere before."),
 (s_code("Move one", "Counts become betting odds",
   ["after 't': h=40  o=10  ' '=50", "divide by the total:", "h: 40%   o: 10%   space: 50%"],
   note="Every row becomes odds that sum to one hundred percent."),
  "Move one: turn counts into probabilities. If after t the table saw h forty times, o ten times, and space fifty times, divide by the total. Forty percent, ten percent, fifty percent. Every row of the table becomes a set of betting odds."),
 (s_loop("Move two", "The generation loop", ["look up the row", "roll the dice", "append the winner"],
         note="This exact loop runs inside every model you have ever talked to."),
  "Move two: roll the dice. Start with a letter, look up its row, pick the next letter randomly, weighted by the odds. Now look up the new letter's row and roll again. A hundred rolls later the machine has written a line of text that has never existed. And this exact loop — look up, roll, append, repeat — is the loop inside every model you have ever talked to. Only the look-up step gets smarter."),
 (s_bullets("This lesson", "Read the gibberish closely", [
   "Wrong the way English is wrong — not the way static is",
   "Word lengths look right; q finds u",
   "Everything it knows, it counted"], closing=True),
  "The output is gibberish — but read it closely. Word lengths look right. Vowels show up on schedule. Q finds u every time. It is wrong the way English is wrong, not the way static is wrong, because everything it knows came from real text. Build it in the notebook and generate your first paragraphs of brand-new text."),
]

L["chsai-tiny-3"] = [
 (s_title("Build a Tiny Language Model · Lesson 3", "The randomness dial",
          "why not always pick the favorite? Try it."),
  "An obvious idea: skip the dice and always pick the most likely letter. It fails in a way you can predict before running it — and fixing it hands you a dial that every real model has."),
 (s_code("Greedy", "Stuck in a loop",
   ["always pick the favorite:", "e the the the the the...", ""],
   err_line=1, note="Deterministic plus a cycle equals stuck forever."),
  "Greedy generation: always take the top choice. But if e's favorite leads to space, and space's favorite leads to t, and t's leads back to e — the machine writes the, the, the, forever. Deterministic plus a cycle equals stuck. The dice were never optional."),
 (s_bullets("The dial", "Temperature", [
   "Cold: favorites get stronger — safe, repetitive",
   "Warm: the odds exactly as counted",
   "Hot: odds flatten — rare letters start winning"]),
  "The dice have a dial called temperature, and it reshapes the odds before you roll. Cold: the favorites get even more favored — safe, repetitive, loop-prone. Warm: the odds exactly as counted. Hot: everything flattens toward equal, rare letters start winning rolls, and far enough up it melts into static."),
 (s_bullets("This lesson", "You built their setting", [
   "The dial in real model dashboards is this dial",
   "Low for facts and code, higher for brainstorms",
   "Find your machine's greedy loop in the notebook"], closing=True),
  "You now know mechanically why a chatbot answers the same question differently on different days — and the temperature setting in real developer dashboards is the dial you just built. Low for facts and code, higher for brainstorming. In the notebook, catch your own machine's greedy loop red-handed, then run the same corpus cold, warm, and hot."),
]

L["chsai-tiny-4"] = [
 (s_title("Build a Tiny Language Model · Lesson 4", "Context and the wall",
          "more memory, better text — and an exploding table."),
  "Your machine has a one-letter memory, which is why its output dissolves. The upgrade is obvious: remember more. It works — and then it hits a wall that stopped the whole field for decades."),
 (s_code("The upgrade", "More letters of context",
   ["1 letter:  27 rows", "2 letters: 729 rows", "3 letters: 19,683 rows", "10 letters: 206 trillion rows"],
   err_line=3, note="Your corpus is a few thousand characters long."),
  "Condition on the last two letters instead of one, and real words surface. Three letters, and phrases appear. But count the rows. One letter of context: twenty-seven rows. Two: seven hundred twenty-nine. Three: nineteen thousand. Ten letters of context: two hundred six trillion rows — for a corpus a few thousand characters long. Almost every row would be empty."),
 (s_bullets("The wall", "Counting cannot scale", [
   "Most long contexts have never occurred — anywhere",
   "This sentence has never existed; you understand it",
   "A counting model can only look up the past"]),
  "This is the wall, and it deserves respect: most long contexts have never occurred even once, anywhere. The sentence you are hearing right now has never existed before, and you understand it fine. A counting model cannot — it can only look up a past it has literally seen. Counting was never going to reach conversation."),
 (s_bullets("This lesson", "Measure the wall", [
   "Flip context length in the figure: 1, 2, 3",
   "The notebook counts the empty rows",
   "Next lesson: the way past the wall"], closing=True),
  "In the figure, flip between one, two, and three letters of memory and watch quality and table size climb together. In the notebook, measure the wall on your own corpus: build the trigram and four-gram machines and count how much of the table is empty. Then come back for lesson five — the way past the wall is the best idea in this course."),
]

L["chsai-tiny-5"] = [
 (s_title("Build a Tiny Language Model · Lesson 5", "It learns",
          "stop storing answers. Start learning them."),
  "Here is the move that broke the wall. No more table of counts. A grid of adjustable numbers — weights — starts out random and gets nudged, example by example, until its bets are good."),
 (s_loop("The loop", "Show, score, nudge, repeat", ["show an example", "score the bet", "nudge the weights"],
         note="The score is called the loss. Falling loss = learning."),
  "The training loop is almost insultingly simple. Show the model one real example: after t came h. Score its bet — how much probability did it put on h? That score is the loss: big when the model was surprised by the truth. Then nudge every weight a tiny step in the direction that would have made the loss smaller. Repeat, thousands of times."),
 (s_bullets("Why it wins", "Generalization", [
   "A table only knows contexts it has literally seen",
   "Weights are shared — similar contexts help each other",
   "Sensible bets on combinations it never met"]),
  "Why does this beat counting? A table can only look up what it has literally seen. Learned weights generalize: similar contexts share weights, so the model places sensible bets even on combinations it never met. That one property, scaled up, is the road from your notebook to the models you talk to every day."),
 (s_bullets("This lesson", "Watch the number fall", [
   "The figure trains 756 real weights in your browser",
   "The notebook builds the learner in numpy, line by line",
   "The falling loss is what every AI lab watches all day"], closing=True),
  "The figure trains a real model — seven hundred fifty six weights — live in your browser, and the curve you watch fall is the actual loss, not an animation of one. Then the notebook builds the same learner in numpy, where you can read every line. The falling number on your screen is the same falling number every AI lab stares at all day. Go make it fall."),
]

L["chsai-tiny-6"] = [
 (s_title("Build a Tiny Language Model · Lesson 6", "Tokens, for real",
          "the vocabulary invents itself — by counting."),
  "Course one told you models read tokens, not letters. Today you build the machine that invents a token vocabulary — and it runs on the skill you started this course with: counting."),
 (s_loop("The algorithm", "Byte-pair encoding", ["count adjacent pairs", "merge the most frequent", "repeat"],
         note="t+h becomes th. th+e becomes the. Nobody chose them."),
  "Byte-pair encoding: start with text split into single characters. Count every adjacent pair. Merge the most frequent one everywhere — t plus h becomes one token, t h. Repeat. Soon th plus e merges into the. Keep going and the vocabulary fills itself with the building blocks of the actual text: common words become single tokens, rare words stay in pieces."),
 (s_bullets("The payoff", "Course 1's oddities, explained", [
   "Models see token-chunks, not letters",
   "That's why letter-counting can fail",
   "Rare words shatter into many pieces"]),
  "And now course one's oddities crack open. Why can a model miscount the letters in strawberry? Because it does not see letters — it sees token chunks, built by exactly this merging. Why do weird spellings confuse it? Rare strings shatter into many small pieces. The tokenizer was never designed. It was counted, on a mountain of text."),
 (s_bullets("This lesson", "Invent a vocabulary", [
   "Click merges in the figure, watch word-pieces appear",
   "The notebook: BPE in about forty lines",
   "Tokenize your own name and see it split"], closing=True),
  "In the figure, every click merges the top pair, and word-pieces appear from nothing but frequency. The notebook implements the whole algorithm in about forty lines, learns a vocabulary from a real book, and then tokenizes your sentences — including your own name, which may shatter in ways that tell you exactly how common your name was in the training text."),
]

L["chsai-tiny-7"] = [
 (s_title("Build a Tiny Language Model · Lesson 7", "The corpus is the voice",
          "same machine, different diet, different character."),
  "Train the same machine on different text and you get a different machine. Not different settings — a different character. Today you prove it, and then you scale the lesson up to the whole internet."),
 (s_chat("The proof", "Two diets",
   [("you", "Same code, trained on formal essays:"),
    ("ai", "the committee concluded that the proposal merited consideration..."),
    ("you", "Same code, trained on chat messages:"),
    ("ai", "lol ok so the game was crazy fr we were dying lmao...")],
   note="Every difference came from the data."),
  "Two identical machines. One counted formal prose, one counted chat messages. The formal one writes long words and careful rhythms. The chat one writes l o l and drops its capitals. Same code, run twice. Every difference you can see came from the data."),
 (s_bullets("Scaled up", "The internet's mirror", [
   "Big models trained on a giant slice of the internet",
   "Over-represented in the data = over-represented in the odds",
   "Nobody has ever built a corpus without a tilt"]),
  "Now scale it. The models you use were trained on a giant slice of the internet — so their voice, their assumptions, and their blind spots are the internet's, averaged. Course one said that as a warning. You can now say it as an engineer: whatever is over-represented in the data is over-represented in the odds. A model is a mirror of its corpus, and nobody has ever built a corpus without a tilt."),
 (s_bullets("This lesson", "Three diets in the notebook", [
   "A classic novel, modern prose, chat-style text",
   "Compare the three voices — and the shared blind spots",
   "Data quality IS model quality"], closing=True),
  "The notebook trains your machine on three corpora and compares the voices. Then the sharper question: what can each machine never say, because its corpus never taught it? Feed a model typos and it learns typos, faithfully. The best upgrade in this whole course is not a smarter algorithm. It is better text."),
]

L["chsai-tiny-8"] = [
 (s_title("Build a Tiny Language Model · Lesson 8", "Your model",
          "your corpus, your machine, your model card."),
  "The capstone. Curate a corpus, train your machine on it, tune it, generate a page — and write the honest model card. The corpus rule: your words, or words old enough to belong to everyone."),
 (s_bullets("The build", "Assemble every piece", [
   "Your own writing in — essays, journals, stories",
   "Tune context length and temperature to your voice",
   "Generate a page; pick best and worst passages"]),
  "Paste in your own writing — old essays, journals, stories. Not your group chat: those are not only your words. Then tune: try context lengths, find the temperature that suits your corpus, and generate a full page. A model trained on your writing picks up your sentence lengths, your favorite words, your habits. Most students find that slightly unsettling. That reaction is correct."),
 (s_bullets("The ladder", "Where you stand, in numbers", [
   "Your model: a few thousand parameters, a few pages",
   "GPT-2, 2019: 1.5 billion — it stunned the field",
   "Frontier models: undisclosed, trained on far more"]),
  "Then place yourself honestly on the ladder. Your model: a few thousand numbers, a few pages of text. GPT-2, which stunned researchers in 2019: one and a half billion. The frontier models: sizes undisclosed, trained on a huge slice of everything written. Same bet-placing idea. Same falling loss. Same data-is-destiny rule. The distance is a factor you can now count."),
 (s_bullets("The finish", "Ship it", [
   "The model card is the course grade",
   "Three minutes: one line, one insight, one limit",
   "You built a small language model. Not a toy one."], closing=True),
  "Finish with the model card — what went in, what works, what fails, and one thing your model believes that is really a fact about your corpus. Present three minutes: one generated line, one thing it learned about your voice, one thing it can never do. You did not build a toy version of a language model. You built a small one. Congratulations, builder."),
]

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    build_all(L, "Build a Tiny Language Model", only)
