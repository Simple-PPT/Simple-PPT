from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import requests

language = ''
download_url = 'https://github.com/YangZhenxun/Auto-make-PPT/archive/master.zip'
sLuJing = ''
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

zh_Hans_CN_all = ['下载','\n现在在下载Auto-make-PPT.zip中......\n','\'github.com\'没有响应','错误','重新下载','下载完成！正在退出......','完成！','下一步','请输入下载到哪里：','选择下载路径']
en_US_all = [' Download','\nNow download Auto-make-PPT.zip...\n','\'github.com\'has no response','Error','Download again','Download completed! Now is exiting......','Done!','next','Please input download where:','Choose download where']
all = []
def spado():
    global all
    if language == '中文（简体）':
        all = zh_Hans_CN_all
    elif language == 'English':
        all = en_US_all

def bar_start(name:str = 'Auto-make-PPT'):
    try:
        for i in range(1):
            r = requests.get(download_url,timeout = 5)
            name = name.replace('/', '_') + '.zip'
            with open("./" + name,'wb') as f:
                f.write(r.content)
            bar['value'] = i + 1
            main_window.update()
        showinfo(all[6],all[5])
        main_window.destroy()
    except:
        showerror(all[3],all[2])
spado()
main_window = Tk(className = all[0])
frame1 = ttk.Frame(main_window,padding = 10).pack()
label = ttk.Label(frame1,text = all[1]).pack()
bar = ttk.Progressbar(frame1,maximum = 1)
bar.pack()
bar['value'] = 0
butt = ttk.Button(frame1,text = all[4],command = bar_start).pack()
bar_start()
main_window.mainloop()
