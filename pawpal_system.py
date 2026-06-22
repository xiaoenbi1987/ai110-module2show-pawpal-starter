"""PawPal+ 核心逻辑层：定义 Task、Pet、Owner、Scheduler 四个类。"""

from dataclasses import dataclass, field


# 把优先级文字映射成数字权重，方便排序（high 最重要）
PRIORITY_WEIGHT = {"high": 3, "medium": 2, "low": 1}


@dataclass
class Task:
    """一个宠物护理任务（如遛狗、喂食）。"""
    name: str
    duration: int          # 时长（分钟）
    priority: str          # "high" / "medium" / "low"
    completed: bool = False

    def mark_complete(self):
        """把这个任务标记为已完成。"""
        self.completed = True


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
    """“大脑”：负责把任务组织成每日计划。"""

    def sort_tasks(self, tasks):
        """按优先级排序（high 在前）。"""
        return sorted(tasks, key=lambda t: PRIORITY_WEIGHT[t.priority], reverse=True)

    def generate_plan(self, owner):
        """为主人生成每日护理计划（按优先级排好序的任务列表）。"""
        all_tasks = owner.get_all_tasks()
        return self.sort_tasks(all_tasks)