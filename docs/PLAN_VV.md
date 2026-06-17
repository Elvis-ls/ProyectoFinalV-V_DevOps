# Plan de Verificación y Validación (V&V) - Task Manager

## 1. Alcance
Este plan cubre las pruebas funcionales, de regresión y de validación de usuario para la aplicación Task Manager.

## 2. Estrategia de Pruebas
- **Pruebas Unitarias/Funcionales:** Ejecutadas con `Pytest` para validar la lógica del servidor y la base de datos.
- **Pruebas de Integración:** Verificación de la persistencia de datos y comunicación entre el contenedor web y la base de datos SQLite.
- **Validación de Usuario:** Simulación de flujos de trabajo reales para confirmar que la herramienta resuelve la necesidad de gestión de equipos.

## 3. Matriz de Trazabilidad
| Requisito | Caso de Prueba | Tipo | Resultado Esperado |
|-----------|----------------|------|--------------------|
| Crear Tarea | `test_add_task` | Funcional | Tarea guardada y visible en UI |
| Tarea sin título | `test_add_empty_task` | Negativo | El sistema ignora la solicitud |
| Cambiar Estado | `test_update_task_status` | Funcional | Estado cambia de 'pendiente' a 'completado' |
| Eliminar Tarea | `test_delete_task` | Funcional | Tarea desaparece de la lista |
| ID inexistente | `test_update_non_existent_task` | Borde | Respuesta 404 Error |

## 4. Criterios de Aceptación
1. 100% de los casos de prueba automáticos en verde.
2. Interfaz web accesible y responsive.
3. Despliegue reproducible mediante Docker.

## 5. Análisis de Validación (¿Cumple necesidades?)
El sistema permite a un equipo visualizar y actualizar sus pendientes de forma centralizada, eliminando la falta de visibilidad mencionada en el problema inicial.
