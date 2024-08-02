import math
from base import task_study, user_var
from random import randint, choice

class TaskUser:
    def __init__(self, user_id):
        self.user_id = user_id
        self.tasks = task_study()
        self.user = user_var()

    def get_task(self, category):
        user = self.user.get_user(self.user_id)
        number = user['bonus'][category] + 1
        elem = self.tasks.get_task(number, category)
        if elem['types'] == 'cod':
            return 'cod', *self.task_cod(elem['text'])


    @staticmethod
    def task_cod(txt_task):
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
