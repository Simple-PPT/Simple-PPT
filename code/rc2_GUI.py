import time,requests,os,rc2_system,pickle
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

zh_Hans_CN_all = ['语言','版本','请先输入写info.xlsx文件的时间（秒）：','好了','检查更新','错误','不要输入文字！','时间到','你写好info.xlsx文件了吗？','完成！','您的PPT完成了！','提示','\'github.com\'没有响应','新的','有新的版本！','下载','你想下载新的版本吗？','你的版本是最新的！']
en_US_all = ['Language','Version','Please input write the info.xlsx file\'s time frist(s):','OK','Check new','Error','Don\'t input string!','Timed up','Have you finished writing the info.xlsx file?','Done!','Your PPT is OK!','info','\'github.com\' has no response','new','Have new version!','Download','Do you want download new version?','Your version is new!']
all = []

def write_en_US():
    with open('info_server.info','wb') as f:
        pickle.dump('en-US',f)
    showinfo('restart','It has been set, please restart the software.')

def write_zh_Hans_CN():
    with open('info_server.info','wb') as f:
        pickle.dump('zh-Hans-CN',f)
    showinfo('重启','已经设置好了，请重启软件。')

def load_language():
    global all
    if os.path.isfile('./info_server.info'):
        with open('./info_server.info','rb') as f:
            ah = pickle.load(f)
        if ah == 'en-US':
            all = en_US_all
        elif ah == 'zh-Hans-CN':
            all = zh_Hans_CN_all
        else:
            os.remove('./info_server.info')
    else:
        with open('./info_server.info','wb') as f:
            all = en_US_all
rc2_system.system().make_excel()
main_window = Tk(className=" Auto make PPT's GUI")
main_window.geometry('600x300')
load_language()
frame = ttk.Frame(main_window,padding=10).grid()
menubar = Menu(frame)
S_Menu = Menu(frame,tearoff = 0)
S_Menu.add_command(label = 'English',command = write_en_US)
S_Menu.add_command(label = '中文（简体）',command = write_zh_Hans_CN)
menubar.add_cascade(label = all[0],menu = S_Menu)
version = ttk.Label(frame,text = all[1] + ":0.0.1-rc2").grid(row = 0,column = 0)
label = ttk.Label(frame,text = all[2]).grid(row = 1,column = 0)
def entry_get():
    try:
        entry.get()
        bar['maximum'] = entry.get()
    except:
        exce = showerror(all[5],all[6])

def bar_star():
    for i in range(int(entry.get())):
        bar['value'] = i + 1
        main_window.update()
        time.sleep(1)

def start_if():
    r = askyesno(all[7],all[8])
    if str(r) == 'True':
        showinfo(all[9],all[10])
        rc2_system.system().read_and_make()
    else:
        while True:
            showinfo(all[11],all[2])
            entry_get()
            bar_star()
            re = askyesno(all[7],all[8])
            if str(re) == 'True':
                showinfo(all[9],all[10])
                rc2_system.system().read_and_make()
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
            showinfo(all[13],all[14])
            rres = askyesno(all[15],all[16])
            if rres == True:
                download_newfile('Auto-make-PPT')
        else:
            showinfo(all[3],all[17])
    except:
        showerror(all[5],all[12])
entry = ttk.Entry(frame,width = 35)
entry.grid(row = 1,column = 1)

get = ttk.Button(frame,text = all[3],command = lambda:[entry_get(),bar_star(),start_if()]).grid(row = 2,column = 0)
check_new = ttk.Button(frame,text = all[4],command = check_news).grid(row = 0,column = 1)
bar = ttk.Progressbar(frame,length = 150,mode = 'determinate')
bar.grid(row = 3,column = 0)
bar['value'] = 0

main_window.config(menu = menubar)
main_window.mainloop()
