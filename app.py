import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
st.markdown("Plan your pet's daily care tasks, sorted by priority.")

# ---- 应用"记忆"：用 session_state 存住任务列表 ----
# Streamlit 每次点按钮都会重跑整个脚本，
# 把数据存进 session_state 才不会在刷新时丢失。
if "tasks" not in st.session_state:
    st.session_state.tasks = []   # 存的是真正的 Task 对象

st.divider()

# ---- 主人和宠物信息 ----
st.subheader("Owner & Pet")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.divider()

# ---- 添加任务 ----
st.subheader("Add a Task")
col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    # 创建一个真正的 Task 对象，存进 session_state
    new_task = Task(name=task_title, duration=int(duration), priority=priority)
    st.session_state.tasks.append(new_task)
    st.success(f"Added task: {task_title}")

# 显示当前任务
if st.session_state.tasks:
    st.write("Current tasks:")
    st.table([
        {"Task": t.name, "Duration (min)": t.duration, "Priority": t.priority}
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
        # 1. 用当前输入重新搭建 Owner 和 Pet
        owner = Owner(owner_name)
        pet = Pet(pet_name, species)
        for task in st.session_state.tasks:
            pet.add_task(task)
        owner.add_pet(pet)

        # 2. 让调度器生成排好序的计划
        scheduler = Scheduler()
        plan = scheduler.generate_plan(owner)

        # 3. 显示结果
        st.success(f"Today's plan for {owner.name} (pet: {pet.name})")
        st.table([
            {"Task": t.name, "Duration (min)": t.duration, "Priority": t.priority}
            for t in plan
        ])