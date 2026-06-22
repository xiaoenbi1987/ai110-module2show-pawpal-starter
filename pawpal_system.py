"""PawPal+ 核心逻辑层：定义 Task、Pet、Owner、Scheduler 四个类。"""

from dataclasses import dataclass, field


@dataclass
class Task:
    """一个宠物护理任务（如遛狗、喂食）。"""
    name: str
    duration: int          # 时长（分钟）
    priority: str          # "high" / "medium" / "low"
    completed: bool = False

    def mark_complete(self):
        """把这个任务标记为已完成。"""
        pass


@dataclass
class Pet:
    """一只宠物，拥有自己的任务列表。"""
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """给这只宠物添加一个任务。"""
        pass

    def list_tasks(self):
        """返回这只宠物的所有任务。"""
        pass


class Owner:
    """宠物主人，管理一只或多只宠物。"""

    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        """给主人添加一只宠物。"""
        pass

    def get_all_tasks(self):
        """返回该主人名下所有宠物的全部任务。"""
        pass


class Scheduler:
    """“大脑”：负责把任务组织成每日计划。"""

    def sort_tasks(self, tasks):
        """对任务排序（如按优先级或时长）。"""
        pass

    def generate_plan(self, owner):
        """为主人的宠物生成每日护理计划。"""
        pass