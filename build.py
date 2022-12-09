import zipfile
import sys
import os

print("[*] Creating project...")
os.system("python -m venv \""+os.path.join(sys.argv[1],sys.argv[2])+"\"")

print("[*] Extracting Copying files...")
with zipfile.ZipFile(os.path.dirname(__file__)+"/"+"pygui.zip", 'r') as zip_ref:
    zip_ref.extractall(sys.argv[1]+"/"+sys.argv[2])

print("[*] Project created at",os.path.abspath(sys.argv[1]+"/"+sys.argv[2])+"...")
print("[*] Now you need to install required modules by runing \"Scripts/pip\" install -r requirements.txt")
