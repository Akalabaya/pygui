@echo off
cd %1%
echo [*] Installing reuired modules...
"Scripts/pip" install -r requirements.txt
echo [*] Project Created at %1%
echo [*] Activating virtual environment...
"Scripts/activate.bat"
pause