# Create and run .bat file

import os
bat_name = "a64_bat.bat"
bat_content = '''@echo off
echo Hola there!
pause'''

with open(bat_name, "w") as file:
    file.write(bat_content)

os.system(bat_name)