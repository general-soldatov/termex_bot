from os import getenv
from dotenv import load_dotenv
from base.list_users import ListUsers

load_dotenv()
ENDPOINT = getenv('ENDPOINT')

def main():
    users = ListUsers(ENDPOINT)
    series_table = users.create_table()
    print("Table status:", series_table.table_status)


if __name__ == '__main__':
    main()
