from base.list_users import ListUsers

def main():
    users = ListUsers()
    users.put_item(user_id=23343, name='ddss', group='f-44', date='2024-23')
    print("Success")


if __name__ == '__main__':
    main()
