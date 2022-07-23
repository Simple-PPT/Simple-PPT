import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': [], 'excludes': []}

setup(  name = 'make-PPT-b3.py',
        version = '0.0.1b3',
        description = 'It can make a PPT for you',
        options = {'build_exe': build_exe_options},
        executables = [Executable('./b3.py')])
