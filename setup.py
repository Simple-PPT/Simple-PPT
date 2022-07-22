import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': [], 'excludes': []}

setup(  name = 'make-PPT-b2.py',
        version = '0.0.1b2',
        description = 'It can make a PPT for you',
        options = {'build_exe': build_exe_options},
        executables = [Executable('./b2.py')])
