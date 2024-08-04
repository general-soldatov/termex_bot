import gspread
from os import getenv
from datetime import datetime
from dotenv import load_dotenv

class UserSheet:
    def __init__(self, user_id, table="Термех 2/2024"):
        self.user_id = user_id
        load_dotenv()
        self.gs = gspread.service_account(filename=getenv('GOOGLE_SERVICE_ACCOUNT'))
        self.table = self.gs.open(table)
        self.contingent = self.table.worksheet('contingent')

    def search_user(self, name):
        all_rows = self.contingent.get_all_values()
        lst = []
        for row in all_rows:
            if row[0].lower() == name.lower():
                lst = row
                break
        return {
            'user_id': self.user_id,
            'name': lst[0],
            'group': lst[1],
            'date': str(datetime.now()),
        }