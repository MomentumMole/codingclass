def main():
    FTgrams = int(input("enter the amount of grams of fat: "))
    CRgrams = int(input("enter the amount of grams of Carbs: "))
    CalCR(CRgrams)
    CalFT(FTgrams)
    

def CalFT(x):
    Calfrmft = x * 4
    print("you will have", Calfrmft, "from", x, "grams of fat")
def CalCR(z):
    CalfrmCR = z * 9
    print("you will have", CalfrmCR, "from", z, "grams of carbs")


main()