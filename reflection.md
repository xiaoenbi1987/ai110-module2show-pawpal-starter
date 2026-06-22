# PawPal+ Project Reflection

## 1. System Design

My initial design has four classes that mirror the real parts of pet care:

- Task: a single care activity. Stores name, duration (minutes), priority, and a completed flag; has mark_complete().
- Pet: one animal. Stores name and species, and holds a list of its Tasks; can add_task() and list_tasks().
- Owner: the user. Stores name and a list of Pets; can add_pet() and get_all_tasks() across all pets.
- Scheduler: the "brain." It does not store data itself; it reads from an Owner and organizes tasks into a daily plan via sort_tasks() and generate_plan().

Relationships: an Owner has many Pets, each Pet has many Tasks, and the Scheduler reads from the Owner to build the plan. I kept the Scheduler separate from the data classes so the scheduling logic stays in one place and is easy to change later.

**b. Design changes**

Based on AI feedback, I kept the class structure the same but recorded one design decision. The AI pointed out that storing priority as a string ("high"/"medium"/"low") would not sort correctly if compared as plain text (alphabetical order gives the wrong result). I decided to keep priority as a readable string for the user, but have the Scheduler map those strings to numeric weights (high=3, medium=2, low=1) when sorting. I will implement this mapping in the scheduling logic in Phase 4 rather than changing the data class now, to keep the skeleton simple.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler considers three things: priority (high/medium/low), start time (HH:MM), and completion status. Priority decides how important a task is, start time gives the daily order, and completion status lets the owner filter finished vs. unfinished tasks. I treated priority and time as the most important because a busy owner mainly cares about getting urgent tasks done and knowing when each one happens.

**b. Tradeoffs**

One tradeoff: my conflict detection only flags tasks that share the exact same start time, not tasks whose durations overlap. For example, a 30-minute task at 08:00 and a task at 08:15 would not be flagged even though they overlap. This is reasonable for this scenario because it keeps the logic simple and fast, and exact-time clashes are the clearest, most common conflicts for a pet owner. Overlap-by-duration detection could be added later as an improvement.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI throughout the project: to brainstorm the initial class design and generate the Mermaid UML diagram, to scaffold class skeletons, to flesh out method logic, and to debug. The most helpful prompts were specific ones that included my actual code and a clear question, like "here is my Task class skeleton, what relationships or logic bottlenecks am I missing?" Asking for one focused thing at a time worked better than vague open-ended requests.

**b. Judgment and verification**

One moment I did not accept an AI suggestion as-is: the AI flagged that storing priority as a string ("high"/"medium"/"low") would sort incorrectly in alphabetical order. I agreed with the problem but chose my own solution — keeping priority as a readable string and mapping it to numeric weights inside the Scheduler — instead of redesigning the whole field. I verified AI suggestions by running main.py and the pytest suite to confirm the behavior was actually correct, not just plausible-looking.

---

## 4. Testing and Verification

**a. What you tested**

I tested five behaviors: marking a task complete, adding a task to a pet, sorting tasks chronologically by time, daily-task recurrence (a completed daily task creates the next day's task), and conflict detection for two tasks at the same time. These mattered because they are the core promises of the app — if sorting, recurrence, or conflict detection broke, the schedule would be wrong or misleading.

**b. Confidence**

I am fairly confident (4/5) that the scheduler works correctly, because all five automated tests pass and the CLI demo behaves as expected. With more time I would test edge cases: a pet with no tasks, weekly recurrence, and overlapping durations rather than only exact-time conflicts.

---

## 5. Reflection

**a. What went well**

I am most satisfied with the CLI-first workflow: building and verifying the logic in main.py and the test suite before touching the UI made the Streamlit integration smooth, because the "brain" was already proven to work.

**b. What you would improve**

If I had another iteration, I would improve conflict detection to handle overlapping durations (not just identical start times), and let the scheduler balance priority and time together instead of offering them as two separate sorts.

**c. Key takeaway**

The biggest thing I learned is that being the "lead architect" means using AI to move fast while still owning the design decisions and verifying every suggestion. AI is great at generating options and boilerplate, but I had to decide what fit the system and confirm it with tests. Using separate chat sessions for design, implementation, algorithms, and testing also kept each conversation focused and easier to follow.
