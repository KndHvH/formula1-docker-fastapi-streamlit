APP_NAME="formula1-overview"
IMAGE_NAME="kndhvh/formula1-docker-fastapi-streamlit"

local/install: generate-default-env-file
	pipenv install --dev --skip-lock

local/lint:
	black app/
	flake8 app/

local/check-packages:
	pipenv check --system -e PIPENV_PYUP_API_KEY=""

local/bandit:
	bandit -r . app *.py

local/shell:
	pipenv shell

local/test:
	ENV_FOR_DYNACONF=test python -m pytest -s -c tests/pytest.ini \
	--pyargs ./tests -v --junitxml=results.xml \
	--cov-fail-under 100 --cov-report xml \
	--cov-report term \
	--cov-report html --cov ./app

local/run:
	python run.py


docker/build: generate-default-env-file
	docker-compose build ${APP_NAME}

docker/up:
	docker-compose up -d --build

docker/down:
	docker-compose down --remove-orphans

docker/lint:
	docker-compose run ${APP_NAME} black app/
	docker-compose run ${APP_NAME} flake8 app/

docker/check-packages:
	docker-compose run -e PIPENV_PYUP_API_KEY="" ${APP_NAME} pipenv check --system

docker/bandit:
	docker-compose run ${APP_NAME} bandit -r . app *.py

docker/verify:
	make docker/lint
	make docker/bandit

docker/test:
	docker-compose run -e ENV_FOR_DYNACONF=test ${APP_NAME} \
	python -m pytest -s -c tests/pytest.ini \
	--pyargs ./tests -v  \
	--cov-fail-under 100 --cov-report xml \
	--cov-report term \
	--cov-report html --cov ./app

docker/run:
	docker-compose run --service-port ${APP_NAME} python run.py

docker/migrations/generate:
	docker-compose run ${APP_NAME} alembic revision --autogenerate

docker/migrations/upgrade:
	docker-compose run ${APP_NAME} alembic upgrade head

image/build:
	docker build . --target production -t ${IMAGE_NAME}:${VERSION}

image/push:
	docker push ${IMAGE_NAME}:${VERSION}

generate-default-env-file:
	@if not exist .env copy template.env .env


docker/build/database:
	docker build -t f1_db_image .\database

docker/run/database:
	docker run -e 'POSTGRES_USER=postgres' -e 'POSTGRES_PASSWORD=postgres' -p 5432:5432 -d --name f1_db_server f1_db_image