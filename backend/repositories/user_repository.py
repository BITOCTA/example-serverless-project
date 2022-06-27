from abc import abstractmethod, ABC
import boto3

import uuid

from models.user import User, CreateUser

class UserRepository(ABC):

    @abstractmethod
    def create_user(self, user: CreateUser) -> str:
        pass

    @abstractmethod
    def get_users(self) -> list:
        pass

    @abstractmethod
    def get_user(self, user_id: str) -> User:
        pass

    @abstractmethod
    def delete_user(self, user_id: str):
        pass

class DynamoUserRepository:

    def __init__(self, users_table_name: str):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(users_table_name)

    def create_user(self, user: CreateUser) -> str:
        user_id = str(uuid.uuid4())
        self.table.put_item(Item={"id": user_id,**user.__dict__})
        return user_id

    def get_users(self) -> list:
        response = self.table.scan()
        return [User(**item).id for item in response['Items']]

    def get_user(self, user_id: str) -> User:
        response = self.table.get_item(Key={"id": user_id})
        return User(**response['Item'])

    def delete_user(self, user_id: str):
        self.table.delete_item(Key={"id": user_id})
        return True
