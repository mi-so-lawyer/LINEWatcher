@echo off
set SCRIPT=%~dp0create_shortcut.vbs
set TARGET=%~dp0LINEWatcher.exe
set LINK=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\LINEWatcher.lnk

cscript //nologo "%SCRIPT%" "%TARGET%" "%LINK%"
echo スタートアップに登録しました。
pause