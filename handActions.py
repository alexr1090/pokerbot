import pyautogui

def goAllIn():
    """tries to press both all in buttons. Returns 1 if they couldn't be pressed and 0 if all in 2 can be pressed"""
    try:
        allIn1Tup = pyautogui.locateOnScreen("./images/allin.png")

        if allIn1Tup is not None:
            allIn1Click = pyautogui.center(allIn1Tup)
            pyautogui.click(allIn1Click)
            print("clicked all in 1")
    except TypeError as e:
        print ("couldn't find All in 1")

    try:
        allIn3Tup = pyautogui.locateOnScreen("./images/allin3.png",confidence=0.7)
        if allIn3Tup is not None:
            allin3Click = pyautogui.center(allIn3Tup)
            pyautogui.click(allin3Click)
            print ("clicked all in 3")
            return 0
    except TypeError as e:
        print ("couldn't find allin3.png")

    try:
        allIn2Tup = pyautogui.locateOnScreen("./images/allin2.png",confidence=0.7)

        if allIn2Tup is not None:
            allIn2Click = pyautogui.center(allIn2Tup)
            pyautogui.click(allIn2Click)
            print("clicked all in 2")
            return 0
        else:
            print ("couldn't find allin2.png")
            return 1
    except TypeError as e:
        print("couldn't find All in 2")
        return 1

    return 0

def fold():
    """function attempts to click the fold button by attempting to click all of the types of them"""
    try:

        cf_tup = pyautogui.locateOnScreen("./images/cfnow.png")

        if cf_tup is not None:
            cf_click = pyautogui.center(cf_tup)
            pyautogui.click(cf_click)
            print("Clicked cfold")
            pyautogui.moveTo(1,1)
            return()
    except TypeError as e:
        print("couldn't find cfnow.png.")
    try:
        f_tup = pyautogui.locateOnScreen("./images/fold.png")
        if f_tup is not None:

            f_click = pyautogui.center(f_tup)
            pyautogui.click(f_click)
            print("Clicked fold")
            pyautogui.moveTo(1,1)
            return()
    except TypeError as e:
        print("couldn't find fold.png.")

    try:
        fnow_tup = pyautogui.locateOnScreen("./images/foldnow.png", confidence=0.9)
        if fnow_tup is not None:

            fnow_click = pyautogui.center(fnow_tup)
            pyautogui.click(fnow_click)
            print("Clicked fnow")
            pyautogui.moveTo(1,1)
            return()

    except TypeError as e:
        print("couldn't find foldnow.png.")

def clickIamBack():

    try:
        iambackTup = pyautogui.locateOnScreen("./images/iamback.png", confidence=0.9)
        if iambackTup is not None:

            iamback_click = pyautogui.center(iambackTup)
            pyautogui.click(iamback_click)
            print("Clicked I am Back")
            pyautogui.moveTo(1,1)
            return()

    except TypeError as e:
        print("couldn't find iamback.png.")

def click_buyin():
    left = 321
    top = 511
    width = 440
    height = 58

    im = pyautogui.screenshot("./images/card_screens/rebuy_temp.png", region=(left, top, width, height))
    rebuy_tup = pyautogui.locate("./images/buyinafterbust.png", "./images/card_screens/rebuy_temp.png", grayscale=False,
                                confidence=0.9)
    if rebuy_tup is not None:
        rebuy_tup =pyautogui.locateOnScreen("./images/buyinafterbust.png", confidence=0.9)
        rebuy_click = pyautogui.center(rebuy_tup)
        pyautogui.click(rebuy_click)
        print("rebought")
        pyautogui.moveTo(1, 1)
        return ()

