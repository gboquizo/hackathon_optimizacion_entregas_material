@echo off
title Del-ia's Setup

::#################################################################################################################################
:: Elevate this script                                                                                                            #
::#################################################################################################################################

(
    :: Check Admin rights and create VBS Script to elevate
      >nul fsutil dirty query %SYSTEMDRIVE% 2>&1 ||(

        :: Very little red console
        mode con cols=80 lines=3 
        color cf

        :: Message
        title Please wait...
        echo.
        echo                         Requesting elevated shell...
	timeout 3

        :: Create VBS script
        echo Set UAC = CreateObject^("Shell.Application"^)>"%TEMP%\elevate.vbs"
        echo UAC.ShellExecute "%~f0", "%TEMP%\elevate.vbs", "", "runas", 1 >>"%TEMP%\elevate.vbs"
        if exist "%TEMP%\elevate.vbs" start /b /wait >nul cscript /nologo "%TEMP%\elevate.vbs" 2>&1

        :: Delete elevation script if exist
        if exist "%TEMP%\elevate.vbs" >nul del /f "%TEMP%\elevate.vbs" 2>&1

        exit /b
    )    
)

pushd "%~dp0"

timeout 3
title Del-ia's Setup
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

choco install -y git
choco install -y python --version=3.6.7
choco install -y nodejs

git clone https://github.com/daniel8rc/hackathon_optimizacion_entregas_material.git
SET mypath=%~dp0
SET proyectPath=%mypath:~0,-1%/hackathon_optimizacion_entregas_material
cd %proyectPath%

install.bat

popd
