from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
import sqlite3
import pyotp
import http.client


'''
#update requests table
#create a database or connect to one
conn=sqlite3.connect('update_requests.db')

#create cursor
c=conn.cursor()

#create table
c.execute("""CREATE TABLE STUDENT_UPDATE(
         roll_id integer primary key,
         first_name text,
         last_name text,
         email_id text UNIQUE,
         phone_number integer UNIQUE,
         address text,
         department text,
         cgpa real)
	""")'''

root=Tk()
root.title("Student_Login")
root.geometry("500x500")
root.config(bg="turquoise1")
frame1=LabelFrame(root,bg="red2")
frame1.pack(padx=50,pady=100)

def register():
	root.destroy()
	import register_page


def student_details():
	root2=Tk()
	root2.title("student_details")
	root2.geometry("900x700")
	root2.config(bg="cyan")

	def update_request():
		top_update=Toplevel()
		top_update.geometry("500x600")
		top_update.title("Update Request")
		top_update.config(bg="yellow")

		sqliteConnection = sqlite3.connect('student_data.db')
		cursor = sqliteConnection.cursor()
		#print(roll_number)
		cursor.execute(" SELECT roll_id,first_name,last_name,email_id,phone_number,address,department,cgpa FROM STUDENT_TABLE WHERE roll_id=?",[roll_number])
		row_update=cursor.fetchone()


		#update page labels and entry widgets
		rollno_label=Label(top_update,text="ROLL NUMBER :",bg="red",width=20)
		rollno_label.grid(row=0,column=0,padx=20,pady=(40,0),columnspan=1)
		f_name_label=Label(top_update,text="FIRST NAME :",bg="red",width=20)
		f_name_label.grid(row=1,column=0,padx=20,pady=(30,0))
		l_name_label=Label(top_update,text="LAST NAME :",bg="red",width=20)
		l_name_label.grid(row=2,column=0,padx=20,pady=(30,0))
		email_label=Label(top_update,text="EMAIL ID :",bg="red",width=20)
		email_label.grid(row=3,column=0,padx=20,pady=(40,0),columnspan=1)
		ph_label=Label(top_update,text="PHONE NUMBER :",bg="red",width=20)
		ph_label.grid(row=4,column=0,padx=20,pady=(40,0),columnspan=1)
		address_label=Label(top_update,text="ADDRESS :",bg="red",width=20)
		address_label.grid(row=5,column=0,padx=20,pady=(40,0),columnspan=1)
		dept_label=Label(top_update,text="DEPARTMENT :",bg="red",width=20)
		dept_label.grid(row=6,column=0,padx=20,pady=(40,0),columnspan=1)
		cgpa_label=Label(top_update,text="CGPA :",bg="red",width=20)
		cgpa_label.grid(row=7,column=0,padx=20,pady=(40,0),columnspan=1)

		rollno_update=Entry(top_update,bg="cyan2",width=20)
		rollno_update.grid(row=0,column=1,padx=20,pady=(40,0),columnspan=1)
		f_name_update=Entry(top_update,bg="cyan2",width=20)
		f_name_update.grid(row=1,column=1,padx=20,pady=(30,0))
		l_name_update=Entry(top_update,bg="cyan2",width=20)
		l_name_update.grid(row=2,column=1,padx=20,pady=(30,0))
		email_update=Entry(top_update,bg="cyan2",width=20)
		email_update.grid(row=3,column=1,padx=20,pady=(40,0),columnspan=1)
		ph_update=Entry(top_update,bg="cyan2",width=20)
		ph_update.grid(row=4,column=1,padx=20,pady=(40,0),columnspan=1)
		address_update=Entry(top_update,bg="cyan2",width=20)
		address_update.grid(row=5,column=1,padx=20,pady=(40,0),columnspan=1)
		dept_update=Entry(top_update,bg="cyan2",width=20)
		dept_update.grid(row=6,column=1,padx=20,pady=(40,0),columnspan=1)
		cgpa_update=Entry(top_update,bg="cyan2",width=20)
		cgpa_update.grid(row=7,column=1,padx=20,pady=(40,0),columnspan=1)


		#insertion in update page
		rollno_update.insert(0,row_update[0])
		f_name_update.insert(0,row_update[1])
		l_name_update.insert(0,row_update[2])
		email_update.insert(0,row_update[3])
		ph_update.insert(0,row_update[4])
		address_update.insert(0,row_update[5])
		dept_update.insert(0,row_update[6])
		cgpa_update.insert(0,row_update[7])

		sqliteConnection.commit()
		cursor.close()
		sqliteConnection.close()

		def send_request():
			try:
				sqliteConnection = sqlite3.connect('update_requests.db')
				cursor = sqliteConnection.cursor()
				cursor.execute( """ INSERT INTO STUDENT_UPDATE (roll_id,first_name,last_name,email_id,phone_number,address,department,cgpa) VALUES (?,?,?,?,?,?,?,?)""",[rollno_update.get(),f_name_update.get(),l_name_update.get(),email_update.get(),ph_update.get(),address_update.get(),dept_update.get(),cgpa_update.get()])
				sqliteConnection.commit()
				cursor.close()
				messagebox.showinfo("success","Request Has Sent To ADMIN")
				top_update.destroy()
			except sqlite3.Error as error:
				messagebox.showerror("Error",f"Error due to: {str(error)}")
				top_update.destroy()

			sqliteConnection.close()

		send_req=Button(top_update,text="SEND REQUEST",command=send_request,bg="medium purple")
		send_req.grid(row=8,column=1,columnspan=1,padx=10,pady=30)


	def writetofile(data,filename):
		# Convert binary data to proper format and write it on Hard Disk
		with open(filename,'wb') as file:
			file.write(data)
		return filename

	f_name_label=Label(root2,text="FIRST NAME :",bg="snow4",width=20)
	f_name_label.grid(row=3,column=0,padx=20,pady=(30,0))
	l_name_label=Label(root2,text="LAST NAME :",bg="snow4",width=20)
	l_name_label.grid(row=3,column=2,padx=20,pady=(30,0))
	email_label=Label(root2,text="EMAIL ID :",bg="snow4",width=20)
	email_label.grid(row=4,column=0,padx=20,pady=(40,0),columnspan=1)
	ph_label=Label(root2,text="PHONE NUMBER :",bg="snow4",width=20)
	ph_label.grid(row=4,column=2,padx=20,pady=(40,0),columnspan=1)
	rollno_label=Label(root2,text="ROLL NUMBER:",bg="snow4",width=20)
	rollno_label.grid(row=5,column=0,padx=20,pady=(40,0),columnspan=1)
	address_label=Label(root2,text="ADDRESS :",bg="snow4",width=20)
	address_label.grid(row=5,column=2,padx=20,pady=(40,0),columnspan=1)
	dept_label=Label(root2,text="DEPARTMENT :",bg="snow4",width=20)
	dept_label.grid(row=6,column=0,padx=20,pady=(40,0),columnspan=1)
	cgpa_label=Label(root2,text="CGPA:",bg="snow4",width=20)
	cgpa_label.grid(row=6,column=2,padx=20,pady=(40,0),columnspan=1)
	role_label=Label(root2,text="ROLE:",bg="snow4",width=20)
	role_label.grid(row=7,column=0,padx=20,pady=(40,0),columnspan=1)

	sqliteConnection = sqlite3.connect('student_data.db')
	cursor = sqliteConnection.cursor()

	cursor.execute( " SELECT * FROM STUDENT_TABLE WHERE email_id=? and password=?" ,(email_data,password_data))
	row=cursor.fetchone()

	f_name_label1=Label(root2,text=row[1],bg="mediumpurple2",width=20)
	f_name_label1.grid(row=3,column=1,padx=20,pady=(30,0))
	l_name_label1=Label(root2,text=row[2],bg="mediumpurple2",width=20)
	l_name_label1.grid(row=3,column=3,padx=20,pady=(30,0))
	email_label1=Label(root2,text=row[3],bg="mediumpurple2",width=20)
	email_label1.grid(row=4,column=1,padx=20,pady=(40,0),columnspan=1)
	ph_label1=Label(root2,text=row[4],bg="mediumpurple2",width=20)
	ph_label1.grid(row=4,column=3,padx=20,pady=(40,0),columnspan=1)
	rollno_label1=Label(root2,text=row[0],bg="mediumpurple2",width=20)
	rollno_label1.grid(row=5,column=1,padx=20,pady=(40,0),columnspan=1)
	address_label1=Label(root2,text=row[5],bg="mediumpurple2",width=30)
	address_label1.grid(row=5,column=3,padx=20,pady=(40,0),columnspan=1)
	dept_label1=Label(root2,text=row[6],bg="mediumpurple2",width=20)
	dept_label1.grid(row=6,column=1,padx=20,pady=(40,0),columnspan=1)
	cgpa_label1=Label(root2,text=row[8],bg="mediumpurple2",width=20)
	cgpa_label1.grid(row=6,column=3,padx=20,pady=(40,0),columnspan=1)
	role_label1=Label(root2,text=row[9],bg="mediumpurple2",width=20)
	role_label1.grid(row=7,column=1,padx=20,pady=(40,0),columnspan=1)
	photo1=row[10]
	photopath=str(row[0])+".jpg"
	#if you want to save the retrived photos in any path  add a path to photopath
	#"C:\\Users\\HP\\Desktop\\Backgrounds\\project photos\\"
	photo_data=writetofile(photo1,photopath)
	img=Image.open(photo_data)
	img=img.resize((200,200),Image.ANTIALIAS)
	img=ImageTk.PhotoImage(img)
	panel = Label(root2, image = img)
	panel.image = img
	panel.grid(row=0,column=1)


	roll_number=row[0]
	update_btn=Button(root2,text="UPDATE DETAILS",bg="blue",width=20,command=update_request)
	update_btn.grid(row=12,column=2,sticky=N,pady=(40,0))

	sqliteConnection.commit()
	cursor.close()
	sqliteConnection.close() 




def log_in():
	global email_data
	global password_data

	email_data=email_entry.get()
	password_data=password_entry.get()

	if(email_entry.get()=="" or password_entry.get()==""):
		messagebox.showerror("Error","Fill all the fields")
	else:
		try:
			sqliteConnection = sqlite3.connect('student_data.db')
			cursor = sqliteConnection.cursor()

			cursor.execute( " SELECT * FROM STUDENT_TABLE WHERE email_id=? and password=?" ,(email_entry.get(),password_entry.get()))
			r1=cursor.fetchone()
			if(r1==None):
				messagebox.showerror("Error","Incorrect EMAIL ID or PASSWORD")
			else:
				messagebox.showinfo("success","You Have successfully Logged In")
				root.destroy()
				student_details()
			sqliteConnection.commit()
			cursor.close()
		except sqlite3.Error as er:
			messagebox.showerror("Error",f"Error due to: {str(er)}")
		sqliteConnection.close() 




def admin():
	if(email_entry.get()=="" or password_entry.get()==""):
		messagebox.showerror("Error","Fill all the fields")
	else:
		try:
			sqliteConnection = sqlite3.connect('student_data.db')
			cursor = sqliteConnection.cursor()

			cursor.execute( " SELECT * FROM STUDENT_TABLE WHERE email_id=? and password=? and role=?",(email_entry.get(),password_entry.get(),"ADMIN"))
			r2=cursor.fetchone()
			if(r2==None):
				messagebox.showerror("Error","Incorrect EMAIL ID or PASSWORD or You are not an Admin")
			else:
				messagebox.showinfo("success","Successfully Logged In")
				root.destroy()
				import admin_page
			sqliteConnection.commit()
			cursor.close()
		except sqlite3.Error as er:
			messagebox.showerror("Error",f"Error due to: {str(er)}")
		sqliteConnection.close()


def reset_password():
	top3=Toplevel()
	top3.geometry("400x400")
	top3.title("Forgot Password")
	top3.config(bg="MediumPurple2")

	def otp_get():
		global code
		totp = pyotp.TOTP('base32secret3232') #algorithm used for securing otp
		code=totp.now() #getting 6 digit otp randomly
		print(code)
		mobile_no=ph_entry.get()
		conn = http.client.HTTPSConnection("api.authkey.io")
		conn.request("GET", "/request?authkey=9cead05e00bf81ac&mobile="+str(mobile_no)+"&country_code=91&otp="+str(code)+"&sid=1082&time=20seconds&company=RIT")
		res = conn.getresponse()
		data = res.read()
		#print(data.decode("utf-8"))
		return code

	def done():
		if (email_entry.get()=="" or ph_entry.get()=="" or password_entry.get()=="" or con_password_entry.get()=="" or otp_entry.get()==""):
			messagebox.showerror("Error","Fill all the fields")
		elif(len(password_entry.get())<8 or len(password_entry.get())>15 ):
			messagebox.showwarning("Warning","Enter Characters between 8 to 15")
		elif(password_entry.get()!=con_password_entry.get()):
			messagebox.showerror("Error","Password Not matching with confirm password")
		elif(code!=otp_entry.get()):
			messagebox.showerror("Error","Enter Correct OTP")
		else:
			try:
				sqliteConnection = sqlite3.connect('student_data.db')
				cursor = sqliteConnection.cursor()
				cursor.execute( """ UPDATE STUDENT_TABLE SET password=? WHERE email_id=? AND phone_number=?""",[password_entry.get(),email_entry.get(),ph_entry.get()])
				sqliteConnection.commit()
				cursor.close()
				try:
					sqliteConnection = sqlite3.connect('student_data.db')
					cursor = sqliteConnection.cursor()

					cursor.execute( " SELECT * FROM STUDENT_TABLE WHERE email_id=? and phone_number=?",[email_entry.get(),ph_entry.get()])
					r2=cursor.fetchone()
					if(r2==None):
						messagebox.showerror("Error","Incorrect EMAIL ID or PHONE NUMBER")
						top3.destroy()
					sqliteConnection.commit()
					cursor.close()
				except sqlite3.Error as er:
					messagebox.showerror("Error",f"Error due to: {str(er)}")
				sqliteConnection.close()
				messagebox.showinfo("success","Password Successfully Updated")
			except sqlite3.Error as error:
				messagebox.showerror("Error",f"Error due to: {str(error)}")

			sqliteConnection.close()


	email_id=Label(top3,text="EMAIL ID:",bg="cyan",width=20).grid(row=0,column=0,pady=10,padx=20)
	ph_no=Label(top3,text="PHONE NUMBER:",bg="cyan",width=20).grid(row=1,column=0,pady=10,padx=20)
	password=Label(top3,text="PASSWORD:",bg="cyan",width=20).grid(row=2,column=0,pady=10,padx=20)
	email_entry=Entry(top3,width=20)
	email_entry.grid(row=0,column=1,pady=10,padx=20)
	ph_entry=Entry(top3,width=20)
	ph_entry.grid(row=1,column=1,pady=10,padx=20)
	password_entry=Entry(top3,width=20)
	password_entry.grid(row=2,column=1,pady=10,padx=20)
	con_password=Label(top3,text="CONFIRM PASSWORD:",bg="cyan",width=20).grid(row=3,column=0,pady=10,padx=20)
	otp=Label(top3,text="OTP:",bg="cyan",width=20).grid(row=4,column=0,pady=10,padx=20)
	con_password_entry=Entry(top3)
	con_password_entry.grid(row=3,column=1,pady=10,padx=20)
	otp_entry=Entry(top3)
	otp_entry.grid(row=4,column=1,pady=10,padx=20)

	otp_btn=Button(top3,text="GET OTP",width=30,cursor="hand2",command=otp_get,bg="blue2")
	otp_btn.grid(row=5,column=0,pady=(30,10),columnspan=3)
	done_btn=Button(top3,text="DONE",width=30,cursor="hand2",command=done,bg="blue2")
	done_btn.grid(row=6,column=0,pady=(10,0),columnspan=3)


email_id_login=Label(frame1,text="EMAIL ID:",bg="yellow",width=16).grid(row=0,column=0,pady=10,padx=20)
password_login=Label(frame1,text="PASSWORD:",bg="yellow",width=16).grid(row=1,column=0,pady=10,padx=20)
email_entry=Entry(frame1,width=25)
email_entry.grid(row=0,column=1,pady=10,padx=20)
password_entry=Entry(frame1,width=25,show="*")
password_entry.grid(row=1,column=1,pady=10,padx=20)

log_in_btn=Button(frame1,text="Log In",width=10,cursor="hand2",command=log_in,bg="green2")
log_in_btn.grid(row=2,column=0,pady=10,padx=20,columnspan=1)
admin_btn=Button(frame1,text="Admin",width=10,cursor="hand2",command=admin,bg="green2")
admin_btn.grid(row=2,column=1,pady=10)

reg_label=Label(frame1,text="Fresh Registeration Here",bg="cyan").grid(row=3,columnspan=2)
reg_btn=Button(frame1,text="Register",width=30,command=register,cursor="hand2",bg="green2")
reg_btn.grid(row=4,column=0,pady=10,columnspan=3)

fp_label=Label(frame1,text="Forgot Password?",bg="cyan").grid(row=5,columnspan=2)
fp_btn=Button(frame1,text="Reset Password",width=30,cursor="hand2",command=reset_password,bg="green2")
fp_btn.grid(row=6,column=0,pady=10,columnspan=3)






mainloop()