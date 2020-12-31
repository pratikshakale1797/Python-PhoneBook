from tkinter import *


class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x550+550+200")
        self.title("About Us")
        self.resizable(False, False)

        self.top = Frame(self, width=550, height=550, bg='#ffa500')
        self.top.pack(fill=BOTH)

        self.text = Label(self.top, text='About Us :'
                                         '\n Phonebook will ask you for your name ,'
                                         '\n surname ,your address, phone number '
                                         '\n and your email address.'
                                         '\n'
                                         '\n Contact Us:www.phonebook.com',

                          font='arial 14 bold', bg='#ffa500', fg='white'
                          )
        self.text.place(x=75, y=90)
