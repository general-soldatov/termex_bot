from base.list_users import ListUsers
from base.uservar import UserVar
from base.user_un import UserUn

def main():
    users = UserUn()
    # users.create_table()
    # users.delete_table()
    # users.put_item(user_id=124, name='Dap', active=1)
    # users.update_active(user_id=124, active=1)
    # users.delete_note(123)
    # info = users.info_user(23343)
    print("Success")
    print(users.for_mailer())
    # print(users.all_users())


if __name__ == '__main__':
    main()
