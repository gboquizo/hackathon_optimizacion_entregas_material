SET projectPath=%~dp0
call "%projectPath%\scripts\dependencies.bat"
timeout 1
call "%projectPath%\scripts\development.bat"
timeout 5
call "%projectPath%\scripts\pydependencies.bat"
