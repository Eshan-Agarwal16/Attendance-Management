from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
  def __init__(self,root):

    self.root = root
    self.root.title("Attendance Manager")
    self.root.state('zoomed')

    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()
    # self.root.configure(bg="#cbf3f0")

    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()

    background_frame = Frame(self.root)
    background_frame.place(x=0,y=0,width=screen_width,height=screen_height)

    title_size = 70*screen_width
    title_size = int(title_size/1920)
    heading = Label(background_frame ,text = "STUDENT DETAILS",font = ("Berlin Sans FB",title_size),fg= "#2ec4b6",bg = "#cbf3f0",pady=10)
    heading.place(x=0,y=0,width=screen_width,height=90)

    #variables declare
    self.var_id = StringVar()
    self.var_name = StringVar()
    self.var_gen = StringVar()
    self.var_dob = StringVar()
    self.var_dept = StringVar()
    self.var_course = StringVar()
    self.var_year = StringVar()
    self.var_sem = StringVar()
    self.var_email = StringVar()

    main_frame=Frame(background_frame, bg="#cbf3f0",highlightthickness=20, highlightbackground="#cbf3f0",highlightcolor="#cbf3f0")
    main_frame.place(x=0,y=80,width=screen_width,height=screen_height-210)
    
    #left label fram 
    left_frame=LabelFrame(main_frame,bd=0,relief=RIDGE,bg="#cbf3f0",text=" Student details ",font=("Berlin Sans FB",20))
    left_frame.place(x=20,y=15,width=700,height=580)


    #current corse
    current_course_frame=LabelFrame(left_frame,bd=0,relief=RIDGE,bg="#cbf3f0",text=" current course information ",font=("Berlin Sans FB",16))
    current_course_frame.place(x=8,y=20,width=680,height=160)

    dep_label=Label(current_course_frame,text=" Department: ",font=("Berlin Sans FB",12),bg="#cbf3f0")
    dep_label.grid(row=0,column=0,padx=5,pady=20,sticky=E)

    dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=("Berlin Sans FB",12,),width=17, state="read only")
    dep_combo["values"]=("select depratment","computer","electronics","electical","civil","mechanical","chemical")
    dep_combo.current(0)
    dep_combo.grid(row=0,column=1,padx=2,pady=20,sticky=E)

    course_label=Label(current_course_frame,text=" Course: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    course_label.grid(row=0,column=2,padx=5,pady=20,sticky=E) 

    course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Berlin Sans FB",12,),width=17, state="read only")
    course_combo["values"]=("select course","B.Tech","M.tech","PhD")
    course_combo.current(0)
    course_combo.grid(row=0,column=3,padx=2,pady=20,sticky=E)

    year_label=Label(current_course_frame,text=" Year: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    year_label.grid(row=1,column=0,padx=5,pady=10,sticky=E)

    year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Berlin Sans FB",12,),width=17, state="read only")
    year_combo["values"]=("select Year","1st","2nd","3rd","4th")
    year_combo.current(0)
    year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=E)

    sem_label=Label(current_course_frame,text=" Semester: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    sem_label.grid(row=1,column=2,padx=5,pady=10,sticky=E)

    sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("Berlin Sans FB",12,),width=17, state="read only")
    sem_combo["values"]=("select semester","even","odd")
    sem_combo.current(0)
    sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=E)

    #student information
    student_info_frame=LabelFrame(left_frame,bd=0,relief=RIDGE,bg="#cbf3f0",text=" student information ",font=("Berlin Sans FB",16))
    student_info_frame.place(x=8,y=180,width=680,height=230)

    admission_no_label=Label(student_info_frame,text=" Admission number: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    admission_no_label.grid(row=0,column=0,padx=5,pady=(20,10),sticky=E)

    admission_no_entry=ttk.Entry(student_info_frame,textvariable=self.var_id,width=15,font=("Berlin Sans FB",12,))
    admission_no_entry.grid(row=0,column=1,padx=5,pady=(20,10),sticky=E)

    name_label=Label(student_info_frame,text=" Name: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    name_label.grid(row=0,column=2,padx=5,pady=(20,10),sticky=E)

    name_entry=ttk.Entry(student_info_frame,textvariable=self.var_name,width=15,font=("Berlin Sans FB",12,))
    name_entry.grid(row=0,column=3,padx=5,pady=(20,10),sticky=E)

    DOB_label=Label(student_info_frame,text=" Date of Birth: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    DOB_label.grid(row=1,column=0,padx=5,pady=10,sticky=E)

    DOB_entry=ttk.Entry(student_info_frame,textvariable=self.var_dob,width=15,font=("Berlin Sans FB",12,))
    DOB_entry.grid(row=1,column=1,padx=5,pady=10,sticky=E)

    email_label=Label(student_info_frame,text=" Email: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    email_label.grid(row=1,column=2,padx=5,pady=10,sticky=E)

    email_entry=ttk.Entry(student_info_frame,textvariable=self.var_email,width=15,font=("Berlin Sans FB",12,))
    email_entry.grid(row=1,column=3,padx=5,pady=10,sticky=E)

    gender_label=Label(student_info_frame,text=" Gender: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    gender_label.grid(row=2,column=0,padx=5,pady=10,sticky=E)

    gender_combo=ttk.Combobox(student_info_frame,textvariable=self.var_gen,font=("Berlin Sans FB",12,),width=10, state="read only")
    gender_combo["values"]=("select gender","Male","Female")
    gender_combo.current(0)
    gender_combo.grid(row=2,column=1,padx=5,pady=10,sticky=W)
    
    # s = ttk.Style()                     # Creating style element
    # s.configure('style.TRadiobutton',background="#cbf3f0")

    # radio_button_1=ttk.Radiobutton(student_info_frame,text="Sample photo taken",value="Yes",style="style.TRadiobutton")
    # radio_button_1.grid(row=3,column=0,pady=20)

    # radio_button_2=ttk.Radiobutton(student_info_frame,text="Sample photo not taken",value="Yes",style="style.TRadiobutton")
    # radio_button_2.grid(row=3,column=1,pady=20)

    #button frame 1
    btn_frame_1=Frame(left_frame,bd=0,relief=RIDGE,bg="#cbf3f0")
    btn_frame_1.place(x=8,y=420,width=680)

    save_btn=Button(btn_frame_1,text="Save",command = self.add_data,font=("Berlin Sans FB",12),bg="#2ec4b6",relief=RIDGE,border=2,width=18)
    save_btn.grid(row=0,column=0)

    update_btn=Button(btn_frame_1,text="Update",font=("Berlin Sans FB",12),bg="#2ec4b6",relief=RIDGE,border=2,width=17)
    update_btn.grid(row=0,column=1)

    reset_btn=Button(btn_frame_1,text="Reset",font=("Berlin Sans FB",12),bg="#2ec4b6",relief=RIDGE,border=2,width=17)
    reset_btn.grid(row=0,column=2)

    delete_btn=Button(btn_frame_1,text="Delete",font=("Berlin Sans FB",12),bg="#2ec4b6",relief=RIDGE,border=2,width=18)
    delete_btn.grid(row=0,column=3)


    #button frame 2
    btn_frame_2=Frame(left_frame,bd=0,relief=RIDGE,bg="#cbf3f0")
    btn_frame_2.place(x=8,y=455,width=680,height=40)

    take_photo_btn=Button(btn_frame_2,text="Take Photo Samples",font=("Berlin Sans FB",12),bg="#2ec4b6",relief=RIDGE,border=2,width=36)
    take_photo_btn.grid(row=0,column=0)

    update_photo_btn=Button(btn_frame_2,text="Update Photo Samples",font=("Berlin Sans FB",12),bg="#2ec4b6",relief=RIDGE,border=2,width=36)
    update_photo_btn.grid(row=0,column=1)

    #right label fram 
    right_frame=LabelFrame(main_frame,bd=0,relief=RIDGE,bg="#cbf3f0",text=" Student data ",font=("Berlin Sans FB",20))
    right_frame.place(x=740,y=15,width=700,height=580)

    #===========search system================
    search_frame=LabelFrame(right_frame,bd=0,relief=RIDGE,bg="#cbf3f0",text=" Search data ",font=("Berlin Sans FB",16))
    search_frame.place(x=8,y=15,width=680,height=130)

    search_label=Label(search_frame,text=" Search By: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    search_label.grid(row=0,column=0,padx=5,pady=(20,10),sticky=E)

    search_combo=ttk.Combobox(search_frame,font=("Berlin Sans FB",12,),width=10, state="read only")
    search_combo["values"]=("select","Admission number","Name")
    search_combo.current(0)
    search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

    search_entry=ttk.Entry(search_frame,width=15,font=("Berlin Sans FB",12))
    search_entry.grid(row=0,column=2,padx=5,pady=10,sticky=E)

    btn_frame_3=Frame(search_frame,bd=0,relief=RIDGE,bg="#cbf3f0")
    btn_frame_3.place(x=8,y=60,width=660,height=40)

    search_btn=Button(btn_frame_3,text="Search",font=("Berlin Sans FB",12),bg="#2ec4b6",relief=RIDGE,border=2,width=15)
    search_btn.grid(row=0,column=0,padx=(5,140))

    show_all_btn=Button(btn_frame_3,text="Show all",font=("Berlin Sans FB",12),bg="#2ec4b6",relief=RIDGE,border=2,width=15)
    show_all_btn.grid(row=0,column=1,padx=(140,5))


    #===================table frame===================
    table_frame=Frame(right_frame,bd=0,relief=RIDGE,bg="#cbf3f0")
    table_frame.place(x=8,y=170,width=680,height=320)

    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

    self.student_table=ttk.Treeview(table_frame,column=("adm_no","name","gender","DOB","dep","course","year","sem","email","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=self.student_table.xview)
    scroll_y.config(command=self.student_table.yview)

    self.student_table.heading("adm_no",text="Admission no")
    self.student_table.heading("name",text="Name")
    self.student_table.heading("gender",text="Gender")
    self.student_table.heading("DOB",text="DOB")
    self.student_table.heading("dep",text="Department")
    self.student_table.heading("course",text="Course")
    self.student_table.heading("year",text="Year")
    self.student_table.heading("sem",text="Semester")
    self.student_table.heading("email",text="Email")
    self.student_table.heading("photo",text="Photo sample status")
    self.student_table["show"]="headings"

    self.student_table.column("adm_no",width=100)
    self.student_table.column("name",width=100)
    self.student_table.column("gender",width=100)
    self.student_table.column("DOB",width=100)
    self.student_table.column("dep",width=100)
    self.student_table.column("course",width=100)
    self.student_table.column("year",width=100)
    self.student_table.column("sem",width=100)
    self.student_table.column("email",width=100)
    self.student_table.column("photo",width=150)

    self.student_table.pack(fill=BOTH,expand=1)




    #fodder
    fodder_frame=Frame(background_frame, bg="#2ec4b6")
    fodder_frame.place(x=0,y=screen_height-160,width=screen_width,height=screen_height)
  
  #===========FUNCTION DECLARATION==============  
  def add_data(self):
    if self.var_dept.get() == "select depratment" or self.var_course.get() == "select course" or self.var_year.get() == "select Year" or self.var_sem.get() == "select semester":
      messagebox.showerror("Error","All the Fields are required")
    elif self.var_email.get == "" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_dob.get() == "" or self.var_gen.get() == "select gender" :
      messagebox.showerror("Error","All the Fields are required")
    else:
      conn = mysql.connector.connect(host = "localhost",user = 'root',password = '1234' , database = "attendance_manager")
      my_cursor = conn.cursor()
      



if __name__=="__main__":
  root=Tk()
  obj=Student(root)
  root.mainloop()