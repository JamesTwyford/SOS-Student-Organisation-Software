::Developed by Julien Di Lorenzo
@echo off

set /p UIFILE=UI File Path? 
set /p XPFILE=Export File Path/Name? 

pyuic5 -x %UIFILE% -o %XPFILE%

echo Task completed successfully
pause