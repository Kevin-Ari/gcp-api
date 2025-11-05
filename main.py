from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="API de Usuarios Ficticios",
    description="Una API simple para devolver usuarios de ejemplo.",
    version="1.0.0"
)

# Modelo de datos
class Usuario(BaseModel):
    id: int
    nombre: str
    email: str
    edad: int
    ciudad: str

# Datos ficticios
usuarios_db = [
    Usuario(id=1, nombre="Ana García", email="ana.garcia@example.com", edad=28, ciudad="Buenos Aires"),
    Usuario(id=2, nombre="Carlos López", email="carlos.lopez@example.com", edad=34, ciudad="Rosario"),
    Usuario(id=3, nombre="Lucía Fernández", email="lucia.fernandez@example.com", edad=22, ciudad="Córdoba"),
    Usuario(id=4, nombre="Mariano Torres", email="mariano.torres@example.com", edad=40, ciudad="Mendoza"),
    Usuario(id=5, nombre="Valentina Díaz", email="valentina.diaz@example.com", edad=30, ciudad="La Plata"),
]

# Rutas
@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de usuarios ficticios"}

@app.get("/usuarios", response_model=List[Usuario])
def listar_usuarios():
    return usuarios_db

@app.get("/usuarios/{usuario_id}", response_model=Usuario)
def obtener_usuario(usuario_id: int):
    usuario = next((u for u in usuarios_db if u.id == usuario_id), None)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.get("/buscar")
def buscar_usuario(nombre: str = None, ciudad: str = None):
    resultados = usuarios_db
    if nombre:
        resultados = [u for u in resultados if nombre.lower() in u.nombre.lower()]
    if ciudad:
        resultados = [u for u in resultados if ciudad.lower() in u.ciudad.lower()]
    return resultados
