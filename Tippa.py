import sqlite3
import csv
import os
from customtkinter import *
import customtkinter
from screeninfo import get_monitors

conn = sqlite3.connect('database.db')
cur = conn.cursor()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



class SignIn(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tippa")
        self.geometry("1600x800")
        self.resizable(width=False, height=False)
        self.current_page = None

        self.mainFrame = CTkFrame(self, corner_radius=10)
        self.mainFrame.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')

        self.initSigninPage()

    def initSigninPage(self):
        self.loginframe = CTkFrame(self, width=1560, height=760, corner_radius=10)
        self.loginframe.grid(column=0, row=0, padx=20, pady=20)

        self.titlelogin = CTkLabel(self.loginframe, text="Tippa")
        self.titlelogin.grid(column=1, row=1)









app = SignIn()
app.mainloop()

