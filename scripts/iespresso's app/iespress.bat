@echo off

for /F "delims=" %%A in ("%0") do set ARG0=%%~dpnxA
for /F "delims=" %%A in ("%ARG0%") do set THIS=%%~nxA
for /F "delims=" %%A in ("%ARG0%") do set WDIR=%%~dpA
set WDIR=%WDIR:~0,-1%

for /F "delims=" %%A in ('cscript "%WDIR%\iespress.vbs" 3') do set WDIR=%%~dpA
set WDIR=%WDIR:~0,-1%

echo .\excludes.txt>excludes.txt
echo .\iespress.bat>>excludes.txt
echo .\iespress.vbs>>excludes.txt
xcopy . "%WDIR%\" /E /I /-Y /EXCLUDE:excludes.txt
del /F /Q excludes.txt

cd "%WDIR%"
:: start %*

set /a num=(%Random% %%9)+1
color %num%
@echo:
@echo:
@echo:
@echo:
@echo:
@echo:
echo                                                                                                   
echo                                                  `...``      ``..``                                
echo                                               `+so+//+oo:` -os+//+oo:`                             
echo  `.......``                           `.     :y:       .+s:` `     `+y.    ``                      
echo  .:-.....----`                        -:`   .d.       `  -o+ `       +y   `--                      
echo  .:.       `.:-`                      -:`   :h        ` ``` `        .d                            
echo  .:.         `-:`      `.----..`      -:`   .d.      ``` `  `        +y    -.      `..----.`       
echo  .:.          `::    .--.`````.--.    -:`    /y-     `` `` ```     `/y.    ::    .---.````.--.     
echo  .:.           -:` `-:.         .:-   -:`     -so.  ``` ``   ``   -so`     ::   -:.`        .:-`   
echo  .:.           -:` .:-```````````-:.  -:`       :s+` .  ``    . -so.       ::  `:-           .:-   
echo  .:.          .:-  -:-.............`  -:`        `/s/.`  ``   -os-         ::  .:.           `:-   
echo  .:.        `-:-   `::`               -:`          `/y/`` ` `os:           ::  `-:`         `-:-   
echo  .:.    ``.-:-`     `-:.`     `.-`    -:`            `+y/ .+y:`            ::   `-:-`     `.:::-   
echo  .::------..`         `.-------.`     -:`              .oyy/`              :-     `.-------.``:-   
echo                            `                             ``                            `           
@echo:
@echo:      
@echo:
@echo:
@echo:
@echo:

timeout 5
post.bat
pause