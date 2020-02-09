import pygame
from src import controller
from src import tkinterlog

def login():
    logtk = tkinterlog.TkAPI()
    logtk.tkintloop()
    f_read = open("log.txt", "r")
    last_line = f_read.readlines()[-1]
    print(last_line)
    if "Owen" in last_line and "Ifferte" in last_line:
        main("EDDIE")
    elif "sysadmin" in last_line and "sudo" in last_line:
        main("TEST")


def main(state):
    window = controller.Controller()
    window.mainloop(state)

login()
#main("EDDIE")
