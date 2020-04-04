echo %projectPath%
cmd /k "cd /d %projectPath%\venv\Scripts & activate & cd /d %projectPath% & pip install -r requirements.txt && pipenv install"