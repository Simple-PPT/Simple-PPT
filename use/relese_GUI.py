import sys
import time,requests
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from relese_system import *

alls = system().load_language()
system().make_excel()
main_window = Tk(className=" Auto make PPT's GUI")
main_window.geometry('600x300')
frame = ttk.Frame(main_window,padding=10).grid()
menubar = Menu(frame)
S_Menu = Menu(frame,tearoff = 0)
S_Menu.add_command(label = 'English',command = lambda:[system().write_en_US(),showinfo('restart','It has been set, please restart the software.')])
S_Menu.add_command(label = '中文（简体）',command = lambda:[system().write_zh_Hans_CN(),showinfo('重启','已经设置好了，请重启软件。')])
menubar.add_cascade(label = alls[0],menu = S_Menu)
version = ttk.Label(frame,text = alls[1] + ":v0.0.1").grid(row = 0,column = 0)
label = ttk.Label(frame,text = alls[2]).grid(row = 1,column = 0)
def entry_get():
    try:
        entry.get()
        bar['maximum'] = entry.get()
    except:
        exce = showerror(alls[5],alls[6])

def bar_star():
    for i in range(int(entry.get())):
        bar['value'] = i + 1
        main_window.update()
        time.sleep(1)

def start_if():
    r = askyesno(alls[7],alls[8])
    if str(r) == 'True':
        system().read_and_make()
        showinfo(alls[9],alls[10])
        sys.exit()
    else:
        while True:
            showinfo(alls[11],alls[2])
            entry_get()
            bar_star()
            re = askyesno(alls[7],alls[8])
            if str(re) == 'True':
                system().read_and_make()
                showinfo(alls[9],alls[10])
                sys.exit()
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
            alls_info = requests.get(api_url,timeout = 5).json()
            new_time = time.mktime(time.strptime(alls_info["updated_at"], "%Y-%m-%dT%H:%M:%SZ"))
            if not old_time:
                old_time = alls_info["updated_at"]
            if new_time > old_time:
                old_time = new_time
                return True
            else:
                return False
        def download_newfile(name):
            r = requests.get(download_url,timeout = 5)
            name = name.replace('/', '_') + '.zip'
            with open("./" + name,'wb') as f:
                f.write(r.content)

        files = get_FileModifyTime('./')
        for i in files:
            print(i, files[i])
            name = i.split('.')[0].replace('_', '/')
            old = is_old(files[i], name)
        if old:
            showinfo(alls[13],alls[14])
            rres = askyesno(alls[15],alls[16])
            if rres == True:
                download_newfile('Auto-make-PPT')
        else:
            showinfo(alls[3],alls[17])
    except:
        showerror(alls[5],alls[12])
entry = ttk.Entry(frame,width = 35)
entry.grid(row = 1,column = 1)

get = ttk.Button(frame,text = alls[3],command = lambda:[entry_get(),bar_star(),start_if()]).grid(row = 2,column = 0)
check_new = ttk.Button(frame,text = alls[4],command = check_news).grid(row = 0,column = 1)
bar = ttk.Progressbar(frame,length = 150,mode = 'determinate')
bar.grid(row = 3,column = 0)
bar['value'] = 0

main_window.config(menu = menubar)
main_window.mainloop()
