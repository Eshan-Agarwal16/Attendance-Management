from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
import webbrowser as wb
global screen_width 

#cbf3f0
#2ec4b6 check 1 check 2

def github_link():
    wb.open("https://github.com/Eshan-Agarwal16/Attendance-Management")



class student_attendance_system:

    def __init__(self,root):

        self.root = root
        self.root.title("Attendance Manager")
        #self.root.state('zoomed')
        self.root['background'] = "#cbf3f0"
        self.root.geometry("1536x864+0+0")
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        screen_height = 864
        screen_width = 1536
        print(screen_height,screen_width)
        
        
        main_frame = Frame(self.root,bg = "#cbf3f0")
        main_frame.place(x=0,y=0,width=screen_width,height=screen_height)
        
        #ADDING MAIN LABEL
        title_size = 70*screen_width
        title_size = int(title_size/1920)
        heading = Label(main_frame,text = "ATTENDANCE MANAGEMENT SYSTEM",font = ("Berlin Sans FB",title_size),fg= "#2ec4b6",bg = "#cbf3f0")
        heading.place(x=0,y=0,width=screen_width)

        #BUTTON FRAME
        button_frame = Frame(main_frame,bg = "#cbf3f0")
        x_but_frame = screen_width-800
        x_but_frame = int(x_but_frame/2)
        button_frame.place(x = x_but_frame,y = 300,height = 450,width = 800)
        #BRINGING IMAGES
        student_img = Image.open(r"Assets/student.png")
        developer_img = Image.open(r"Assets/developer.png")
        train_data_img = Image.open(r"Assets/train_data.png")
        photos_img = Image.open(r"Assets/photos.png")
        face_img = Image.open(r"Assets/face.png")
        attendance_img = Image.open(r"Assets/attendance.png")
        
        #resizing images

        student_img = student_img.resize((250,187),Image.ANTIALIAS)
        developer_img = developer_img.resize((250,187),Image.ANTIALIAS)
        train_data_img = train_data_img.resize((250,187),Image.ANTIALIAS)
        photos_img = photos_img.resize((250,187),Image.ANTIALIAS)
        face_img = face_img.resize((250,187),Image.ANTIALIAS)
        attendance_img = attendance_img.resize((250,187),Image.ANTIALIAS)

        #making images usable
        self.student_img_photo = ImageTk.PhotoImage(student_img)
        self.developer_img_photo = ImageTk.PhotoImage(developer_img)
        self.train_data_img_photo = ImageTk.PhotoImage(train_data_img)
        self.photos_img_photo = ImageTk.PhotoImage(photos_img)
        self.face_img_photo = ImageTk.PhotoImage(face_img)
        self.attendance_img_photo = ImageTk.PhotoImage(attendance_img)

        # frame_text = Frame(frame_check1,bg = "white")
        # frame_text.place(x = 0,y = 187.5,width = 250,height =25 ) 


        frame_check1 = Frame(button_frame,bg = "#2ec4b6")
        frame_check1.place(x=0,y=0,width = 250,height = 212.5)

        button_text_1 = Button(frame_check1,command=self.student_detials,text = "Student Info",cursor = "hand2",font = ("Berlin Sans FB",14),relief=FLAT)
        button_text_1.place(x = 0,y = 187.5,width = 250,height =25)

        check_button1 = Button(frame_check1,command=self.student_detials,image = self.student_img_photo,cursor = "hand2",bd = 0 )
        check_button1.place(x=1,y=1)

        frame_check2 = Frame(button_frame,bg = "white")
        frame_check2.place(x=275,y=0,width = 250,height = 212.5)

        button_text_2 = Button(frame_check2,text = "Face Recognition",cursor = "hand2",font = ("Berlin Sans FB",14),relief=FLAT)
        button_text_2.place(x = 0,y = 187.5,width = 250,height =25)
        
        check_button2 = Button(frame_check2,image = self.developer_img_photo,cursor = "hand2",bd = 0 )
        check_button2.place(x=1,y=1)

        frame_check3 = Frame(button_frame,bg = "white")
        frame_check3.place(x=550,y=0,width = 250,height = 212.5)

        button_text_3 = Button(frame_check3,command = self.train,text = "Train Data",cursor = "hand2",font = ("Berlin Sans FB",14),relief=FLAT)
        button_text_3.place(x = 0,y = 187.5,width = 250,height =25)

        check_button3 = Button(frame_check3,command = self.train,image = self.train_data_img_photo,cursor = "hand2",bd = 0 )
        check_button3.place(x=1,y=1)
        
        frame_check4 = Frame(button_frame,bg = "white")
        frame_check4.place(x=0,y=237.5,width = 250,height = 212.5)

        button_text_4 = Button(frame_check4,text = "Github",cursor = "hand2",command = github_link,font = ("Berlin Sans FB",14),relief=FLAT)
        button_text_4.place(x = 0,y = 187.5,width = 250,height =25)

        check_button4 = Button(frame_check4,image = self.photos_img_photo,cursor = "hand2",command = github_link,bd = 0 )
        check_button4.place(x=1,y=1)
        
        frame_check5 = Frame(button_frame,bg = "white")
        frame_check5.place(x=275,y=237.5,width = 250,height = 212.5)

        button_text_5 = Button(frame_check5,text = "Attendance",cursor = "hand2",font = ("Berlin Sans FB",14),relief=FLAT)
        button_text_5.place(x = 0,y = 187.5,width = 250,height =25)

        check_button5 = Button(frame_check5,image = self.face_img_photo,cursor = "hand2",bd = 0 )
        check_button5.place(x=1,y=1)
        
        frame_check6 = Frame(button_frame,bg = "white")
        frame_check6.place(x=550,y=237.5,width = 250,height = 212.5)

        button_text_6 = Button(frame_check6,text = "Help Desk",cursor = "hand2",font = ("Berlin Sans FB",14),relief=FLAT)
        button_text_6.place(x = 0,y = 187.5,width = 250,height =25)

        check_button6 = Button(frame_check6,image = self.attendance_img_photo,cursor = "hand2",bd = 0 )
        check_button6.place(x=1,y=1)

        #ADDING BUTTONS OF MENUs

    #==============function buttons================

    def student_detials(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

        

    



root = Tk()
obj = student_attendance_system(root)
root.mainloop()
