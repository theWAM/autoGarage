import os, time
# import pyautogui as pag

def runInTerminal(arg):
    arr = arg.split("^^")
    for args in arr:
        os.system(args)
        # time.sleep(2)

arg = "cd ~/Documents/dev/autoGarage^^pwd^^python3 ~/Documents/dev/autoGarage/autoRun.py"

runInTerminal(arg)