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

    background_frame = Frame(self.root,bg = "#cbf3f0")
    background_frame.place(x=0,y=0,width=screen_width,height=screen_height)

    title_size = 70*screen_width
    title_size = int(title_size/1920)
    heading = Label(background_frame ,text = "STUDENT DETAILS",font = ("Berlin Sans FB",title_size),fg= "#2ec4b6",bg = "#cbf3f0")
    heading.place(x=0,y=20,width=screen_width)

    main_frame=Frame(background_frame, bg="#cbf3f0",highlightthickness=20, highlightbackground="#cbf3f0",highlightcolor="#cbf3f0")
    main_frame.place(x=0,y=120,width=screen_width,height=screen_height-140)
    
    #left label fram 
    left_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,bg="#cbf3f0",text=" Student details ",font=("Berlin Sans FB",12,))
    left_frame.place(x=20,y=10,width=700,height=650)

    #right label fram 
    right_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,bg="#cbf3f0",text=" Student details ",font=("Berlin Sans FB",12,))
    right_frame.place(x=740,y=10,width=700,height=650)

    #current corse
    current_course_frame=LabelFrame(left_frame,bd=5,relief=RIDGE,bg="#cbf3f0",text=" current course information ",font=("Berlin Sans FB",12,))
    current_course_frame.place(x=5,y=5,width=680,height=170)

    dep_label=Label(current_course_frame,text=" Department: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
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
    student_info_frame=LabelFrame(left_frame,bd=5,relief=RIDGE,bg="#cbf3f0",text=" student information ",font=("Berlin Sans FB",12,))
    student_info_frame.place(x=5,y=190,width=680,height=200)

    admission_no_label=Label(student_info_frame,text=" Admission number: ",font=("Berlin Sans FB",12,),bg="#cbf3f0")
    admission_no_label.grid(row=0,column=0,padx=5,pady=10,sticky=E)

    admission_no_entry=ttk.Entry(student_info_frame,width=20,font=("Berlin Sans FB",12,))
    admission_no_entry.grid(row=0,column=1,padx=5,pady=10,sticky=E)

    



if __name__=="__main__":
  root=Tk()
  obj=student(root)
  root.mainloop()