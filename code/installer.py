from tkinter.messagebox import *
import requests,tkinter
from tkinter import ttk
download_url = 'https://github.com/YangZhenxun/Auto-make-PPT/archive/master.zip'
def download_newfile(name):
    try:
        for i in range(1):
            r = requests.get(download_url,timeout = 5)
            name = name.replace('/', '_') + '.zip'
            with open("./" + name,'wb') as f:
                f.write(r.content)
            snowbar['value'] = i +1
            __mainwindow__.update()
        showinfo('Done!|完成！','Auto-make-PPT is ready.\nAuto-make-PPT准备好了。')
    except Exception as e:
        showerror('Error|错误','\'github.com\'has no response \n \'github.com\'没有响应')
        print(e)
__mainwindow__ = tkinter.Tk(className = ' Download')
__mainwindow__.geometry('400x200')
frame = ttk.Frame(__mainwindow__,padding = 10).pack()
label = ttk.Label(frame,text = '\n Now,Download Auto-make-PPT.zip \n 现在下载Auto-make-PPT.zip \n \n').pack()
snowbar = ttk.Progressbar(frame,maximum = 1)
snowbar.pack()
snowbar['value'] = 0
download_newfile('Auto-make-PPT')
download_again = ttk.Button(frame,text = 'Download',command = lambda : download_newfile('Auto-make-PPT')).pack()
__mainwindow__.mainloop()
