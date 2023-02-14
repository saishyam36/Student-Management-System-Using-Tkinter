from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
import sqlite3


root3=Tk()
root3.title("ADMIN PAGE")
root3.geometry("900x600")
root3.config(bg="DarkOrchid3")
frame2=LabelFrame(root3,bg="cyan")
frame2.pack(pady=150,anchor=CENTER)



def all_data():
	global rows
	top1=Toplevel()
	top1.geometry("1200x500")
	label_top=Label(top1,text="STUDENT DATA",font=("Arial",30))
	label_top.pack(fill=X)
	midview=Frame(top1,width=900)
	midview.pack(side=RIGHT)



	sqliteConnection = sqlite3.connect('student_data.db')
	cursor = sqliteConnection.cursor()

	cursor.execute( " SELECT roll_id,first_name,last_name,email_id,phone_number,address,department,password,cgpa,role FROM STUDENT_TABLE")
	rows=cursor.fetchall()
	#print(rows)
	scrollbarx=Scrollbar(midview,orient=HORIZONTAL)
	scrollbary=Scrollbar(midview,orient=VERTICAL)
	cols=("ROLL NUMBER","FIRST NAME","LAST NAME","EMAIL ID","PHONE NUMBER","ADDRESS","DEPARTMENT","PASSWORD","CGPA","ROLE")
	list_tree=ttk.Treeview(midview,columns=cols,selectmode="extended",height=80,yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
	scrollbary.config(command=list_tree.yview)
	scrollbary.pack(side=RIGHT, fill=Y)
	scrollbarx.config(command=list_tree.xview)
	scrollbarx.pack(side=BOTTOM, fill=X)

	for i in range(0,len(cols)):
		if i==0:
			list_tree.column("#0",stretch=NO,minwidth=0,width=0)
			list_tree.heading(cols[i],text=cols[i])
			list_tree.pack()
		else:
			list_tree.heading(cols[i],text=cols[i])
			list_tree.pack()

	for data in rows:
		list_tree.insert("",'end',values=data)
	sqliteConnection.commit()
	cursor.close()
	sqliteConnection.close()



def roll_data():
	top1=Toplevel()
	top1.geometry("1200x500")
	label_top=Label(top1,text="STUDENT DATA",font=("Arial",30))
	label_top.pack(fill=X)
	midview=Frame(top1,width=900)
	midview.pack(side=RIGHT)



	sqliteConnection = sqlite3.connect('student_data.db')
	cursor = sqliteConnection.cursor()

	cursor.execute( " SELECT roll_id,first_name,last_name,email_id,phone_number,address,department,password,cgpa,role FROM STUDENT_TABLE WHERE roll_id=?",[roll.get()])
	rows=cursor.fetchall()
	#print(rows)
	scrollbarx=Scrollbar(midview,orient=HORIZONTAL)
	scrollbary=Scrollbar(midview,orient=VERTICAL)
	cols=("ROLL NUMBER","FIRST NAME","LAST NAME","EMAIL ID","PHONE NUMBER","ADDRESS","DEPARTMENT","PASSWORD","CGPA","ROLE")
	list_tree=ttk.Treeview(midview,columns=cols,selectmode="extended",height=80,yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
	scrollbary.config(command=list_tree.yview)
	scrollbary.pack(side=RIGHT, fill=Y)
	scrollbarx.config(command=list_tree.xview)
	scrollbarx.pack(side=BOTTOM, fill=X)

	for i in range(0,len(cols)):
		if i==0:
			list_tree.column("#0",stretch=NO,minwidth=0,width=0)
			list_tree.heading(cols[i],text=cols[i])
			list_tree.pack()
		else:
			list_tree.heading(cols[i],text=cols[i])
			list_tree.pack()

	for data in rows:
		list_tree.insert("",'end',values=data)
	sqliteConnection.commit()
	cursor.close()
	sqliteConnection.close()
	entry2.delete(0,END)




def dept_data():
	top1=Toplevel()
	top1.geometry("1200x500")
	label_top=Label(top1,text="STUDENT DATA",font=("Arial",30))
	label_top.pack(fill=X)
	midview=Frame(top1,width=900)
	midview.pack(side=RIGHT)



	sqliteConnection = sqlite3.connect('student_data.db')
	cursor = sqliteConnection.cursor()
	#print(dept.get())

	cursor.execute( """SELECT roll_id,first_name,last_name,email_id,phone_number,address,department,password,cgpa,role FROM STUDENT_TABLE WHERE department=?""",[dept.get()])
	rows=cursor.fetchall()
	#print(rows)
	scrollbarx=Scrollbar(midview,orient=HORIZONTAL)
	scrollbary=Scrollbar(midview,orient=VERTICAL)
	cols=("ROLL NUMBER","FIRST NAME","LAST NAME","EMAIL ID","PHONE NUMBER","ADDRESS","DEPARTMENT","PASSWORD","CGPA","ROLE")
	list_tree=ttk.Treeview(midview,columns=cols,selectmode="extended",height=80,yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
	scrollbary.config(command=list_tree.yview)
	scrollbary.pack(side=RIGHT, fill=Y)
	scrollbarx.config(command=list_tree.xview)
	scrollbarx.pack(side=BOTTOM, fill=X)

	for i in range(0,len(cols)):
		if i==0:
			list_tree.column("#0",stretch=NO,minwidth=0,width=0)
			list_tree.heading(cols[i],text=cols[i])
			list_tree.pack()
		else:
			list_tree.heading(cols[i],text=cols[i])
			list_tree.pack()

	for data in rows:
		list_tree.insert("",'end',values=data)
	sqliteConnection.commit()
	cursor.close()
	sqliteConnection.close()
	entry3.delete(0,END)




def cgpa_data():
	top1=Toplevel()
	top1.geometry("1200x500")
	label_top=Label(top1,text="STUDENT DATA",font=("Arial",30))
	label_top.pack(fill=X)
	midview=Frame(top1,width=900)
	midview.pack(side=RIGHT)



	sqliteConnection = sqlite3.connect('student_data.db')
	cursor = sqliteConnection.cursor()
	#print(cgpa.get())

	cursor.execute("SELECT roll_id,first_name,last_name,email_id,phone_number,address,department,password,cgpa,role FROM STUDENT_TABLE WHERE cgpa>=?",[cgpa.get()])
	rows=cursor.fetchall()
	#print(rows)
	scrollbarx=Scrollbar(midview,orient=HORIZONTAL)
	scrollbary=Scrollbar(midview,orient=VERTICAL)
	cols=("ROLL NUMBER","FIRST NAME","LAST NAME","EMAIL ID","PHONE NUMBER","ADDRESS","DEPARTMENT","PASSWORD","CGPA","ROLE")
	list_tree=ttk.Treeview(midview,columns=cols,selectmode="extended",height=80,yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
	scrollbary.config(command=list_tree.yview)
	scrollbary.pack(side=RIGHT, fill=Y)
	scrollbarx.config(command=list_tree.xview)
	scrollbarx.pack(side=BOTTOM, fill=X)

	for i in range(0,len(cols)):
		if i==0:
			list_tree.column("#0",stretch=NO,minwidth=0,width=0)
			list_tree.heading(cols[i],text=cols[i])
			list_tree.pack()
		else:
			list_tree.heading(cols[i],text=cols[i])
			list_tree.pack()

	for data in rows:
		list_tree.insert("",'end',values=data)
	sqliteConnection.commit()
	cursor.close()
	sqliteConnection.close()
	entry4.delete(0,END)



def update_req():
	top1=Toplevel()
	top1.geometry("1200x700")
	label_top=Label(top1,text="STUDENT DATA",font=("Arial",30))
	label_top.pack(fill=X)
	sideview=Frame(top1,width=200)
	sideview.pack(side=LEFT)
	midview=Frame(top1,width=700)
	midview.pack(side=RIGHT)


	def get_cursor(event):
		global row
		cursor_row=list_tree.focus()
		contents=list_tree.item(cursor_row)
		row=contents['values']




	sqliteConnection = sqlite3.connect('update_requests.db')
	cursor = sqliteConnection.cursor()
	#print(cgpa.get())

	cursor.execute("SELECT roll_id,first_name,last_name,email_id,phone_number,address,department,cgpa FROM STUDENT_UPDATE")
	rows_update=cursor.fetchall()
	#print(rows)
	scrollbarx=Scrollbar(midview,orient=HORIZONTAL)
	scrollbary=Scrollbar(midview,orient=VERTICAL)
	cols=("ROLL NUMBER","FIRST NAME","LAST NAME","EMAIL ID","PHONE NUMBER","ADDRESS","DEPARTMENT","CGPA")
	list_tree=ttk.Treeview(midview,columns=cols,selectmode="extended",height=80,yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
	scrollbary.config(command=list_tree.yview)
	scrollbary.pack(side=RIGHT, fill=Y)
	scrollbarx.config(command=list_tree.xview)
	scrollbarx.pack(side=BOTTOM, fill=X)

	for i in range(0,len(cols)):
		if i==0:
			list_tree.column("#0",stretch=NO,minwidth=0,width=0)
			list_tree.heading(cols[i],text=cols[i])
			list_tree.pack()
		else:
			list_tree.heading(cols[i],text=cols[i])
			list_tree.pack()

	for data in rows_update:
		list_tree.insert("",'end',values=data)

	list_tree.bind("<ButtonRelease-1>",get_cursor)

	sqliteConnection.commit()
	cursor.close()
	sqliteConnection.close()



	def update_record():
		try:
			sqliteConnection = sqlite3.connect('student_data.db')
			cursor = sqliteConnection.cursor()
			cursor.execute( """ UPDATE  STUDENT_TABLE SET roll_id=?,first_name=?,last_name=?,email_id=?,phone_number=?,address=?,department=?,cgpa=? WHERE roll_id=?""",[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[0]]) 
			sqliteConnection.commit()
			cursor.close()
			messagebox.showinfo("success","Successfully Updated")
		except sqlite3.Error as error:
			print(error)
			messagebox.showerror("Error",f"Error due to: {str(error)}")

		sqliteConnection.close()



	def delete_record():
		try:
			sqliteConnection = sqlite3.connect('update_requests.db')
			cursor = sqliteConnection.cursor()
			cursor.execute( """ DELETE FROM STUDENT_UPDATE WHERE roll_id=?""",[row[0]]) 
			sqliteConnection.commit()
			cursor.close()
			messagebox.showinfo("success","Successfully  Deleted")
		except sqlite3.Error as error:
			print(error)
			messagebox.showerror("Error",f"Error due to: {str(error)}")

		sqliteConnection.close()





	update_btn=Button(sideview,text="UPDATE",width=20,height=4,command=update_record,bg="lime green")
	update_btn.pack(fill=X)	
	delete_btn=Button(sideview,text="DELETE",width=20,height=4,command=delete_record,bg="orange red")
	delete_btn.pack(fill=X)


label1=Label(frame2,text="View All The Student Data",bg="red",width=30)
label1.grid(row=0,column=0,rowspan=2,columnspan=1,pady=30,padx=(30,10))
label2=Label(frame2,text="View Student Data With Roll Number",bg="red",width=30)
label2.grid(row=1,column=0,rowspan=2,columnspan=1,pady=30,padx=(30,10))
label3=Label(frame2,text="View Student Data With Department",bg="red",width=30)
label3.grid(row=2,column=0,rowspan=2,columnspan=1,pady=30,padx=(30,10))
label4=Label(frame2,text="View Student Data According To CGPA",bg="red",width=30)
label4.grid(row=3,column=0,rowspan=2,columnspan=1,pady=30,padx=(30,10))
label5=Label(frame2,text="Update Requests From Students",bg="red",width=30)
label5.grid(row=4,column=0,rowspan=2,columnspan=1,pady=30,padx=(30,10))

roll=IntVar()
entry2=Entry(frame2,width=20,textvariable=roll)
entry2.grid(row=1,column=1,rowspan=2,columnspan=1,pady=30,padx=10)
dept=StringVar()
entry3=Entry(frame2,width=20,textvariable=dept)
entry3.grid(row=2,column=1,rowspan=2,columnspan=1,pady=30,padx=10)
cgpa=DoubleVar()
entry4=Entry(frame2,width=20,textvariable=cgpa)
entry4.grid(row=3,column=1,rowspan=2,columnspan=1,pady=30,padx=10)

btn1=Button(frame2,text="OPEN",width=20,command=all_data,bg="green2")
btn1.grid(row=0,column=1,rowspan=2,columnspan=1,pady=30,padx=10)
btn2=Button(frame2,text="FETCH DATA",width=20,command=roll_data,bg="green2")
btn2.grid(row=1,column=2,rowspan=2,columnspan=1,pady=30,padx=(10,30))
btn3=Button(frame2,text="FETCH DATA",width=20,command=dept_data,bg="green2")
btn3.grid(row=2,column=2,rowspan=2,columnspan=1,pady=30,padx=(10,30))
btn4=Button(frame2,text="FETCH DATA",width=20,command=cgpa_data,bg="green2")
btn4.grid(row=3,column=2,rowspan=2,columnspan=1,pady=30,padx=(10,30))
btn5=Button(frame2,text="OPEN",width=20,command=update_req,bg="green2")
btn5.grid(row=4,column=1,rowspan=2,columnspan=1,pady=30,padx=10)

	