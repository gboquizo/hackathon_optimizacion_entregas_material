@echo off
title Del-ia's deploying
echo Deploying server...
SET mypath=%~dp0
SET proyectPath=%mypath:~0,-1%/hackathon_optimizacion_entregas_material
cd %proyectPath%
cmd /c "python main.py runserver"
title Del-ia's cleaning
echo Cleaning the house...
cd..
del post.bat
START /B CMD.EXE /D /C "DEL clean.bat"

exit