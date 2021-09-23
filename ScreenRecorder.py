import cv2
import numpy as np
import pyautogui
ScreenSize = (1920,1080)
Fourcc = cv2.VideoWriter_fourcc(*"XVID")
Output = cv2.VideoWriter("output.avi",Fourcc,20.0, (ScreenSize))
while True:
    Image = pyautogui.screenshot()
    Frame = np.array(Image)
    Frame = cv2.cvtColor(Frame,cv2.COLOR_BGR2RGB)
    Output.write(Frame)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
Output.release()