import pyautogui
import time
pyautogui.FAILSAFE = True

try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse Position :  x - {x},Y - {y}")
        
        pyautogui.moveTo(100,100,duration=0.5)
        time.sleep(0.5)

except pyautogui.FailSafeException:
    print('Caught a FailSafeException, exiting. . .')