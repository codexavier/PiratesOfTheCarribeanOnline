@echo off
cd ..

rem Read the contents of the PPYTHON_PATH file into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

set /P PO_PLAYCOOKIE="Username: "
set PO_GAMESERVER=127.0.0.1

echo ==============================
echo Starting Pirates Online...
echo ppython: %PPYTHON_PATH%
echo Username: %PO_PLAYCOOKIE%
echo Gameserver: %PO_GAMESERVER%
echo ==============================

%PPYTHON_PATH% -m pirates.piratesbase.PiratesStart
pause
