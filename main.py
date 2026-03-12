from fastapi import FastAPI, HTTPException
from database.db import crear_tablas
from services.biblioteca_service import (
    registrar_libro,
    registrar_usuario,
    ver_libros,
    ver_usuarios,
    ver_prestamos,
    prestar_libro,
    devolver_libro
)
from schemas import LibroCreate, UsuarioCreate, PrestamoCreate

app = FastAPI(title="Sistema de Biblioteca")

crear_tablas()

@app.get("/")
def inicio():
    return {
        "mensaje": "API de biblioteca funcionando",
        "opciones": {
            "1": "POST /libros",
            "2": "POST /usuarios",
            "3": "POST /prestamos",
            "4": "DELETE /prestamos/{codigo_libro}",
            "5": "GET /libros",
            "6": "GET /usuarios",
            "7": "GET /prestamos"
        }
    }

@app.post("/libros", summary="1. Registrar libro")
def crear_libro(libro: LibroCreate):
    try:
        mensaje = registrar_libro(libro.titulo, libro.autor, libro.codigo)
        return {"mensaje": mensaje}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/usuarios", summary="2. Registrar usuario")
def crear_usuario(usuario: UsuarioCreate):
    try:
        mensaje = registrar_usuario(usuario.nombre, usuario.id_usuario)
        return {"mensaje": mensaje}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/prestamos", summary="3. Prestar libro")
def crear_prestamo(prestamo: PrestamoCreate):
    try:
        mensaje = prestar_libro(prestamo.codigo_libro, prestamo.id_usuario)
        return {"mensaje": mensaje}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/prestamos/{codigo_libro}", summary="4. Devolver libro")
def devolver_prestamo(codigo_libro: int):
    try:
        mensaje = devolver_libro(codigo_libro)
        return {"mensaje": mensaje}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/libros", summary="5. Ver libros")
def obtener_libros():
    return ver_libros()

@app.get("/usuarios", summary="6. Ver usuarios")
def obtener_usuarios():
    return ver_usuarios()

@app.get("/prestamos", summary="7. Ver préstamos")
def obtener_prestamos():
    return ver_prestamos()