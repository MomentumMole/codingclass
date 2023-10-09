def main():

    km = int(input("please enter distance in killometers: "))
    MtKm(km)

def MtKm(x):

    mi = x * 0.6214
    print("the distance is", mi, "miles")

main()    