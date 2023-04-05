"""pre_gen_project"""

import os
import sys

# Colors for differents messeges
ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

# Variables to work in this code
project_slug = "{{ cookiecutter.project_slug }}"

# Variables to show like parameters
project_name = "{{ cookiecutter.project_name }}"
module_name = "{{ cookiecutter.project_module_name }}"
author_name = "{{ cookiecutter.project_author_name }}"
project_email = "{{ cookiecutter.project_author_email }}"

parameters = {
    "project_name =>": project_name,
    "project_slug =>": project_slug,
    "module_name =>": module_name,
    "author_name =>": author_name,
    "project_email =>": project_email
}

# This code to dicard names
"""
if project_slug.startswith("x"):
    print(
        f"{ERROR_COLOR}ERROR: projec name => |{project_slug}|" +
        "is not a valid name for this template.{RESET_ALL}"
    )

    sys.exit(1)
"""

# check names of the project

print("\n")
for keys, values in parameters.items():
    print(keys, values, "\n")

check = input("Do you like these names for your project? y/n => ")

while check != "y" and check != "n":
    print("\n" + f"{ERROR_COLOR}select a right answer" + "\n")
    check = input("Do you like these name for your project? y/n => ")

if check == "n":
    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")
