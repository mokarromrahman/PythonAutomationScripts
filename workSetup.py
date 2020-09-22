import pyautogui
import sys
import time

# print the position of the mouse


def printMousePosition():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')


# go to the google chrome icon and right click it
pyautogui.rightClick(132, 1059)
# left click new window
pyautogui.leftClick(170, 921)
# wait 2 seconds for chrome to open
time.sleep(2)
# make sure the window is full screen
pyautogui.hotkey('winleft', 'up')
# wait 1 seconds
time.sleep(1)
# left click the ualberta tile
pyautogui.leftClick(3155, 172)
# wait 2 seconds
time.sleep(2)
# left click on the email and apps option
# this option is for when their is a banner at the top of the screen (ie COVID-19 info banner at the top of ualberta site in Sept 2020)
# if this does not work, then it means that there is a banner and the 2nd one should be clicked just in case
pyautogui.leftClick(3411, 168)
# this is the option for no banner
pyautogui.leftClick(3404, 98)
# wait 2 seconds for new tab to open
time.sleep(2)
# middle click the email, calendar and the google drive icons
pyautogui.middleClick(2420, 342)  # email
pyautogui.middleClick(2772, 329)  # calendar
pyautogui.middleClick(2588, 501)  # drive
# sleep for 2 seconds and wait for the tabs to open
time.sleep(2)
# close the unneeded tabs
pyautogui.middleClick(2269, 14)
pyautogui.middleClick(2043, 19)
# open asana
# sleep for 2 seconds and wait for the tabs to open
time.sleep(2)
pyautogui.leftClick(2669, 19)  # new tab
# sleep for 2 seconds and wait for the tab to open
time.sleep(2)
pyautogui.leftClick(2620, 448)  # asana tile
# open discord and slack
pyautogui.leftClick(652, 1060)  # discord
pyautogui.leftClick(761, 1060)  # slack
# printMousePosition()
