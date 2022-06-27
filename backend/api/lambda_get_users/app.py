import json
import os

from repositories.user_repository import DynamoUserRepository

user_repository = DynamoUserRepository(os.environ.get("USERS_TABLE_NAME"))


def lambda_handler(event, context):
    return {"statusCode": 200, "body": json.dumps(user_repository.get_users())}
