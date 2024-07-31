import boto3
from os import getenv
from dotenv import load_dotenv


class ListUsers:
    def __init__(self, dynamodb=None):
        self.dynamodb = dynamodb
        self.table = 'List_Users'
        if not self.dynamodb:
            load_dotenv()
            self.dynamodb = boto3.resource(
                'dynamodb',
                endpoint_url=getenv('ENDPOINT'),
                region_name='ru-central1',
                aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY')
                )

    def create_table(self):
        table = self.dynamodb.create_table(
            TableName = self.table,
            KeySchema = [
                {
                    'AttributeName': 'user_id',
                    'KeyType': 'HASH'  # Ключ партицирования
                }
            ],
            AttributeDefinitions = [
                {
                "AttributeName": "user_id",
                "AttributeType": "N"
                },
                {
                "AttributeName": "name",
                "AttributeType": "S"
                },
                {
                "AttributeName": "group",
                "AttributeType": "S"
                },
                {
                "AttributeName": "date",
                "AttributeType": "S"
                }

            ]
        )
        return table

    def put_item(self, user_id, name, group, date):
        table = self.dynamodb.Table(self.table)
        response = table.put_item(
            Item = {
                    'user_id': user_id,
                    'name': name,
                    'group': group,
                    'date': date
            }
        )
        return response

    def update(self, user_id, name, group, date):
        table = self.dynamodb.Table(self.table)
        # response = table.put_item(
        #     Item = {
        #             'user_id': user_id,
        #             'name': name,
        #             'group': group,
        #             'date': date
        #     }
        # )
        # return response

    def delete_table(self):
        table = self.dynamodb.Table(self.table)
        table.delete()
