@echo off
cd ..

set /P PPYTHON_PATH=<PPYTHON_PATH
%PPYTHON_PATH% -m pirates.piratesbase.PiratesStart

pause
