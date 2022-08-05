import cv2
import time
import datetime

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

detection = False
detection_stopped_time = None
timer_started = False
second_to_start_detection = 7

frame_size = (int(cap.get(3)),int(cap.get(4)))
fource = cv2.VideoWriter_fourcc(*"mp4v")
#out = cv2.VideoWriter("video.mp4",fource,20,frame_size)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 9)
    #for (x, y, w, h) in faces_rect:
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    for (x,y,width,height) in faces:
        cv2.rectangle(frame,(x,y),(x+width, y+height),(255,0,0),3)

    if len(faces)> 0 :
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f'{current_time}.mp4', fource, 20, frame_size)
            print("start recording")
    elif detection:
        if timer_started :
            if time.time() - detection_stopped_time >= second_to_start_detection:
                detection = False
                timer_started = False
                out.release()
                print("stop recordning")
        else:
            timer_started = True
            detection_stopped_time = time.time()
    if detection:
        out.write(frame)

    cv2.imshow("frame",frame)
    if cv2.waitKey(1)== ord("q"):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
