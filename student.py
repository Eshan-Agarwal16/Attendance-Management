from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk

class student:
  def __init__(self,root):

    self.root = root
    self.root.title("Attendance Manager")
    self.root.state('zoomed')
    # self.root.configure(bg="#cbf3f0")

    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()

    background_frame = Frame(self.root)
    background_frame.place(x=0,y=0,width=screen_width,height=screen_height)

    title_size = 70*screen_width
    title_size = int(title_size/1920)
    heading = Label(background_frame ,text = "STUDENT DETAILS",font = ("Berlin Sans FB",title_size),fg= "#2ec4b6",bg = "#cbf3f0",pady=10)
    heading.place(x=0,y=0,width=screen_width)

    main_frame=Frame(background_frame, bg="#cbf3f0",highlightthickness=20, highlightbackground="#cbf3f0",highlightcolor="#cbf3f0")
    main_frame.place(x=0,y=80,width=screen_width,height=screen_height-210)
    
    #left label fram 
    left_frame=LabelFrame(main_frame,bd=0,relief=RIDGE,bg="#cbf3f0",text=" Student details ",font=("Berlin Sans FB",20))
    left_frame.place(x=20,y=15,width=700,height=600)


    #current corse
    current_course_frame=LabelFrame(left_frame,bd=0,relief=RIDGE,bg="#cbf3f0",text=" current course information ",font=("Berlin Sans FB",16))
    current_course_frame.place(x=8,y=20,width=680,height=160)

    dep_label=Label(current_course_frame,text=" Department: ",font=("Berlin Sans FB",12),bg="#cbf3f0")
    dep_label.grid(row=0,column=0,padx=5,pady=20,sticky=E)

    dep_combo=ttk.Combobox(current_course_frame,font=("Berlin Sans FB",12,),width=17, state="read only")
    dep_combo["values"]=("select depratment","computer","electronics","electical","civil","mechanical","chemical")
    dep_combo.current(0)
    dep_combo.grid(row=0,column=1,padx=2,pady=20,sticky=E)

    course_label=Label(current_course_frame,text=" Course: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    course_label.grid(row=0,column=2,padx=5,pady=20,sticky=E) 

    course_combo=ttk.Combobox(current_course_frame,font=("Berlin Sans FB",12,),width=17, state="read only")
    course_combo["values"]=("select course","B.Tech","M.tech","PhD")
    course_combo.current(0)
    course_combo.grid(row=0,column=3,padx=2,pady=20,sticky=E)

    year_label=Label(current_course_frame,text=" Year: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    year_label.grid(row=1,column=0,padx=5,pady=10,sticky=E)

    year_combo=ttk.Combobox(current_course_frame,font=("Berlin Sans FB",12,),width=17, state="read only")
    year_combo["values"]=("select Year","1st","2nd","3rd","4th")
    year_combo.current(0)
    year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=E)

    sem_label=Label(current_course_frame,text=" Semester: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    sem_label.grid(row=1,column=2,padx=5,pady=10,sticky=E)

    sem_combo=ttk.Combobox(current_course_frame,font=("Berlin Sans FB",12,),width=17, state="read only")
    sem_combo["values"]=("select semester","even","odd")
    sem_combo.current(0)
    sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=E)

    #student information
    student_info_frame=LabelFrame(left_frame,bd=0,relief=RIDGE,bg="#cbf3f0",text=" student information ",font=("Berlin Sans FB",16))
    student_info_frame.place(x=8,y=180,width=680,height=230)

    admission_no_label=Label(student_info_frame,text=" Admission number: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    admission_no_label.grid(row=0,column=0,padx=5,pady=(20,10),sticky=E)

    admission_no_entry=ttk.Entry(student_info_frame,width=15,font=("Berlin Sans FB",12,))
    admission_no_entry.grid(row=0,column=1,padx=5,pady=(20,10),sticky=E)

    name_label=Label(student_info_frame,text=" Name: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    name_label.grid(row=0,column=2,padx=5,pady=(20,10),sticky=E)

    name_entry=ttk.Entry(student_info_frame,width=15,font=("Berlin Sans FB",12,))
    name_entry.grid(row=0,column=3,padx=5,pady=(20,10),sticky=E)

    DOB_label=Label(student_info_frame,text=" Date of Birth: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    DOB_label.grid(row=1,column=0,padx=5,pady=10,sticky=E)

    DOB_entry=ttk.Entry(student_info_frame,width=15,font=("Berlin Sans FB",12,))
    DOB_entry.grid(row=1,column=1,padx=5,pady=10,sticky=E)

    email_label=Label(student_info_frame,text=" Email: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    email_label.grid(row=1,column=2,padx=5,pady=10,sticky=E)

    email_entry=ttk.Entry(student_info_frame,width=15,font=("Berlin Sans FB",12,))
    email_entry.grid(row=1,column=3,padx=5,pady=10,sticky=E)

    gender_label=Label(student_info_frame,text=" Gender: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    gender_label.grid(row=2,column=0,padx=5,pady=10,sticky=E)

    gender_combo=ttk.Combobox(student_info_frame,font=("Berlin Sans FB",12,),width=10, state="read only")
    gender_combo["values"]=("select gender","Male","Female","Prefer not to tell")
    gender_combo.current(0)
    gender_combo.grid(row=2,column=1,padx=5,pady=10,sticky=W)
    
    s = ttk.Style()                     # Creating style element
    s.configure('style.TRadiobutton',background="#cbf3f0")

    radio_button_1=ttk.Radiobutton(student_info_frame,text="Sample photo taken",value="Yes",style="style.TRadiobutton")
    radio_button_1.grid(row=3,column=0,pady=20)

    radio_button_2=ttk.Radiobutton(student_info_frame,text="Sample photo not taken",value="Yes",style="style.TRadiobutton")
    radio_button_2.grid(row=3,column=1,pady=20)

    #button frame 1
    btn_frame_1=Frame(left_frame,bd=0,relief=RIDGE,bg="#cbf3f0")
    btn_frame_1.place(x=8,y=420,width=680)

    save_btn=Button(btn_frame_1,text="Save",font=("Berlin Sans FB",12),bg="#2ec4b6",relief=RIDGE,border=2,width=18)
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
    right_frame=LabelFrame(main_frame,bd=0,relief=RIDGE,bg="#cbf3f0",text=" Student details ",font=("Berlin Sans FB",20))
    right_frame.place(x=740,y=15,width=700,height=600)

    #fodder
    main_frame=Frame(background_frame, bg="#2ec4b6")
    main_frame.place(x=0,y=730,width=screen_width,height=screen_height)
    

if __name__=="__main__":
  root=Tk()
  obj=student(root)
  root.mainloop()