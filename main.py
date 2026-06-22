"""PawPal+ 演示脚本：验证核心逻辑和智能调度功能。"""

from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner("Alice")
    biscuit = Pet("Biscuit", "Golden Retriever")
    mochi = Pet("Mochi", "Cat")
    owner.add_pet(biscuit)
    owner.add_pet(mochi)

    # 故意乱序添加任务，并带上开始时间和频率
    biscuit.add_task(Task("Evening walk", duration=30, priority="high", start_time="18:00"))
    biscuit.add_task(Task("Morning walk", duration=30, priority="high", start_time="08:00", frequency="daily"))
    mochi.add_task(Task("Feeding", duration=10, priority="medium", start_time="12:00"))
    # 故意制造冲突：和 Feeding 同样 12:00
    mochi.add_task(Task("Medication", duration=5, priority="high", start_time="12:00"))

    scheduler = Scheduler()
    all_tasks = owner.get_all_tasks()

    # 1) 按时间排序
    print("===== Schedule sorted by time =====")
    for t in scheduler.sort_by_time(all_tasks):
        print(f"{t.start_time}  {t.name}  ({t.duration} min)  priority: {t.priority}")

    # 2) 筛选：只看未完成
    print("\n===== Unfinished tasks =====")
    for t in scheduler.filter_tasks(all_tasks, completed=False):
        print(f"- {t.name}")

    # 3) 冲突检测
    print("\n===== Conflict check =====")
    conflicts = scheduler.detect_conflicts(all_tasks)
    if conflicts:
        for w in conflicts:
            print(w)
    else:
        print("No conflicts found.")

    # 4) 重复任务：每日任务完成后自动生成下一次
    print("\n===== Recurring task =====")
    morning = biscuit.list_tasks()[1]   # Morning walk（daily）
    next_task = morning.mark_complete()
    print(f"Completed: {morning.name} on {morning.due_date}")
    if next_task:
        print(f"Auto-created next: {next_task.name} on {next_task.due_date}")


if __name__ == "__main__":
    main()