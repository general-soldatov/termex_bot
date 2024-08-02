from base import user_un, user_var, user_study
from tasks import task_user



def main():
    text = """
F1 = F2 = randint(3, 10)
alpha = choice([30, 45, 60])
text = f'Определить модуль равнодействующей двух равных по модулю сходящихся сил F1 = F2 = {F1} Н, образующих между собой угол α = {alpha}°. Ответ округлить до сотых.'
alpha = rad(alpha)
result = round((F1**2 + F2**2 + 2 * F1 * F2 * cos(alpha))**0.5, 2)"""
    # Операции с базой данных
    users = user_var()
    task = task_user(122)
    # users.create_table()
    # users.delete_table()
    # users.put_item(user_id=122, name='Gvido', group='f-11', var=11, var_d1=12)
    # users.update_active(user_id=124, active=1)
    # users.delete_note(123)
    # info = users.info_user(23343)
    # elem = users.get_task(task_id=1, category='static')
    # task(elem['text'])
    # print(users.for_mailer())
    # users.add_bonus(122, 'kinematic')
    print(task('static'))
    # print(task(text))
    # print(task())


if __name__ == '__main__':
    main()
