from pywinauto.application import Application
from PIL import ImageGrab
import time
import pyautogui

app = Application(backend='uia').start("button_test_exe.exe")
window = app["button_test_exe"]

count = 0
f=open(".\\steps\\1","w")
while True:
    try:
        time.sleep(2)
        button_name = window.descendants()[0].window_text()
    except:
        print("end .....")
        break
    else:
        im = ImageGrab.grab((150, 150, 1200, 600))
        im.save("./images/" + str(count) + ".png")
        print(button_name+"....")
        f.write(button_name+"\n")
        count += 1
        pyautogui.click(200, 200)

        #DEFSPLITBUTTON can not by click
        # try:
        #     window[button_name].click()
        # except:
        #     print("ignore click error")


f.close()


