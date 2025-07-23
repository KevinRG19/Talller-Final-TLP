from fastapi import FastAPI, HTTPException, status, Query
from pydantic import BaseModel, Field
from typing import List, Optional

# Configuración de FastAPI y Swagger
app = FastAPI(
    title="API de Libros",
    description="Sistema de gestión de una biblioteca digital ",
    version="1.0.0",
)

# Base de datos temporal en memoria
libros_db = []

# Modelo Pydantic para validación
class Libro(BaseModel):
    id: int
    titulo: str = Field(..., min_length=1, example="1984")
    autor: str = Field(..., example="George Orwell")
    precio: float = Field(..., gt=0, example=20.99)
    paginas: int = Field(..., gt=0, example=328)

# Endpoints
@app.get(
    "/libros",
    response_model=List[Libro],
    description="Obtiene el listado completo de libros.",
)
def listar_libros():
    return libros_db

@app.post(
    "/libros",
    response_model=Libro,
    status_code=status.HTTP_201_CREATED,
    description="Agrega un nuevo libro a la biblioteca.",
)
def crear_libro(libro: Libro):
    libros_db.append(libro)
    return libro

@app.put(
    "/libros/{libro_id}",
    response_model=Libro,
    description="Modifica un libro (páginas o aplica descuento).",
)
def modificar_libro(
    libro_id: int,
    paginas: Optional[int] = None,
    descuento: Optional[float] = Query(None, ge=0, le=100),  
):
    for libro in libros_db:
        if libro.id == libro_id:
            if paginas is not None:
                libro.paginas = paginas
            if descuento is not None:
                libro.precio *= (1 - descuento / 100)
            return libro
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Libro no encontrado",
    )

@app.delete(
    "/libros/{libro_id}",
    status_code=status.HTTP_200_OK,
    description="Elimina un libro por su ID.",
)
def eliminar_libro(libro_id: int):
    for i, libro in enumerate(libros_db):
        if libro.id == libro_id:
            libros_db.pop(i)
            return {"message": "Libro eliminado"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Libro no encontrado",
    )