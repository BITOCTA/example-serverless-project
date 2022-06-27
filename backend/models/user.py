from dataclasses import dataclass

@dataclass
class CreateUser:
    first_name: str
    last_name: str
    date_of_birth: str
    email: str


@dataclass
class User(CreateUser):
    id: str
