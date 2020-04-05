@echo off
findstr /m "home=C:\Python36" pyvenv.cfg 
if NOT %errorlevel%==0 (
    ren pyvenv.cfg pyvenv.old
    ren pyvenv36.cfg pyvenv.cfg
) else (
    echo No matches!
)