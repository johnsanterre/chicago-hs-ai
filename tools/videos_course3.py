#!/usr/bin/env python3
"""Course 3 — Python in Colab: animated lesson videos.
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_course3.py [slug]"""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from vidlib import (s_title, s_bullets, s_notebook, s_loop, s_chat, build_all)

L = {}

L["chsai-python-1"] = [
 (s_title("Python in Colab · Lesson 1", "Code in your browser",
          "a notebook of cells — text that explains, code that runs."),
  "Welcome to Python. Type colab dot research dot google dot com and a notebook opens: a page made of cells. Text cells explain. Code cells run. Nothing to install, nothing you can break — and by the end of this lesson you will have run real Python."),
 (s_notebook("First run", "Press play",
   [(["print(\"hello\")"], [("hello", "ok")])],
   note="It ran on a Google computer far away — and sent the answer back."),
  "Click a code cell and press the play button. Print, quote, hello. A second later: hello, right underneath. Here is the idea to hold onto — the code did not run on your laptop. It ran on a Google computer far away, which sent the result back. That is why nothing needs installing."),
 (s_notebook("Break it on purpose", "Your first error",
   [(["prnt(\"hello\")"],
     [("NameError: name 'prnt' is not defined", "err"),
      ("      did you mean: 'print'?", "err")])],
   note="Read it out loud. The computer is reporting, not judging."),
  "Now break it on purpose. Spell print wrong and run it. Red text: name error — name p r n t is not defined, did you mean print? Read errors out loud, every time. An error is the computer filing a report about exactly what confused it — and this one even guesses the fix."),
 (s_bullets("This lesson", "Your move", [
   "Open Colab, run your first cells",
   "Cause three different errors on purpose — read each aloud",
   "File - Save a copy in Drive keeps your work"], closing=True),
  "Your build: open the lesson notebook in Colab, run every cell, then cause three different errors on purpose and read each one aloud before you fix it. People who fear errors go slow; people who read them go fast. And remember: File, save a copy in Drive, keeps everything yours."),
]

L["chsai-python-2"] = [
 (s_title("Python in Colab · Lesson 2", "Names with values in them",
          "variables, strings, and the f-string you'll use forever."),
  "A variable is a name with a value in it — and that one idea powers everything. Change the value once, and everything using the name updates. This lesson: variables, math, text, and the single most useful line of Python you will learn all course."),
 (s_notebook("Variables", "Change once, update everywhere",
   [(["age = 15", "year = 2026", "born = year - age", "print(born)"],
     [("2011", "ok")]),
    (["age = 16   # birthday!"], [("rerun the cell above: 2010", "ok")])],
   note="Downstream code follows the name, not the old value."),
  "Watch: age equals fifteen, born equals year minus age — twenty eleven. Now change age to sixteen and rerun: everything downstream updates, because the code follows the NAME, not the old number. That is the whole point of a variable."),
 (s_notebook("Strings", "The star of the show",
   [(["name = \"Ada\"", "print(f\"{name} is {age}\")"],
     [("Ada is 16", "ok")]),
    (["print(name.upper(), len(name), \"go! \" * 3)"],
     [("ADA 3 go! go! go!", "ok")])],
   note="The f-string: variables dropped straight into text. Every lesson from now on."),
  "Strings are text in quotes — and the star of the show is the f-string: an f before the quote, and your variables drop straight into the text inside curly braces. Ada is sixteen. You will use this every single lesson from now on. Strings also have superpowers: upper, len, and multiplication."),
 (s_bullets("This lesson", "Your build", [
   "The intro card: name, age, school — built with f-strings",
   "Then Mad Libs: your variables, someone else's story",
   "Rule: predict every cell's output before you run it"], closing=True),
  "Your build: an intro card about you, assembled with f-strings — then Mad Libs, where your variables fill someone else's story. Carry the course rule with you: predict what every cell will print before you press play. Prediction is how typing becomes understanding."),
]

L["chsai-python-3"] = [
 (s_title("Python in Colab · Lesson 3", "Lists and loops",
          "many values, one name — and code that repeats itself."),
  "One variable holds one value. A list holds many, in order — your crew, your songs, your scores. And the for loop makes code run once for every item. Together they are the first genuinely powerful thing you will write."),
 (s_notebook("Lists", "Counting starts at zero",
   [(["crew = [\"Maya\", \"DeShawn\", \"Alex\"]", "print(crew[0])"],
     [("Maya", "ok")]),
    (["print(crew[1])"], [("DeShawn", "ok")])],
   note="crew[0] is the FIRST item. Everyone trips on it once — now you won't."),
  "A list in square brackets, items in order. Crew of zero is Maya — because counting starts at zero. Every programmer alive tripped on that exactly once. You just used up your trip for free."),
 (s_notebook("The loop", "Once per item",
   [(["for person in crew:", "    print(f\"Go {person}!\")"],
     [("Go Maya!", "ok"), ("Go DeShawn!", "ok"), ("Go Alex!", "ok")]),
    (["total = 0", "for n in [12, 8, 30]:", "    total = total + n", "print(total)"],
     [("50", "ok")])],
   note="The indented lines ARE the loop body. The collector pattern: total = total + n."),
  "The for loop: for person in crew — and the indented line runs once per item. The indent is the loop body; add a second indented line and it repeats too. Then the collector pattern: start a total at zero, add each item inside the loop. Sums, counts, scores — this pattern is everywhere."),
 (s_bullets("This lesson", "Own the machinery", [
   "Remember printing your name 100 times in lesson 1?",
   "range(100) — now that mystery code is yours",
   "Build: the crew cheer, the total, and a countdown"], closing=True),
  "Remember lesson one, when mystery code printed your name a hundred times? Range of one hundred — you now own that machinery. Your build: the crew cheer, the collector total, and a countdown. Loops plus lists is where Python starts feeling like power."),
]

L["chsai-python-4"] = [
 (s_title("Python in Colab · Lesson 4", "Today, you're the someone",
          "you've used functions all course. Now you write them."),
  "Print. Len. Range. You have been using functions all course — someone wrote those. Today you are the someone. A function is a named block of code: define it once, use it forever."),
 (s_notebook("Define and call", "cheer, twice",
   [(["def cheer(name):", "    print(f\"Go {name}!\")", "", "cheer(\"Maya\")",
      "cheer(\"DeShawn\")"],
     [("Go Maya!", "ok"), ("Go DeShawn!", "ok")])],
   note="def once — call forever."),
  "Def cheer, taking a name: the indented body prints the cheer. Then call it — cheer Maya, cheer DeShawn. Defined once, used twice, used forever. Any code you write twice is begging to become a function."),
 (s_notebook("Return", "Functions hand values back",
   [(["def area(w, h):", "    return w * h", "",
      "def cost(w, h, price):", "    return area(w, h) * price", "",
      "print(cost(3, 4, 2))"],
     [("24", "ok")])],
   note="cost() calls area(): small functions stack into bigger ones."),
  "Return is the upgrade: the function hands a value back, and the caller can store it, print it, or feed it to another function. Watch cost call area — small functions stacking into bigger ones. That is how all real software is built, including the AI you have been working with."),
 (s_bullets("This lesson", "Your build", [
   "Write cheer, area, and a greeting function of your own",
   "Compose: one function that calls another",
   "Name functions for what they DO — future-you reads the name"], closing=True),
  "Your build: cheer, area, and a greeting function of your own design — then a composition, one function calling another. Name your functions for what they do; future-you will read the name and not the body. From here on, everything you build is made of these."),
]

L["chsai-python-5"] = [
 (s_title("Python in Colab · Lesson 5", "Label your data",
          "dictionaries: ask by name, not by position."),
  "A list can hold Maya, thirty-one, Wildcats — but which number is which? A dictionary labels its contents: name colon Maya, points colon thirty-one. Ask by label, not position. Real data almost always ships with labels."),
 (s_notebook("Key and value", "Ask by label",
   [(["player = {\"name\": \"Maya\", \"points\": 31}",
      "print(player[\"points\"])"],
     [("31", "ok")]),
    (["player[\"team\"] = \"Wildcats\"", "player[\"points\"] = 33", "print(player)"],
     [("{'name': 'Maya', 'points': 33, 'team': 'Wildcats'}", "ok")])],
   note="Add a key. Change a value. The labels make it readable."),
  "Curly braces, key colon value. Player of points — thirty-one, asked for by label. Add a team key, update the points, print the whole thing: readable, labeled data. Loop over a dictionary and you get the keys; look up each value as you go."),
 (s_notebook("The tally", "Five lines you'll use forever",
   [(["votes = [\"pizza\", \"tacos\", \"pizza\", \"pizza\"]",
      "tally = {}", "for v in votes:",
      "    tally[v] = tally.get(v, 0) + 1", "print(tally)"],
     [("{'pizza': 3, 'tacos': 1}", "ok")])],
   note="Count votes, words, anything. (Course 1's bias tally? This exact pattern.)"),
  "Now the pattern you will use forever: the tally. An empty dictionary; for each vote, get the current count or zero, add one. Pizza three, tacos one. Count votes, count words, count anything — and if you took How AI Works, the bias tally you ran there is this exact pattern."),
 (s_bullets("This lesson", "Your build", [
   "A contact card dict, then the class-vote tally",
   "Loop over the dictionary and print a report line per key",
   "f-strings + dicts = readable output"], closing=True),
  "Your build: a contact-card dictionary, then the class-vote tally, then a loop that prints one clean report line per key using f-strings. Lists hold order; dictionaries hold meaning. You now have both."),
]

L["chsai-python-6"] = [
 (s_title("Python in Colab · Lesson 6", "Memory that survives",
          "every program so far forgot everything. Files remember."),
  "Every program you have written forgot everything the moment it ended. Files fix that — memory that survives. Today your code makes a real file on a real computer, writes to it, and reads it back."),
 (s_notebook("Write", "Your code made a real file",
   [(["with open(\"note.txt\", \"w\") as f:",
      "    f.write(\"Day 1: started files\\n\")"],
     [("(click the folder icon — note.txt is THERE)", "ok")])],
   note="w writes fresh · a appends without erasing · r reads."),
  "With open, note dot t x t, in write mode — write a line. Now click Colab's folder icon on the left: the file is there. Your code created a real file. Three modes to know: w writes fresh, a appends without erasing, r reads."),
 (s_notebook("Read it back", "And the honest gotcha",
   [(["with open(\"note.txt\") as f:", "    for i, line in enumerate(f):",
      "        print(i, line.strip())"],
     [("0 Day 1: started files", "ok")])],
   note="Colab's files vanish when the session ends — download what you keep."),
  "Read it back with a loop — enumerate numbers the lines for free. And the honest gotcha: Colab's files live on that faraway session machine, and they vanish when the session ends. Download anything you want to keep. That is not a bug; it is a loaner computer."),
 (s_bullets("This lesson", "Your build", [
   "A journal: append a dated line each run",
   "A reader: print the journal back, numbered",
   "Download the file — proof your code made something real"], closing=True),
  "Your build is a journal: each run appends one dated line, and a reader prints the whole journal back with line numbers. Then download the file — proof that your code made something that exists outside the notebook. Programs that remember are programs that matter."),
]

L["chsai-python-7"] = [
 (s_title("Python in Colab · Lesson 7", "Standing on others' code",
          "import opens a toolbox someone already built."),
  "Two lessons ago you built the tally pattern by hand, five careful lines. Watch this. From collections import counter. Counter of votes. Done — one line. That is a library: a toolbox of working code someone already wrote, and import opens it."),
 (s_notebook("The one-liner", "Counter, and why you earned it",
   [(["from collections import Counter",
      "votes = [\"pizza\", \"tacos\", \"pizza\", \"pizza\"]",
      "print(Counter(votes).most_common(1))"],
     [("[('pizza', 3)]", "ok")])],
   note="You built this pattern yourself — so you know exactly what the shortcut does."),
  "Counter of votes, most common — pizza, three. Here is why the order mattered: because you built the tally yourself two lessons ago, you know exactly what this shortcut is doing. Build it once, then take the ride. That is the right relationship with libraries — and with AI-generated code, too."),
 (s_notebook("The tour", "random and datetime",
   [(["import random", "print(random.choice([\"heads\", \"tails\"]))",
      "print(random.randint(1, 6))"],
     [("tails", "ok"), ("4", "ok")]),
    (["from datetime import date",
      "print((date(2027, 3, 14) - date.today()).days, \"days\")"],
     [("196 days", "ok")])],
   note="Dice, coin flips, countdowns — working code, one import away."),
  "A quick tour of two toolboxes you will use constantly. Random: coin flips, dice rolls, random choices. Datetime: real dates you can subtract — days until your birthday, live. Working code, one import away, and you understand what it stands on."),
 (s_bullets("This lesson", "Your build", [
   "The dice game: roll, tally with Counter, crown a winner",
   "The countdown: days until a date you care about",
   "Rule stands: read what the import hands you"], closing=True),
  "Your build: the dice game — roll many times, tally with counter, crown the winning number — and a countdown to a date you actually care about. The course rule does not retire for libraries: read what the import hands you, and know what it is doing on your behalf."),
]

L["chsai-python-8"] = [
 (s_title("Python in Colab · Lesson 8", "Aim it all at one chore",
          "eight lessons of tools. One real program."),
  "Variables, strings, lists, loops, functions, dictionaries, files, libraries — eight lessons of tools on the table. The finale aims them at one target: a program that does a real chore. Pick yours: the chore wheel, the flashcard quizzer, the password maker, the allowance tracker — or your own, at this size."),
 (s_loop("The method", "How real programs get built",
         ["plan", "build a piece", "test it", "next piece"],
         note="Plan in comments FIRST — the plan is the design, and it is yours."),
  "The method matters more than the project. One: plan in comments first — four to six plain-English lines before any code. The plan is the design, and the AI helps best when the plan is yours. Two: build in pieces, one function at a time. Three: test each piece before the next. Around the loop until it works."),
 (s_chat("The AI pair", "Sign for every line",
   [("you", "Here is my plan in comments. Write ONLY the spin_wheel function — and explain it line by line."),
    ("ai", "Here is spin_wheel using random.choice, with an explanation of each line…")],
   note="The sign-for-every-line rule: if you can't explain it, you don't ship it."),
  "Use your pair the way this course taught you: hand it YOUR plan, ask for one piece at a time, and make it explain every line. Then the rule this whole course has been building toward — you sign for every line. If you cannot explain a line, you do not ship it."),
 (s_bullets("Course complete", "Run it twice", [
   "Finish the chore program — and run it twice, fresh",
   "Commit it to GitHub with a real message",
   "You write Python. The next courses put it to work"], closing=True),
  "Ship it: finish the program, run it twice from a fresh session so you know it really works, and commit it to GitHub with a message future-you will thank you for. Course complete. You write Python now — and the data and A I courses on this site are where it goes to work."),
]

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    build_all(L, "Python in Colab", only)
