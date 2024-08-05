import boto3
from boto3.dynamodb.conditions import Key
from os import getenv
from dotenv import load_dotenv

class TaskStudy:
    """Класс для управления записями в базе данных YDB, название класса не принципиально.
    """
    def __init__(self, dynamodb=None):
        """Инициализация базы данных и сервисного аккаунта, в целях безопасности используются
           переменные окружения, либо указанные в файле .env
        """
        self.dynamodb = dynamodb
        self.table = 'Task_Study'
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
        """Метод создания таблицы, инициализируются ключи и столбцы таблицы
        """
        table = self.dynamodb.create_table(
            TableName = self.table,
            KeySchema = [
                {
                    'AttributeName': 'task_id',
                    'KeyType': 'HASH'  # Ключ партицирования
                },
                {
                    'AttributeName': 'category',
                    'KeyType': 'RANGE'  # Ключ сортировки
                }
            ],
            AttributeDefinitions = [
                {
                "AttributeName": "task_id",
                "AttributeType": "N"
                },
                {
                "AttributeName": "category",
                "AttributeType": "S"
                },
                {
                "AttributeName": "types",
                "AttributeType": "S"
                },
                {
                "AttributeName": "text",
                "AttributeType": "S"
                }
            ]
        )
        return table

    def put_item(self, task_id, category, types, text):
        """Метод добавления записи в таблицу.
        """
        table = self.dynamodb.Table(self.table)
        response = table.put_item(
            Item = {
                    'task_id': task_id,
                    'category': category,
                    'types': types,
                    'text': text
            }
        )
        return response

    def update_task(self, task_id, category, text):
        """Метод обновления задачи по ключам партицирования и сортировки.
        """
        table = self.dynamodb.Table(self.table)
        response = table.update_item(
            Key = {
                'task_id': task_id,
                'category': category
            },
            UpdateExpression = f"set text = :t ",
            ExpressionAttributeValues = {
                ':t': text
            },
            ReturnValues = "UPDATED_NEW"
        )
        return response

    def get_task(self, task_id, category):
        """Метод запроса задачи по ключу партицирования и ключу сортировки
        """
        table = self.dynamodb.Table(self.table)
        response = table.get_item(
            Key = {
                'task_id': task_id,
                'category': category
            }
        )
        return response['Item']

    def all_tasks(self):
        """Метод сканирования всех элементов таблицы.
        """
        table = self.dynamodb.Table(self.table)
        return table.scan()['Items']


    def delete_note(self, task_id, category):
        """Метод удаления записи из базы данных.
        """
        table = self.dynamodb.Table(self.table)
        try:
            response = table.delete_item(
                Key = {
                    'task_id': task_id,
                    'category': category
                    },
                )
            return response

        except Exception as e:
            print('Error', e)


    def delete_table(self):
        """Метод удаления таблицы из базы данных
        """
        table = self.dynamodb.Table(self.table)
        table.delete()