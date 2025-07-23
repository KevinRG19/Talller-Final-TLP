📘 API para Gestión de Biblioteca Digital
Este sistema ofrece una API para gestionar una biblioteca digital. Está orientado a permitir operaciones básicas sobre libros, tales como registro, consulta, modificación y eliminación.

🚀 Funcionalidades
📖 Listar libros: Retorna todos los libros registrados en el sistema, incluyendo su título, autor, número de páginas y precio.

➕ Agregar libro: Permite registrar un nuevo libro, validando que los campos requeridos (título, autor, precio y páginas) sean válidos.

❌ Eliminar libro: Elimina un libro usando su identificador único (id). Si no existe, retorna un error adecuado.

✏️ Modificar libro: Permite actualizar el número de páginas o aplicar un descuento porcentual sobre su precio (entre 0% y 100%).

📚 Documentación automática
La documentación de la API se genera automáticamente gracias a FastAPI y está disponible de forma interactiva en Swagger UI:

🔗 http://localhost:8000/docs – Swagger UI (interactiva)