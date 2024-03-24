
btn_frame=tk.Frame(detail_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
btn_frame.place(x=18,y=390,width=346,height=120)

add_btn=tk.Button(btn_frame,bg="lightgrey",text="Add",bd=7,font=("Arial",13),width=15)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn=tk.Button(btn_frame,bg="lightgrey",text="Update",bd=7,font=("Arial",13),width=15)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn=tk.Button(btn_frame,bg="lightgrey",text="Delete",bd=7,font=("Arial",13),width=15)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn=tk.Button(btn_frame,bg="lightgrey",text="Clear",bd=7,font=("Arial",13),width=15)
clear_btn.grid(row=1,column=1,padx=3,pady=2)