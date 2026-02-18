.PHONY: run migrate test shell superuser help

help:
	@echo "Usage:"
	@echo "  make run        - Run the development server"
	@echo "  make migrate    - Apply database migrations"
	@echo "  make test       - Run tests"
	@echo "  make shell      - Open Django shell"
	@echo "  make superuser  - Create a superuser"
	@echo "  make seed       - Populate database with fake data"

PORT ?= 8000

run:
	uv run python manage.py runserver $(PORT)

migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate

test:
	uv run python manage.py test

shell:
	uv run python manage.py shell

superuser:
	uv run python manage.py createsuperuser

seed:
	uv run python manage.py seed_todo
