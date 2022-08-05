import cv2
import numpy as np

vid_0 = cv2.VideoCapture(0)
vid_1 = cv2.VideoCapture(1)

while True:
    ret0, frame0 = vid_0.read()
    ret1, frame1 = vid_1.read()

    hsv0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2HSV)
    hsv1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 0, 247])
    higher_red = np.array([255, 255, 255])

    mask = cv2.inRange(hsv0, lower_red, higher_red)
    image_binary = cv2.inRange(hsv0, lower_red, higher_red)
    check_if_fire_detected = cv2.countNonZero(image_binary)

    mask1 = cv2.inRange(hsv1, lower_red, higher_red)
    image_binary1 = cv2.inRange(hsv1, lower_red, higher_red)
    check_if_fire_detected1 = cv2.countNonZero(image_binary1)



    print(int(check_if_fire_detected))
    if int(check_if_fire_detected) >= 5000:
        cv2.putText(frame0, "Fire Detected !", (100, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    print(int(check_if_fire_detected1))
    if int(check_if_fire_detected1) >= 5000:
        cv2.putText(frame1, "Fire Detected !", (100, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    #if (ret0):
    cv2.imshow("cam 0",frame0)
    cv2.imshow("mask1",mask)
    #if (ret1):
    cv2.imshow("cam1",frame1)
    cv2.imshow("mask1", mask1)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
vid_0.release()
vid_1.release()
cv2.destroyAllWindows()