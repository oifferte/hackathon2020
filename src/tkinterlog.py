import tkinter as tk
import pygame

class TkAPI():

    def __init__(self):

        pygame.init()

        self.root= tk.Tk()

        self.canvas1 = tk.Canvas(self.root, width = 400, height = 300)
        self.canvas1.pack()

        self.username = tk.Entry(self.root)
        self.canvas1.create_window(200, 130, window=self.username)

        self.password = tk.Entry(self.root)
        self.canvas1.create_window(200, 170, window=self.password)

        self.nametag = tk.Label(self.root, text="E.D.D.I.E.")
        self.canvas1.create_window(200, 100, window=self.nametag)

        self.credentials = []

        self.button1 = tk.Button(text='login', command=self.loginattempt)
        self.canvas1.create_window(200, 210, window=self.button1)

        self.attempts = 0

    def loginattempt(self):
        self.credentials = [self.username.get(), self.password.get()]
        print(self.credentials)
        self.create_log(self.credentials)
        if (self.credentials[0] == "Owen" and self.credentials[1] == "Ifferte") or (self.credentials[0] == "sysadmin" and self.credentials[1] == "sudo"):
            self.label1 = tk.Label(self.root, text="success")
            self.canvas1.create_window(200, 240, window=self.label1)
            pygame.mixer.music.load("startup.mp3")
            pygame.mixer.music.play()
            pygame.time.wait(2700)
            self.root.destroy()
        else:
            self.attempts+= 1
            print("failed login attempts: "+str(self.attempts))
            pygame.mixer.music.load("error.mp3")
            pygame.mixer.music.play()
        if self.attempts == 3:
            print("AHHHH")
            pygame.mixer.music.load("shutdown.mp3")
            pygame.mixer.music.play()
            pygame.time.wait(3400)
            self.root.destroy()

    def create_log(self,credentialslist):
        fref = open("log.txt","a")
        fref.write(str(credentialslist)+"\n")
        fref.close()

    def tkintloop(self):
        self.root.mainloop()
