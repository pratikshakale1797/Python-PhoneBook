from tkinter import *
import datetime
from mypeople import MyPeople
from addpeople import AddPeople
from aboutus import About

date = datetime.datetime.now().date()
date = str(date)


class Application(object):
    def __init__(self, master):
        self.master = master

        # ------frames-----------
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#34baeb')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/phonebook.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text='My Phonebook App', font='arial 15 bold',
                             bg='white', fg='#ebb434')
        self.heading.place(x=230, y=50)

        self.date_lbl = Label(self.top, text="Today's date:" + date,
                              font='arial 12 bold', fg='#ebb434', bg='white')
        self.date_lbl.place(x=450, y='110')

        # buttons 1: view people
        self.viewButton = Button(self.bottom, text="  My People  ", fg='#42bcf5', bg='white', font='arial 12 bold',command=self.my_people)
        self.viewButton.place(x=250, y=70)

        # button 2:Add people
        self.addButton = Button(self.bottom, text=" Add People ", fg='#42bcf5', bg='white', font='arial 12 bold',command=self.addpeoplefunction)
        self.addButton.place(x=250, y=130)

        # button 3:About US
        self.aboutButton = Button(self.bottom, text="   About Us   ", fg='#42bcf5', bg='white', font='arial 12 bold',command=self.about_us)
        self.aboutButton.place(x=250, y=190)

    def my_people(self):
        people = MyPeople()

    def about_us(self):
        aboutpage=About()

    def addpeoplefunction(self):
        addpeoplewindow=AddPeople()



def main():
    root = Tk()
    app = Application(root)
    root.title("PhoneBook App")
    root.geometry("650x550+350+200")
    root.resizable(False, False)

    root.mainloop()


if __name__ == '__main__':
    main()
