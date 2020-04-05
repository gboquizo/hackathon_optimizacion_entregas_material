@echo off
title Delia's Installing Python Dependencies

SET projectPath=%~dp0..
echo %projectPath%

pause
cmd /k "cd /d %projectPath%\venv & checkIfExist.bat & cd /d %projectPath%\venv\Scripts & activate & cd /d %projectPath% &  pip install -r requirements.txt & pipenv install &  deactivate & cd..& clean.bat"