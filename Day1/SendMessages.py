import random
import time

import pyautogui

time.sleep(3)
a = ["Mahesh","Pawan","Charan","Ram"]
count = 0;
n= 10
while count<=n:
    pyautogui.typewrite("answer the call"+random.choice(a))
    pyautogui.press("enter")
    count+=1
