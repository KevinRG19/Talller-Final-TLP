from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

# Datos de prueba
LIBRO_EJEMPLO = {
    "id": 1,
    "titulo": "1984",
    "autor": "George Orwell",
    "precio": 20.0,
    "paginas": 328,
}

def test_listar_libros_vacia():
    response = client.get("/libros")
    assert response.status_code == 200
    assert response.json() == []

def test_crear_libro():
    response = client.post("/libros", json=LIBRO_EJEMPLO)
    assert response.status_code == 201
    assert response.json()["titulo"] == "1984"

def test_listar_libros_con_datos():
    response = client.get("/libros")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_modificar_paginas():
    response = client.put("/libros/1?paginas=400")
    assert response.status_code == 200
    assert response.json()["paginas"] == 400

def test_aplicar_descuento():
    response = client.put("/libros/1?descuento=50")
    assert response.status_code == 200
    assert response.json()["precio"] == 10.0  # 50% de 20.0

def test_eliminar_libro():
    response = client.delete("/libros/1")
    assert response.status_code == 200
    response = client.get("/libros")
    assert response.json() == []

def test_error_libro_inexistente():
    # PUT para libro que no existe
    response = client.put("/libros/999?paginas=100")
    assert response.status_code == 404
    # DELETE para libro que no existe
    response = client.delete("/libros/999")
    assert response.status_code == 404