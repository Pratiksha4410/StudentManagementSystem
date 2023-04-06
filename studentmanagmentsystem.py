import pymysql
def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobno = mobval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        adddate = time.strftime("%d/%m/%y")
        try:
            query = '''insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            data = id, name, mobno, address, email, gender, dob,adddate
            curser.execute(query, data)
            con.commit()
            res = messagebox.askyesnocancel('notification',
                                            f'Id:{id} Name:{name} Added succesfully!....And you wont to clear the form',
                                            parent=addmaster)
            if res == True:
                idval.set('')
                nameval.set('')
                mobval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('notification', 'Id Already exits Try Another Id', parent=addmaster)
        query = 'SELECT * FROM studentdata'
        curser.execute(query)
        data = curser.fetchall()
        showdataFream.delete(*showdataFream.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            showdataFream.insert('', END, values=vv)

    addmaster = Toplevel(master=dataEntryFram)
    addmaster.resizable(False, False)
    addmaster.grab_set()
    addmaster.geometry("470x470+150+150")
    addmaster.title("Student managment system")
    addmaster.config(bg='blue')
    # ---------------------------------Add student lables
    idlable = Label(addmaster, text='Enter Id:', bg='gold2', font=("times", 20, 'bold'), width=12, relief=GROOVE,
                    borderwidth=3, anchor='w')
    idlable.place(x=10, y=10)

    namelable = Label(addmaster, text='Enter Name:', bg='gold2', font=("times", 20, 'bold'), width=12, relief=GROOVE,
                      borderwidth=3, anchor='w')
    namelable.place(x=10, y=70)

    moblable = Label(addmaster, text='Enter Mobile:', bg='gold2', font=("times", 20, 'bold'), width=12, relief=GROOVE,
                     borderwidth=3, anchor='w')
    moblable.place(x=10, y=130)

    emaillable = Label(addmaster, text='Enter Email:', bg='gold2', font=("times", 20, 'bold'), width=12, relief=GROOVE,
                       borderwidth=3, anchor='w')
    emaillable.place(x=10, y=190)

    addresslable = Label(addmaster, text='Enter Address:', bg='gold2', font=("times", 20, 'bold'), width=12,
                         relief=GROOVE,
                         borderwidth=3, anchor='w')
    addresslable.place(x=10, y=250)

    genderlable = Label(addmaster, text='Enter Gender:', bg='gold2', font=("times", 20, 'bold'), width=12,
                        relief=GROOVE,
                        borderwidth=3, anchor='w')
    genderlable.place(x=10, y=310)

    doblable = Label(addmaster, text='Enter D.O.B:', bg='gold2', font=("times", 20, 'bold'), width=12, relief=GROOVE,
                     borderwidth=3, anchor='w')
    doblable.place(x=10, y=370)

    subButton = Button(addmaster, text='Submit', font=('roman', 15, 'bold'), width=20, activeforeground='white', bd=5,
                       bg='red', activebackground='blue', command=submitadd)
    subButton.place(x=140, y=420)
    # --------------------------------------------------------Add student Entry
    idval = StringVar()
    nameval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    mobval = StringVar()
    dobval = StringVar()
    genderval = StringVar()

    identry = Entry(addmaster, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addmaster, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobentry = Entry(addmaster, font=('roman', 15, 'bold'), bd=5, textvariable=mobval)
    mobentry.place(x=250, y=130)

    emailentry = Entry(addmaster, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addmaster, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addmaster, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addmaster, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)
    addmaster.mainloop()


def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobno = mobval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        adddate = time.strftime("%d:%m:%y")
        if (id != ''):
            query = 'select * from studentdata where id = %s'
            curser.execute(query, (id))
            data = curser.fetchall()
            showdataFream.delete(*showdataFream.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                showdataFream.insert('', END, values=vv)

        elif (name != ''):
            query = 'select * from studentdata where name = %s'
            curser.execute(query, (name))
            data = curser.fetchall()
            showdataFream.delete(*showdataFream.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                showdataFream.insert('', END, values=vv)

        elif (mobno != ''):
            query = 'select * from studentdata where mobno = %s'
            curser.execute(query, (mobno))
            data = curser.fetchall()
            showdataFream.delete(*showdataFream.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                showdataFream.insert('', END, values=vv)

        elif (email != ''):
            query = 'select * from studentdata where email = %s'
            curser.execute(query, (email))
            data = curser.fetchall()
            showdataFream.delete(*showdataFream.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                showdataFream.insert('', END, values=vv)

        elif (address != ''):
            query = 'select * from studentdata where address = %s'
            curser.execute(query, (address))
            data = curser.fetchall()
            showdataFream.delete(*showdataFream.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                showdataFream.insert('', END, values=vv)

        elif (gender != ''):
            query = 'select * from studentdata where gender = %s'
            curser.execute(query, (gender))
            data = curser.fetchall()
            showdataFream.delete(*showdataFream.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                showdataFream.insert('', END, values=vv)

        elif (dob != ''):
            query = 'select * from studentdata where dob = %s'
            curser.execute(query, (dob))
            data = curser.fetchall()
            showdataFream.delete(*showdataFream.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                showdataFream.insert('', END, values=vv)

        elif (adddate != ''):
            query = 'select * from studentdata where adddate = %s'
            curser.execute(query, (adddate))
            data = curser.fetchall()
            showdataFream.delete(*showdataFream.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                showdataFream.insert('', END, values=vv)

    searchmaster = Toplevel(master=dataEntryFram)
    searchmaster.resizable(False, False)
    searchmaster.grab_set()
    searchmaster.geometry("470x540+150+120")
    searchmaster.title("Student managment system")
    searchmaster.config(bg='firebrick1')
    # ---------------------------------Add student lables
    idlable = Label(searchmaster, text='Enter Id:', bg='gold2', font=("times", 20, 'bold'), width=12, relief=GROOVE,
                    borderwidth=3, anchor='w')
    idlable.place(x=10, y=10)

    namelable = Label(searchmaster, text='Enter Name:', bg='gold2', font=("times", 20, 'bold'), width=12,
                      relief=GROOVE,
                      borderwidth=3, anchor='w')
    namelable.place(x=10, y=70)

    moblable = Label(searchmaster, text='Enter Mobile:', bg='gold2', font=("times", 20, 'bold'), width=12,
                     relief=GROOVE,
                     borderwidth=3, anchor='w')
    moblable.place(x=10, y=130)

    emaillable = Label(searchmaster, text='Enter Email:', bg='gold2', font=("times", 20, 'bold'), width=12,
                       relief=GROOVE,
                       borderwidth=3, anchor='w')
    emaillable.place(x=10, y=190)

    addresslable = Label(searchmaster, text='Enter Address:', bg='gold2', font=("times", 20, 'bold'), width=12,
                         relief=GROOVE,
                         borderwidth=3, anchor='w')
    addresslable.place(x=10, y=250)

    genderlable = Label(searchmaster, text='Enter Gender:', bg='gold2', font=("times", 20, 'bold'), width=12,
                        relief=GROOVE,
                        borderwidth=3, anchor='w')
    genderlable.place(x=10, y=310)

    doblable = Label(searchmaster, text='Enter D.O.B:', bg='gold2', font=("times", 20, 'bold'), width=12,
                     relief=GROOVE,
                     borderwidth=3, anchor='w')
    doblable.place(x=10, y=370)

    datelable = Label(searchmaster, text='Enter Date:', bg='gold2', font=("times", 20, 'bold'), width=12,
                      relief=GROOVE,
                      borderwidth=3, anchor='w')
    datelable.place(x=10, y=430)

    subButton = Button(searchmaster, text='Submit', font=('roman', 15, 'bold'), width=20, activeforeground='white',
                       bd=5,
                       bg='red', activebackground='blue', command=search)
    subButton.place(x=140, y=480)
    # --------------------------------------------------------Search student Entry
    idval = StringVar()
    nameval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    mobval = StringVar()
    dobval = StringVar()
    genderval = StringVar()
    dateval = StringVar()
    identry = Entry(searchmaster, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchmaster, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobentry = Entry(searchmaster, font=('roman', 15, 'bold'), bd=5, textvariable=mobval)
    mobentry.place(x=250, y=130)

    emailentry = Entry(searchmaster, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchmaster, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchmaster, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchmaster, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchmaster, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)
    searchmaster.mainloop()


def deletestudent():
    cc = showdataFream.focus()
    content = showdataFream.item(cc)
    pp = content['values'][0]
    query = 'delete from studentdata where id = %s'
    curser.execute(query, (pp))
    con.commit()
    messagebox.showinfo('notification', f'Id:{pp} id deleted successfully')
    query = 'select * from studentdata'
    curser.execute(query)
    data = curser.fetchall()
    showdataFream.delete(*showdataFream.get_children())
    for i in data:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        showdataFream.insert('', END, values=vv)


def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobno = mobval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()
        query = 'update studentdata set name=%s,mobno=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id = %s'
        data = name, mobno, email, address, gender, dob, date, time, id
        curser.execute(query, (data))
        con.commit()
        messagebox.showinfo('notification', 'Data is modify successsfully!', parent=updatemaster)
        query = 'select * from studentdata'
        curser.execute(query)
        data = curser.fetchall()
        showdataFream.delete(*showdataFream.get_children())
        for i in data:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            showdataFream.insert('', END, values=vv)

    updatemaster = Toplevel(master=dataEntryFram)
    updatemaster.resizable(False, False)
    updatemaster.grab_set()
    updatemaster.geometry("470x610+150+60")
    updatemaster.title("Student managment system")
    updatemaster.config(bg='firebrick1')
    # ---------------------------------Add student lables
    idlable = Label(updatemaster, text='Update Id:', bg='gold2', font=("times", 20, 'bold'), width=12, relief=GROOVE,
                    borderwidth=3, anchor='w')
    idlable.place(x=10, y=10)

    namelable = Label(updatemaster, text='Enter Name:', bg='gold2', font=("times", 20, 'bold'), width=12,
                      relief=GROOVE,
                      borderwidth=3, anchor='w')
    namelable.place(x=10, y=70)

    moblable = Label(updatemaster, text='Update Mobile:', bg='gold2', font=("times", 20, 'bold'), width=12,
                     relief=GROOVE,
                     borderwidth=3, anchor='w')
    moblable.place(x=10, y=130)

    emaillable = Label(updatemaster, text='Update Email:', bg='gold2', font=("times", 20, 'bold'), width=12,
                       relief=GROOVE,
                       borderwidth=3, anchor='w')
    emaillable.place(x=10, y=190)

    addresslable = Label(updatemaster, text='Update Address:', bg='gold2', font=("times", 20, 'bold'), width=12,
                         relief=GROOVE,
                         borderwidth=3, anchor='w')
    addresslable.place(x=10, y=250)

    genderlable = Label(updatemaster, text='Update Gender:', bg='gold2', font=("times", 20, 'bold'), width=12,
                        relief=GROOVE,
                        borderwidth=3, anchor='w')
    genderlable.place(x=10, y=310)

    doblable = Label(updatemaster, text='Update D.O.B:', bg='gold2', font=("times", 20, 'bold'), width=12,
                     relief=GROOVE,
                     borderwidth=3, anchor='w')
    doblable.place(x=10, y=370)

    datelable = Label(updatemaster, text='Update Date:', bg='gold2', font=("times", 20, 'bold'), width=12,
                      relief=GROOVE,
                      borderwidth=3, anchor='w')
    datelable.place(x=10, y=430)

    timelable = Label(updatemaster, text='Update Time:', bg='gold2', font=("times", 20, 'bold'), width=12,
                      relief=GROOVE,
                      borderwidth=3, anchor='w')
    timelable.place(x=10, y=490)

    subButton = Button(updatemaster, text='Submit', font=('roman', 15, 'bold'), width=20, activeforeground='white',
                       bd=5,
                       bg='red', activebackground='blue', command=update)
    subButton.place(x=140, y=550)

    # --------------------------------------------------------Search student Entry
    idval = StringVar()
    nameval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    mobval = StringVar()
    dobval = StringVar()
    genderval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    identry = Entry(updatemaster, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updatemaster, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobentry = Entry(updatemaster, font=('roman', 15, 'bold'), bd=5, textvariable=mobval)
    mobentry.place(x=250, y=130)

    emailentry = Entry(updatemaster, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updatemaster, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updatemaster, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updatemaster, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updatemaster, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updatemaster, font=('roman', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)
    cc = showdataFream.focus()
    content = showdataFream.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
    updatemaster.mainloop()


def showstudent():
    query = 'select * from studentdata'
    curser.execute(query)
    data = curser.fetchall()
    showdataFream.delete(*showdataFream.get_children())
    for i in data:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        showdataFream.insert('', END, values=vv)


def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = showdataFream.get_children()
    id, name, mobno, email, address, gender, dob, adddate, addtime = [], [], [], [], [], [], [], [], []
    for i in gg:
        content = showdataFream.item(i)
        pp = content['values']
        id.append(pp[0]), name.append(pp[1]), mobno.append(pp[2]), email.append(pp[3]), address.append(
            pp[4]), gender.append(pp[5]),
        dob.append(pp[6]), adddate.append(pp[7]), addtime.append(pp[8])
        dd = ['id', 'name', 'mobno', 'email', 'address', 'gender', 'dob', 'daadate', 'addtime']
        df = pandas.DataFrame(list(zip(id, name, mobno, email, address, gender, dob, adddate, addtime)), columns=dd)
        paths = r'{}.csv'.format(ff)
        df.to_csv(paths, index=False)
        messagebox.showinfo('Notifications', f'Data is Saved: {paths}')
    print(ff)


def exitstudent():
    res = messagebox.askyesnocancel("Notification", 'Do You Want To Exit')
    if res == True:
        master.destroy()


##########################################################connecttion database
def connectdb():
    def submitdb():
        global con, curser
        host = hostval.get()
        user = userval.get()
        password = passval.get()
        try:
            con = pymysql.Connect(host=host, user=user, password=password)
            curser = con.cursor()
        except:
            messagebox.showerror("Notification", "Data is Incarete Plz Try Again ", parent=masterdb)
            return
        try:
            query = '''Create database studentmanagmentsystem'''
            curser.execute(query)
            query = '''use studentmanagmentsystem'''
            curser.execute(query)
            query = '''create table studentdata(id int primary key auto_increment,
            name varchar(255),
            mobno varchar(255),
            email varchar(255),
            address varchar(255),
            gender varchar(255),
            dob varchar(255),
            date varchar(255),
            time varchar(255))'''
            curser.execute(query)
            query = '''alter table studentdata auto_increment = 1011'''
            curser.execute(query)
            messagebox.showinfo('notification', "you are connected to database!", parent=masterdb)

        except:
            query = '''use studentmanagmentsystem'''
            curser.execute(query)
            messagebox.showinfo('notification', "you are connected to database!", parent=masterdb)

    masterdb = Toplevel()
    masterdb.geometry("470x250+700+230")
    masterdb.config(bg='blue')
    masterdb.grab_set()
    masterdb.resizable(False, False)
    # ---------------------------------------------connectdb lables
    lablehost = Label(masterdb, text='Enter Host:', bg='gold2', font=("times", 20, 'bold'), width=13, relief=GROOVE,
                      borderwidth=3, anchor='w')
    lablehost.place(x=10, y=10)

    lableuser = Label(masterdb, text='Enter User:', bg='gold2', width=13, font=("times", 20, 'bold'), relief=GROOVE,
                      borderwidth=3, anchor='w')
    lableuser.place(x=10, y=70)

    lablepassword = Label(masterdb, text='Enter Password:', bg='gold2', width=13, font=("times", 20, 'bold'),
                          relief=GROOVE,
                          borderwidth=3, anchor='w')
    lablepassword.place(x=10, y=130)
    # --------------------------------------------------connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passval = StringVar()
    entryhost = Entry(masterdb, font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
    entryhost.place(x=250, y=10)
    entryuser = Entry(masterdb, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    entryuser.place(x=250, y=70)
    entrypass = Entry(masterdb, font=('roman', 15, 'bold'), bd=5, textvariable=passval)
    entrypass.place(x=250, y=130)
    # -----------------------------------------------------connectdb Button
    subButton = Button(masterdb, text='Submit', font=('roman', 15, 'bold'), width=20,
                       activeforeground='white', bd=5, bg='red', activebackground='blue', command=submitdb)
    subButton.place(x=150, y=190)


def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d:%M:%Y")
    clock.config(text='Date:' + date_string + "\nTime:" + time_string)
    clock.after(200, tick)


###################################################################Intro-slider-color
import random

colors = ['red', 'yellow', 'blue', 'orange', 'Green', 'gold2', 'purple', 'pink', 'red2', 'black']

def slidercolor():
    fg = random.choice(colors)
    sliderlable.config(fg=fg)
    sliderlable.after(2, slidercolor)


def introTick():
    global count, text
    if (count >= len(ss)):
        count = -1
        text = ''
        sliderlable.config(text=text)
    else:
        text = text + ss[count]
        sliderlable.config(text=text)
    count += 1
    sliderlable.after(110, introTick)


################################################################################
from tkinter import *
import time
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql

master = Tk()
master.title("Student Managment System")
master.wm_iconbitmap('logo.ico')
master.config(bg="gold2")
master.geometry("1174x650+100+30")
master.resizable(False, False)
###############Frames#################################################################
dataEntryFram = Frame(master, bg='gold2', relief=GROOVE, borderwidth=5)
dataEntryFram.place(x=10, y=80, width=500, height=570)
###########################################################################show data fream
showframe = Frame(master, bg='gold2', relief=GROOVE, borderwidth=5)
showframe.place(x=550, y=80, width=600, height=570)

##--------------------------------------------------------------------------------show data main Freams
srcoll_x = Scrollbar(showframe, orient=HORIZONTAL)
srcoll_y = Scrollbar(showframe, orient=VERTICAL)
showdataFream = Treeview(showframe, columns=(
"Id", "Name", "MobNo", "Email", "Address", "Gender", 'D.O.B', 'Added Date', 'Added Time'),
                         yscrollcommand=srcoll_y.set, xscrollcommand=srcoll_x.set)
style = ttk.Style()
style.configure("Treeview.Heading", font=('chiller', 15, 'bold'), foreground='red')
style.configure("Treeview", font=('times', 14, 'bold'), foreground='black', background='blue')

srcoll_x.pack(side=BOTTOM, fill=X)
srcoll_y.pack(side=RIGHT, fill=Y)
srcoll_x.config(command=showdataFream.xview)
srcoll_y.config(command=showdataFream.yview)
showdataFream.heading('Id', text='Id')
showdataFream.heading('Name', text='Name')
showdataFream.heading('MobNo', text='MobNo')
showdataFream.heading('Email', text='Email')
showdataFream.heading('Address', text='Address')
showdataFream.heading('Gender', text='Gender')
showdataFream.heading('D.O.B', text='D.O.B')
showdataFream.heading('Added Date', text='Added Date')
showdataFream.heading('Added Time', text='Added Time')
showdataFream['show'] = 'headings'
showdataFream.column('Id', width=100)
showdataFream.column('Name', width=200)
showdataFream.column('MobNo', width=200)
showdataFream.column('Email', width=200)
showdataFream.column('Address', width=300)
showdataFream.column("Gender", width=150)
showdataFream.column('D.O.B', width=200)
showdataFream.column('Added Date', width=200)
showdataFream.column('Added Time', width=200)
showdataFream.pack(fill=BOTH, expand=1)
##############################################################dataentry frems
fontlable = Label(dataEntryFram, text='-----------------Welcome-----------------', bg='gold2',
                  font=('arial', 22, 'italic bold'), width=30)
fontlable.pack(side=TOP, expand=True)

addbutton = Button(dataEntryFram, text='1.Add Student', command=addstudent, font=('chiller', 18, 'bold'), width=23,
                   activeforeground="white", bd=6, bg='skyblue3', activebackground='blue')
addbutton.pack(side=TOP, expand=True)

searchbutton = Button(dataEntryFram, text='2.Search Student', command=searchstudent, font=('chiller', 18, 'bold'),
                      width=23, activeforeground="white", bd=6, bg='skyblue3', activebackground='blue')
searchbutton.pack(side=TOP, expand=True)

deletebutton = Button(dataEntryFram, text='3.Delete Student', command=deletestudent, font=('chiller', 18, 'bold'),
                      width=23, activeforeground="white", bd=6, bg='skyblue3', activebackground='blue')
deletebutton.pack(side=TOP, expand=True)

updatebutton = Button(dataEntryFram, text='4.Update Student', command=updatestudent, font=('chiller', 18, 'bold'),
                      width=23, activeforeground="white", bd=6, bg='skyblue3', activebackground='blue')
updatebutton.pack(side=TOP, expand=True)

showbutton = Button(dataEntryFram, text='5.Show All', command=showstudent, font=('chiller', 18, 'bold'), width=23,
                    activeforeground="white", bd=6, bg='skyblue3', activebackground='blue')
showbutton.pack(side=TOP, expand=True)

exportbutton = Button(dataEntryFram, text='6.Export Data', command=exportstudent, font=('chiller', 18, 'bold'),
                      width=23, activeforeground="white", bd=6, bg='skyblue3', activebackground='blue')
exportbutton.pack(side=TOP, expand=True)

exitbutton = Button(dataEntryFram, text='7.Exit', command=exitstudent, font=('chiller', 18, 'bold'), width=23,
                    activeforeground="white", bd=6, bg='skyblue3', activebackground='blue')
exitbutton.pack(side=TOP, expand=True)
###############Silder#################################################################################################################################3
ss = "Welcome to Student Management System"
count = 0
text = ''
sliderlable = Label(master, text=ss, bg="cyan", borderwidth=5, relief=RIDGE, font=("chiller", 22, 'italic bold'),
                    width=35)
sliderlable.place(x=250, y=0)
introTick()
slidercolor()
#############################Clock#############################################################
clock = Label(master, bg="lawn green", borderwidth=4, font=("times", 14, 'bold'), width=20, relief=RIDGE, bd=6)
clock.place(x=0, y=0)
tick()
################################################################################ConnectDatabase
connectButton = Button(master, text="Connect to Database", width=18, font=("chiller", 17, 'italic bold'), bd=6,
                       borderwidth=4, relief=RIDGE,
                       activeforeground='blue', command=connectdb, foreground='white', bg='green2')
connectButton.place(x=900, y=0)

master.mainloop()
