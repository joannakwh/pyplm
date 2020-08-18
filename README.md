# Python Product List Manager

## Setting up and creating a test project with PyQt5

1. install latest pip and python

2. install pyqt5-tools globally

   ```
   pip install pyqt5-tools
   ```

3. create virtual environment in project folder to better manage dependencies

   ```
   python -m venv venv
   ```

4. activate virtual environment

   for cmd: 

   ```
   call venv/scripts/activate.bat
   ```

   **or**

   for powershell:

   ```
   . .\venv\Scripts\activate.ps1
   ```

5. install Qt for Python in virtual environment

   ```
   pip install pyqt5
   ```

6. make a test hello_world.py inside the root folder

7. run  hello_world.py inside virtual environment

   ```
   python hello_world.py
   ```

## Creating projects with PyQt5-tools

1. Make sure pyqt5-tools are installed

2. Make a template with Qt Designer and save as .ui file

3. Run command

   ```
   pyuic5 -x inputfilename.ui -o outputfilename.py
   ```

## Create executable with pyinstaller

1. install pyinstaller package

```bash
pip install pyinstaller
```

2. Run command

```
pyinstaller --onefile helloworld.py
```

```
pyinstaller --paths "C:\Program Files (x86)\Windows Kits\10\Redist\10.0.17763.0\ucrt\DLLs\x86" -F pyPLM.py
```

## Create executable with fbs

1. install fbs

```
pip install fbs
```

2. initialize new app

```
fbs startproject
fbs run
fbs freeze --debug
```



## Resources

https://build-system.fman.io/pyqt5-tutorial

https://doc.qt.io/qtforpython/quickstart.html

https://datatofish.com/executable-pyinstaller/