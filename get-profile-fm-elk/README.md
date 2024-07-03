Development in local machine
=============================
1. Install python 
2. Define python path as environment variable to use python command.
3. Install poetry
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
4. Install elasticsearch package
$ python -m pip install elasticsearch
5. For using async/await
$ python -m pip install elasticsearch[async]