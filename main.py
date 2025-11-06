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
    telefono: int

# Datos ficticios
usuarios_db = [
    Usuario(id=1, 
            nombre="Ana García",
            email="ana.garcia@example.com",
            edad=28, ciudad="Buenos Aires",
            telefono=11-6556-4534),
    Usuario(id=2, nombre="Carlos López", email="carlos.lopez@example.com", edad=34, ciudad="Rosario", telefono=11-3456-6767),
    Usuario(id=3, nombre="Lucía Fernández", email="lucia.fernandez@example.com", edad=22, ciudad="Córdoba", telefono=11-3455-4566),
    Usuario(id=4, nombre="Mariano Torres", email="mariano.torres@example.com", edad=40, ciudad="Mendoza", telefono=11-5678-7677),
    Usuario(id=5, nombre="Valentina Díaz", email="valentina.diaz@example.com", edad=30, ciudad="La Plata", telefono=11-6788-9999),
    Usuario(id=6, nombre="Carlos Rodríguez", email="carlos.rodriguez@example.com", edad=35, ciudad="Córdoba", telefono=11-6788-8888),
    Usuario(id=7, nombre="Ana Martínez", email="ana.martinez@example.com", edad=28, ciudad="Rosario", telefono=11-1111-1111),
    Usuario(id=8, nombre="Diego Fernández", email="diego.fernandez@example.com", edad=42, ciudad="Tucumán", telefono=11-2345-4567),
    Usuario(id=9, nombre="Lucía Sánchez", email="lucia.sanchez@example.com", edad=26, ciudad="Mar del Plata", telefono=11-4567-4567),
    Usuario(id=10, nombre="Javier López", email="javier.lopez@example.com", edad=33, ciudad="Salta", telefono=11-4568-7899),
    Usuario(id=11, nombre="Sofía Ramírez", email="sofia.ramirez@example.com", edad=29, ciudad="San Juan", telefono=11-2344-2344),
    Usuario(id=12, nombre="Miguel Castro", email="miguel.castro@example.com", edad=45, ciudad="Santa Fe", telefono=11-2456-7654),
    Usuario(id=13, nombre="Elena Morales", email="elena.morales@example.com", edad=31, ciudad="Corrientes", telefono=11-4567-8789),
    Usuario(id=14, nombre="Andrés Ruiz", email="andres.ruiz@example.com", edad=38, ciudad="Neuquén", telefono=11-4567-7777)
]

# Rutas
@app.get("/")
def root():
    return {"mensaje": "Bienvenido a mi api de usuarios ficticios"}

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
