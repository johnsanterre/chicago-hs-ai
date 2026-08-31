#!/usr/bin/env python3
"""Course 6 — Think with AI: animated lesson videos.
Run: /Users/john/Dropbox/_/tts/venv/bin/python videos_course6.py [slug]"""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from vidlib import s_title, s_bullets, s_chat, s_loop, build_all

L = {}

L["chsai-think-1"] = [
 (s_title("Think with AI · Lesson 1", "Partner, not oracle",
          "fast, tireless, and wrong in specific ways."),
  "Welcome to Think with AI. People get this tool wrong in both directions — some treat it like a genius that is always right, some like a toy that is always wrong. Both groups lose. It is a partner: unbelievably fast at some jobs, quietly unreliable at others. And it never tells you which is which. That part is your job."),
 (s_chat("The blind spots", "Confidently wrong",
   [("you", "What year did our school open?"),
    ("ai", "Your school opened in 1962 and was renamed in 1994."),
    ("you", "...it opened in 1978. It has never been renamed.")],
   note="Same calm tone for right and wrong answers."),
  "Here is the failure mode to memorize: it states wrong facts in exactly the same confident tone as right ones. It cannot see your life, it cannot check its own claims, and it will never say, actually, I am not sure. The confidence is constant. The accuracy is not."),
 (s_bullets("The habit", "Three buckets, every task", [
   "Delegate — low stakes, and you can check it in seconds",
   "Collaborate — it drafts, you decide. Or you draft, it critiques",
   "Never — graded work as yours, judgment calls, anything unverifiable"]),
  "So every task gets sorted before you type anything. Delegate: brainstorms, practice quizzes, explanations — low stakes, instantly checkable. Collaborate: anything going out under your name — it drafts and you decide, or you draft and it critiques. Never: graded work presented as yours, decisions about people, anything you could not verify or defend."),
 (s_bullets("This lesson", "Your move", [
   "Sort nine tasks in the figure, then ten of your own",
   "Two tests: can I check it? does it carry my name?",
   "Your sorted list becomes your lesson-8 playbook"], closing=True),
  "The lesson has a sorting machine with nine real tasks — some of them are genuinely arguable, which is the point. Then sort ten tasks from your own week using the two tests: can I check the result, and does this carry my name. Keep the list. In lesson eight it becomes the front page of your playbook."),
]

L["chsai-think-2"] = [
 (s_title("Think with AI · Lesson 2", "The second message",
          "the first answer is a first draft."),
  "The people who get the most out of AI are not writing magic first prompts. They are better at the second message — because the first answer is almost never the best answer available. This lesson is about what you say next."),
 (s_chat("Steering", "Specifics move it",
   [("you", "Help me plan a study group."),
    ("ai", "1) Pick a time 2) Choose a leader 3) Bring snacks 4) Stay positive!"),
    ("you", "4 of us, chem final in 10 days, one hour Tue/Thu. Plan those sessions."),
    ("ai", "Tuesday: stoichiometry problem set, hardest first. Thursday: everyone brings the 3 problems they missed...")],
   note="Vague reactions steer nothing. Specific reactions steer everything."),
  "Move one: steer. The plan about snacks is not a failure — it is what a vague ask deserves. Say what is wrong and what direction to go. Four of us. Chem final. Ten days. One hour, Tuesday Thursday. Watch a greeting card become a working plan in one message."),
 (s_bullets("Two more moves", "Show, or start clean", [
   "Show an example: “here's one I like — match this style”",
   "Restart when the chat is built on a wrong assumption",
   "Bonus: “ask me two questions before you answer”"]),
  "Move two: show an example. Paste a paragraph in the style you want and say, match this. One example beats three sentences of description. Move three: start clean. When the chat has latched onto a bad assumption, stop arguing with it — open a fresh chat and write a better first ask using everything the wreck taught you."),
 (s_bullets("This lesson", "Run the experiment", [
   "One mediocre answer, improved three ways",
   "Steer it · show it an example · restart clean",
   "Compare the three results — which move earned the most?"], closing=True),
  "The experiment: get one mediocre answer about something real, then improve it three separate ways — steer, show an example, restart. Put the three results side by side. Which move earned the most is worth knowing about the tool. Noticing that it was two minutes of work is worth knowing about everything."),
]

L["chsai-think-3"] = [
 (s_title("Think with AI · Lesson 3", "Make it quiz you",
          "rereading feels like learning. Retrieval is learning."),
  "The trap every student falls into: rereading and highlighting feel productive, because the material starts to look familiar. Familiar is not known. What builds memory is retrieval — pulling the answer out of your own head and finding out immediately if you had it. The struggle is not a problem. The struggle is the mechanism."),
 (s_loop("The session", "How a tutor session runs",
         ["ask", "you answer", "honest feedback"],
         note="One question at a time. No answer until you commit."),
  "The AI is an infinitely patient quizmaster — once you configure it. One question at a time, or it dumps twenty and you skim. Wait for my answer, or it blurts. Tell me exactly what I missed. Get harder as I improve. Around and around: ask, commit, feedback. Forty minutes of that outworks three rereads."),
 (s_bullets("The rule", "Only your notes", [
   "The model can invent facts with total confidence",
   "Studying invented facts is worse than not studying",
   "So: paste YOUR notes, quiz from those only"]),
  "One setting is non-negotiable: quiz me only from the notes I pasted. Here is why. The model can invent plausible facts, and studying invented facts is worse than not studying at all. Your notes go in, its inventions stay out. This rule comes back in lesson five, wearing a different costume."),
 (s_bullets("This lesson", "A real test, a real session", [
   "Configure the five-setting tutor in the figure",
   "Run ten questions on your nearest actual test",
   "Then: teach it your hardest topic, have it grade you"], closing=True),
  "Build the tutor prompt in the figure, then use it for real: your nearest test, your pasted notes, ten questions minimum, committed answers only. Then flip it — explain your hardest topic to the AI and have it grade your explanation. Teaching a thing is the fastest way to find the holes in your version of it."),
]

L["chsai-think-4"] = [
 (s_title("Think with AI · Lesson 4", "Ghostwriter or coach",
          "one makes you better. One makes you replaceable."),
  "There are two ways to point an AI at your writing. Rewrite this for me — the ghostwriter. Or critique this, do not rewrite it — the coach. Same model, same draft, opposite outcomes. This lesson is the difference, and the line."),
 (s_chat("The coach", "Critique keeps the pen in your hand",
   [("you", "Critique my paragraph — don't rewrite it."),
    ("ai", "1) 'basicly' — spelling, and it hedges. 2) 'brought stuff here' — name the stuff. 3) Your best idea is hiding in the last line.")],
   note="Then YOU rewrite. Every word of the revision is yours."),
  "The ghostwriter hands back something smooth, correct, and hollow — it sounds like the average of everything, because that is what the model is. The coach points at your three weakest sentences and says why. Then you rewrite. That is what a great editor does, and nobody calls an editor cheating."),
 (s_bullets("The line", "One test, one sentence", [
   "Could you defend every sentence as yours, out loud?",
   "Voice is the tell — your fingerprints or nobody's",
   "Disclosure: “I drafted this; AI critiqued; I revised.”"]),
  "The line in one test: could you defend every sentence as yours, out loud, to the teacher who assigned it? Yes means coach. No means ghostwriter. Know your school's actual policy, and when AI help is allowed, one honest sentence covers you: I drafted this myself, used AI to critique it, and revised. If writing that sentence would feel like a confession — that is your answer."),
 (s_bullets("This lesson", "Both paths, your paragraph", [
   "Run ghostwriter and coach on something you wrote",
   "Write your own revision from the critique alone",
   "Read all three out loud — which one is a person?"], closing=True),
  "Take a paragraph you actually wrote. Run both paths in separate chats, then write your revision using only the critique. Read all three out loud: original, ghostwritten, revised. One of them stopped sounding like a person. One of them sounds like you — after practice. Keep that one."),
]

L["chsai-think-5"] = [
 (s_title("Think with AI · Lesson 5", "Map, then check",
          "a great research tool that sometimes lies."),
  "For getting oriented in a new topic, the AI is the best tool ever built — the sides of a debate, the key terms, the questions worth asking, in thirty seconds. And in the same thirty seconds it can hand you a wrong number or a source that has never existed. Both things are true. The workflow holds both."),
 (s_chat("The trap", "A perfect-looking citation",
   [("you", "Give me sources on the Chicago River reversal."),
    ("ai", "See Harold Vance's 1962 book 'The River That Ran Backwards' (University of Chicago Press).")],
   note="This book does not exist. The formatting is flawless."),
  "Here is the trap at full strength. Real-sounding author. Plausible title. Proper publisher, right era. This book does not exist. Formatting is the one thing the model never gets wrong — which is exactly why formatting proves nothing. If a citation is load-bearing, open the source or drop the claim."),
 (s_bullets("The workflow", "Two passes", [
   "Pass one — map: overview, vocabulary, the claims",
   "Pass two — verify: every number, name, date, quote",
   "Check against a source you can actually open"]),
  "So: two passes. Pass one, the map — use it freely, it is the AI at its best. Pass two, the verify pass — anything with a number, a name, a date, or a quote gets checked against a source you can actually open before you repeat it. Background framing is low risk. The specific impressive sentence is exactly the one that is sometimes invented."),
 (s_bullets("This lesson", "Catch it lying", [
   "First: a topic you know deeply — hunt the errors",
   "Then: real schoolwork — verify before it enters your notes",
   "The claims that die in checking are the lesson"], closing=True),
  "Start where you have home-field advantage: ask about something you know deeply and hunt for the errors. Seeing how they look in familiar territory teaches you to spot them anywhere. Then do it for real schoolwork. Some claims will die on the verify pass. Those are not the failure of the exercise — they are the point of it."),
]

L["chsai-think-6"] = [
 (s_title("Think with AI · Lesson 6", "Split until it fits",
          "big things stall because they don't fit in a day."),
  "You know the feeling. Research project, due in four weeks, sitting in your head as one giant object — too big to start, so you don't. The problem is not effort. The problem is that do-the-project is not a task. It is a category of tasks, pretending to be one."),
 (s_loop("The method", "Decomposition", ["split", "check the pieces", "split again"],
         note="Stop when each piece fits one sitting and has a visible finish."),
  "The fix is splitting: break the thing, then break the pieces, until every task passes two tests. It fits in one sitting. And it has a visible finish — three sources found and saved, you know when it is done. Work on research — you never know when it is done. Split, check, split again."),
 (s_bullets("The partnership", "AI proposes, you own it", [
   "Give it the assignment AND your real constraints",
   "Push back on lazy splits: “step 2 is still three tasks”",
   "You put the dates on — it can't see your life"]),
  "The AI is a strong splitting partner: hand it the whole assignment and your real constraints — forty-five minutes on weekdays, practice on Wednesdays — and it proposes a plan. Then do the three things it cannot. Push back on lazy splits. Add the steps it could not know about. And put the dates on yourself, with the scary task early — week four is a bad time to discover the hard part."),
 (s_bullets("This lesson", "Split something real", [
   "The biggest thing looming in your life, split with the AI",
   "Fix two lazy splits, add one step it missed",
   "Then do task one this week — did it fit the sitting?"], closing=True),
  "Take the biggest thing actually looming — project, application, event — and split it with the AI. Earn the plan: fix at least two lazy splits, add at least one step it could not know, date everything. Then the real test: do task one this week and report whether it truly fit one sitting. Plans that survive contact with a Tuesday are the only kind that count."),
]

L["chsai-think-7"] = [
 (s_title("Think with AI · Lesson 7", "Prompts with slots",
          "the tenth same request is a workflow."),
  "Look at a month of your AI use and patterns jump out: the email that needs to sound right, the long thing you need short, practice questions before every test. The tenth time you type the same kind of prompt, you do not have a habit. You have a workflow. Write it down once."),
 (s_chat("A template", "Written once, reused forever",
   [("you", "Draft a short email to [my counselor — schedule change]. What I need: [approve the switch]. Keep my casual tone, don't make it stiff. Under 120 words, one specific ask.")],
   note="The brackets are slots. Everything else is saved judgment."),
  "A template is a prompt with slots — the parts that change get brackets, everything else is your accumulated judgment: the tone you want, the format that works, the limits that keep it honest. Lesson four lives inside your templates now. Filling two slots takes thirty seconds. The judgment was written once."),
 (s_bullets("The file", "Keep them somewhere boring", [
   "A note on your phone: “my prompts”",
   "Five great templates beat fifty screenshots",
   "Each use improves the template — add the fix"]),
  "Keep them somewhere boring and permanent — a note titled my prompts. Five templates you actually reuse beat fifty clever screenshots you will never find again. And templates are drafts forever: every time one comes back missing something, add the fix. Yours get better every week. That compounding is the whole reason to write them down."),
 (s_bullets("This lesson", "Find your third repeat", [
   "Two template patterns in the figure are yours to steal",
   "Find the repeat that's actually yours; write it with slots",
   "Use it once for real, then improve it"], closing=True),
  "The figure hands you two template patterns to steal outright. The assignment is the third one: the repeat that is actually yours. Write it with the slots marked, use it once for real, improve it from what came back. Your prompt file starts at three templates and becomes a section of your lesson-eight playbook."),
]

L["chsai-think-8"] = [
 (s_title("Think with AI · Lesson 8", "One real week",
          "not a demo. Your actual week, documented."),
  "Everything in this course was practice for an ordinary week. The capstone is running one. Your real classes, your real deadlines, your AI partner — with the log open the whole time. Not a demo week. The one you were going to have anyway."),
 (s_bullets("The shape", "Sunday to Friday", [
   "Sunday: split the week, sort every task into its bucket",
   "All week: tutor before tests, critique on writing, verify facts",
   "Templates for the repeats; steer, show, restart as needed"]),
  "Sunday: split the coming week, lesson-six style, and sort every task into its bucket. Then work the plan. Tutor sessions before anything test-like. Critique mode — never ghostwriting — on anything you write. The verify pass on any fact before you repeat it. Your templates for the repeats. Every skill, one ordinary week."),
 (s_bullets("The log", "Failures required", [
   "Each interaction: what you asked, what came back, kept / fixed / thrown out",
   "A spotless log means light use — or no scrutiny",
   "The throwaways are evidence you were paying attention"]),
  "The log is the assignment. For every real interaction: what you asked, what came back, and the verdict — kept it, fixed it, threw it out. Failures are required. A week of real use produces throwaways, so a spotless log means you either barely used the tool or never looked hard at what it returned."),
 (s_bullets("The playbook", "One page, your voice", [
   "Your buckets, your tutor prompt, your templates, your never-list",
   "The one rule you'd give a friend starting out",
   "Presented to the class in five minutes — this is the grade"], closing=True),
  "Friday: write the playbook. One page, your voice. Your buckets with your examples. Your tutor prompt. Your templates. Your never-list. And the one rule you would give a friend who is starting out. That page is the actual product of this course — present it in five minutes, defend it, and expect it to change by spring. Good playbooks always do."),
]

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    build_all(L, "Think with AI", only)
