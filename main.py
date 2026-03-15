from fastapi import FastAPI, HTTPException, Request, Form, Path
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
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

# Montamos la carpeta frontend para servir los archivos estáticos (style.css, app.js)
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Configuramos Jinja2 para cargar las plantillas desde la carpeta frontend
templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Registrar libro
@app.post("/libros")
async def registrar_libro_api(titulo: str = Form(...), autor: str = Form(...), codigo: int = Form(...)):
    try:
        mensaje = registrar_libro(titulo, autor, codigo)
        return {"mensaje": mensaje, "titulo": titulo, "autor": autor, "codigo": codigo}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Registrar usuario
@app.post("/usuarios")
async def registrar_usuario_api(nombre: str = Form(...), id_usuario: int = Form(...)):
    try:
        mensaje = registrar_usuario(nombre, id_usuario)
        return {"mensaje": mensaje, "nombre": nombre, "id_usuario": id_usuario}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Prestar libro
@app.post("/prestamos")
async def prestar_libro_api(codigo_libro: int = Form(...), id_usuario: int = Form(...)):
    try:
        mensaje = prestar_libro(codigo_libro, id_usuario)  # Llama a la función del servicio
        return {"mensaje": mensaje}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Devolver libro
@app.post("/devoluciones")
async def devolver_libro_api(codigo_libro: int = Form(...)):
    try:
        mensaje = devolver_libro(codigo_libro)
        return {"mensaje": mensaje}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Ver libros
@app.get("/libros")
async def obtener_libros():
    libros = ver_libros()
    return {"libros": libros}

# Ver usuarios
@app.get("/usuarios")
async def obtener_usuarios():
    usuarios = ver_usuarios()
    return {"usuarios": usuarios}

# Ver préstamos
@app.get("/prestamos")
async def obtener_prestamos():
    prestamos = ver_prestamos()
    return {"prestamos": prestamos}

# Inicializar base de datos (crear tablas)
from database.db import crear_tablas
crear_tablas()