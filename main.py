from base import task_study
from base import user_un, user_var, user_study

from math import pi, cos, sin, atan
from random import randint, choice
rad = lambda x: x * pi / 180
grad = lambda x: 180 * x / pi

def task(text_task):
    text, result = None, None
    exec(text_task)
    return text, result


def main():
    def task():
        pass
    text = """
def task():
    F1 = F2 = randint(3, 10)
    alpha = choice([30, 45, 60])
    text = f'Определить модуль равнодействующей двух равных по модулю сходящихся сил F1 = F2 = {F1} Н, образующих между собой угол α = {alpha}°.'
    alpha = rad(alpha)
    result = round((F1**2 + F2**2 + 2 * F1 * F2 * cos(alpha))**0.5, 2)
    return text, result"""
    # Операции с базой данных
    users = task_study()
    # users.create_table()
    # users.delete_table()
    # users.put_item(task_id=1, category='static', types='cod', text=text)
    # users.update_active(user_id=124, active=1)
    # users.delete_note(123)
    # info = users.info_user(23343)
    elem = users.get_task(task_id=1, category='static')

    # print(users.for_mailer())
    # print(users.all_tasks())
    print(elem['text'])
    # print(task())


if __name__ == '__main__':
    main()
