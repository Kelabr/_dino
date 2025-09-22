from fastapi import FastAPI 

from http import HTTPStatus

from .schemas import Menssage, UserSchema, UserPublic, UserDB

from fastapi.responses import HTMLResponse

app = FastAPI()  

database = []

@app.get('/', status_code=HTTPStatus.OK, response_model=Menssage)  
def read_root():  
    return {'message': 'Olá Mundo!'}

@app.get('/html', response_class=HTMLResponse)
def read_html():
    return"<h1>Olá Mundo!</h1>"

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id
