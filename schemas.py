from pydantic import BaseModel

class LibroCreate(BaseModel):
    titulo: str
    autor: str
    codigo: int

class UsuarioCreate(BaseModel):
    nombre: str
    id_usuario: int

class PrestamoCreate(BaseModel):
    codigo_libro: int
    id_usuario: int