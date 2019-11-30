from pydantic import BaseModel
#in progress of my learning
class User(BaseModel):
    id : int
    name : str

user = User(id=123,name=234)
# assert user.id == 123
# assert user.name == 234
print(user.id)
print(user.name)
