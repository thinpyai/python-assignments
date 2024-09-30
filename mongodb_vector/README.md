#### Setup development environment in local.
In window, 
1. Download python 3.12.* from https://www.python.org/
2. Setup python home (Define PYTHON_HOME. Add to %PYTHON_HOME%/Scripts to Path)
3. Open PowerShell
4. Execute
`
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
`
5. Confirm installed version
`poetry --version`
6. Setup poetry home (Define POETRY_HOME. Add to %POETRY_HOME%/Scripts to Path)
7. Install libraries
`poetry install`


#### TODO
1. write program
2. move to src package
2. add config 
3. read from a file server