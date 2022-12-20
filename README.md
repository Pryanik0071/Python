# Python
[![python](https://github.com/Pryanik0071/Python/actions/workflows/test.yml/badge.svg)](https://github.com/Pryanik0071/Python/actions/workflows/test.yml)

## Pyenv
+ `pyenv versions` - List all versions
+ `pyenv version` - Global version
+ `pyenv install <vers>` - Install vers
+ `pyenv global|local` - Set pyenv version 

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

### Pytest
+ `poetry run pytest` -s - Include prints, -vv - Details.
+ `poetry add pytest-cov` - Установить зависимость
+ `poetry run pytest --cov`

## Solutions
### python\bin_operations\bin
`to_bin:`
+ Число из 10ой в 2ую с count незначащих нулей
+ Return bin number with count left filled '0' digits
