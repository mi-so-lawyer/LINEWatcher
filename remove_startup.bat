@echo off
set LINK=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\LINEWatcher.lnk
if exist "%LINK%" (
    del "%LINK%"
    echo スタートアップから削除しました。
) else (
    echo スタートアップには登録されていません。
)
pause