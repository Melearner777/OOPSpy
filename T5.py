import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Performance Management System")

title_label = tk.Label(win, text="Student Performance Management System", font=("Cascadia Code SemiBold", 30, "bold"), border=13, relief=tk.GROOVE, bg="Green", foreground="yellow")
title_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Arial Rounded MT Bold", 17), bd=13, relief=tk.GROOVE, bg="lightgrey")
detail_frame.place(x=20, y=90, width=426, height=575)

data_frame = tk.LabelFrame(win, bd=13, bg="lightgrey", relief=tk.GROOVE)
data_frame.place(x=460, y=90, width=813, height=575)


#==========Variables=======

rollno=tk.StringVar()
name=tk.StringVar()
class_var=tk.StringVar()
section=tk.StringVar()
contact=tk.StringVar()
Fathersnme=tk.StringVar()
address=tk.StringVar()
gender=tk.StringVar()
dob=tk.StringVar()

search_by=tk.StringVar()

# ==========Entry==========
rollno_lbl=tk.Label(detail_frame,text="Roll No.",font=('Arial',15),bg='lightgrey')
rollno_lbl.grid(row=0,column=0,padx=2,pady=2)

rollno_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=rollno)
rollno_lbl.grid(row=0,column=1,padx=2,pady=2)

name_lbl=tk.Label(detail_frame,text="Name",font=('Arial',15),bg='lightgrey')
name_lbl.grid(row=1,column=0,padx=2,pady=2)

name_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=name)
name_lbl.grid(row=1,column=1,padx=2,pady=2)

Class_lbl=tk.Label(detail_frame,text="Class",font=('Arial',15),bg='lightgrey')
Class_lbl.grid(row=2,column=0,padx=2,pady=2)

Class_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=class_var)
Class_lbl.grid(row=2,column=1,padx=2,pady=2)

Section_lbl=tk.Label(detail_frame,text="Section",font=('Arial',15),bg='lightgrey')
Section_lbl.grid(row=3,column=0,padx=2,pady=2)

Section_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=section)
Section_lbl.grid(row=3,column=1,padx=2,pady=2)

Contact_lbl=tk.Label(detail_frame,text="Contact",font=('Arial',15),bg='lightgrey')
Contact_lbl.grid(row=4,column=0,padx=2,pady=2)

Contact_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=contact)
Contact_lbl.grid(row=4,column=1,padx=2,pady=2)

Fathersnme_lbl=tk.Label(detail_frame,text="Father's Name",font=('Arial',15),bg='lightgrey')
Fathersnme_lbl.grid(row=5,column=0,padx=2,pady=2)

Fathersnme_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=Fathersnme)
Fathersnme_lbl.grid(row=5,column=1,padx=2,pady=2)

Address_lbl=tk.Label(detail_frame,text="Address",font=('Arial',15),bg='lightgrey')
Address_lbl.grid(row=6,column=0,padx=2,pady=2)

Address_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15),textvariable=address)
Address_lbl.grid(row=6,column=1,padx=2,pady=2)

gender_lbl=tk.Label(detail_frame,text="Gender",font=("Arial",15),bg="lightgrey")
gender_lbl.grid(row=7,column=0,padx=2,pady=2)

gender_ent=ttk.Combobox(detail_frame,text="Gender",font=('Arial',15),state="readonly",textvariable=gender)
gender_ent['values']=("Male","Female","Others")
gender_ent.grid(row=7,column=1,padx=2,pady=2)

dob_lbl=tk.Label(detail_frame,text="D.O.B",font=('Arial',15),bg="lightgrey")
dob_lbl.grid(row=8,column=0,padx=2,pady=2)

dob_ent=tk.Entry(detail_frame,bd=7,font=('arial',15))
dob_ent.grid(row=8,column=1,padx=2,pady=2)



#==============Functions ==============#

def fetch_data():
    conn =pymysql.connect(host="localhost",user="root",password="",database="sms1")
    curr= conn.cursor()
    curr.execute("SELECT* FROM data")
    rows=curr.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END,values=row)
        conn.commit()
    conn.close()


def add_func():
    if rollno.get() == "" or name.get() == "" or class_var.get() == "":
        messagebox.showerror("Error!","Please fill all the fields!")
    else:
        conn = pymysql.connect(host="localhost",user="root",password="",database="sms1")
        curr=conn.cursor()
        curr.execute("INSERT INTO data VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollno.get(),name.get(),class_var.get(),contact.get(),Fathersnme.get(),address.get(),gender.get(),dob.get()))
        conn.commit()
        conn.close()

        fetch_data() #This will fetch the data after heading
        
def get_cursor(event):
    
    cursor_row= student_table.focus()
    content= student_table.item(cursor_row)
    row=content['values']
    rollno.set(row[0])
    name.set(row[1])
    class_var.set(row[2])
    section.set(row[3])
    contact.set(row[4])
    Fathersnme.set(row[5])
    address.set(row[6])
    gender.set(row[7])
    dob.set(row[8])
    
def clear():
    
    
    rollno.set("")
    name.set("")
    class_var.set("")
    section.set("")
    contact.set("")
    Fathersnme.set("")
    address.set("")
    gender.set("")
    dob.set("")

def update_func():
    conn=pymysql.connect(host="localhost",user="root",password="",database="sms1")
    curr=conn.cursor()
    curr.execute("UPDATE data SET name=%s, class_var=%s, section=%s, contact=%s, fathersnme=%s, address=%s, gender=%s, dob=%s WHERE roll_no=%s", (name.get(), class_var.get(), section.get(), contact.get(), Fathersnme.get(), address.get(), gender.get(), dob.get(), rollno.get()))
    conn.commit()
    fetch_data()
    conn.close()
    clear()


# ==============Button==============

btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=18, y=410, width=346, height=120)

add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Arial", 13), width=15,command=add_func)
add_btn.grid(row=0, column=0, padx=2, pady=2)

update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Arial", 13), width=15,command=add_func)
update_btn.grid(row=0, column=1, padx=2, pady=2)

delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Arial", 13), width=15)
delete_btn.grid(row=1, column=0, padx=2, pady=2)

clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("Arial", 13), width=15)
clear_btn.grid(row=1, column=1, padx=3, pady=2)

# =======search==========

search_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, text="Search", bg="lightgrey", font=("Arial", 14))
search_lbl.grid(row=0, column=0, padx=12, pady=2)

search_in = ttk.Combobox(search_frame, font=("Arial", 14), state="readonly")
search_in['values'] = ("Name", "Roll No", "Contact", "Father's Name", "Class", "Section", "D.O.B")
search_in.grid(row=0, column=1, padx=12, pady=2)

search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), bd=9, width=14, bg="lightgrey")
search_btn.grid(row=0, column=2, padx=12, pady=2)

showall_btn = tk.Button(search_frame, text="Show All", font=("Arial", 13), bd=9, width=14, bg="lightgrey")
showall_btn.grid(row=0, column=3, padx=12, pady=2)

# =====================#

# =============Database frame========

main_frame = tk.Frame(data_frame, bg="lightgrey", bd=11, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

student_table = ttk.Treeview(main_frame, columns=("Roll No.", "Name","Class", "Section", "Contact", "Father's Name", "Address","Gender","D.O.B"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

student_table.heading("Roll No.", text="Roll No.")
student_table.heading("Name", text="Name")
student_table.heading("Class", text="Class")
student_table.heading("Section", text="Section")
student_table.heading("Contact", text="Contact")
student_table.heading("Father's Name", text="Father's Name")
student_table.heading("Address", text="Address")
student_table.heading("Gender", text="Gender")
student_table.heading("D.O.B", text="D.O.B")
student_table['show'] = 'headings'

student_table.column("Roll No.",width=100)
student_table.column("Name", width=100)
student_table.column("Class", width=100)
student_table.column("Section", width=100)
student_table.column("Contact",width=100)
student_table.column("Father's Name",width=100)
student_table.column("Address",width=100)
student_table.column("Gender",width=100)
student_table.column("D.O.B",width=100)


student_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)


fetch_data()
student_table.bind("<ButtonRelease-1>",get_cursor)
win.mainloop()
