#!/usr/bin/python3

# This file contains a script that will run the conversion tools on all files in this directory 
# replace them, and then diff the output. All the programmer needs to do is run this script

import os 
import sys
import fileinput
import subprocess

def update_script_locations(cconv_loc, include_loc, python_loc): 
    for line in fileinput.input("convert_all.sh", inplace=1):
        if "CCONV=" in line:
            line = "CCONV=" + cconv_loc
        elif "INCLUDES=" in line: 
            line = "INCUDES=" + include_loc
        sys.stdout.write(line) 
    for line in fileinput.input("replace.py", inplace=1):
        if "#!" in line: 
            line = "#!" + python_loc 
        sys.stdout.write(line)
    for line in fileinput.input("update_database.py", inplace=1):
        if "#!" in line: 
            line = "#!" + python_loc 
        sys.stdout.write(line)

# asking the user information about their path locations
print("Please provide the path to the cconv-standalone tool:") 
cconv_loc = input("[CCONV LOCATION] > ") + "\n"
print("Please provide the path to the checkedc include directory:")
include_loc = input("[INCLUDE LOCATION] > ") + "\n"
print("Please provide the path to checked c's clang:")
clang_loc = input("[CLANG LOCATION] > ") + "\n"
print("Please provide the path to python (which python3 in a new tab)")
python_loc = input("[PYTHON LOCATION] > ") + "\n"

print("##########\tupdating scripts with new locations...\t##########")

update_script_locations(cconv_loc, include_loc, python_loc)

print("##########\tupdating the database with your locations...\t##########")
os.system("python3 update_database.py") 

print("##########\trunning the conversion tool...\t##########")
os.system("sh convert_all.sh")

print("##########\treplacing the output\t##########")
os.system("python3 replace.py")



exit()
compiles = True
print("##########\tcompiling...\t##########")
out = subprocess.Popen(['make', 'CC={}'.format(clang_loc), '-i'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
stdout, stderr = out.communicate()
stdout = str(stdout) 
if "error:" in stdout: 
    compiles = False
if not compiles: 
    print("\nFailure to compile!\n")
os.system("rm *.o")  