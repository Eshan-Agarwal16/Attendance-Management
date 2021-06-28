import os
import numpy as np
from PIL import Image,ImageTk
import cv2

data_dir = ("data")
path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
print(path)
image =  path[0]
img = Image.open(image).convert('L')
ImageNp = np.array(img,'uint8')
print(ImageNp)
while True:
    cv2.imshow("Test",ImageNp)
    if cv2.waitKey(1)==13:
        break