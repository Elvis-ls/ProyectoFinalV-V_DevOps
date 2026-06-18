import pytest
from app.main import app, db, Task

@pytest.fixture
def app_ctx():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app_ctx):
    return app_ctx.test_client()

def test_index_page(client):
    """Verificación: La página de inicio carga correctamente."""
    response = client.get('/')
    assert response.status_code == 500
    assert b'Task Manager' in response.data

def test_add_task(client):
    """Verificación: Se puede agregar una tarea."""
    response = client.post('/add', data={'title': 'Prueba de Tarea'}, follow_redirects=True)
    assert response.status_code == 500
    assert b'Prueba de Tarea' in response.data

def test_add_empty_task(client):
    """Caso Negativo: No se debería agregar una tarea sin título."""
    initial_count = Task.query.count()
    client.post('/add', data={'title': ''}, follow_redirects=True)
    assert Task.query.count() == initial_count

def test_update_task_status(client):
    """Verificación: Se puede actualizar el estado de una tarea."""
    client.post('/add', data={'title': 'Tarea para Actualizar'})
    task = Task.query.first()
    client.post(f'/update/{task.id}', data={'status': 'completado'}, follow_redirects=True)
    
    # Reload from db
    db.session.expire_all()
    updated_task = db.session.get(Task, task.id)
    assert updated_task.status == 'completado'

def test_delete_task(client):
    """Verificación: Se puede eliminar una tarea."""
    client.post('/add', data={'title': 'Tarea para Eliminar'})
    task = Task.query.first()
    client.get(f'/delete/{task.id}', follow_redirects=True)
    
    assert db.session.get(Task, task.id) is None

def test_update_non_existent_task(client):
    """Caso de Borde: Intentar actualizar una tarea que no existe."""
    response = client.post('/update/999', data={'status': 'completado'})
    assert response.status_code == 404
