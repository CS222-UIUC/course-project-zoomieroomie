import shutil
import sys
from pathlib import Path
import os
import time
import subprocess

response = input("Running this program will delete your current .git folder, if it exists. Are you sure you want to proceed? [Y/N] ")
if response != "Y":
    print("Ok, I won't do anything. Exiting...")
    exit()
print("Going ahead...")

if len(sys.argv) != 2:
    print("Usage: python3 git_from_sequence.py [path_to_sequence]")
    print("Exiting...")
    exit()

git_path = Path(".git/")
if git_path.exists() and git_path.is_dir():
    shutil.rmtree(".git/")

time.sleep(5)

subprocess.run(["git", "init"])

dummy_filename = "a.txt"
change_count = 1

input_file = sys.argv[1]
with open(input_file, 'rb') as f:
    for line in f:
        str_line = line.decode("UTF-8")
        if "commit" in str_line:
            # make changes so the commit will have an effect
            with open(dummy_filename, 'wb') as d:
                d.write(("a"*change_count).encode("UTF-8"))
                change_count += 1
            subprocess.run(["git", "add", "."])
        p = subprocess.run(str_line, shell=True)

time.sleep(1)

result = os.popen("python3 graph_from_git.py")
print("Done. Check our your graph here: ")
print(result.read())
