#!/usr/bin/env python3
"""Course 4 — Working with Data: animated lesson videos.
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_course4.py [slug]"""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from vidlib import (s_title, s_bullets, s_notebook, s_loop, s_chart, build_all)

L = {}

L["chsai-data-1"] = [
 (s_title("Working with Data · Lesson 1", "Tables underneath everything",
          "screen time, Spotify Wrapped, the CTA tracker — all tables."),
  "Your phone's screen-time report. Spotify Wrapped. A gradebook. The C T A bus tracker. Underneath every one of them: a table. This course teaches you to ask tables real questions — and by the end, to investigate your own city's data."),
 (s_bullets("The shape", "Rows and columns", [
   "Each ROW is a thing: a student, a song, a bus",
   "Each COLUMN is a fact about it: name, minutes, route",
   "Data analysis = asking questions of that shape"]),
  "The shape to learn once and use forever: each row is a thing — a student, a song, a bus. Each column is a fact about it — name, minutes, route. Every question you will ever ask of data is a question about rows and columns."),
 (s_notebook("The file", "CSV — the universal table",
   [(["text = \"\"\"name,neighborhood,hours_online,grade",
      "Maya,Pilsen,3,A", "DeShawn,Austin,5,B", "Alex,Uptown,2,A\"\"\"",
      "open(\"friends.csv\", \"w\").write(text)"],
     [("(friends.csv created)", "ok")]),
    (["import pandas as pd", "df = pd.read_csv(\"friends.csv\")", "df.head()"],
     [("  name    neighborhood  hours_online grade", "ok"),
      ("  Maya    Pilsen        3            A", "ok")])],
   note="CSV: rows as lines, columns by commas. Pandas reads it in one line."),
  "The universal table file is C S V — comma separated values. Rows are lines; commas split the columns. Build a tiny one — five friends, four facts — then hand it to pandas with read c s v, and the table comes back as a data frame. That object is this whole course."),
 (s_bullets("This lesson", "Your build", [
   "Build a CSV about YOUR crew — real facts, 4+ columns",
   "Load it with pandas, print the shape and the head",
   "Name what each row IS and each column MEANS"], closing=True),
  "Your build: a C S V about your own crew — real people, at least four columns — loaded with pandas, shape and head printed. Then the sentence that proves you get it: what is a row here, and what does each column mean? Say it precisely. Everything else builds on that."),
]

L["chsai-data-2"] = [
 (s_title("Working with Data · Lesson 2", "The code does the looking",
          "filter, sort, count — the three moves."),
  "Sixty rows is already too big to eyeball — and real tables have thousands. That is the point of pandas: from today, the code does the looking. Three moves cover most questions you will ever ask: filter, sort, count."),
 (s_notebook("Move one", "Filter — read it inside-out",
   [(["df[df[\"neighborhood\"] == \"Pilsen\"]"],
     [("(only the Pilsen rows remain)", "ok")]),
    (["df.sort_values(\"hours_online\", ascending=False).head()"],
     [("(top five, instantly)", "ok")])],
   note="Inner part: a True/False column. Outer part: keep the True rows."),
  "Move one, filter. D f of d f neighborhood equals Pilsen. Read it inside out: the inner comparison makes a true-false column, and the outer bracket keeps the true rows. Every filter you will ever write is that shape. Move two, sort values — descending — and the top five appear instantly."),
 (s_notebook("Move three", "Count",
   [(["df[\"grade\"].value_counts()"],
     [("A    31", "ok"), ("B    22", "ok"), ("C     7", "ok")])],
   note="Three moves, chained, answer most questions a table gets asked."),
  "Move three, count. Value counts on a column tallies every value — thirty-one A's, twenty-two B's. And the real power is chaining: filter to one neighborhood, sort by hours, count the grades. Three moves, snapped together like bricks."),
 (s_bullets("This lesson", "Your build", [
   "Ten questions, ten one-liners, on the class dataset",
   "For each: say the answer BEFORE you run it",
   "Wrong guesses are the lesson working"], closing=True),
  "Your build: ten questions against the lesson dataset, each answered in one line — a filter, a sort, a count, or a chain. Predict each answer before you run, and treat wrong guesses as the lesson working. The prediction habit from the Python course carries straight into data."),
]

L["chsai-data-3"] = [
 (s_title("Working with Data · Lesson 3", "Real data is messy",
          "and cleaning it is a series of decisions, not deletions."),
  "Here is a table with pilsen lowercase, Pilsen capitalized, and PILSEN shouting — three different neighborhoods as far as the computer knows. Plus a missing value, a duplicate row, and someone with negative one hours online. Welcome to real data. Every real project starts here."),
 (s_notebook("Rule one", "Diagnose before touching",
   [(["df.isna().sum()"], [("hours_online    1", "ok")]),
    (["df[\"neighborhood\"].unique()"],
     [("['pilsen' 'Pilsen' 'PILSEN' 'Austin']", "ok")]),
    (["df.duplicated().sum()"], [("1", "ok")])],
   note="Three commands. Look first. Every fix you make is a decision to defend."),
  "Rule one: diagnose before touching. Three commands. Is n a dot sum — missing values per column. Unique — and there is the spelling chaos. Duplicated dot sum — one copy-paste ghost. Look first, because every fix you are about to make is a decision you should be able to defend."),
 (s_notebook("The fixes", "Narrate every decision",
   [(["df = df.drop_duplicates()",
      "df[\"neighborhood\"] = df[\"neighborhood\"].str.title()",
      "df[\"hours_online\"] = df[\"hours_online\"].fillna(df[\"hours_online\"].median())"],
     [("# LOG: dropped 1 dupe; unified spelling;", "ok"),
      ("# filled 1 missing with the median (why: skewed data)", "ok")])],
   note="Keep a cleaning log. Future-you audits present-you."),
  "Then fix, one problem at a time, narrating each decision. Drop duplicates. Unify the spelling with str dot title. The missing value: fill with the median — and write down WHY the median. Negative one hours? That is a judgment call, and judgment calls go in the log. Cleaning is decisions, not deletions."),
 (s_bullets("This lesson", "Your build", [
   "Clean the planted-mess dataset — six problems hide in it",
   "Keep the cleaning log: what you did and why",
   "The log is the deliverable as much as the clean table"], closing=True),
  "Your build: a dataset with six planted problems. Find them with the diagnose commands, fix them one at a time, and keep the cleaning log — what you did and why, in plain sentences. In real data work, the log is the deliverable as much as the clean table is."),
]

L["chsai-data-4"] = [
 (s_title("Working with Data · Lesson 4", "The sentence machine",
          "BY ___, the ___ OF ___."),
  "Eighty students, study hours, scores. Which neighborhood scores highest? Eyeballing is hopeless — and one line is not. Groupby is the most powerful sentence in data analysis, and this lesson you learn to speak it."),
 (s_notebook("The line", "groupby, live",
   [(["df.groupby(\"neighborhood\")[\"score\"].mean()"],
     [("Austin    78.2", "ok"), ("Pilsen    84.1", "ok"), ("Uptown    81.5", "ok")]),
    (["df.groupby(\"grade\")[\"hours_online\"].max()"],
     [("A    4.5", "ok"), ("B    6.0", "ok")])],
   note="groupby(thing)[fact].measure — swap any piece, ask a new question."),
  "Group by neighborhood, take score, average it — and the answer table appears. The shape is a sentence: BY neighborhood, the AVERAGE of score. Swap any piece: by grade, the max of hours. It is a sentence machine, and every swap is a new question answered in seconds."),
 (s_bullets("The trap", "Found is not explained", [
   "Pilsen scores highest — TRUE. Pilsen CAUSES high scores? Not shown.",
   "Groupby finds patterns; it never explains them",
   "Say what you found, not what you wish it meant"]),
  "Now the trap this lesson springs on purpose. Pilsen scores highest — true, the table says so. Does living in Pilsen CAUSE high scores? The table does not say that, and neither should you. Group by finds patterns; it never explains them. Data people say what they found — not what they wish it meant."),
 (s_bullets("This lesson", "Your build", [
   "Five groupby sentences on the class data — written in words first",
   "Then translated to code, then run",
   "One finding written up in two careful sentences"], closing=True),
  "Your build: five group-by questions, written as sentences first — by what, the what, of what — then translated to code and run. Finish with one finding, written up in two careful sentences that claim exactly what the data shows and not a word more."),
]

L["chsai-data-5"] = [
 (s_title("Working with Data · Lesson 5", "Charts that tell the truth",
          "one honest picture beats a table of numbers."),
  "A table of sign-ups by neighborhood: true, complete, and unreadable at a glance. One line — plot kind bar — and the eye does in a second what the table made it work for. This lesson: making charts, and making them honest."),
 (s_chart("The chart", "Sign-ups by neighborhood",
   ["Pilsen", "Austin", "Uptown", "Hyde Park"], [34, 21, 17, 12],
   claim="Pilsen leads sign-ups",
   note="The title states the CLAIM. The axis starts at zero. Bars encode amount."),
  "Counts dot plot, kind bar — a chart appears. Now the honesty kit. The title should state the chart's claim: not sign-ups, but Pilsen leads sign-ups — say what the chart shows. Label the axes. And for bar charts, the axis starts at zero, always — bars encode amount, and a chopped bar is a visual lie."),
 (s_bullets("The kit", "Every honest chart has", [
   "A claim title: what this chart SAYS",
   "Labeled axes: what the numbers ARE",
   "A zero-based axis on bars: amounts don't start midair",
   "The right chart: bars compare, lines show change over time"]),
  "The kit, in full. A claim title — what the chart says. Labeled axes — what the numbers are. Zero-based bars — amounts do not start midair. And the right chart for the job: bars compare things; lines show change over time. Four checks, ten seconds, every chart you ever ship."),
 (s_bullets("This lesson", "Your build", [
   "Three charts from the class data, each with a claim title",
   "Trade with a classmate: can they say your claim from the chart alone?",
   "If they can't, the chart isn't done"], closing=True),
  "Your build: three charts from the lesson data, each carrying a claim title and the full honesty kit. Then the real test — trade with a classmate. If they cannot read your claim from the chart alone, the chart is not done yet. Charts are sentences; make them say something true."),
]

L["chsai-data-6"] = [
 (s_title("Working with Data · Lesson 6", "Same numbers, two stories",
          "nothing false was entered. The chart still lies."),
  "Scores four months running: seventy-one, seventy-two, seventy-three, seventy-four. Basically flat. Now watch the same four numbers tell two different stories — and learn to catch the trick everywhere it hides."),
 (s_chart("The trick", "One dataset, two charts",
   ["May", "June", "July", "Aug"], [71, 72, 73, 74],
   claim="Scores basically flat",
   compare_ylim=(70, 75), claim2="SCORES SKYROCKET!",
   note="Right chart: axis chopped at 70. Nothing false entered. Still a lie."),
  "Left: honest bars, zero-based axis — scores basically flat, which is the truth. Right: the same four numbers with the axis chopped at seventy. Suddenly the last bar towers. Scores skyrocket! Nothing false was entered — the lie lives entirely in the axis. This trick is in ads, politics, and pitch decks, every single day."),
 (s_bullets("The checklist", "Three questions for any chart", [
   "Where does the axis start? (Chopped bars = inflated differences)",
   "What's the time window? (Cherry-picked months hide the year)",
   "What's NOT shown? (The data that didn't make the chart)"]),
  "Your permanent checklist, three questions. Where does the axis start — chopped bars inflate small differences. What is the time window — July to September can hide a year that dipped and recovered. And what is NOT shown — the rows that did not make the chart. Ask all three, every time, including of your own charts."),
 (s_bullets("This lesson", "Your build", [
   "Take YOUR honest chart from lesson 5 — now make it lie",
   "Same data, chopped axis, cherry-picked window, spun title",
   "Then write the two-sentence confession of how the lie works"], closing=True),
  "Your build is deliciously sneaky: take your honest lesson-five chart and make it lie. Same data — chopped axis, cherry-picked window, spun title. Then write the confession: two sentences on exactly how the lie works. You will never be fooled by this trick again, because you will have built it."),
]

L["chsai-data-7"] = [
 (s_title("Working with Data · Lesson 7", "Your city, publishing itself",
          "data.cityofchicago.org — live, real, yours to query."),
  "Go to data dot city of chicago dot org and scroll: crime reports, pothole repairs, library locations, restaurant inspections. Your city publishes itself, live. This lesson your code reaches out and takes a real dataset off the internet."),
 (s_notebook("The idea", "An API is a URL that returns data",
   [(["import requests",
      "url = \"https://data.cityofchicago.org/resource/x8fc-8rcq.json\"",
      "libs = requests.get(url).json()", "print(len(libs), libs[0][\"name_\"])"],
     [("81 Albany Park", "ok")])],
   note="JSON = dictionaries in lists — the exact shapes from Python lesson 5."),
  "An A P I is a U R L that returns data instead of a page. Requests dot get, dot json — and eighty-one Chicago libraries land in your notebook as dictionaries inside lists, the exact nested shapes you learned in Python lesson five. Ugly in the browser; familiar in the code."),
 (s_notebook("Into pandas", "From the internet to a table",
   [(["df = pd.DataFrame(libs)",
      "df[\"zip\"].value_counts().head(3)"],
     [("60625    4", "ok"), ("60617    3", "ok"), ("60632    3", "ok")])],
   note="One line from JSON to table — then every move you know applies."),
  "One more line — data frame of the JSON — and the internet's answer becomes a table. Now everything you know applies: filter, sort, count, group by, chart. The whole course stacks onto live city data. Be polite: cache what you fetch and do not hammer the endpoint in a loop."),
 (s_bullets("This lesson", "Your build", [
   "Pull a real Chicago dataset (libraries, or pick your own)",
   "Three questions answered with your three moves",
   "One honest chart, claim title and all"], closing=True),
  "Your build: pull a real Chicago dataset — the libraries, or choose your own from the portal — answer three questions with your moves, and ship one honest chart with a claim title. This is not practice data. This is your actual city, and next lesson you investigate it properly."),
]

L["chsai-data-8"] = [
 (s_title("Working with Data · Lesson 8", "The investigation",
          "question first. Chart last. Log everything between."),
  "Seven lessons of skills: tables, the three moves, cleaning, group by, honest charts, lie-spotting, live city data. The finale is an investigation of your own — and the pipeline that carries every real data project from question to answer."),
 (s_loop("The pipeline", "Every investigation, same shape",
         ["question", "load", "clean", "analyze", "chart"],
         note="The question comes FIRST — before you ever touch the data."),
  "The pipeline, in order. Question first, written down before you touch data — like: which side of the city has more library coverage? Then load. Then clean, with the log. Then analyze — group by does the heavy lifting. Then chart, with a claim title. The question leads; the data answers."),
 (s_bullets("The write-up", "What you ship", [
   "The question, stated up front",
   "The cleaning log — every decision, defended",
   "The chart with its claim title",
   "Two sentences of findings that claim ONLY what the data shows"]),
  "What you ship: the question up front, the cleaning log with every decision defended, the chart with its claim, and two sentences of findings that claim only what the data shows. If lesson four taught you anything: found is not explained. Your write-up says what is true and stops."),
 (s_bullets("Course complete", "Investigate something real", [
   "Pick a city dataset that touches YOUR neighborhood",
   "Run the pipeline end to end; commit the notebook",
   "You can now put evidence under an argument. Use it."], closing=True),
  "Pick a dataset that touches your own neighborhood, run the pipeline end to end, and commit the notebook with a real message. Course complete. You can load, clean, question, and chart real data honestly — which means you can put evidence under an argument. That skill does not expire."),
]

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    build_all(L, "Working with Data", only)
