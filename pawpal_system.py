"""PawPal+ 核心逻辑层：定义 Task、Pet、Owner、Scheduler 四个类。"""

from dataclasses import dataclass, field
from datetime import date, timedelta


# 把优先级文字映射成数字权重，方便排序（high 最重要）
PRIORITY_WEIGHT = {"high": 3, "medium": 2, "low": 1}


@dataclass
class Task:
    """一个宠物护理任务（如遛狗、喂食）。"""
    name: str
    duration: int                  # 时长（分钟）
    priority: str                  # "high" / "medium" / "low"
    start_time: str = "00:00"      # 开始时间，"HH:MM" 格式
    frequency: str = "once"        # "once" / "daily" / "weekly"
    due_date: date = field(default_factory=date.today)
    completed: bool = False

    def mark_complete(self):
        """标记为已完成；若是重复任务，返回下一次的新任务，否则返回 None。"""
        self.completed = True
        return self.next_occurrence()

    def next_occurrence(self):
        """为 daily/weekly 任务生成下一次的新 Task；其他返回 None。"""
        if self.frequency == "daily":
            next_date = self.due_date + timedelta(days=1)
        elif self.frequency == "weekly":
            next_date = self.due_date + timedelta(weeks=1)
        else:
            return None
        return Task(
            name=self.name,
            duration=self.duration,
            priority=self.priority,
            start_time=self.start_time,
            frequency=self.frequency,
            due_date=next_date,
            completed=False,
        )


@dataclass
class Pet:
    """一只宠物，拥有自己的任务列表。"""
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """给这只宠物添加一个任务。"""
        self.tasks.append(task)

    def list_tasks(self):
        """返回这只宠物的所有任务。"""
        return self.tasks


class Owner:
    """宠物主人，管理一只或多只宠物。"""

    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        """给主人添加一只宠物。"""
        self.pets.append(pet)

    def get_all_tasks(self):
        """返回该主人名下所有宠物的全部任务。"""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.list_tasks())
        return all_tasks


class Scheduler:
    """“大脑”：负责排序、筛选、冲突检测，生成每日计划。"""

    def sort_tasks(self, tasks):
        """按优先级排序（high 在前）。"""
        return sorted(tasks, key=lambda t: PRIORITY_WEIGHT[t.priority], reverse=True)

    def sort_by_time(self, tasks):
        """按开始时间排序（早的在前）。HH:MM 字符串本身就能正确排序。"""
        return sorted(tasks, key=lambda t: t.start_time)

    def filter_tasks(self, tasks, completed=None):
        """按完成状态筛选；True=只看已完成，False=只看未完成，None=全部。"""
        if completed is None:
            return list(tasks)
        return [t for t in tasks if t.completed == completed]

    def detect_conflicts(self, tasks):
        """检测开始时间相同的任务，返回警告文字列表（不会让程序崩溃）。"""
        warnings = []
        seen = {}
        for t in tasks:
            if t.start_time in seen:
                warnings.append(
                    f"Conflict: '{t.name}' and '{seen[t.start_time]}' are both at {t.start_time}"
                )
            else:
                seen[t.start_time] = t.name
        return warnings

    def generate_plan(self, owner):
        """生成每日计划：按优先级排好序的任务列表。"""
        all_tasks = owner.get_all_tasks()
        return self.sort_tasks(all_tasks)