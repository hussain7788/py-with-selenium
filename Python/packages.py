import os

pip_commands = ["django", "selenium", "pytest"]

for command in pip_commands:
    root = "pip install --no-cache-dir "
    # root = "pip uninstall "
    res = root + command
    print(res)
    os.system(res)
