.PHONY: setup run stop clean test lint

setup:
	@echo "Construyendo contenedores..."
	docker-compose build

run:
	@echo "Iniciando aplicación en modo Desarrollo..."
	docker-compose up -d
	@echo "Accede en: http://localhost:5000"

stop:
	docker-compose down

test:
	@echo "Ejecutando pruebas en ambiente efímero..."
	docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit

lint:
	flake8 app tests

clean:
	docker-compose down -v
	docker system prune -f
