
# ESTE ES UN EJEMPLO DE UN HELLO WORLD

# Python:
from typing import Optional # Para tipado Estatico: 

# Pydantic:
from pydantic import BaseModel

# Importamos la clase FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

# Creamos una variable que contendra toda nuesta aplicación,
# Instanciando la clase de fastAPI:
app = FastAPI()

# Models:

class Person(BaseModel):
    '''
    Hereda la clase BaseModel
    '''
    # Caracteristicas o atributos de la entidad:
    firts_name: str
    last_name: str 
    age: int
    # Valores Opcionales:
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None



# Path Operations Decorator:
@app.get("/") # Con esto decimos que en el home de la app se ejecutara la función:
def home():
    '''Hello World Function'''
    # Cuando una API se comunica lo hace mediante archivos JSON y en python
    # un JSON son equivalentes a un diccionario.
    return {'Hello':'World'}


# ------- Request and Response Body ------- #

# Como vamos a enviar datos desde el cliente es necesario usa el post.
# En este caso el entry poit, el cual por su texto nos permitira crear
# una nueva persona.
@app.post("/person/new")
# Los triples ... como un parametro son sinonimo de un parametro obligatorio en FastAPI
def create_person(person: Person = Body(...)):
    return person

# Validaciones: Query Parameters:
@app.get("/person/detail") # Ende Point Recibe Query parameter
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        # Esto fue colocado en validaciones de parametros:
        title="Person Name",
        description="This is the persone name. It's between 1 and 50 characters"
        ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required")
):
    return {name: age}

# Validaciones: Path Parameters:
# Recibe Path Parameters:

@app.get('/person/detail/{person_id}')
def show_person(
    person_id : int = Path(
        ..., 
        gt=0,
        title="Person id",
        description="This is the person age & must be greater than 0") # Greater than
):
    return {person_id: "It exists!"}