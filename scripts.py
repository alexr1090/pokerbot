"""scripts created to help the program collect data. May or may not be used in final project"""
import pyautogui
import time

def screenCropLocateandClick(left,top,width,height, tempSavePath, imageToFindPath ):
    """script to click buy_chips"""
    im = pyautogui.screenshot(tempSavePath, region=(left, top, width, height))
    found_tup = pyautogui.locate(imageToFindPath, tempSavePath, grayscale=False,
                                 confidence=0.9)
    try:
        if found_tup is not None:
            found_tup = pyautogui.locateOnScreen("./images/buy_chip_tmp.png", confidence=0.9)
            found_click = pyautogui.center(found_tup)
            pyautogui.click(found_click)
            print("clicked"+ imageToFindPath)
            pyautogui.moveTo(1, 1)

        else: print (imageToFindPath +" not found.")
    except TypeError as e: print (imageToFindPath+" not found.")

def getBuyChipsScreenShot():
    """script for getting screenshots of numbers for buy chips"""
    screenCropLocateandClick(20,541,178,44,"./images/buy_chip_tmp.png","./images/buychips.png")
    time.sleep(1)
    im = pyautogui.screenshot("./images/tempscreens/temp.png",region=(117,454,55,46))
    #count+=1

def rathole():
    """script to close out of the game window (if it's in default position) and re-enter from lobby"""
    #click x to close out, click apporpriate table to enter, click ok
    pyautogui.click(945,16) #x (close) for default screen location
    pyautogui.click(383,331)
    time.sleep(2)
    pyautogui.doubleClick(944,578)  #default 2/5c game
    time.sleep(1)
    pyautogui.click(910,618) #ok button after double clicking game

