#!/usr/bin/env python3
"""Course 5 — Build with LLMs: animated lesson videos.
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_course5.py [slug]"""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from vidlib import (s_title, s_bullets, s_notebook, s_loop, s_chat, build_all)

L = {}

L["chsai-llm-1"] = [
 (s_title("Build with LLMs · Lesson 1", "Today, you are the code",
          "underneath every chat window: a request. You send it now."),
  "Every chat window you have ever typed into is code sending a request underneath. Today you are the code. This course you build with language models — and it starts with one call, and one ceremony that keeps everyone safe."),
 (s_bullets("The key ceremony", "Before anything runs", [
   "The class API key is money AND identity",
   "getpass hides it as you paste — NEVER typed into a cell",
   "Never shared, never posted — bots scrape GitHub for keys in minutes"]),
  "First, the key ceremony, because it matters. The class A P I key is money and identity in one string. Getpass hides it as you paste it in — it never gets typed into a cell, never shared, never posted anywhere. Bots scrape GitHub for leaked keys in minutes. Treat it like a debit card number."),
 (s_notebook("The call", "Your first request",
   [(["import anthropic", "client = anthropic.Anthropic()",
      "msg = client.messages.create(", "    model=MODEL, max_tokens=200,",
      "    messages=[{\"role\": \"user\",",
      "      \"content\": \"One fun fact about Chicago.\"}])",
      "print(msg.content[0].text)"],
     [("The Chicago River flows backwards - engineers", "ok"),
      ("reversed it in 1900 to protect the water supply.", "ok")])],
   note="That text came back from the model, through YOUR code."),
  "Now the call. Client dot messages dot create: a model, a token budget, and your message. Run it — and the reply arrives in your notebook, through your code. Same machine as the chat window, no window. From here on, everything the model does, your program controls."),
 (s_bullets("This lesson", "Your build", [
   "Run the ceremony, make three calls with different questions",
   "Print token counts — every call has a cost",
   "Rule of the course: the model is a component YOU direct"], closing=True),
  "Your build: run the ceremony, make three calls with your own questions, and print the token counts — every call costs someone money, and professionals watch the meter. The rule of this whole course: the model is a component, and you are the one directing it."),
]

L["chsai-llm-2"] = [
 (s_title("Build with LLMs · Lesson 2", "You write souls now",
          "same model, different system prompt — different app."),
  "A coding helper, a poem bot, a study coach — three apps, and the secret is they can be the same model. The difference is one parameter: the system prompt. It sets who the model IS before any user says a word. You write souls now."),
 (s_notebook("The soul", "A system prompt, live",
   [(["msg = client.messages.create(", "    model=MODEL, max_tokens=300,",
      "    system=\"You are a writing coach for high-schoolers.\"",
      "           \" Never rewrite their work. Point at weaknesses\"",
      "           \" and ask leading questions.\",",
      "    messages=[{\"role\": \"user\", \"content\": essay}])"],
     [("Your second paragraph makes two claims -", "ok"),
      ("which one is this essay really about?", "ok")])],
   note="Users never see the system prompt. It is the app's soul."),
  "System: you are a writing coach for high-schoolers. Never rewrite their work — point at weaknesses and ask leading questions. Now the model IS that, and the user never sees the instruction. Notice the coach refused to ghostwrite — because the soul you wrote told it to."),
 (s_notebook("The template", "Prompts inside functions",
   [(["def flashcard(topic):",
      "    p = f\"Make one flashcard about {topic}.\"",
      "    return ask(p)   # your call, wrapped", "",
      "flashcard(\"the Chicago Fire\")"],
     [("Q: What year did the Great Chicago Fire begin?", "ok"),
      ("A: 1871", "ok")])],
   note="An f-string builds the prompt; a function makes it reusable. This is an app."),
  "Second move: the template. An f-string drops the topic into a prompt; a function wraps the call. Flashcard of anything, one line. A prompt inside a function inside a loop — that is what an A I app actually is, and you just wrote your first one."),
 (s_bullets("This lesson", "Your build", [
   "Write three souls: a coach, a hype bot, a strict editor",
   "Same user message to each — compare who answers",
   "Then a template function of your own design"], closing=True),
  "Your build: three different souls — a coach, a hype bot, a strict editor — hit with the same user message, answers compared side by side. Then a template function of your own. Lesson four of How A I Works taught you the levers; now you install them permanently."),
]

L["chsai-llm-3"] = [
 (s_title("Build with LLMs · Lesson 3", "The model becomes a component",
          "programs can't read prose. They read JSON."),
  "The model says: the meeting is Thursday at four in room two-fourteen. Lovely sentence — useless to a program. Programs need labeled data: date, time, place. This lesson the model's answers become data your code can use."),
 (s_notebook("The extraction", "ONLY the JSON",
   [(["p = (\"Extract as JSON with keys date, time, place.\"",
      "     \" Output ONLY the JSON.\\n\" + note_text)",
      "raw = ask(p)", "import json", "event = json.loads(raw)",
      "print(event[\"place\"])"],
     [("room 214", "ok")])],
   note="json.loads turns the reply into a real dictionary. Now code can use it."),
  "The extraction prompt: as JSON with keys date, time, place — output ONLY the JSON. Then json dot loads turns the reply into a real dictionary, and event of place just works. The model stopped being a chat partner and became a component in your pipeline."),
 (s_notebook("It will break", "The retry pattern",
   [(["try:", "    event = json.loads(raw)", "except json.JSONDecodeError:",
      "    raw = ask(p + \" JSON ONLY. No other words.\")",
      "    event = json.loads(raw)"],
     [("(the second ask almost always lands)", "ok")])],
   note="Sometimes it adds 'Here's your JSON!' — plan for it. Try, except, retry."),
  "And here is the honest part: sometimes the model adds, here is your JSON! — and json dot loads chokes on the chatter. So professionals wrap it: try, except, retry with a firmer instruction. You learned in course one that the model is a prediction machine; this is what engineering around that fact looks like."),
 (s_bullets("This lesson", "Your build", [
   "Extract events from three messy announcement texts",
   "The try/except retry around every loads",
   "Print event fields into a clean f-string report"], closing=True),
  "Your build: three messy real-world announcements, extracted to dictionaries, with the retry pattern around every parse, and a clean report printed with f-strings. Structured output is the bridge between A I and software. You just walked across it."),
]

L["chsai-llm-4"] = [
 (s_title("Build with LLMs · Lesson 4", "Put the document in the prompt",
          "how every 'chat with your PDF' product actually works."),
  "Ask the model about your robotics club's attendance rule and it cannot know — the cutoff, plus it never read your handbook. Every chat-with-your-P D F product ever built solves this the same way: put the document in the prompt. That is the whole trick, and today it is yours."),
 (s_notebook("The move", "Answer ONLY from the document",
   [(["doc = open(\"handbook.txt\").read()",
      "p = (\"Answer using ONLY the document below.\"",
      "     \" If the answer is not in it, say so.\\n\\n\"",
      "     + doc + \"\\n\\nQ: \" + question)", "print(ask(p))"],
     [("Members may miss two practices per season", "ok"),
      ("before losing competition eligibility.", "ok")])],
   note="Your document, in the context window — the desk from course 1."),
  "Load the handbook into a string. Then the prompt: answer using ONLY the document below — and if the answer is not in it, say so. The correct rule comes back, from YOUR handbook. The document is sitting on the model's desk — the context window you met in How A I Works."),
 (s_bullets("The two guards", "Why the prompt is worded that way", [
   "ONLY the document: blocks confident guesses from training data",
   "Say so if absent: an honest 'not in here' beats an invented rule",
   "The desk has edges: giant documents need trimming to the relevant part"]),
  "The wording carries two guards. ONLY the document blocks the model from confidently answering out of its training data instead of your handbook. Say so if absent gives it an honest exit — because an invented rule read aloud at practice is worse than no answer. And remember the desk has edges: huge documents need trimming to the relevant part."),
 (s_bullets("This lesson", "Your build", [
   "A question-answerer over a document YOU choose",
   "Test it with three answerable and two unanswerable questions",
   "The unanswerable ones are the real test"], closing=True),
  "Your build: a question answerer over a document you choose — club rules, a syllabus, the student handbook. Test with three questions it can answer and two it cannot. The unanswerable pair is the real test: a trustworthy tool says not in here, and yours will."),
]

L["chsai-llm-5"] = [
 (s_title("Build with LLMs · Lesson 5", "Memory is your list",
          "the API forgets everything. Your app remembers."),
  "The chat apps you use feel like they remember you. Here is the secret: the A P I forgets everything between calls. The memory lives in your code — a plain Python list — and today you build a chat app around it, end to end."),
 (s_notebook("The app", "Fifteen honest lines",
   [(["history = []", "", "def chat_turn(user_text):",
      "    history.append({\"role\": \"user\", \"content\": user_text})",
      "    msg = client.messages.create(model=MODEL,",
      "        max_tokens=300, messages=history)",
      "    reply = msg.content[0].text",
      "    history.append({\"role\": \"assistant\", \"content\": reply})",
      "    return reply"],
     [("chat_turn(\"My name is Amara.\")  ...", "ok"),
      ("chat_turn(\"Use my name!\")  -  \"Of course, Amara!\"", "ok")])],
   note="Send THE WHOLE LIST every turn. The list is the memory."),
  "History starts empty. Each turn: append the user message, send the WHOLE list, append the reply. That is the entire app. The proof: tell it your name, then ask it to use your name — and it does, because the list carried it. Fifteen lines, and you have built what the big apps build."),
 (s_bullets("The amnesia demo", "Comment out the appends", [
   "Without the appends, every turn starts from nothing",
   "'Use my name!' - 'You haven't told me your name.'",
   "Sound familiar? The desk demo from course 1 — now it's YOUR desk"]),
  "Now the amnesia demo: comment out the two appends and ask again. You haven't told me your name. Every turn starts from nothing, because nothing carried. If you took How A I Works, you watched Amara's name slide off the desk — this is that demo, except now you own the desk and decide what stays on it."),
 (s_bullets("This lesson", "Your build", [
   "The chat loop, with a soul from lesson 2",
   "A /forget command that clears the list",
   "Print the token count as history grows — desks have edges"], closing=True),
  "Your build: the chat loop with a system-prompt soul from lesson two, a forget command that clears the list, and the token count printed each turn — watch it grow, because desks have edges and long chats cost more. You now understand chat apps at the level of the people who build them."),
]

L["chsai-llm-6"] = [
 (s_title("Build with LLMs · Lesson 6", "Measure, don't argue",
          "two prompts walk in. An eval decides."),
  "Two system prompts for your flashcard maker — which is better? Two people could argue all lunch. Or: measure. An eval is a small harness that scores outputs automatically, and it is the single most professional habit in A I work."),
 (s_notebook("The harness", "Fixed inputs, plain checks",
   [(["topics = [\"the Fire\", \"the El\", \"deep-dish\",",
      "          \"Route 66\", \"the Bean\"]   # never change",
      "def has_qa(c):    return \"Q:\" in c and \"A:\" in c",
      "def short_q(c):   return len(c.split(\"A:\")[0]) < 120",
      "def not_empty(c): return len(c.strip()) > 0"],
     [("(three checks: output in, True/False out)", "ok")]),
    (["# run: both prompts x five topics x three checks"],
     [("Prompt A: 9/15     Prompt B: 13/15", "ok")])],
   note="Fixed topics make scores comparable. B wins — no argument required."),
  "The harness: five fixed topics — fixed, so scores are comparable run to run. Three checks, each a plain function: does it have a Q and an A? Is the question short? Is it non-empty? Run both prompts across all topics: nine out of fifteen versus thirteen. B wins. No argument required."),
 (s_bullets("Why this matters", "Evals are the adult table", [
   "Every serious AI team lives and dies by evals",
   "A check you can code beats an opinion you can argue",
   "Change the prompt? Re-run. Numbers move or they don't."]),
  "This is how the adult table works: every serious A I team lives and dies by evals. A check you can code beats an opinion you can argue. And the payoff compounds — change your prompt, re-run the harness, and the numbers either move or they do not. Vibes cannot do that."),
 (s_bullets("This lesson", "Your build", [
   "Write a third check of your own design",
   "Improve the losing prompt until it beats the winner",
   "Prove the improvement with the harness, not your feelings"], closing=True),
  "Your build: add a third check of your own design, then take the losing prompt and improve it until it beats the winner — proven by the harness, not your feelings. From this lesson on, no prompt in this course ships without a number attached."),
]

L["chsai-llm-7"] = [
 (s_title("Build with LLMs · Lesson 7", "Chatbots talk. Agents do.",
          "the loop that lets a model use tools — built by hand."),
  "Chatbots talk. Agents DO — they check schedules, look things up, take actions. The difference is a loop, and you are about to build it with your own hands, so it will never be magic to you."),
 (s_loop("The loop", "Model asks, you run, result returns",
         ["send + tools", "model: tool_use?", "run the tool", "return result"],
         note="If stop_reason is 'tool_use', the model is ASKING you to run a function."),
  "The loop. Send the question along with a list of tools — plain functions with descriptions the model reads. If the response says stop reason tool use, the model is asking you to run one. Run it, send the result back, and the model finishes its answer with real information. That is an agent — a model in a loop with tools."),
 (s_notebook("The tool", "A function plus a description",
   [(["def practice_schedule(team):",
      "    return SCHEDULES.get(team, \"no such team\")", "",
      "# description the MODEL reads:",
      "# name: practice_schedule",
      "# what: looks up a team's practice time",
      "# input: team (string)"],
     [("model called practice_schedule('robotics')", "ok"),
      ("-> \"Tuesdays 4pm, room 112\" -> final answer", "ok")])],
   note="The description is a prompt. Write it clearly and the model uses it well."),
  "A tool is just a function — practice schedule, team in, time out — plus a description the model reads: the name, what it is for, what inputs it takes. That description is a prompt; write it clearly. Watch the model choose the tool, receive the schedule, and fold it into the answer."),
 (s_bullets("The rules", "Careful is the whole point", [
   "Only tools YOU wrote — the model runs nothing on its own",
   "Read-only tools first; actions need a human yes",
   "Cap the loop — never let it run unattended"], closing=True),
  "The safety rules are the lesson. The model runs nothing — it asks, and YOUR code decides. Start with read-only tools; anything that acts on the world needs a human yes. And cap the loop at a few turns, always. Your build: the schedule agent with two lookup tools, built exactly this carefully."),
]

L["chsai-llm-8"] = [
 (s_title("Build with LLMs · Lesson 8", "Aim it at your week",
          "calls, souls, JSON, documents, memory, evals, tools — yours."),
  "The toolkit is on the table: A P I calls, system prompts, structured output, documents in the prompt, chat memory, evals, and the agent loop. The finale aims all of it at one real helper for YOUR actual week. Pick your build."),
 (s_bullets("The menu", "Pick one, or bring your own", [
   "Study buddy: quizzes you from your own notes",
   "Club communicator: chaos in, clean announcements out",
   "Homework explainer with a strict hint-first soul",
   "Schedule agent with two lookup tools"]),
  "The menu. A study buddy that quizzes you from your own notes — documents plus memory. A club communicator that turns group-chat chaos into clean announcements — extraction plus a soul. A homework explainer with a strict hint-first soul. Or the schedule agent with two tools. Or your own idea, at this size."),
 (s_loop("The method", "Unchanged since the Python capstone",
         ["plan", "build a piece", "test it", "eval it"],
         note="Plan in comments first. One piece at a time. A number before it ships."),
  "The method has not changed since the Python capstone, except for one upgrade: plan in comments first, build one piece at a time, test each piece — and now, eval it. Your helper ships with a small harness and a number attached, because that is what shipping means in this course."),
 (s_bullets("Course complete", "Demo day", [
   "Sign for every line — explain it or don't ship it",
   "Commit with a real message; demo to a classmate",
   "You build with AI now. The practicum is where it goes next"], closing=True),
  "Ship it: sign for every line, commit with a real message, and demo it to a classmate before demo day. Course complete — and look at what you carry out: you call models, write souls, extract data, ground answers in documents, build memory, measure quality, and loop tools safely. You build with A I now."),
]

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    build_all(L, "Build with LLMs", only)
