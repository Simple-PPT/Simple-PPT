import time,b4_system
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

b4_system.system().make_excel()
main_window = Tk(className=" Auto make PPT's GUI")
frame = ttk.Frame(main_window,padding=10).grid()
label = ttk.Label(frame,text = "Please input your write time(s):").grid(row = 0,column = 0)
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

def start_if():
    r = askyesno('Yes(Y)|No(N)','Have you finished writing the info.xlsx file?')
    if str(r) == 'True':
        b4_system.system().read_and_make()
    else:
        while True:
            re = askyesno('Yes(Y)|No(N)','Have you finished writing the info.xlsx file?')
            if str(re) == 'True':
                b4_system.system().read_and_make()
                break
            else:
                pass
entry = ttk.Entry(frame,width = 35)
entry.grid(row = 0,column = 1)

get = ttk.Button(frame,text = "OK",command = lambda:[entry_get(),bar_star(),start_if()]).grid(row = 1,column = 0)

bar = ttk.Progressbar(frame)
bar.grid(row = 2,column = 0)
bar['value'] = 0

main_window.mainloop()
