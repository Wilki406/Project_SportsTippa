# Programmer: Benjamin D Wilkinson
import os
from customtkinter import *
import customtkinter
from screeninfo import get_monitors
from argon2 import PasswordHasher

import Database

data = Database.getData()
Database.startDB()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class SignIn(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tippa")
        self.geometry("1140x570")
        self.resizable(width=False, height=False)
        self.current_page = None

        self.mainframe = CTkFrame(self, fg_color="#292e2e", corner_radius=0)
        self.mainframe.grid(column=0, row=0, sticky='nsew')

        self.usernames = []

        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.mainframe.grid_columnconfigure(1, weight=1)

        self.hiddenState = "*"

        self.initSigninPage()
        self.initRegisterPage()
        self.initForgotPage()

        self.goSigninPage()

    def showFrame(self, frame):
        for f in [self.loginframe, self.regframe, self.forframe]:
            f.grid_remove()
        frame.grid(column=0,row=0, padx=(50), pady=(50), sticky='nsew')

    def seePassword(self):
        self.hiddenState = self.passcheck.get()
        self.passwordentry.configure(show=self.hiddenState)

    def initSigninPage(self):
        self.loginframe = CTkFrame(self, width=1560, height=760, corner_radius=10, fg_color="#404747", border_color="#09d8eb", bg_color="#292e2e", border_width=2)
        self.loginframe.grid(column=0, row=0, padx=20, pady=20)

        self.titlelogin = CTkLabel(self.loginframe,
                                   text="Tippa",
                                   text_color="White",
                                   font=("Copperplate Gothic Bold",60))
        self.titlelogin.grid(column=1, row=1, padx=400, pady=(30,60))

        self.userentry = CTkEntry(self.loginframe,
                               placeholder_text="Username",
                               width=240,
                               height=36,
                               border_width=2,
                               corner_radius=10)
        self.userentry.grid(column=1, row=2, padx=400, pady=(10,10))

        self.passwordentry = CTkEntry(self.loginframe, show=self.hiddenState,
                                  placeholder_text="Password",
                                  width=240,
                                  height=36,
                                  border_width=2,
                                  corner_radius=10,)

        self.passwordentry.grid(column=1, row=3, padx=400, pady=(10, 30))

        self.passcheck = CTkCheckBox(self.loginframe, text="",command=self.seePassword,
                               onvalue="", offvalue="*")
        self.passcheck.grid(column=1,row=3,padx=(360,0),pady=(10,30))

        self.SIerrormessage = CTkLabel(self.loginframe, text="", text_color="red")
        self.SIerrormessage.grid(column=1, row=4)

        self.loginbutton = CTkButton(self.loginframe, text='Login', command=self.AttempSignin,
                                 width=300,
                                 fg_color="#32a852",
                                 border_width=0,
                                 corner_radius=8,)
        self.loginbutton.grid(column=1, row=5, pady=(10,30))

        self.forgotbutton = CTkButton(self.loginframe, text='Forgot Password?', command=self.goForgotPage, fg_color="#9e0000")
        self.forgotbutton.grid(column=1, row=6, pady=(10,100), padx=(0,160))

        self.regbutton = CTkButton(self.loginframe, text='Register', command=self.goRegisterPage, fg_color="#009e99")
        self.regbutton.grid(column=1, row=6, pady=(10,100), padx=(160,0))

    def initRegisterPage(self):
        self.regframe = CTkFrame(self, width=1560, height=760, corner_radius=10, fg_color="#404747",
                                   border_color="#09d8eb", bg_color="#292e2e", border_width=2)
        self.regframe.grid(column=0, row=0, padx=20, pady=20)

        self.titlereg = CTkLabel(self.regframe,
                                   text="Tippa",
                                   text_color="White",
                                   font=("Copperplate Gothic Bold", 60))

        self.titlereg.grid(column=1, row=1, padx=400, pady=(30, 60))

        self.nameentry = CTkEntry(self.regframe,
                                  placeholder_text="Fullname",
                                  width=240,
                                  height=36,
                                  border_width=2,
                                  corner_radius=10)

        self.nameentry.grid(column=1, row=2, padx=400, pady=(10, 10))

        self.reguserentry = CTkEntry(self.regframe,
                                  placeholder_text="Username",
                                  width=240,
                                  height=36,
                                  border_width=2,
                                  corner_radius=10)

        self.reguserentry.grid(column=1, row=3, padx=400, pady=(10, 10))

        self.regpasswordentry = CTkEntry(self.regframe, show="*",
                                      placeholder_text="Password",
                                      width=240,
                                      height=36,
                                      border_width=2,
                                      corner_radius=10, )

        self.regpasswordentry.grid(column=1, row=4, padx=400, pady=(10, 10))

        self.regpasswordentry2 = CTkEntry(self.regframe, show="*",
                                      placeholder_text="Repeat Password",
                                      width=240,
                                      height=36,
                                      border_width=2,
                                      corner_radius=10, )

        self.regpasswordentry2.grid(column=1, row=5, padx=400, pady=(10, 30))

        self.backbuttonreg = CTkButton(self.regframe, text='Back', command=self.goSigninPage, fg_color="#8a0000")
        self.backbuttonreg.grid(column=1, row=6, pady=(0, 40), padx=(0,160))

        self.buttonreg = CTkButton(self.regframe, text='Register', command=self.AttemptRegister, fg_color="#009e99")
        self.buttonreg.grid(column=1, row=6, pady=(0, 40), padx=(160,0))

    def initForgotPage(self):
        self.forframe = CTkFrame(self, width=1560, height=760, corner_radius=10, fg_color="#404747",
                                 border_color="#09d8eb", bg_color="#292e2e", border_width=2)
        self.forframe.grid(column=0, row=0, padx=20, pady=20)

        self.titlefor = CTkLabel(self.forframe,
                                 text="Tippa",
                                 text_color="White",
                                 font=("Copperplate Gothic Bold", 60))
        self.titlefor.grid(column=1, row=1, padx=400, pady=(30, 60))

        self.backbuttonfor = CTkButton(self.forframe, text='Back', command=self.goSigninPage)
        self.backbuttonfor.grid(column=1, row=2)

    def goSigninPage(self):
        self.showFrame(self.loginframe)
        self.getUsernames()
        self.SIerrormessage.configure(text="")
        return

    def getUsernames(self):
        global data
        data = Database.getData()

        self.usernames.clear()
        for i in data:
            self.usernames.append(i[0])
        print(self.usernames)

    def AttempSignin(self):
        if self.passwordentry.get() == "" and self.userentry.get() == "":
            self.SIerrormessage.configure(text="Enter your details or register below")
        elif self.passwordentry.get() == "":
            self.SIerrormessage.configure(text="Please enter your Password")
        elif self.userentry.get() == "":
            self.SIerrormessage.configure(text="Please enter your Username")

        for i in data:
            if i[0] == self.userentry.get() and i[1] == self.passwordentry.get():
                self.current_user_username = self.userentry.get()
                #Log in
                print("Yippee")
            else:
                print("bad data")

    def goRegisterPage(self):
        self.showFrame(self.regframe)
        return

    def checkSpace(fullname):
        count = 0
        for i in range(0, len(fullname)):
            if fullname[i] == " ":
                count += 1
        return count

    def AttemptRegister(self):
        self.getUsernames()
        username = self.reguserentry.get().strip()
        password = self.regpasswordentry.get()
        password_confirm = self.regpasswordentry2.get()
        fullname = self.nameentry.get().strip()

        if not username or not password or not password_confirm or not fullname:
            print("All fields must be filled")

        if username in self.usernames:
            print("Username already exists")

        if password != password_confirm:
            print("Passwords do not match")

        name_parts = fullname.split()
        if len(name_parts) < 2:
            print("Please enter both first and last name")

        fname = name_parts[0]
        lname = " ".join(name_parts[1:])

        Database.insertRow(username,password,fname,lname)
        Database.commitDB()
        print("Registration successful")

    def goForgotPage(self):
        if self.userentry.get() == "":
            self.SIerrormessage.configure(text="Please enter Username")
            return
        else:
            self.showFrame(self.forframe)
            return

app = SignIn()
app.mainloop()

Database.startDB()
