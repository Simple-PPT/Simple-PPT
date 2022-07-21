import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': [], 'excludes': []}

setup(  name = 'make-PPT-US-.pptx.py',
        version = 'v0.0.1-alpha',
        description = 'It can make a PPT for you',
        options = {'build_exe': build_exe_options},
        executables = [Executable('./make-PPT-US-.pptx.py')])
