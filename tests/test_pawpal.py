"""PawPal+ 快速测试：验证核心行为。"""

from pawpal_system import Pet, Task


def test_mark_complete():
    """验证 mark_complete() 能把任务状态改成已完成。"""
    task = Task("Walk", duration=30, priority="high")
    assert task.completed is False   # 一开始没完成
    task.mark_complete()
    assert task.completed is True    # 调用后变成已完成


def test_add_task_increases_count():
    """验证给宠物加任务后，任务数量增加。"""
    pet = Pet("Biscuit", "Dog")
    assert len(pet.tasks) == 0       # 一开始没有任务
    pet.add_task(Task("Feeding", duration=10, priority="medium"))
    assert len(pet.tasks) == 1       # 加了一个后变成 1