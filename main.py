# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from python_imagesearch.imagesearch import imagesearch
import pyautogui
import time
from os import listdir
from os.path import join
from python_imagesearch.imagesearch import *
from scripts import *
from handActions import *
import pytesseract
from PIL import Image

#pytesseract ocr, py2exe, pyinstaller
def main():

    def find_play_hand():
        card_pics = [f for f in listdir("./images/cards/")]
        im = pyautogui.screenshot("./images/card_screens/temp.png", region=(323, 353, 95, 55))
        click_buyin()

        card1found = False
        card2found = False
        card1 = ""
        card2 = ""
        for card in card_pics:
            #imagesearcharea("./images/cards/"+str(card),
            #print (str(card))


            #card_tup = pyautogui.locateOnScreen("./images/cards/"+str(card), confidence=0.9)
            card_tup = pyautogui.locate("./images/cards/" + str(card), "./images/card_screens/temp.png", grayscale=False, confidence=0.9)
            if card_tup is not None and card1found is False:
                print ("card 1 found, " + str(card))
                card1found = True
                card1 = str(card)
            elif card_tup is not None and card1found is True:
                print ("card 2 found, "+ str(card))
                card2found = True
                card2 = str(card)
                break
        if card1found is True and card2found is True:
            print("both cards found")
            card1List = [*card1]
            card2List = [*card2]
            if card1List[0] == 'a':
                if card2List[0] == 'a' or card2List[0] == 'k':
                    while goAllIn() != 0: continue
                    time.sleep(15)
                    rathole()
                else: fold()
            elif card1List[0] == 'k':
                if card2List[0] == 'k':
                    while goAllIn() != 0: continue
                    time.sleep(15)
                    rathole()
                elif card2List[0] == 'a':
                    while goAllIn() != 0: continue
                    time.sleep(15)
                    rathole()
                else: fold()
            elif card1List[0] == 'q' and card2List[0] == 'q':
                while goAllIn() != 0: continue
                time.sleep(15)
                rathole()
            elif card1List[0] == 'j' and card2List[0] == 'j':
                while goAllIn() != 0: continue
                time.sleep(15)
                rathole()
            else: fold()
        else: fold()

    screenshotcount = 4
    while 1:
        find_play_hand()
        clickIamBack()
        #click buy chips, screenshot it, save screenshot
        time.sleep(4)

        getBuyChipsScreenShot()
        pyautogui.click(102,523) #click buy to autorebuy
        #print(str(pytesseract.image_to_string(Image.open("./images/tempscreens/temp.png")))[-1:])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
