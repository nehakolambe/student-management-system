from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter.tix as tix
from PIL import Image, ImageTk #pip install pillow
from time import strftime 
import datetime
from playsound import playsound #pip install playsound

root = tix.Tk()
root.title(" S.M.S. ")
root.geometry("1270x800-1+1")
root.resizable(False,False)
root.iconbitmap('icon.ico')
#root.config`ure(bg='LightCyan2')
load = Image.open("1.jpg")
load = load.resize((200,200),Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(root,image=render)
img.image=render
img.place(x=500,y=-280,relwidth=1,relheight=1)

def time(): 
    string = strftime('%H:%M:%S %p')
    date = datetime.datetime.now().date() 
    lbl.config(text = string) 
    lbl1.config(text = date)
    lbl.after(1000, time) 

  
lbl = Label(root, font = ('calibri', 20, 'bold'), foreground = 'black') 
lbl1 = Label(root, font = ('calibri', 20, 'bold'), foreground = 'black')

 
lbl.pack(anchor = 'nw') 
lbl1.pack(anchor = 'nw') 



def f1():
	root.withdraw()
	addst.deiconify()


def f2():
	addst.withdraw()
	root.deiconify()

def f3():
	root.withdraw()
	viewst.deiconify()

	import cx_Oracle

	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		stData.delete('1.0',END)
		sql = "select rno,name,marks from try"
		cursor.execute(sql)
		data = cursor.fetchall()
		con.commit()
		msg = ""
		for d in data:
			msg = msg + "rno: "+ str(d[0]) + " name: " + d[1]  + " marks: " + str(d[2]) +"\n" 
		stData.insert(INSERT, msg)
	except cx_Oracle.DatabaseError as e:
		print("Some issues",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()


def f4():
	viewst.withdraw()
	root.deiconify()

def f5():
		import cx_Oracle

		con = None
		cursor = None
		try:
			con = cx_Oracle.connect("system/abc123")
			rno = entRno.get()
			name = entName.get()
			marks = entMarks.get()
			cursor = con.cursor()
			if rno.isdigit() :
				rno = int(entRno.get())
				if name.isalpha():
					if len(name) > 1 :
						name = entName.get()
						if marks.isdigit() :
							if (int)(marks) <= 100:
								marks = int(entMarks.get())
								sql = "insert into try values ('%d','%s','%d')"
								args = (rno, name, marks)
								cursor.execute(sql % args)
								con.commit()
								msg = str(cursor.rowcount) + " records inserted "
								messagebox.showinfo("Success", msg);playsound('clap.mp3')
								entRno.delete(0, END)
								entName.delete(0,END)
								entMarks.delete(0,END)
								entRno.focus()
							else:
								msg = "Range of marks is 0-100"
								messagebox.showerror("Failure",msg)
								playsound('oh-shit.mp3')
								entMarks.delete(0,END)
								entMarks.focus()
						else:
							msg = "Marks should be in digits"
							messagebox.showerror("Failure",msg)
							playsound('oh-shit.mp3')
							entMarks.delete(0,END)
							entMarks.focus()
					else:
						msg = "Name should be max of 2 letters"
						messagebox.showerror("Failure",msg)
						playsound('oh-shit.mp3')
						entName.delete(0,END)
						entName.focus()
				else:
						msg = "Name should be in letters"
						messagebox.showerror("Failure",msg)
						playsound('oh-shit.mp3')
						entName.delete(0,END)
						entName.focus()
			else:
				msg = "Enter Roll no correctly"
				messagebox.showerror("Failure",msg)
				playsound('oh-shit.mp3')
				entRno.delete(0,END)
				entRno.focus()

		except cx_Oracle.DatabaseError as e:
			print("Some issues")
			messagebox.showerror("Failure", e)
			playsound('oh-shit.mp3')
			con.rollback()
		finally:
			if cursor is not None:
				cursor.close()
			if con is not None:
				con.close()

def f6():
		import cx_Oracle
		con = None
		cursor = None
		try:
			con = cx_Oracle.connect("system/abc123")
			r = entRnod.get()
			rno = r
			if rno.isdigit():
				r = int(entRnod.get())
				rno = int(r)
				cursor = con.cursor()
				sql = "delete from try where rno = '%d'"
				args = (rno)
				cursor.execute(sql % args)
				con.commit()
				if cursor.rowcount!=0:
					msg = str(cursor.rowcount) + " Record deleted "
				else:
					msg = "Record doesn't exists"
				messagebox.showinfo("Success", msg)
				playsound('clap.mp3')
				entRnod.delete(0, END)
				entRnod.focus()
			else:
				msg = "Enter Roll no correctly"
				messagebox.showerror("Failure",msg)
				playsound('oh-shit.mp3')
				entRnod.delete(0, END)
				entRnod.focus()
		except cx_Oracle.DatabaseError as e:
			print("some issue ",e)
			messagebox.showerror("Failure", e)
			playsound('oh-shit.mp3')
		finally:
			if cursor is not None:
				cursor.close()
			if con is not None:
				con.close()


def f7():
	deletest.withdraw()
	root.deiconify()

def f8():
	root.withdraw()
	deletest.deiconify()

def f9():
	import requests
	import bs4

	res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
	soup = bs4.BeautifulSoup(res.text , 'lxml')
	quote = soup.find('img' , {"class": "p-qotd"})

	text = quote['alt']
	return text

def f10():
	import socket
	import requests
	try:
		city = 'mumbai'
		socket.create_connection(("www.google.com",80))
		a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2 = "&q=" + city
		a3 = "&appid=c6e315d09197cec231495138183954bd"
		api_address = a1 + a2 + a3
		res1=requests.get(api_address)
		data = res1.json()
		main = data['main']
		temp = main['temp']
		return temp
	except OSError:
		print("check network")

def f11():
	
	import cx_Oracle
	con = None
	cursor = None
	import matplotlib.pyplot as plt
	import pandas as pd
	import numpy as np

	con = cx_Oracle.connect("system/abc123")
	cur = con.cursor()
	x = cur.execute("select name,marks from try")
	plt.title('Student Records',color='b')
	plt.xlabel('Name',color='g')
	plt.ylabel('Marks',color='g')
	plt.ylim(0,100)

	rows = cur.fetchall()
	df = pd.DataFrame([[xy for xy in x] for x in rows])

	x=df[0]
	y=df[1]
	plt.bar(x,y,color = ['r','g','b','orange','y'],alpha=0.6)
	plt.grid()

	plt.show()
	
	cur.close()
	con.close()


def f12():
	updatest.withdraw()
	root.deiconify()

def f13():
	root.withdraw()
	updatest.deiconify()

def f14():
	root.withdraw()
	updatest.deiconify()
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		r = entRnou.get()
		rno1 = r
		name1 = entNameu.get()
		m = entMarksu.get()
		marks1 = m
		cursor = con.cursor()
		if rno1.isdigit() :
			r = int(entRnou.get())
			rno1 = int(r)
			if name1.isalpha():
				if len(name1) > 1 :
					name1 = entNameu.get()
					if marks1.isdigit() :
						if (int)(marks1) <= 100:
							m = int(entMarksu.get())
							marks1 = int(m)
							sql = "update try set name = '%s', marks = '%d' where rno = '%d' "
							args = (name1,marks1,rno1)
							cursor.execute(sql % args)
							con.commit()
							if cursor.rowcount!=0:
								msg = str(cursor.rowcount) + " Record Updated "
							else:
								msg = "Record doesn't exists"
							messagebox.showinfo("Success", msg)
							playsound('clap.mp3')
							# import pyglet
							# animation = pyglet.image.load_animation('2.gif')
							# animSprite = pyglet.sprite.Sprite(animation)
							# w = animSprite.width
							# h = animSprite.height
							# window = pyglet.window.Window(width = w, height = h)
							# r,g,b,alpha = 0.5, 0.5, 0.8, 0.5
							# pyglet.gl.glClearColor(r,g,b,alpha)
							# @window.event
							# def on_draw():
							# 	window.clear()
							# 	animSprite.draw()
							# pyglet.app.run()
							entRnou.delete(0, END)
							entNameu.delete(0,END)
							entMarksu.delete(0,END)
							entRnou.focus()
						else:
							msg = "Range of marks is 0-100"
							messagebox.showerror("Failure",msg)
							playsound('oh-shit.mp3')
							entMarksu.delete(0,END)
							entMarksu.focus()
					else:
						msg = "Marks should be in digits"
						messagebox.showerror("Failure",msg)
						playsound('oh-shit.mp3')
						entMarksu.delete(0,END)
						entMarksu.focus()
				else:
					msg = "Name should be of max 2 letters"
					messagebox.showerror("Failure",msg)
					playsound('oh-shit.mp3')
					entNameu.delete(0,END)
					entNameu.focus()
			else:
				msg = "Name should be in alphabets"
				messagebox.showerror("Failure",msg)
				playsound('oh-shit.mp3')
				entNameu.delete(0,END)
				entNameu.focus()
		else:
			msg = "Roll no should be positive"
			messagebox.showerror("Failure",msg)
			playsound('oh-shit.mp3')
			entRnou.delete(0, END)
			entRnou.focus()


	except cx_Oracle.DatabaseError as e:
		print("some issue ",e)
		messagebox.showerror("Failure", e)
		playsound('oh-shit.mp3')
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def f15():
	import socket
	import requests

	try:
		socket.create_connection( ("www.google.com",80) )
		res = requests.get("https://ipinfo.io/")
		data = res.json()
		city = data['city']
		return city
	except OSError as e:
		print("check network ",e)

def f16():
	import re
	regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
	
	name = entNamee.get()
	if len(name) == 0:
		messagebox.showerror("Incomplete","name is empty")
		entNamee.focus()
		return
	marks = entMarkse.get()
	if marks.isdigit() :
		if (int)(marks) <= 100:
			pass
	else:
		messagebox.showerror("Incomplete","marks is empty")
		entMarkse.focus()
		return
	email = entMaile.get()
	if len(email) == 0:
		messagebox.showerror("Incomplete","Parent Email is empty")
		entMaile.focus()
		return 

	try:
	    if(re.search(regex,email)):
	    	pass 
        	#print("Valid Email")  
	except EmailNotValidError as e:
		messagebox.showinfo("Error",str(e))
		return

	email1 = entMail1e.get() 
	if len(email1) == 0:
		messagebox.showerror("Incomplete","Sender Email is empty")
		entMail1e.focus()
		return 
	
	try:
	    if(re.search(regex,email1)):
	    	pass 
        	#print("Valid Email")  
	except EmailNotValidError as e:
		messagebox.showinfo("Error",str(e))
		return

	# import cx_Oracle
	# con = None
	# cursor = None
	# try:
	# 	con = cx_Oracle.connect("system/abc123")
	# 	sql = "select marks from try where name = '%s'"
	# 	args = (name)
	# 	cursor.execute(sql % args)
	# 	data = cursor.fetchall()
	# 	con.commit()
	# 	for d in data:
	# 		marksd = data[1]
      	
	# except cx_Oracle.DatabaseError as e:
	# 	print("Some issues",e)
	# finally:
	# 	if cursor is not None:
	# 		cursor.close()
	# 	if con is not None:
	# 		con.close()

      	



	fb = ""
	res = f.get()
    
	if res == 1:
		fb = "Excellent"
	elif res == 2:
		fb = "Good"
	else:
		fb = "Can Do Better"
	


	msg = "Name = " + name + "\nFeedback " + fb +"\nMarks " + marks
	messagebox.showinfo("Feedback",msg)

	to = email
	subject = "Feedback of " + name
	text = msg
	import smtplib
	sender = email1
	password = entPasse.get()
	message = 'Subject: {}\n\n{}'.format(subject,text)
	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.ehlo()
	server.login(sender,password)
	print('logged in')
	try:
		server.sendmail(sender, to, message)
		print('email sent')
	except:
		print('error sending email')
	server.quit

def f17():
	emailst.withdraw()
	root.deiconify()	

def f18():
	root.withdraw()
	emailst.deiconify()		


lbltitle = Label(root,text= "Student Records", font=("BankGothic Lt BT", "30" , "bold"),fg="crimson").place(x=420,y=10)		
btnAdd = tix.Button(root, text="Add",font= ("arial", 18, "bold"), width=10,command = f1, bg='SpringGreen2', activebackground='red')
btnView = tix.Button(root, text="View",font= ("arial", 18, "bold"), width=10, command = f3, bg='SpringGreen2', activebackground='red')
btnUpdate = tix.Button(root, text="Update",font= ("arial", 18, "bold"), width=10,command = f13 , bg='SpringGreen2', activebackground='red')
lblTemp = Label(root, text="Temperature :",font= ("Gadugi", 18, "bold")).place(x=700,y=540)
t = f10()
lblTemp1 = Label(root, text=str(t) + "\u00B0C", font=('Segoe Script', 15, 'bold'),fg='dark slate blue').place(x=900,y=540)
lblQotd = Label(root, text="Quote for the day:",font= ("Gadugi", 18, "bold")).place(x=40,y=580)
q = f9()
lblQotd1 = Label(root, text=q , font=('Segoe Script', 15, 'bold' ),fg='dark slate blue',wraplength=1000).place(x=250,y=580)
btnDelete = tix.Button(root, text="Delete",font= ("arial", 18, "bold"), width=10 , command= f8, bg='SpringGreen2', activebackground='red')
btnGraph = tix.Button(root, text="Graph",font= ("arial", 18, "bold"), width=10,command = f11 , bg='SpringGreen2', activebackground='red')
btnEmail = tix.Button(root, text="Email",font= ("arial", 18, "bold"), width=10, bg='SpringGreen2', activebackground='red',command = f18)
time() 	
lblCity = Label(root, text="City :",font= ("Gadugi", 18, "bold")).place(x=40,y=540)
c = f15()
lblCity1 = Label(root, text=c , font=('Segoe Script', 15, 'bold' ),fg='dark slate blue',wraplength=1000).place(x=150,y=540)

balloon = tix.Balloon(root)
# bind balloon to buttons
balloon.bind_widget(btnAdd, balloonmsg='Click to Add Records' 	)
balloon.bind_widget(btnView, balloonmsg='Click to View Records')
balloon.bind_widget(btnUpdate, balloonmsg='Click to Update Records')
balloon.bind_widget(btnDelete, balloonmsg='Click to Delete Records')
balloon.bind_widget(btnGraph, balloonmsg='Click to see Graph')
balloon.bind_widget(btnEmail, balloonmsg='Click to send Email')

#lbltitle.pack(pady=10)
btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)
btnEmail.pack(pady=10)



addst = Toplevel(root)
addst.title("Add S")
addst.geometry("1270x800-1+1")
addst.resizable(False,False)
addst.configure(bg='LightCyan2')
addst.iconbitmap('icon.ico')
addst.withdraw()
lblRno = Label(addst, text="Enter rno ",font= ("arial", 18, "bold"))
entRno = Entry(addst, bd=5,font= ("arial", 18, "bold"))
lblName = Label(addst, text="Enter name ",font= ("arial", 18, "bold"))
entName = Entry(addst, bd=5,font= ("arial", 18, "bold"))
lblMarks = Label(addst, text="Enter marks ",font= ("arial", 18, "bold"))
entMarks = Entry(addst, bd=5,font= ("arial", 18, "bold"))
#btnAddPhoto = Button(addst, text="Photo",font= ("arial", 18, "bold"), width=10,command =f15, bg='SpringGreen2', activebackground='red')
btnAddSave = Button(addst, text="Save",font= ("arial", 18, "bold"), width=10, command = f5, bg='SpringGreen2', activebackground='red')
btnAddBack = Button(addst, text="Back",font= ("arial", 18, "bold"), width=10, command = f2, bg='SpringGreen2', activebackground='red')

lblRno.pack(pady=5)
entRno.pack(pady=5)
lblName.pack(pady=5)
entName.pack(pady=5)
lblMarks.pack(pady=5)
entMarks.pack(pady=5)
#btnAddPhoto.pack(pady=5)
btnAddSave.pack(pady=5)
btnAddBack.pack(pady=5)



viewst = Toplevel(root)
viewst.title("View S")
viewst.geometry("1270x800-1+1")
viewst.resizable(False,False)
viewst.configure(bg='LightCyan2')
viewst.iconbitmap('icon.ico')
viewst.withdraw()

stData = scrolledtext.ScrolledText(viewst, width = 40, height = 30)
btnViewBack = Button(viewst, text="Back",font=("arial",18,"bold"),command = f4, bg='SpringGreen2', activebackground='red')

stData.pack()
btnViewBack.pack()


updatest = Toplevel(root)
updatest.title("Update S")
updatest.geometry("1270x800-1+1")
updatest.resizable(False,False)
updatest.configure(bg='LightCyan2')
updatest.iconbitmap('icon.ico')
updatest.withdraw()
lblRnou = Label(updatest, text="Enter rno ",font= ("arial", 18, "bold"))
entRnou = Entry(updatest, bd=5,font= ("arial", 18, "bold"))
lblNameu = Label(updatest, text="Enter name ",font= ("arial", 18, "bold"))
entNameu = Entry(updatest, bd=5,font= ("arial", 18, "bold"))
lblMarksu = Label(updatest, text="Enter marks ",font= ("arial", 18, "bold"))
entMarksu = Entry(updatest, bd=5,font= ("arial", 18, "bold"))
btnAddSave = Button(updatest, text="Save",font= ("arial", 18, "bold"), width=10, command = f14, bg='SpringGreen2', activebackground='red')
btnAddBack = Button(updatest, text="Back",font= ("arial", 18, "bold"), width=10, command = f12, bg='SpringGreen2', activebackground='red')

lblRnou.pack(pady=5)
entRnou.pack(pady=5)
lblNameu.pack(pady=5)
entNameu.pack(pady=5)
lblMarksu.pack(pady=5)
entMarksu.pack(pady=5)
btnAddSave.pack(pady=5)
btnAddBack.pack(pady=5)

deletest = Toplevel(root)
deletest.title("Delete S")
deletest.geometry("1270x800-1+1")
deletest.configure(bg='LightCyan2')
deletest.resizable(False,False)
deletest.iconbitmap('icon.ico')
deletest.withdraw()
lblRnod = Label(deletest, text="Enter rno ",font= ("arial", 18, "bold"))
entRnod = Entry(deletest, bd=5,font= ("arial", 18, "bold"))
btnAddSave = Button(deletest, text="Save",font= ("arial", 18, "bold"), width=10,command = f6, bg='SpringGreen2', activebackground='red')
btnAddBack = Button(deletest, text="Back",font= ("arial", 18, "bold"), width=10 , command = f7, bg='SpringGreen2', activebackground='red')

lblRnod.pack(pady=5)
entRnod.pack(pady=5)
btnAddSave.pack(pady=5)
btnAddBack.pack(pady=5)

emailst = Toplevel(root)
emailst.title("Email S")
emailst.geometry("1270x800-1+1")
emailst.configure(bg='LightCyan2')
emailst.resizable(False,False)
emailst.iconbitmap('icon.ico')
emailst.withdraw()

lblNamee = Label(emailst, text="Enter Student Name", font=("arial",18,"bold"))
entNamee = Entry(emailst, bd = 5, font=("arial",18,"bold"))
lblMarkse = Label(emailst, text="Enter Student Marks", font=("arial",18,"bold"))
entMarkse = Entry(emailst, bd = 5, font=("arial",18,"bold"))
lblMaile = Label(emailst, text="Enter Parent E-mail", font=("arial",18,"bold"))
entMaile = Entry(emailst, bd = 5, font=("arial",18,"bold"))
lblMail1e = Label(emailst, text="Enter Sender E-mail", font=("arial",18,"bold"))
entMail1e = Entry(emailst, bd = 5, font=("arial",18,"bold"))
lblPasse = Label(emailst, text="Sender enter password", font=("arial",18,"bold"))
entPasse = Entry(emailst, bd = 5, font=("arial",18,"bold")) 
entPasse.config(show="*");


lblNamee.place(x = 300, y = 100)
entNamee.place(x = 300, y = 140)
lblMarkse.place(x=800,y=100)
entMarkse.place(x=800,y=140)
lblMaile.pack(pady=10)
entMaile.pack(pady=10)
lblMail1e.place(x = 300, y = 240)
entMail1e.place(x = 300, y = 300)
lblPasse.place(x=800,y=240)
entPasse.place(x=800,y=300)
lblSp = Label(emailst, text="Student Performance :", font=("arial",18,"bold"))
f = IntVar()
f.set(2)

rbExcellent = Radiobutton(emailst, text="Excellent", font=("arial",18,"bold"),variable=f, value=1)
rbGood = Radiobutton(emailst, text="Good", font=("arial",18,"bold"),variable=f, value=2)
rbCdb = Radiobutton(emailst, text="Can Do Better", font=("arial",18,"bold"),variable=f, value=3)

lblSp.place(x=270,y=360)
rbExcellent.place(x=600,y=360) 
rbGood.place(x=600,y=430) 
rbCdb.place(x=600,y=490)

btnEmailSubmit = Button(emailst, text="Submit",command=f16,font=("arial", 18,"bold"), width=10, bg='SpringGreen2', activebackground='red')
btnEmailBack = Button(emailst, text="Back",command=f17,font=("arial", 18,"bold"), width=10, bg='SpringGreen2', activebackground='red')

btnEmailSubmit.place(x=480,y=550)
btnEmailBack.place(x=700,y=550)

root.mainloop()