import os
import sys
import subprocess

BUILD_DIR = "build"
EXEC = "simple_project"

def default():
    if not os.path.exists(BUILD_DIR):
        os.mkdir(BUILD_DIR)

    subprocess.run("cmake ..", cwd=BUILD_DIR, shell=True)
    subprocess.run("make", cwd=BUILD_DIR, shell=True)
    subprocess.run("./" + EXEC, cwd=BUILD_DIR, shell=True)

if len(sys.argv) == 1:
    default()
