import cv2

def classify(img):
    gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    all_cordi = face_classifier.detectMultiScale(gray_img,1.2,5)
    for (x,y,w,h) in all_cordi:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    return img

video = cv2.VideoCapture(0)

while True:
    _,img = video.read()
    img = classify(img)
    cv2.imshow("Face detection",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
    