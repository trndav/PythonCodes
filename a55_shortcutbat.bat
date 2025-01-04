@echo off
set TARGET_PATH=D:\test\test.bat
set SHORTCUT_PATH=C:\Users\Public\Desktop\Test shortcut.lnk

:: Use Windows Script Host to create the shortcut
echo Set oWS = WScript.CreateObject("WScript.Shell") > create_shortcut.vbs
echo sLinkFile = "%SHORTCUT_PATH%" >> create_shortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> create_shortcut.vbs
echo oLink.TargetPath = "%TARGET_PATH%" >> create_shortcut.vbs
echo oLink.Save >> create_shortcut.vbs

:: Run the script
cscript //nologo create_shortcut.vbs

:: Clean up
del create_shortcut.vbs

echo Shortcut created successfully at %SHORTCUT_PATH%
pause
