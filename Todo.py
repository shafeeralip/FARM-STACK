from fastapi import HTTPException,status,APIRouter
from models import Todo
from database import (
    fetch_all_todo,
    fetch_one_todo,
    deletes_todo,
    create_todo,
    update_todo
)


router=APIRouter(
    tags=['TODO'],
    prefix='/api/todo'
)
# @app.get("/")
# async def get_home():
#     return{"helloo"}

@router.get("")
async def get_todos():
    
    response = await fetch_all_todo()
    return response

@router.get("/{title}",response_model=Todo)
async def get_todo(title:str):
    response=await fetch_one_todo(title)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='not found')
    return response

@router.post("/",response_model=Todo)
async def post_todo(requset:Todo):
    response=await create_todo(requset.dict())
    if response:
        return response
    raise HTTPException(status_code=400,detail='something went wrong')
    
@router.put("/{title}/", response_model=Todo)
async def put_todo(title: str, desc: str):
    print(desc)
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

# @router.put("/{title}",response_model=Todo)
# async def update_todo(title,desc:str):
#     response=await update_todo(title,desc=desc)
#     if response:
#         return response
        
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not updated")

# @router.delete("/{title}/")
# async def delete_todo(title:str):
#     response=await delete_todo(title)
#     if response:
#         return response
#     raise HTTPException(status_code=400,detail='something went wrong')

@router.delete("/{title}")
async def delete_todo(title):
    response = await deletes_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")

