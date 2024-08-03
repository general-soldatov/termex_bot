import gspread

class UserSheet:
    def __init__(self, table):
        self.gs = gspread.service_account(filename='termex-bot-0ea77baf201b.json')
        self.table = self.gs.open(table)
        self.contingent = self.table.worksheet('contingent')

    def search_user(self, name):
        pass