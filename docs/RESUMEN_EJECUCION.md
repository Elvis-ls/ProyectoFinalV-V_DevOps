# Resumen de Ejecución - Proyecto Integrador Final

## 1. Estado de la Implementación
- **CRUD Funcional:** La aplicación permite crear, listar, actualizar estado y eliminar tareas.
- **Frontend:** Implementado con Bootstrap 5, responsivo y con indicadores de ambiente.
- **Docker:** Configurado para Desarrollo (`docker-compose.yml`) y Pruebas (`docker-compose.test.yml`).
- **Automatización:** `Makefile` y scripts de Bash (`scripts/`) operativos.

## 2. Resultados de DevOps
- **Ambientes:** Separación clara entre desarrollo y test.
- **CI/CD:** Pipeline de GitHub Actions definido para linting y pruebas automáticas.
- **Reproducibilidad:** El sistema se puede levantar con un solo comando `make run`.

## 3. Resultados de V&V
- **Pruebas Unitarias/Funcionales:** 6 pruebas ejecutadas con éxito.
- **Casos Cubiertos:**
    - Carga de página principal.
    - Creación de tarea (éxito).
    - Prevención de tareas vacías (negativo).
    - Actualización de estado.
    - Eliminación de tarea.
    - Manejo de error 404 para tareas inexistentes (borde).
- **Evidencia:** Pruebas ejecutadas con éxito tanto localmente (`pytest`) como en contenedor (`docker-compose.test.yml`) con resultado 100% PASS.
- **Scripts de Soporte:** Se incluyeron scripts `.ps1` para compatibilidad con Windows (PowerShell), además de los scripts `.sh` para Linux.

## 4. Instrucciones de Uso
1. **Instalar dependencias:** `pip install -r requirements.txt`
2. **Ejecutar Pruebas:** `make test` o `python -m pytest tests/`
3. **Iniciar App:** `make run` o `python app/main.py`
