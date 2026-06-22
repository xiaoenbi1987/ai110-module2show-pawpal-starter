# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## ✨ Features

- **Task management** — add pets and care tasks with a name, duration, priority, start time, and frequency.
- **Priority & time sorting** — order tasks by priority (`Scheduler.sort_tasks()`) or chronologically by start time (`Scheduler.sort_by_time()`).
- **Filtering** — filter tasks by completion status (`Scheduler.filter_tasks()`).
- **Conflict warnings** — automatically flags tasks at the same time (`Scheduler.detect_conflicts()`) without crashing.
- **Recurring tasks** — daily/weekly tasks auto-create their next occurrence when completed (`Task.next_occurrence()`, using `timedelta`).
- **Streamlit UI** — an interactive web app to add tasks and generate a conflict-checked daily schedule.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
===== Today's Schedule for Alice =====
[ ] Morning walk  (30 min)  priority: high
[ ] Play time  (15 min)  priority: high
[ ] Feeding  (10 min)  priority: medium
[ ] Litter cleaning  (5 min)  priority: low
```

## 🧪 Testing PawPal+

Run the full test suite from the project root:

```bash
python -m pytest
```

The tests cover five core behaviors: marking a task complete, adding a task to a pet, sorting tasks by time, daily-task recurrence (auto-creating the next day's task), and conflict detection for tasks at the same time.

Sample test output:

```
collected 5 items

tests/test_pawpal.py .....                                  [100%]

===== 5 passed in 0.04s =====
```

**Confidence Level:** ⭐⭐⭐⭐ (4/5) — the core scheduling behaviors are verified by automated tests. With more time I would add edge cases: a pet with no tasks, weekly recurrence, and overlapping durations instead of only exact-time conflicts.

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | Scheduler.sort_by_time(), Scheduler.sort_tasks() | Sort by start time (HH:MM) or by priority |
| Filtering | Scheduler.filter_tasks() | Filter by completion status |
| Conflict handling | Scheduler.detect_conflicts() | Flags tasks with the same start time; returns warnings without crashing |
| Recurring tasks | Task.mark_complete(), Task.next_occurrence() | Daily/weekly tasks auto-create the next occurrence using timedelta |

## 📸 Demo Walkthrough

PawPal+ runs as a Streamlit web app (`streamlit run app.py`). The main screen lets a user:

1. Enter the owner and pet details (name, species).
2. Add care tasks with a title, duration, start time, priority, and frequency, then click **Add task**.
3. Click **Generate schedule** to see today's plan.

When the schedule is generated, the app:
- Sorts all tasks chronologically by start time.
- Shows a yellow **conflict warning** for any two tasks set at the same time.
- Displays the final plan in a clean table.

Example workflow: add the pet "Mochi" → add a "Morning walk" at 08:00 and a "Feeding" at 08:00 → click Generate schedule → the app warns that the two tasks conflict and shows the sorted plan.

Sample CLI output from running `python main.py`:

```
===== Schedule sorted by time =====
08:00  Morning walk  (30 min)  priority: high
12:00  Feeding  (10 min)  priority: medium
12:00  Medication  (5 min)  priority: high
18:00  Evening walk  (30 min)  priority: high

===== Conflict check =====
Conflict: 'Medication' and 'Feeding' are both at 12:00

===== Recurring task =====
Completed: Morning walk on 2026-06-22
Auto-created next: Morning walk on 2026-06-23
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
