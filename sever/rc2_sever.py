import socket
from tkinter.messagebox import *

s = socket.socket()
host = '192.168.3.242'
port = 8080
s.bind((host, port))
s.listen()
conn,addr = s.accept()
while True:
    ret = conn.recv(2048)
    if ret == b'Timed out:':
        showerror('error','Github has a timeout!')
