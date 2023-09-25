def main():

    POP = int(input('please give starting population: '))
    POPinc = float(input("please giveaverage daily population increase, give a decimial: "))
    POPinc = POPinc + 1
    Day = int(input("please give the number of days: "))
    DayAprox = 1
    POPr = POP

    print('Day Aproxamate', '\t', 'population' )
    for Day in range(0, Day):
        print(DayAprox, '\t', POPr)
        POP = POP * POPinc
        POPr = POP
        POPr = int(POPr * 1000) / 1000
        DayAprox = DayAprox + 1

main()    