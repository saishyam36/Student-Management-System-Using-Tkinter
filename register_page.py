from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
import sqlite3
import pyotp
import http.client



'''
#student data table
#create a database or connect to one
conn=sqlite3.connect('student_data.db')

#create cursor
c=conn.cursor()

#create table
c.execute("""CREATE TABLE STUDENT_TABLE(
		 roll_id INTEGER PRIMARY KEY,
         first_name text,
         last_name text,
         email_id text UNIQUE,
         phone_number integer UNIQUE,
         address text,
         department text,
         password text,
         cgpa real,
         role text,
         photo BLOB NOT NULL)
	""")'''

def register():
	root1=Tk()
	root1.title("SIGN UP")
	root1.geometry("1000x750")
	root1.config(bg="cyan2")

	#register page details

	#create text box labels
	f_name_label=Label(root1,text="FIRST NAME :",bg="orchid2",width=20)
	f_name_label.grid(row=1,column=0,padx=20,pady=(40,0))
	l_name_label=Label(root1,text="LAST NAME :",bg="orchid2",width=20)
	l_name_label.grid(row=1,column=2,padx=20,pady=(40,0))
	email_label=Label(root1,text="EMAIL ID :",bg="orchid2",width=20)
	email_label.grid(row=2,column=0,padx=20,pady=(40,0),columnspan=1)
	ph_label=Label(root1,text="PHONE NUMBER :",bg="orchid2",width=20)
	ph_label.grid(row=2,column=2,padx=20,pady=(40,0),columnspan=1)
	otp_label=Label(root1,text="OTP NUMBER:",bg="orchid2",width=20)
	otp_label.grid(row=3,column=2,padx=20,pady=(40,0),columnspan=1)
	rollno_label=Label(root1,text="ROLL NUMBER:",bg="orchid2",width=20)
	rollno_label.grid(row=3,column=0,padx=20,pady=(40,0),columnspan=1)
	address_label=Label(root1,text="ADDRESS :",bg="orchid2",width=20)
	address_label.grid(row=4,column=0,padx=20,pady=(40,0),columnspan=1)
	dept_label=Label(root1,text="DEPARTMENT :",bg="orchid2",width=20)
	dept_label.grid(row=4,column=2,padx=20,pady=(40,0),columnspan=1)
	password_label=Label(root1,text="PASSWORD :",bg="orchid2",width=20)
	password_label.grid(row=5,column=0,padx=20,pady=(40,0),columnspan=1)
	con_password_label=Label(root1,text="CONFIRM PASSWORD :",bg="orchid2",width=20)
	con_password_label.grid(row=5,column=2,padx=20,pady=(40,0),columnspan=1)

	
	f_name=Entry(root1,width=30,bg="white")
	f_name.grid(row=1,column=1,padx=10,pady=(40,0),columnspan=1)

	l_name=Entry(root1,width=30,bg="white")
	l_name.grid(row=1,column=3,padx=10,pady=(40,0),columnspan=1)

	email_id=Entry(root1,width=30,bg="white")
	email_id.grid(row=2,column=1,padx=10,pady=(40,0),columnspan=1)

	ph_no=Entry(root1,width=30,bg="white")
	ph_no.grid(row=2,column=3,padx=10,pady=(40,0),columnspan=1)

	roll_no=Entry(root1,width=30,bg="white")
	roll_no.grid(row=3,column=1,padx=10,pady=(40,0),columnspan=1)

	otp=Entry(root1,width=30,bg="white")
	otp.grid(row=3,column=3,padx=10,pady=(40,0),columnspan=1)


	def otp_get():
		global code
		totp = pyotp.TOTP('base32secret3232') #algorithm used for securing otp
		code=totp.now() #getting 6 digit otp randomly
		print(code)
		mobile_no=ph_no.get()
		conn = http.client.HTTPSConnection("api.authkey.io")
		conn.request("GET", "/request?authkey=9cead05e00bf81ac&mobile="+str(mobile_no)+"&country_code=91&otp="+str(code)+"&sid=1082&time=20seconds&company=RIT")
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))
		return code 

	address=Entry(root1,width=30,bg="white")
	address.grid(row=4,column=1,padx=10,pady=(40,0),columnspan=1)

	dept=Entry(root1,width=30,bg="white")
	dept.grid(row=4,column=3,padx=10,pady=(40,0),columnspan=1)

	p=StringVar()
	password=Entry(root1,width=30,bg="white",textvariable=p)
	password.grid(row=5,column=1,padx=10,pady=(40,0),columnspan=1)
	con_password=Entry(root1,width=30,bg="white")
	con_password.grid(row=5,column=3,padx=10,pady=(40,0),columnspan=1)

	c1=IntVar()
	c=Checkbutton(root1,text="I Agree with Terms & conditions",cursor="hand2",bg="forest green",variable=c1,onvalue=1,offvalue=0)  
	c.deselect()
	c.grid(row=8,column=1,padx=20,pady=(10,0),columnspan=1)

	def show_role():
		global role
		role=click_drop.get()
	
	options=["STUDENT","ADMIN"]
	click_drop=StringVar()
	click_drop.set(options[0])
	drop=OptionMenu(root1,click_drop,*options)
	drop.grid(row=6,column=0,pady=(40,0))
	drop_btn=Button(root1,text="DONE",command=show_role,cursor="hand2").grid(row=7,column=0,padx=10,pady=(10,0),columnspan=1)

	cgpa=Entry(root1,width=30,bg="white")
	cgpa.grid(row=6,column=3,padx=20,pady=(40,0),columnspan=1)
	cgpa_label=Label(root1,text="CGPA :",bg="orchid2",width=20)
	cgpa_label.grid(row=6,column=2,pady=(40,0),columnspan=1)


	def login_reg():
		#go back to login page
		root1.destroy()
		import Project

	def clear():
		f_name.delete(0,END)
		l_name.delete(0,END)
		email_id.delete(0,END)
		ph_no.delete(0,END)
		roll_no.delete(0,END)
		address.delete(0,END)
		dept.delete(0,END)
		password.delete(0,END)
		con_password.delete(0,END)
		cgpa.delete(0,END)
		otp.delete(0,END)


	def submit():
		#check password if correct and has same parameters required if wrong show a error pop up
		#if success show popup for success
		#for database
		if (f_name.get()=="" or l_name.get()=="" or email_id.get()=="" or ph_no.get()=="" or roll_no.get()=="" or address.get()=="" or dept.get()=="" or password.get()=="" or con_password.get()==""):
			messagebox.showerror("Error","Fill all the fields")
		elif(len(p.get())<8 or len(p.get())>15 ):
			messagebox.showwarning("Warning","Enter Characters between 8 to 15")
		elif(password.get()!=con_password.get()):
			messagebox.showerror("Error","Password Not matching with confirm password")
		elif(code!=otp.get()):
			messagebox.showerror("Error","Enter Correct OTP")
		elif(c1.get()==0):
			messagebox.showwarning("Warning","Please Agree with our Terms and Conditions")
		else:
			try:
				sqliteConnection = sqlite3.connect('student_data.db')
				cursor = sqliteConnection.cursor()

				user_Photo=convertToBinaryData(photo_file)
				# Convert data into tuple format
				cursor.execute( """ INSERT INTO STUDENT_TABLE (roll_id,first_name,last_name,email_id,phone_number,address,department,password,cgpa,role,photo) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",[roll_no.get(),f_name.get(),l_name.get(),email_id.get(),ph_no.get(),address.get(),dept.get(),password.get(),cgpa.get(),role,user_Photo])
				sqliteConnection.commit()
				cursor.close()
				messagebox.showinfo("success","You have successfully registered")
				clear()
			except sqlite3.Error as error:
				messagebox.showerror("Error",f"Error due to: {str(error)}")

			sqliteConnection.close()

			
	def select_img():
		picture=openfilename()

		# opens the image
		img=Image.open(picture)
		
		# resize the image and apply a high-quality down sampling filter
		img=img.resize((150,150), Image.ANTIALIAS)

		# PhotoImage class is used to add image to widgets, icons etc
		img=ImageTk.PhotoImage(img)

		panel=Label(root1, image = img)
		
		# set the image as img
		panel.image=img
		panel.grid(row=0,column=1,padx=10,pady=5,columnspan=1)

	def openfilename():
		global photo_file
		filename=filedialog.askopenfilename(title ='"pen')
		photo_file=filename
		return filename

	# Create a button and place it into the window using grid layout
	photo_btn=Button(root1,text ='select image',command=select_img).grid(row=0,column=0,padx=5,pady=(5,0))

	def convertToBinaryData(photo_file):
    # Convert digital data to binary format
		with open(photo_file,'rb') as file:
			blobData=file.read()
		return blobData

	get_otp=Button(root1,text="SENT OTP",bg="firebrick2",font=("times new roman",15),cursor="hand2",width=10,command=otp_get).grid(row=9,sticky=SE,column=1,pady=(10,20),padx=20)
	submit_btn=Button(root1,text="SUBMIT",bg="firebrick2",font=("times new roman",15),cursor="hand2",width=10,command=submit).grid(row=10,sticky=SE,column=1,pady=(10,20),padx=20)
	log_in_btn=Button(root1,text="LOGIN",bg="firebrick2",font=("times new roman",15),cursor="hand2",width=10,command=login_reg).grid(row=11,sticky=SE,column=1,padx=20)



register()