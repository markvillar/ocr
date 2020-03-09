import cv2 
import pytesseract
import pyttsx3

camera = cv2.VideoCapture(0)

engine = pyttsx3.init()

while(True):
    
    ret, frame = camera.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    
    cv2.imshow('Window', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('r'):
        text = pytesseract.image_to_string(frame)
        print(text)
        engine.say(text)
        engine.runAndWait()
        continue

camera.release()
cv2.destroyAllWindows()