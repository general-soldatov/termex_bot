from .database.tasks_study import TaskStudy
from .database.user_list import ListUsers
from .database.user_var import UserVar
from .database.user_un import UserUn
from .database.gsheet import UserSheet
from .config_data.config import Config, load_config

class task_study(TaskStudy):
    """База данных задач для студентов
    """
    pass

class user_study(ListUsers):
    """Класс базы данных отслеживания и операций с обучающимися из контингента с целью рассылки
    """
    pass

class user_var(UserVar):
    """Класс базы данных запроса первичных данных и баллов обучающегося
    """
    pass

class user_un(UserUn):
    """Класс базы данных для отслеживания активности неавторизованных пользователей"""
    pass

class user_sheet(UserSheet):
    """Класс для работы с гугл-таблицами"""
    pass