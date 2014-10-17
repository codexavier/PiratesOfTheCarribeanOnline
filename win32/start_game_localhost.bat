@echo off
cd ..

rem Read the contents of the PYTHON_PATH file into %PYTHON_PATH%:
set /P PYTHON_PATH=<PYTHON_PATH

set /P LOGIN_COOKIE="Username: "
set GAME_SERVER=127.0.0.1

echo ==============================
echo Starting Pirates Online...
echo Python: %PYTHON_PATH%
echo Username: %LOGIN_COOKIE%
echo Gameserver: %GAME_SERVER%
echo ==============================

%PYTHON_PATH% -m pirates.piratesbase.PiratesStart
pause
