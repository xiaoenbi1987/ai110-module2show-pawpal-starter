"""PawPal+ 演示脚本：在终端验证核心逻辑是否正常工作。"""

from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # 1. 创建一个主人
    owner = Owner("Alice")

    # 2. 创建两只宠物
    biscuit = Pet("Biscuit", "Golden Retriever")
    mochi = Pet("Mochi", "Cat")

    # 3. 把宠物加给主人
    owner.add_pet(biscuit)
    owner.add_pet(mochi)

    # 4. 给宠物添加任务（不同优先级和时长）
    biscuit.add_task(Task("Morning walk", duration=30, priority="high"))
    biscuit.add_task(Task("Feeding", duration=10, priority="medium"))
    mochi.add_task(Task("Litter cleaning", duration=5, priority="low"))
    mochi.add_task(Task("Play time", duration=15, priority="high"))

    # 5. 用调度器生成今日计划
    scheduler = Scheduler()
    plan = scheduler.generate_plan(owner)

    # 6. 打印今日计划
    print(f"===== Today's Schedule for {owner.name} =====")
    for task in plan:
        status = "x" if task.completed else " "
        print(f"[{status}] {task.name}  ({task.duration} min)  priority: {task.priority}")


if __name__ == "__main__":
    main()