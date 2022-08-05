import cv2
import numpy as np
import playsound
import smtplib
import time
import datetime

cap = cv2.VideoCapture(0)

detection = False
detection_stopped_time = None
timer_started = False
second_to_start_detection = 4

frame_size = (int(cap.get(3)),int(cap.get(4)))
fource = cv2.VideoWriter_fourcc(*"mp4v")

#Email_status = False

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
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            #out = cv2.VideoWriter(f'{current_time}.mp4', fource, 20, frame_size)
            playsound.playsound('alarm.mp3', True)

            print("start recording")
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= second_to_start_detection:
                detection = False
                timer_started = False
                #out.release()
                print("stop recordning")
        else:
            timer_started = True
            detection_stopped_time = time.time()
    #if detection:
        #out.write(frame)

    cv2.imshow("frame",frame)
    #cv2.imshow("mask",mask)
    #cv2.imshow("output", output)
    if cv2.waitKey(100)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
