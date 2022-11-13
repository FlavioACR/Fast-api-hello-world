
# Imporamos la clase FastAPI
from fastapi import FastAPI

# Creamos una variable que contendra toda nuesta aplicación,
# Instanciando la clase de fastAPI:
app = FastAPI()

# Path Operations Decorator:
@app.get("/") # Con esto decimos que en el home de la app se ejecutara la función:
def home():
    '''Hello World Function'''
    # Cuando una API se comunica lo hace mediante archivos JSON y en python
    # un JSON son equivalentes a un diccionario.
    return {'Hello':'World'}
