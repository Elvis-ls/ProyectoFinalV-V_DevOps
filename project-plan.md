# Proyecto Integrador Final – DevOps + V&V: Plan de Ejecución

## 1. Objetivo
Desarrollar y desplegar una aplicación web de gestión de tareas (Task Manager) implementando un flujo completo de DevOps y un marco riguroso de Verificación y Validación (V&V) para garantizar calidad, confiabilidad y automatización.

## 2. Tecnologías Seleccionadas
- **Lenguaje/Framework:** Python 3.11 con Flask.
- **Base de Datos:** SQLite (dentro de contenedores).
- **Frontend:** HTML5/Bootstrap (para rapidez y mejor apariencia).
- **Infraestructura & Ambientes:** Docker & Docker Compose.
- **Automatización:** Bash Scripts y `Makefile`.
- **CI/CD:** GitHub Actions (Build -> Test -> Docker Build -> Push).
- **Pruebas:** Pytest (Unit/Funcional) y Selenium (E2E básico).

## 3. Fases del Proyecto

### Fase 1: Entorno y Arquitectura (Día 1)
- Definir arquitectura multi-contenedor.
- Configurar `Dockerfile` y `docker-compose.yml`.
- Estructura de carpetas: `/app`, `/tests`, `/scripts`, `/docs`.

### Fase 2: Desarrollo del Task Manager (Día 2)
- Implementar API Flask (CRUD).
- Interfaz web con Bootstrap.
- Persistencia en volumen de Docker.

### Fase 3: Componente DevOps (Día 3)
- **Automatización:** Scripts `setup.sh` y `run.sh` para orquestar Docker.
- **Gestión de Ambientes:** Uso de `docker-compose.dev.yml`, `docker-compose.test.yml` y `docker-compose.prod.yml`.
- **CI/CD:** Pipeline en GitHub Actions:
    - Linting con Flake8.
    - Ejecución de Pytest en contenedor efímero.
    - Construcción de imagen de producción.

### Fase 4: Componente V&V (Día 4)
- **Plan de Pruebas:** Matriz de trazabilidad de requisitos.
- **Casos de Prueba:** Escenarios de éxito, fallo de validación y límites.
- **Validación:** Entrevistas simuladas de usuario para confirmar cumplimiento de necesidades.

### Fase 5: Documentación y Entrega (Día 5)
- Documento técnico siguiendo la estructura de la actividad.
- Carpeta de evidencias con logs de Docker y capturas de UI.

## 4. Gestión de Ambientes
- **Dev:** Local o Codespaces, base de datos de desarrollo, debug mode on.
- **Test:** Entorno de CI (GitHub Actions), base de datos efímera, ejecución de pruebas.
- **Producción:** Despliegue simulado (ej. puerto diferente o contenedor separado) con configuraciones de seguridad activas.

## 5. Criterios de Éxito (Basado en Rúbrica)
- Scripts 100% funcionales en Linux.
- Pipeline CI/CD que falle si las pruebas no pasan.
- Casos de prueba que cubran escenarios no felices.
- Documento técnico profesional con arquitectura clara.
