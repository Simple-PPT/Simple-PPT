from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('D:\\Auto-make-PPT\\rc1_GUI.py', base=base, target_name = 'make-PPT-US.exe')
]

setup(name='Auto-make-PPT',
      version = '0.0.1-rc1',
      description = '',
      options = {'build_exe': build_options},
      executables = executables)
