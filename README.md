# Backend prueba técnica Notus
Repositorio para prueba técnica Notus.

# Descripción
En este repositorio se encuentra una API hecha con Django Rest Framework para la prueba técnica. Está API simula una herramienta que ejecuta un modelo matemático de predicción de ventas. Cada ejecución del modelo matemático predice las ventas para los siguientes 10 días. Existen 2 tablas principales: Executions y Predictions.

Una **Execution** o ejecución corresponde a una ejecución del modelo matemático. Sus campos son los siguientes:
- name: Nombre de la ejecución.
- status: Estado actual de la ejecución. Para este proyecto se usan los estados "Creado" y "Ejecutado".
- start_date: Fecha de inicio de la predicción.

Una **Prediction** o predicción corresponde a la predicción de ventas de un día para una ejecución. Cada ejecución tiene 10 predicciones asociadas, correspondientes a 10 días consecutivos. Sus campos son los siguientes:
- execution: Ejecución asociada a está predicción.
- sales: Ventas predichas por el modelo.
- date: Fecha correspondiente la predicción.

Puedes acceder a una versión visual de la API a través de un navegador (http://localhost:8000 si sigues las instrucciones de instalación).
# Instalación

Instalar python: https://www.python.org/downloads/

    # Estos comandos se deben correr en la carpeta raíz del proyecto
    # Crear y activar virtual environment
    python -m venv venv
    venv/Scripts/activate

    # instalar requerimientos
    pip install -r requirements.txt
    
    # correr migraciones
    python manage.py migrate
    
    # cargar datos iniciales
    python manage.py seeds
    
    # iniciar servidor
    python manage.py runserver

# Documentación API
### GET /executions
Entrega lista de ejecuciones

### POST /executions
Crea una ejecución. Automáticamente también se crean 10 predicciones, una por día desde "start_date"

    # body de ejemplo:
    {
      name: "nombre ejecución"
      status: "Ejecutado"
      start_date: "2023-10-15"
    }

### GET /executions/{id}
Entrega una ejecución

### PUT /executions/{id}
Actualiza una ejecución
    
    # body de ejemplo:
    {
      name: "nuevo nombre"
      status: "Creado"
      start_date: "2023-10-15"
    }

### GET /executions/{id}/get_predictions
Retorna las predicciones asociadas a una ejecución
