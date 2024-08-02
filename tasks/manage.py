import math
from base import task_study, user_study
from random import randint, choice

class TaskManager:
    def __init__(self, num, category):
        self.num = num
        self.category = category
        self.tasks = task_study()


def task(txt_task):
    rad = lambda x: x * math.pi / 180
    grad = lambda x: 180 * x / math.pi
    lcls = locals()
    glbl = {
        'pi': math.pi,
        'cos': math.cos,
        'sin': math.sin,
        'tan': math.tan,
        'arctan': math.atan,
        'randint': randint,
        'choice': choice
    }
    exec(txt_task, glbl, lcls)
    return lcls['text'], lcls['result']