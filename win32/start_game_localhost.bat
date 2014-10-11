@echo off
cd ..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

rem Get the user input:
set /P poUsername="Username: "

rem Export the environment variables:
set poPassword=password
set PO_PLAYCOOKIE=%ttiUsername%
set PO_GAMESERVER=127.0.0.1

echo ===============================
echo Starting Pirates Online...
echo ppython: %PPYTHON_PATH%
echo Username: %poUsername%
echo Gameserver: %PO_GAMESERVER%
echo ===============================

%PPYTHON_PATH% -m pirates.piratesbase.PiratesStart
pause
