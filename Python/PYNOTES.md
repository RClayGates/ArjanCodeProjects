# Notes

## Console Commands
- py --help
  - py --list #(list available python versions)
  - py -m {MOD} #(run module as a script)
- py -m venv {ENV_DIR}
  - path conventions like ./ or .\ for relative path managment apply
  - creates unique environment for isolation and management
  - followup with "py -m venv --upgrade-deps {ENV_DIR}" for convenience
  - enter environment by running:
    -  ./ENV_DIR/Scripts/activate (linux shell)
    -  ./ENV_DIR/Scripts/Activate.psy (PowerShell)
    -  .\ENV_DIR\Scripts\activate.bat (windows shell)
  - once in the virtual env, use pip to install python modules specific to your project
- pip
  - General "package manager" for python
  - pip freeze (outputs non standard library )
  - pip freeze > ./requirements.txt (helpful command while in virtual environment)

## TOP3 Python builtin commands
- help()
  - General python help utility
  - help('modules') #(printout of modules installed on system) 
- dir()
  - evaluates current namespace or namespace of chosen variable or object
- type()
  - evaluates type of variable or object, great for troubleshooting/debugging