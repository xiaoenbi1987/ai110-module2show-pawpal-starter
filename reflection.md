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

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
