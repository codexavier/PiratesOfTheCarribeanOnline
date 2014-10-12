@echo off
cd ../..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

echo ===============================
echo Starting Pirates Online AI server...
echo ppython: %PPYTHON_PATH%
echo ===============================

:main
%PPYTHON_PATH% -m pirates.ai.ServiceStart
goto main
