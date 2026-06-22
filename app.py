import streamlit as st
from datetime import time
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
st.markdown("Plan your pet's daily care tasks — sorted, filtered, and conflict-checked.")

# ---- 应用"记忆"：用 session_state 存住任务列表 ----
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.divider()

# ---- 主人和宠物信息 ----
st.subheader("Owner & Pet")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.divider()

# ---- 添加任务 ----
st.subheader("Add a Task")
col1, col2 = st.columns(2)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col2:
    start_time = st.time_input("Start time", value=time(8, 0))
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

if st.button("Add task"):
    new_task = Task(
        name=task_title,
        duration=int(duration),
        priority=priority,
        start_time=start_time.strftime("%H:%M"),
        frequency=frequency,
    )
    st.session_state.tasks.append(new_task)
    st.success(f"Added task: {task_title} at {new_task.start_time}")

# 显示当前任务
if st.session_state.tasks:
    st.write("Current tasks:")
    st.table([
        {"Task": t.name, "Time": t.start_time, "Duration (min)": t.duration,
         "Priority": t.priority, "Frequency": t.frequency}
        for t in st.session_state.tasks
    ])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

# ---- 生成每日计划 ----
st.subheader("Today's Schedule")

if st.button("Generate schedule"):
    if not st.session_state.tasks:
        st.warning("Add at least one task first.")
    else:
        owner = Owner(owner_name)
        pet = Pet(pet_name, species)
        for task in st.session_state.tasks:
            pet.add_task(task)
        owner.add_pet(pet)

        scheduler = Scheduler()
        all_tasks = owner.get_all_tasks()

        # 冲突检测 → 用 st.warning 显示警告
        conflicts = scheduler.detect_conflicts(all_tasks)
        for w in conflicts:
            st.warning(w)

        # 按时间排序 → 用 st.table 显示日程
        plan = scheduler.sort_by_time(all_tasks)
        st.success(f"Today's plan for {owner.name} (pet: {pet.name}), sorted by time")
        st.table([
            {"Time": t.start_time, "Task": t.name, "Duration (min)": t.duration,
             "Priority": t.priority}
            for t in plan
        ])