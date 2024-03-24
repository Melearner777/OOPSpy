import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Performance Management System")

title_label = tk.Label(win, text="Student Performance Management System", font=("Cascadia Code SemiBold", 30, "bold"), border=13, relief=tk.GROOVE, bg="Green", foreground="yellow")
title_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Arial Rounded MT Bold", 17), bd=13, relief=tk.GROOVE, bg="lightgrey")
detail_frame.place(x=20, y=90, width=426, height=575)

data_frame = tk.LabelFrame(win, bd=13, bg="lightgrey", relief=tk.GROOVE)
data_frame.place(x=460, y=90, width=813, height=575)

# ==========Entry==========
rollno_lbl=tk.Label(detail_frame,text="Roll No.",font=('Arial',15),bg='lightgrey')
rollno_lbl.grid(row=0,column=0,padx=2,pady=2)

rollno_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15))
rollno_lbl.grid(row=0,column=1,padx=2,pady=2)

name_lbl=tk.Label(detail_frame,text="Name",font=('Arial',15),bg='lightgrey')
name_lbl.grid(row=1,column=0,padx=2,pady=2)

name_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15))
name_lbl.grid(row=1,column=1,padx=2,pady=2)

Class_lbl=tk.Label(detail_frame,text="Class",font=('Arial',15),bg='lightgrey')
Class_lbl.grid(row=2,column=0,padx=2,pady=2)

Class_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15))
Class_lbl.grid(row=2,column=1,padx=2,pady=2)

Section_lbl=tk.Label(detail_frame,text="Section",font=('Arial',15),bg='lightgrey')
Section_lbl.grid(row=3,column=0,padx=2,pady=2)

Section_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15))
Section_lbl.grid(row=3,column=1,padx=2,pady=2)

Contact_lbl=tk.Label(detail_frame,text="Contact",font=('Arial',15),bg='lightgrey')
Contact_lbl.grid(row=4,column=0,padx=2,pady=2)

Contact_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15))
Contact_lbl.grid(row=4,column=1,padx=2,pady=2)

Fathersnme_lbl=tk.Label(detail_frame,text="Father's Name",font=('Arial',15),bg='lightgrey')
Fathersnme_lbl.grid(row=5,column=0,padx=2,pady=2)

Fathersnme_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15))
Fathersnme_lbl.grid(row=5,column=1,padx=2,pady=2)

Address_lbl=tk.Label(detail_frame,text="Address",font=('Arial',15),bg='lightgrey')
Address_lbl.grid(row=6,column=0,padx=2,pady=2)

Address_lbl=tk.Entry(detail_frame,bd=7,font=("Arial",15))
Address_lbl.grid(row=6,column=1,padx=2,pady=2)
# ==============Button==============

btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=18, y=410, width=346, height=120)

add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Arial", 13), width=15)
add_btn.grid(row=0, column=0, padx=2, pady=2)

update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Arial", 13), width=15)
update_btn.grid(row=0, column=1, padx=3, pady=2)

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

student_table = ttk.Treeview(main_frame, columns=("Roll No.", "Name", "Section", "Contact", "Father's Name", "Gender", "D.O.B", "Address"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

student_table.heading("Roll No.", text="Roll No.")
student_table.heading("Name", text="Name")
student_table.heading("Section", text="Section")
student_table.heading("Contact", text="Contact")
student_table.heading("Father's Name", text="Father's Name")
student_table.heading("Gender", text="Gender")
student_table.heading("D.O.B", text="D.O.B")
student_table.heading("Address", text="Address")

student_table['show'] = 'headings'

student_table.column("Roll No.",width=100)
student_table.column("Name", width=100)
student_table.column("Section", width=100)
student_table.column("Contact",width=100)
student_table.column("Father's Name",width=100)
student_table.column("Gender",width=100)
student_table.column("D.O.B",width=100)
student_table.column("Address",width=100)

student_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

win.mainloop()
