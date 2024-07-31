from base.list_users import ListUsers

def main():
    users = ListUsers()
    # users.create_table()
    # users.delete_table()
    # users.put_item(user_id=12313, name='ddss', group='f-43', date='2024-23')
    # users.update_active(23343, 0)
    # info = users.info_user(23343)
    print("Success")
    print(users.for_mailer(group='f-44'))
    # print(users.all_users())


if __name__ == '__main__':
    main()
