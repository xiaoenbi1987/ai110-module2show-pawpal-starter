"""PawPal+ 测试套件：验证核心行为和智能调度功能。"""

from datetime import date

from pawpal_system import Pet, Task, Owner, Scheduler


def test_mark_complete():
    """验证 mark_complete() 能把任务状态改成已完成。"""
    task = Task("Walk", duration=30, priority="high")
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_add_task_increases_count():
    """验证给宠物加任务后，任务数量增加。"""
    pet = Pet("Biscuit", "Dog")
    assert len(pet.tasks) == 0
    pet.add_task(Task("Feeding", duration=10, priority="medium"))
    assert len(pet.tasks) == 1


def test_sort_by_time():
    """验证任务按开始时间（早到晚）正确排序。"""
    scheduler = Scheduler()
    tasks = [
        Task("Evening", duration=10, priority="low", start_time="18:00"),
        Task("Morning", duration=10, priority="low", start_time="08:00"),
        Task("Noon", duration=10, priority="low", start_time="12:00"),
    ]
    sorted_tasks = scheduler.sort_by_time(tasks)
    times = [t.start_time for t in sorted_tasks]
    assert times == ["08:00", "12:00", "18:00"]


def test_recurring_creates_next_day():
    """验证每日任务完成后，自动生成第二天的新任务。"""
    task = Task("Walk", duration=30, priority="high",
                frequency="daily", due_date=date(2026, 1, 1))
    next_task = task.mark_complete()
    assert next_task is not None
    assert next_task.due_date == date(2026, 1, 2)
    assert next_task.completed is False


def test_detect_conflicts():
    """验证调度器能发现开始时间相同的任务。"""
    scheduler = Scheduler()
    tasks = [
        Task("Feeding", duration=10, priority="medium", start_time="12:00"),
        Task("Medication", duration=5, priority="high", start_time="12:00"),
    ]
    warnings = scheduler.detect_conflicts(tasks)
    assert len(warnings) == 1