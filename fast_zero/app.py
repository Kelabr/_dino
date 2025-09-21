from fastapi import FastAPI 

from http import HTTPStatus

from .schemas import Menssage

from fastapi.responses import HTMLResponse

app = FastAPI()  

@app.get('/', status_code=HTTPStatus.OK, response_model=Menssage)  
def read_root():  
    return {'message': 'Olá Mundo!'}

@app.get('/html', response_class=HTMLResponse)
def read_html():
    return"<h1>Olá Mundo!</h1>"