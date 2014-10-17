@echo off
cd ..

rem Read the contents of the PYTHON_PATH file into %PYTHON_PATH%:
set /P PYTHON_PATH=<PYTHON_PATH

set /P PO_PLAYCOOKIE="Username: "
set PO_GAMESERVER=127.0.0.1

echo ==============================
echo Starting Pirates Online...
echo Python: %PYTHON_PATH%
echo Username: %PO_PLAYCOOKIE%
echo Gameserver: %PO_GAMESERVER%
echo ==============================

%PYTHON_PATH% -m pirates.piratesbase.PiratesStart
pause
