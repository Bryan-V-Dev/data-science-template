"""post_gen_project"""

import subprocess

# Colors for differents messeges
MESSAGE_COLOR = "\x1b[34m"
ERROR_COLOR = "\x1b[31m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", "initial commit"])
subprocess.call(["git", "branch", "-m", "main"])

print(f"{MESSAGE_COLOR}Initial commit done{RESET_ALL}")

# New Enviroment process

create_enviroment = input(
    "Do you want to create a new enviroment for this projec (y/n) => ")

while create_enviroment != "y" and create_enviroment != "n":
    print("\n" + "select a right answer" + "\n")
    create_enviroment = input(
        "Do you want to create a new enviroment for this projec (y/n) => ")

if create_enviroment == "n":
    print("Project created, remember to read the file install.md")

if create_enviroment == "y":
    subprocess.call(["conda env create --file environment.yml"], shell=True)
