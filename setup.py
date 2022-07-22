import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': [], 'excludes': []}

setup(  name = 'make-PPT-BETA.1.py',
        version = 'v0.0.1-beta.1',
        description = 'It can make a PPT for you',
        options = {'build_exe': build_exe_options},
        executables = [Executable('./.beta-1.py')])
