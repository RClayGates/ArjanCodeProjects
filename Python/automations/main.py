
# import: std
import os
import sys
import subprocess as sp
from time import perf_counter

# import: non-std

# import: local

# constants
TARGET_DIR = "../../Python"

# main
def main():
    create_mains()
    create_envs()
    pass

# code blocks

def get_proj_dirs():
    os.chdir(TARGET_DIR)
    proj_dirs = []
    for item in os.listdir():
        if os.path.isdir(item):
            proj_dirs.append(item)
    return proj_dirs

def create_mains():
    with open("template.py","r") as file_obj:
        content = file_obj.read()
    for dir in get_proj_dirs():
        curdir = os.path.join(os.getcwd(),dir)
        if not os.path.exists(main_file := os.path.join(curdir,"main.py")):
            with open(main_file,"w") as new_file:
                new_file.write(content)

def create_envs():
    for dir in get_proj_dirs():
        curdir = os.path.join(os.getcwd(),dir)
        if not os.path.exists(env_dir := os.path.join(curdir,".env")):
            sp.run([sys.executable,"-m","venv",env_dir])



if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    start = perf_counter()
    main()
    print(f"Program Time= {perf_counter() - start:.2f}")

# TODO: Write script that Generates the following per project folder
# TODONE:     main.py template
# TODO:     generates .env folder
