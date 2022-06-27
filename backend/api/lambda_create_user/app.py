import json
from repositories.user_repository import DynamoUserRepository
from models.user import CreateUser

import os

user_repository = DynamoUserRepository(os.environ['USERS_TABLE_NAME'])

def lambda_handler(event, context):
    return {"statusCode": 200, "body" : json.dumps({"id":user_repository.create_user(CreateUser(**json.loads(event['body'])))})}
    
    
    