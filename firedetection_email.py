import cv2
import numpy as np
import playsound
import smtplib

cap = cv2.VideoCapture(0)

fire_report = 0
Alarm_status = False
Email_status = False

def play_audio():
    while True:
        playsound.playsound('alarm.mp3',True)

def sent_email():
    recipientEmail = "7003977@gmail.com"
    recipientEmail = recipientEmail.lower()
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("8001572@gmail.com", 'nmviahzfogghfkdt')
        server.sendmail('8001572@gmail.com', recipientEmail, "Warning A Fire Accident has been reported on ABC Company")
        print("sent to {}".format(recipientEmail))
        server.close()
    except Exception as e:
        print(e)

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    blur = cv2.GaussianBlur(frame,(15,15),0)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    lower = [ 18,50,50]
    upper = [35,255,255]

    lower = np.array(lower,dtype='uint8')
    upper = np.array(upper,dtype='uint8')
    mask = cv2.inRange(hsv,lower,upper)
    output = cv2.bitwise_and(frame,hsv,mask=mask)
    number_fire = cv2.countNonZero(mask)
    print(int(number_fire))

    if int(number_fire)> 15000:
        fire_report = fire_report +1
    if fire_report >= 1:
        if Alarm_status == False:
            sent_email()
            play_audio()
            Alarm_status = True


    #cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    #cv2.imshow("output", output)
    if cv2.waitKey(100)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()