Development in local machine
=============================
1. Install python 
2. Define python path as environment variable to use python command.
3. Install poetry
Note : For Mac, use python3 and pip3 
``` 
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
pip install poetry
``` 
4. Check installed poetry
```
poetry --version
```
5. Set virtual environment location to the current project
```
poetry config virtualenvs.in-project true
```

6. Run
``` 
poetry install
```
7. Activate virtual environment.
In terminal, 
```
.\.venv\Scripts\activate
```
In git bash, 
```
source .venv/Scripts/activate
```
8. Get the profile-nonprod.pem and put under get-customer-profile dir.
9. Selete python interpreter from virtual environment.
10. Run 
by using script file in terminal
```
./run_script.sh
```
by using VSCode Debugger
Choose "main" in debug mode
11. For installing new package, 
```
poetry add <package name>
```
12. For generating requirements.txt
```
pip freeze > requirements.txt
```

Runtime
=======
keyname and target fields can be the following.
Reference the sample data for the data format.
# TO put the fields and data.

Change config
=============
1. In run_script.sh, change filename to target file.
2. In launch.json, change filename in args.

Troubleshoot
============
1. If .venv folder is created at /Users/<username>/Library/Caches/pypoetry,

check config
```
poetry config --list
```

If virtualenvs.path is specific path like /Users/<username>/Library/Caches/pypoetry
change the path by 
```
poetry config virtualenvs.path .venv
```
