from pydantic import BaseModel
from typing import List, Dict
#in progress of my learning
class User(BaseModel):
    id : int
    name : str

user = User(id=123,name=234)
# assert user.id == 123
# assert user.name == 234
print(user.id)
print(user.name)

'''
Type Annotations

'''
age : int = 5
print(age)
age = 'String'
print(age)

'''
Pydantic Library usage.
Huge improvement 
'''
from datetime import datetime
from typing import List
from pydantic import BaseModel

class User(BaseModel):
    id: int
    val: float
    name = 'John Doe'
    signup_ts: datetime = None
    friends: List[int] = []

external_data = {
    'id': '123',
    'val':123,
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3']
}
user = User(**external_data)
print(user.id)
print(repr(user.signup_ts))
print(user.friends)
print(user.dict())
