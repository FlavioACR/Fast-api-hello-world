
# ESTE ES UN EJEMPLO DE UN HELLO WORLD

# Python:
from typing import Optional # Para tipado Estatico: 
from enum import Enum # Enumeraciones de Strings:

# Pydantic:
from pydantic import BaseModel, Field

# Importamos la clase FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

# Creamos una variable que contendra toda nuesta aplicación,
# Instanciando la clase de fastAPI:
app = FastAPI()

# Models:

# Hereda Enum:
class HairColor(Enum):
    white = 'white'
    brown = 'brown'
    black = 'black'
    blonde = 'blonde'
    red = 'red'


class Location(BaseModel):
    city: str
    state: str
    country: str


class Person(BaseModel):
    '''
    Hereda la clase BaseModel
    '''
    # Caracteristicas o atributos de la entidad:
    # Validaciones con Field():
    firts_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Flavio"
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Carrola"
        )
    age: int = Field(
        ...,
        gt=0, 
        le=115,
        example=27
        )
    # Valores Opcionales:
    # Esta Validación se realiza con el modulo Enum: Un conjunto de strins
    # y para validar le pasamos la clase como tipo;
    hair_color: Optional[HairColor] = Field(default=None, example="black")
    is_married: Optional[bool] = Field(default=None, example=False)
    # <>> RETO AGREGAR 3 ATRIBUTOS DE TIPO DE VALOR EXOTICO Y VALIDARLOS.
    # CORREO,# TARJETA,# DIRECCIÓN
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "firt_name": 'Facundo',
    #             "last_name": 'Garcí Martoni',
    #             "age": 21,
    #             "hair_color":'blonde',
    #             "is_married": False,
    #         }
    #     }




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

# Validaciones: Request Body

@app.put("/person/{persone_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the persone ID",
        gt=0
    ),
    person: Person = Body(...),
    # location: Location = Body(...)
   
):
    # Cuando son dos retorno se necesita combertir:
    # results = person.dict()
    # results.update(location.dict())
    # return results
    return person
