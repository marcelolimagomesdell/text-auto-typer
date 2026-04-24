@echo off
echo Building Text Auto Typer executable...
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Build executable
echo.
echo Building executable with PyInstaller...
pyinstaller --onefile --windowed --name "TextAutoTyper" text_auto_typer.py

echo.
echo Build complete!
echo The executable is located in the dist folder: dist\TextAutoTyper.exe
pause
