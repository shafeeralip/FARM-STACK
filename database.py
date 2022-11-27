import motor.motor_asyncio
from models import Todo

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    document=await collection.find_one({"title": title})
    return document

async def fetch_all_todo():
    todos=[]
    cursor=collection.find({})
    async for documents in cursor:
        todos.append(Todo(**documents))
    
    return todos

async def create_todo(todo):
    docoment=todo
    result=await collection.insert_one(docoment)
    return docoment

async def update_todo(title,desc):
    await collection.update_one({"title": title}, {"$set": {"details": desc}})
    document = await collection.find_one({"title": title})
    return document

async def deletes_todo(title):
    await collection.delete_one({"title": title})
    return True



# async def remove_todo(title):
#     await collection.delete_one({"title": title})
#     return True
