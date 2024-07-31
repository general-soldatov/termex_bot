import boto3

class ListUsers:
    def __init__(self, endpoint):
        self.client_docapi = boto3.resource('dynamodb', endpoint_url=endpoint)

    def create_table(self):
        table = self.client_docapi.create_table(
            TableName = 'List_Users',
            KeySchema = [
                {
                    'AttributeName': 'ids',
                    'KeyType': 'HASH'  # Ключ партицирования
                }
            ],
            AttributeDefinitions = [
                {
                "AttributeName": "ids",
                "AttributeType": "INT"
                },
                {
                "AttributeName": "user_id",
                "AttributeType": "INT"
                },
                {
                "AttributeName": "name",
                "AttributeType": "S"
                },
                {
                "AttributeName": "group",
                "AttributeType": "S"
                }

            ]
        )
        return table
