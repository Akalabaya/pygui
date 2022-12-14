
# PYGUI(Now make GUI Applications with Python and HTML)

This is a small but highly ambitious project which works to create Fast,Secure Applications without much hastle.
This uses *Pywebview* to vizualize Html and links it with your code with P2P(Peer to Peer) conection using flask,for two way connection with Html and Python Script.
# BIG NEWS 14th December
Tommorow our re-engineered pygui is rolling out with more faster performance.
## Mechanism
*Set Property*
```
Code --> Server(Flask) --> Html
```
*Get Property*
```
Html --> Server(Flask) --> Code
```
## API Reference

#### Create Project

```
python build.py path/to/project projectname 
```
#### This go to the project dir and activate venv and install modules
```
"Scripts/activate"
pip install -r requirement.txt
```
#### Now go to the Resource dir and create a html file that will be the gui of your app.
``` 
#main.html
<html>
<script src="../aes.js"></script>
<script src="../package.js"></script>
<body>
My First App
</body>
</html>
```
#### Now go to the root dir and create a main.py file.
``` 
#main.py
from pygui import pygui,start_app
app = pygui()
def main():
  print("App Created")
#creating App
app.title = "App1"
app.gui = "Resources/main.html"
app.create_app()
start_app(app1=main)
```
Now run main.py in venv...

## To build
```
build.bat
```
and Standalone Exe will be created at dist/dist/main.exe
## Example
you can get exmple at example.zip
## Acknowledgements

 - [Pywebview](https://pywebview.flowrl.com/)







