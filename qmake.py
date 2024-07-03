import sys
import subprocess
import os

print("QMake starting to run")
os.makedirs(os.path.abspath("gen"), exist_ok=True)

# generate main_window.ui   
print("Setting up the uic")
uic = "pyside6-uic.exe"

print("Finding the input file")
in_file = os.path.abspath(r"forms\main_window.ui")

print("Generating the output file")
out_file = os.path.abspath(r"gen\ui_main_window.py")

subprocess.call([uic, "--from-imports", in_file, '-o', out_file], shell=True)

