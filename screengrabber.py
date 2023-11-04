# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from python_imagesearch.imagesearch import imagesearch
import pyautogui
import time
"""script used to get screenshots and automatically fold"""

def main():
    """
    get screen location of mouse
       print('Press Ctrl-C to quit.')
        try:
            while True:
                x, y = pyautogui.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                print(positionStr, end='')
                print('\b' * len(positionStr), end='', flush=True)
        except KeyboardInterrupt:
            print('\n')
    """

    def take_screenshot():
        x = 1
        while True:

            try:

                cf_tup = pyautogui.locateOnScreen("./images/cfnow.png")

                if cf_tup is not None:
                    screen_shot = pyautogui.screenshot()
                    screen_shot.save("./images/card_screens/" + str(x) + ".png")
                    cf_click = pyautogui.center(cf_tup)
                    pyautogui.click(cf_click)
                    print("Clicked cfold")
                    x+=1
                    time.sleep(3)
                    continue
            except TypeError as e:
                print("couldn't find cfnow.png.")

            try:
                f_tup = pyautogui.locateOnScreen("./images/fold.png")
                if f_tup is not None:
                    screen_shot = pyautogui.screenshot()
                    screen_shot.save("./images/card_screens/" + str(x) + ".png")
                    f_click = pyautogui.center(f_tup)
                    pyautogui.click(f_click)
                    print("Clicked fold")
                    time.sleep(3)
                    x+=1
                    continue
            except TypeError as e:
                print("couldn't find fold.png.")

            """
                try:

                    print(pyautogui.locateOnScreen("./images/fold.png", confidence=0.9))
                    print("o")
                    pyautogui.click("./images/fold.png",confidence=0.9)

                except TypeError as e: print("couldn't find fold.png")
            """
            try:
                fnow_tup = pyautogui.locateOnScreen("./images/foldnow.png", confidence=0.9)
                if fnow_tup is not None:
                    screen_shot = pyautogui.screenshot()
                    screen_shot.save("./images/card_screens/" + str(x) + ".png")
                    fnow_click = pyautogui.center(fnow_tup)
                    pyautogui.click(fnow_click)
                    print("Clicked fnow")
                    x+=1
                    time.sleep(3)
                    continue
            except TypeError as e:
                print("couldn't find foldnow.png.")

            time.sleep(3)

            print(str(x))

    def search_image():
        pos = imagesearch("./images/test.png")
        if pos[0] != -1:
            print("position : ", pos[0], pos[1])
        else:
            print("image not found")

    take_screenshot()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/