from PIL import Image
from os import listdir
from os.path import join
def main():
    card1left=63
    card1upper=138
    card1right=93
    card1lower=182

    card2left=103
    card2upper=138
    card2right=130
    card2lower=182
    screenshots = [f for f in listdir("./images/card_screens/")]
    j=1
    for picpath in screenshots:
            im = Image.open("./images/card_screens/"+str(picpath))
            card1 = im.crop((card1left,card1upper,card1right,card1lower))
            card1.save("./images/cards/card"+str(j)+".png")
            j+=1

            card2 = im.crop((card2left,card2upper,card2right,card2lower))
            card2.save("./images/cards/card"+str(j)+".png")
            j+=1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
