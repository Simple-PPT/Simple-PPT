import time,rc1_system,requests,webbrowser,os

from sqlalchemy import column
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

rc1_system.system().make_excel()
main_window = Tk(className=" Auto make PPT's GUI")
frame = ttk.Frame(main_window,padding=10).grid()
version = ttk.Label(frame,text = "Version:0.0.1 -rc1").grid(row = 0,column = 0)
label = ttk.Label(frame,text = "Please input your write time(s):").grid(row = 1,column = 0)
def entry_get():
    try:
        entry.get()
        bar['maximum'] = entry.get()
    except:
        exce = showerror('Error','Don\'t input string!')
        print(f"Error: {exce}")

def bar_star():
    for i in range(int(entry.get())):
        bar['value'] = i + 1
        main_window.update()
        time.sleep(1)

def bar_1():
    while True:
        main_window.update()
        time.sleep(0.1)
def start_if():
    r = askyesno('Yes(Y)|No(N)','Have you finished writing the info.xlsx file?')
    if str(r) == 'True':
        showinfo('Done!','Your PPT is OK!')
        rc1_system.system().read_and_make()
    else:
        while True:
            showinfo('info','Please input write time frist. ')
            entry_get()
            bar_star()
            re = askyesno('Yes(Y)|No(N)','Have you finished writing the info.xlsx file?')
            if str(re) == 'True':
                showinfo('Done!','Your PPT is OK!')
                rc1_system.system().read_and_make()
            else:
                pass

def check_news():
    try:
        api_url = "https://api.github.com/repos/YangZhenxun/Auto-make-PPT"
        download_url = "https://github.com/YangZhenxun/Auto-make-PPT/archive/master.zip"
        def get_FileModifyTime(path):
            d = {}
            files= os.listdir(path)
            s = []
            for file in files:
                t = os.path.getmtime(path+file)
                d[file] = t
            return d

        def is_old(old_time, name):
            all_info = requests.get(api_url,timeout = 5).json()
            new_time = time.mktime(time.strptime(all_info["updated_at"], "%Y-%m-%dT%H:%M:%SZ"))
            if not old_time:
                old_time = all_info["updated_at"]
                showinfo('This version','This version is new!')
            print(new_time, old_time)
            if new_time > old_time:
                old_time = new_time
                return True
            else:
                return False
        def download_newfile(name):
            r = requests.get(download_url)
            name = name.replace('/', '_') + '.zip'
            name = 'Auto-make-PPT.zip'
            with open("./" + name,'wb') as f:
                f.write(r.content)

        files = get_FileModifyTime('./')
        for i in files:
            print(i, files[i])
            name = i.split('.')[0].replace('_', '/')
            old = is_old(files[i], name)
            if old:
                showinfo('new','Have new version!')
                rres = askyesno('Yes(Y)|No(N)','Do you want download new version?')
                if str(rres) == 'True':
                    download_newfile(name)
    except Exception as e:
        showerror('Error','\'github.com\' has no response')
        raise Exception(e)
entry = ttk.Entry(frame,width = 35)
entry.grid(row = 1,column = 1)

get = ttk.Button(frame,text = "OK",command = lambda:[entry_get(),bar_star(),start_if()]).grid(row = 2,column = 0)
check_new = ttk.Button(frame,text = "Check new",command = lambda:[bar_1,check_news()]).grid(row = 0,column = 1)
bar = ttk.Progressbar(frame,length = 150,mode = 'determinate')
bar.grid(row = 3,column = 0)
bar['value'] = 0
bar1 = ttk.Progressbar(frame,mode = 'indeterminate')
bar1.grid(row = 3,column = 1)


main_window.mainloop()

