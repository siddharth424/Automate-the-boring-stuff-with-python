import pyautogui, time
print("Press ENTER to begin. Press Ctrl-C to quit")
input()
try:
    while True:
        pyautogui.move(5,0,duration=0.25)
        time.sleep(10)
        pyautogui.move(-5,0,duration=0.25)
        time.sleep(10)
except KeyboardInterrupt:
        print("Stopped")

