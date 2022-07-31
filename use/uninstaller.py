import os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

from pip import main
a = '.py'
b = '.exe'
c = '.msi'
d = '.msix'
name = './installer'

def uninstall():
    
    bar['value'] = i + 1
    main_window.update()
        
language = ''
CL_window = Tk(className = 'Language')

def CL(*args):
    global language
    language = box.get()

def bu():
    global language
    if language == '中文（简体）':
        aa = askokcancel('确定','确定吗？')
        if aa == True:
            language = language
    elif language == 'English':
        aa = askokcancel('Sure','Are you sure?')
        if aa == True:
            language = language
    else:
        showerror('Error','No language specified. Please choose one.')

frame = ttk.Frame(CL_window,padding = 10).grid()
var = StringVar()
box = ttk.Combobox(frame,textvariable = var,values = ('English','中文（简体）'))
box.grid(row = 0,column = 0)
box.current(0)
but = ttk.Button(frame,text = "OK",command = lambda: [CL(),bu(),CL_window.destroy()]).grid(row = 1,column = 0)
CL_window.mainloop()
zh_Hans_CN_all = ['卸载.','\n现在在卸载%s中......\n','\'github.com\'没有响应','错误','重新下载','下载完成！正在退出......','完成！']
en_US_all = [' Uninstall','\nNow uninstall %s...\n','\'github.com\'has no response','Error','Download again','Download completed! Now is exiting......','Done!']
all = []
def spado():
    global all
    if language == '中文（简体）':
        all = zh_Hans_CN_all
    elif language == 'English':
        all = en_US_all
spado()
main_window = Tk(className = all[0])
frame = ttk.Frame(main_window,padding = 10).pack()
