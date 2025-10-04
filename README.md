# Python
[![python](https://github.com/Pryanik0071/Python/actions/workflows/test.yml/badge.svg)](https://github.com/Pryanik0071/Python/actions/workflows/test.yml)

## Pyenv
+ `pyenv versions` - List all versions
+ `pyenv version` - Global version
+ `pyenv install <vers>` - Install vers
+ `pyenv global|local` - Set pyenv version

### Linux install - https://www.dwarmstrong.org/pyenv/

## Poetry
+ `poetry config in-project = true` - Create .venv in project folders
+ `poetry init` - Activate poetry. Set ur python version from pyenv
+ `poetry env use python` - Create .venv
+ `poetry add <name> <vers>` - Add module
+ `poetry add --group (-G) <dev> <name>`
+ `poetry remove`
+ `poetry install`
+ `poetry run <>`
+ `poetry show --tree`

## Packages
+ **Flake8**
+ **Pytest**
+ **python-dotenv**
+ **psycopg2-binary**

### Pytest
+ `poetry run pytest` -s - Include prints, -vv - Details.
+ `poetry add pytest-cov` - Установить зависимость
+ `poetry run pytest --cov`

## Solutions
### python\bin_operations\bin
`to_bin:`
+ Число из 10ой в 2ую с count незначащих нулей
+ Return bin number with count left filled '0' digits

## Django
+ django-admin startproject <name> . - Создать проект с именем name
+ python manage.py runserver - Запустить проект
+ python manage.py makemigrations - Миграции
+ python manage.py migrate - Применить миграции

## JS
+ npm init - Создаёт package.json с описанием проекта
+ npm install "lib" - установить зависимости + добавить в package.json инфу о них. Саму папку с зависимостями в .gitignore
+ npm install --save-dev jest - установить dev зависимости

### Links
+ https://ray.so/prompts/code - промты для ИИ
