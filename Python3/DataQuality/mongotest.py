from pymongo import MongoClient

client = MongoClient('localhost',27017)
print(client.list_databases())

client.close()
