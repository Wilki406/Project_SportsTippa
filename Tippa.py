# Programmer: Benjamin D Wilkinson
import os
from customtkinter import *
import customtkinter
from screeninfo import get_monitors
from argon2 import PasswordHasher

import Database


#### THERE IS A BUG WHEN U CHANGE PASSWORD. ANNOYING


data = Database.getData("userdata")
Database.startDB()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class SignIn(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.dropSIbutcol = "#016344"
        self.dropSIbuthovcol = "#013625"
        self.dropSIfgcolor = "#288265"

        self.title("Tippa")
        self.geometry("1140x570")
        self.resizable(width=False, height=False)
        self.current_page = None

        self.mainframe = CTkFrame(self, fg_color="#292e2e", corner_radius=0)
        self.mainframe.grid(column=0, row=0, sticky='nsew')

        self.usernames = []
        self.secretQuestions = ["Select Question","What is the name of your first pet?",
                                "What is the name of the street you grew up on?",
                                "What was the model of your first car?",
                                "What was your childhood nickname?",
                                "What is your mother’s maiden name?",
                                "What is your father’s middle name?",
                                "What is the title of your favorite book?",
                                "What is the name of your favorite childhood friend?",
                                "What city were you born in?",
                                "What is the name of the first school you attended?"]

        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.mainframe.grid_columnconfigure(1, weight=1)

        self.hiddenState = "*"

        self.initSigninPage()
        self.initRegisterPage()
        self.initSQPage()
        self.initForgotPage()
        self.initChangePassPage()

        self.goSigninPage()

    def showFrame(self, frame):
        for f in [self.loginframe, self.regframe, self.forframe, self.SQframe, self.redpassframe]:
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

        self.titlereg.grid(column=1, row=1, padx=400, pady=(30, 10))

        self.REGerrormessage = CTkLabel(self.regframe, text="", text_color="red")
        self.REGerrormessage.grid(column=1, row=2)

        self.nameentry = CTkEntry(self.regframe,
                                  placeholder_text="Fullname",
                                  width=240,
                                  height=36,
                                  border_width=2,
                                  corner_radius=10)

        self.nameentry.grid(column=1, row=3, padx=400, pady=(10, 10))

        self.reguserentry = CTkEntry(self.regframe,
                                  placeholder_text="Username",
                                  width=240,
                                  height=36,
                                  border_width=2,
                                  corner_radius=10)

        self.reguserentry.grid(column=1, row=4, padx=400, pady=(10, 10))

        self.regpasswordentry = CTkEntry(self.regframe, show="*",
                                      placeholder_text="Password",
                                      width=240,
                                      height=36,
                                      border_width=2,
                                      corner_radius=10, )

        self.regpasswordentry.grid(column=1, row=5, padx=400, pady=(10, 10))

        self.regpasswordentry2 = CTkEntry(self.regframe, show="*",
                                      placeholder_text="Repeat Password",
                                      width=240,
                                      height=36,
                                      border_width=2,
                                      corner_radius=10, )

        self.regpasswordentry2.grid(column=1, row=6, padx=400, pady=(10, 30))

        self.backbuttonreg = CTkButton(self.regframe, text='Back', command=self.goSigninPage, fg_color="#8a0000")
        self.backbuttonreg.grid(column=1, row=7, pady=(0, 55), padx=(0,160))

        self.buttonreg = CTkButton(self.regframe, text='Continue', command=self.NextRegister, fg_color="#009e99")
        self.buttonreg.grid(column=1, row=7, pady=(0, 55), padx=(160,0))

    def initSQPage(self):
        self.SQframe = CTkFrame(self, width=1560, height=760, corner_radius=10, fg_color="#404747",
                                 border_color="#09d8eb", bg_color="#292e2e", border_width=2)
        self.SQframe.grid(column=0, row=0, padx=20, pady=20)

        self.titleSQ = CTkLabel(self.SQframe,
                                 text="Tippa",
                                 text_color="White",
                                 font=("Copperplate Gothic Bold", 60))
        self.titleSQ.grid(column=1, row=1, padx=430, pady=(30, 5))

        self.SQerrormessage = CTkLabel(self.SQframe, text="error", text_color="red")
        self.SQerrormessage.grid(column=1, row=2)

        self.SQ1l = CTkLabel(self.SQframe,
                                text="Question 1: ",
                                text_color="White")

        self.SQ1l.grid(column=1, row=3, padx=400, pady=(5, 10))

        self.combo1 = CTkOptionMenu(self.SQframe, values=self.secretQuestions, width=370, command=self.changeSecretQuestion1
                                    , button_color=self.dropSIbutcol, fg_color=self.dropSIfgcolor, button_hover_color=self.dropSIbuthovcol)
        self.combo1.grid(column=1, row=4)

        self.entry1 = CTkEntry(self.SQframe, width=250, placeholder_text="Answer")
        self.entry1.grid(column=1, row=5, pady=(10, 0))

        self.SQ2l = CTkLabel(self.SQframe,
                             text="Question 2: ",
                             text_color="White")

        self.SQ2l.grid(column=1, row=6, padx=400, pady=(10, 10))

        self.combo2 = CTkOptionMenu(self.SQframe, values=self.secretQuestions, width=370, command=self.changeSecretQuestion2
                                    , button_color=self.dropSIbutcol, fg_color=self.dropSIfgcolor, button_hover_color=self.dropSIbuthovcol)
        self.combo2.grid(column=1, row=7, pady=(0, 10))

        self.entry2 = CTkEntry(self.SQframe, width=250, placeholder_text="Answer")
        self.entry2.grid(column=1, row=8,pady=(0, 30))

        self.backbuttonreg = CTkButton(self.SQframe, text='Back', command=self.goRegisterPage, fg_color="#8a0000")
        self.backbuttonreg.grid(column=1, row=9, pady=(0, 55), padx=(0, 160))

        self.buttonreg = CTkButton(self.SQframe, text='Register', command=self.AttemptRegister, fg_color="#009e99")
        self.buttonreg.grid(column=1, row=9, pady=(0, 55), padx=(160, 0))

    def changeSecretQuestion1(self, inputQuestion):
        newList = self.secretQuestions.copy()
        for i, question in enumerate(self.secretQuestions):
            if inputQuestion == question:
                newList.pop(i)
        self.combo2.configure(values=newList)

    def changeSecretQuestion2(self, inputQuestion):
        newList = self.secretQuestions.copy()
        for i, question in enumerate(self.secretQuestions):
            if inputQuestion == question:
                newList.pop(i)
        self.combo1.configure(values=newList)


    def initForgotPage(self):
        self.forframe = CTkFrame(self, width=1560, height=760, corner_radius=10, fg_color="#404747",
                                 border_color="#09d8eb", bg_color="#292e2e", border_width=2)
        self.forframe.grid(column=0, row=0, padx=20, pady=20)

        self.FtitleSQ = CTkLabel(self.forframe,
                                text="Tippa",
                                text_color="White",
                                font=("Copperplate Gothic Bold", 60))
        self.FtitleSQ.grid(column=1, row=1, padx=430, pady=(30, 5))

        self.FSQerrormessage = CTkLabel(self.forframe, text="error", text_color="red")
        self.FSQerrormessage.grid(column=1, row=2)

        self.FSQ1l = CTkLabel(self.forframe,
                             text="Question 1: ",
                             text_color="White")

        self.FSQ1l.grid(column=1, row=3, padx=400, pady=(5, 10))

        self.Fcombo1 = CTkOptionMenu(self.forframe, values=self.secretQuestions, width=370,
                                    command=self.changeSecretQuestion1, button_color=self.dropSIbutcol, fg_color=self.dropSIfgcolor, button_hover_color=self.dropSIbuthovcol)
        self.Fcombo1.grid(column=1, row=4)

        self.Fentry1 = CTkEntry(self.forframe, width=250, placeholder_text="Answer")
        self.Fentry1.grid(column=1, row=5, pady=(10, 0))

        self.FSQ2l = CTkLabel(self.forframe,
                             text="Question 2: ",
                             text_color="White")

        self.FSQ2l.grid(column=1, row=6, padx=400, pady=(10, 10))

        self.Fcombo2 = CTkOptionMenu(self.forframe, values=self.secretQuestions, width=370,
                                    command=self.changeSecretQuestion2, button_color=self.dropSIbutcol, fg_color=self.dropSIfgcolor, button_hover_color=self.dropSIbuthovcol)
        self.Fcombo2.grid(column=1, row=7, pady=(0, 10))

        self.Fentry2 = CTkEntry(self.forframe, width=250, placeholder_text="Answer")
        self.Fentry2.grid(column=1, row=8, pady=(0, 30))

        self.Fbackbuttonreg = CTkButton(self.forframe, text='Back', command=self.goSigninPage, fg_color="#8a0000")
        self.Fbackbuttonreg.grid(column=1, row=9, pady=(0, 55), padx=(0, 160))

        self.Fbuttonreg = CTkButton(self.forframe, text='Submit', command=self.goChangePassPage, fg_color="#009e99")
        self.Fbuttonreg.grid(column=1, row=9, pady=(0, 55), padx=(160, 0))

    def goForgotPage(self):
        if self.userentry.get() == "":
            self.SIerrormessage.configure(text="Please enter Username")
            return
        else:
            if self.userentry.get() in self.usernames:

                self.showFrame(self.forframe)
                self.userSignedIn = self.userentry.get()
                SQdata = Database.getData("usersecretquestions")
                for row in SQdata:
                    if row[0] == self.userSignedIn:
                        self.question1 = row[1]
                        self.question2 = row[3]

                        self.answer1 = row[2]
                        self.answer2 = row[4]
                        break

                self.Fcombo1.set(self.question1)
                self.Fcombo1.configure(state="disabled")
                self.Fcombo2.set(self.question2)
                self.Fcombo2.configure(state="disabled")

            else:
                self.SIerrormessage.configure(text="Enter enter Username")

    def initChangePassPage(self):
        self.redpassframe = CTkFrame(self, width=1560, height=760, corner_radius=10, fg_color="#404747",
                                 border_color="#09d8eb", bg_color="#292e2e", border_width=2)
        self.redpassframe.grid(column=0, row=0, padx=20, pady=20)

        self.titlereg = CTkLabel(self.redpassframe,
                                 text="Tippa",
                                 text_color="White",
                                 font=("Copperplate Gothic Bold", 60))

        self.titlereg.grid(column=1, row=1, padx=400, pady=(30, 10))

        self.REDerrormessage = CTkLabel(self.redpassframe, text="", text_color="red")
        self.REDerrormessage.grid(column=1, row=2)

        self.redpasswordentry = CTkEntry(self.redpassframe, show="*",
                                         placeholder_text="New Password",
                                         width=240,
                                         height=36,
                                         border_width=2,
                                         corner_radius=10, )

        self.redpasswordentry.grid(column=1, row=5, padx=400, pady=(10, 10))

        self.redpasswordentry2 = CTkEntry(self.redpassframe, show="*",
                                          placeholder_text="Repeat New Password",
                                          width=240,
                                          height=36,
                                          border_width=2,
                                          corner_radius=10, )

        self.redpasswordentry2.grid(column=1, row=6, padx=400, pady=(10, 30))

        self.redbackbuttonreg = CTkButton(self.redpassframe, text='Back', command=self.goSigninPage, fg_color="#8a0000")
        self.redbackbuttonreg.grid(column=1, row=7, pady=(0, 55), padx=(0, 160))

        self.redbuttonchange = CTkButton(self.redpassframe, text='Change Password',command=self.attemptRecoverAccount, fg_color="#009e99")
        self.redbuttonchange.grid(column=1, row=7, pady=(0, 55), padx=(160, 0))

    def attemptRecoverAccount(self):
        if self.redpasswordentry.get() == self.redpasswordentry2.get():

            if len(self.redpasswordentry.get()) <= 20:

                if len(self.redpasswordentry.get()) and len(self.redpasswordentry2.get()) >= 8:

                    ph = PasswordHasher()
                    hashedpass = ph.hash(self.redpasswordentry.get())
                    Database.changePassword(self.userentry.get(), hashedpass)
                    self.goSigninPage()

                else:
                    self.REDerrormessage.configure(text="Passwords must be atleast 8 characters")
            else:
                self.REDerrormessage.configure(text="Password must be less than 21 characters")
        else:
            self.REDerrormessage.configure(text="Passwords do not match")


    def goChangePassPage(self):
        if self.Fentry2 or self.Fentry1 != "":
            ph = PasswordHasher()
            if (ph.verify(self.answer1, self.Fentry1.get())) and (ph.verify(self.answer2, self.Fentry2.get())) == True:
                print("success go change password page")
                self.showFrame(self.redpassframe)
        else:
            print("enter shit")

    def goSigninPage(self):
        self.showFrame(self.loginframe)
        self.getUsernames()
        self.SIerrormessage.configure(text="")
        self.REGerrormessage.configure(text="")
        return

    def getUsernames(self):
        global data
        data = Database.getData("userdata")

        self.usernames.clear()
        print(data)
        # self.usernames = [username[0] for username in data]
        for row in data:
            self.usernames.append(row[0])
        print(self.usernames)

    def AttempSignin(self):
        ph = PasswordHasher()
        if self.passwordentry.get() == "" and self.userentry.get() == "":
            self.SIerrormessage.configure(text="Enter your details or register below")
        elif self.passwordentry.get() == "":
            self.SIerrormessage.configure(text="Please enter your Password")
        elif self.userentry.get() == "":
            self.SIerrormessage.configure(text="Please enter your Username")

        for i in data:
            hashedpassword = i[1]
            if i[0] == self.userentry.get() and ph.verify(hashedpassword, self.passwordentry.get()) == True:
                self.current_user_username = self.userentry.get()
                #Log in
                print(f"Yippee {self.userentry.get()}")
            else:
                print("bad data")

    def goRegisterPage(self):
        self.showFrame(self.regframe)
        return

    def clearRegBoxes(self):
        self.nameentry.delete(0, 'end')
        self.reguserentry.delete(0, 'end')
        self.regpasswordentry2.delete(0, 'end')
        self.regpasswordentry.delete(0, 'end')

    def checkSpace(fullname):
        count = 0
        for i in range(0, len(fullname)):
            if fullname[i] == " ":
                count += 1
        return count

    def AttemptRegister(self):

        ph = PasswordHasher()
        secque2 = self.combo2.get()
        secque1 = self.combo1.get()

        if self.entry2.get() and self.entry1.get() != "":
            secqueans2 = ph.hash(self.entry2.get())
            secqueans1 = ph.hash(self.entry1.get())

            if secque2 != secque1:
                hashedpass = ph.hash(self.password)

                Database.createUser(self.username, hashedpass, self.fname, self.lname)
                Database.createUserSQ(self.username, secque1, secqueans1, secque2, secqueans2)

                Database.commitDB()

                print("Registration successful")

                self.clearRegBoxes()
                self.REGerrormessage.configure(text="")
                self.goSigninPage()
                return

    def NextRegister(self):
        self.getUsernames()
        self.username = self.reguserentry.get().strip()
        self.password = self.regpasswordentry.get()
        self.password_confirm = self.regpasswordentry2.get()
        self.fullname = self.nameentry.get().strip()

        if not self.username or not self.password or not self.password_confirm or not self.fullname:
            self.REGerrormessage.configure(text="Enter your details")
            return

        if self.username in self.usernames:
            self.REGerrormessage.configure(text="That username already exists")
            return

        if self.password != self.password_confirm:
            self.REGerrormessage.configure(text="Passwords do not match")
            return

        name_parts = self.fullname.split()
        if len(name_parts) < 2:
            self.REGerrormessage.configure(text="Please enter both first and last name")
            return

        self.fname = name_parts[0]
        self.lname = " ".join(name_parts[1:])
        self.goSQPage()

    def goSQPage(self):
        self.showFrame(self.SQframe)
        return

app = SignIn()
app.mainloop()

Database.startDB()