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

        self.mainframe = CTkFrame(self, corner_radius=10, fg_color="#292e2e")
        self.mainframe.grid(column=0, row=0, sticky='nsew')

        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.mainframe.grid_columnconfigure(1, weight=1)

        self.initSigninPage()
        self.initRegisterPage()

        self.goSigninPage()

    def showFrame(self, frame):
        for f in [self.loginframe, self.regframe]:
            f.grid_remove()
        frame.grid(column=0,row=0, padx=(50), pady=(50), sticky='nsew')

    def initSigninPage(self):
        self.loginframe = CTkFrame(self, width=1560, height=760, corner_radius=10, fg_color="#404747")
        self.loginframe.grid(column=0, row=0, padx=20, pady=20)

        self.titlelogin = CTkLabel(self.loginframe,
                                   text="Tippa",
                                   text_color="White",
                                   font=("Copperplate Gothic Bold",60))
        self.titlelogin.grid(column=1, row=1, padx=400, pady=(10,10))

        self.userentry = CTkEntry(self.loginframe,
                               placeholder_text="Username",
                               width=240,
                               height=36,
                               border_width=2,
                               corner_radius=10)
        self.userentry.grid(column=1, row=2, padx=400, pady=(10,10))

        self.passwordentry = CTkEntry(self.loginframe,
                                  placeholder_text="Password",
                                  width=240,
                                  height=36,
                                  border_width=2,
                                  corner_radius=10)
        self.passwordentry.grid(column=1, row=3, padx=400, pady=(10, 50))

        self.passcheck = CTkCheckBox(self.loginframe, text="")
        self.passcheck.grid(column=1,row=3,padx=(360,0),pady=(10,50))

        self.loginbutton = CTkButton(self.loginframe, text='Login',)
        self.loginbutton.grid(column=1, row=4, pady=(10), padx=(200,0))

        self.regbutton = CTkButton(self.loginframe, text='Register', command=self.goRegisterPage)
        self.regbutton.grid(column=1, row=4, pady=(10), padx=(0,200))



    def initRegisterPage(self):
        self.regframe = CTkFrame(self, width=1560, height=760, corner_radius=10, fg_color="#404747")
        self.regframe.grid(column=0, row=0, padx=20, pady=20)

        self.titlereg = CTkLabel(self.regframe, text="Tippa",text_color="White", font=("Copperplate Gothic Bold",60))
        self.titlereg.grid(column=1, row=1, padx=400, pady=(10,200))

        self.backbutton = CTkButton(self.regframe, text='Back', command=self.goSigninPage)
        self.backbutton.grid(column=1, row=2)


    def goSigninPage(self):
        self.showFrame(self.loginframe)

    def goRegisterPage(self):
        self.showFrame(self.regframe)
        return


app = SignIn()
app.mainloop()

