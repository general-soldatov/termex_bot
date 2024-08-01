from base.list_users import ListUsers
from base.uservar import UserVar

def main():
    users = UserVar()
    # users.create_table()
    # users.delete_table()
    # users.put_item(user_id=123, name='Dap', group='f-44', var=22, var_d1=11)
    users.add_task(user_id=123, task='S4', ball=6)
    # info = users.info_user(23343)
    print("Success")
    # print(users.for_mailer(group='f-44'))
    print(users.all_users())


if __name__ == '__main__':
    main()
