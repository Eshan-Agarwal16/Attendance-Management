from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
  def __init__(self,root):
    
    self.root = root
    self.root.title("Attendance Manager")
    self.root.state('zoomed')

    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()
    self.root.configure(bg="#cbf3f0")

    # screen_width = self.root.winfo_screenwidth()
    # screen_height = self.root.winfo_screenheight()

    background_frame = Frame(self.root,bg="#cbf3f0")
    background_frame.place(x=0,y=0,width=screen_width,height=screen_height)
    background_frame.grid_columnconfigure(0, weight=1)
    background_frame.grid_columnconfigure(2, weight=1)
    background_frame.grid_rowconfigure(1, weight=1)
    background_frame.grid_rowconfigure(3, weight=1)

    title_size = 70*screen_width
    title_size = int(title_size/1920)
    heading = Label(background_frame ,text = "TRAIN DATA",font = ("Berlin Sans FB",title_size),fg= "#2ec4b6",bg = "#cbf3f0",pady=10)
    heading.grid(row=0,column=1)

    train_data_btn=Button(background_frame,command=self.train_classifier,text="Train Data",font=("Berlin Sans FB",12),bg="#2ec4b6",relief=RIDGE,border=2,width=18)
    train_data_btn.grid(row=2,column=1)
    

  def train_classifier(self):
    data_dir=("Data")
    path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

    faces=[]
    ids=[]

    for image in path:
      img=Image.open(image).convert('L') #grey scale convertion
      imageNp=np.array(img,'uint8')
      id=int(os.path.split(image)[1].split('.')[1])

      faces.append(imageNp)
      ids.append(id)
      cv2.imshow("Training",imageNp)
      cv2.waitKey(1)==13
    ids=np.array(ids)

    #======================= training the classifier and storing data =================
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("classifier.xml")
    cv2.destroyAllWindows()
    messagebox.showinfo("Result","Training data set completed!")





if __name__=="__main__":
  root=Tk()
  obj=Train(root)
  root.mainloop()