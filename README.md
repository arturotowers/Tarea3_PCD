## Tarea 3: Creación de una API con FastAPI

### Instrucciones

1. **Crear el repositorio en GitHub**:
   - Nombra el repositorio `Tarea3_PCD`.
   - Clónalo en tu máquina local.

2. **Configurar el entorno local**:
   - Crea un ambiente virtual con `python -m venv env`.
   - Activa el ambiente virtual y luego instala las dependencias:
     ```bash
     pip install "fastapi[standard]" sqlalchemy python-dotenv
     ```

3. **Desarrollar la API**:
   - **Crear `main.py`**: Define los endpoints para crear, actualizar, obtener y eliminar usuarios, asegurando la validación de datos como correos únicos y existencia de usuarios.
   - **Configurar `model.py` y `database.py`**: Define el modelo de la base de datos con SQLAlchemy y configura la conexión a SQLite.

4. **Probar la API**:
   - Ejecuta el servidor con `uvicorn main:app --reload`.
   - Usa la interfaz Swagger en `http://127.0.0.1:8000/docs` para interactuar con los endpoints.

5. **Crear archivos adicionales**:
   - **`requirements.txt`**: Genera el archivo con `pip freeze > requirements.txt` para listar las dependencias.
   - **`README.md`**: Añade instrucciones y detalles del proyecto.

6. **Subir cambios a GitHub**:
   - Realiza un commit con `git add .` y `git commit -m "Initial commit"`.
   - Empuja los cambios con `git push origin main`.

Este proceso crea y despliega una API básica con FastAPI, preparada para ser extendida con funcionalidades adicionales.

