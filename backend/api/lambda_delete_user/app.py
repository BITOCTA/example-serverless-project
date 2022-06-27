import json
from repositories.user_repository import DynamoUserRepository

import os

user_repository = DynamoUserRepository(os.environ['USERS_TABLE_NAME'])


def lambda_handler(event, context):
    return {"statusCode": 200, "body": json.dumps(user_repository.delete_user(event['pathParameters']['user_id']))}
