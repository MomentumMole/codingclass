def main():

    rainfall = []
    for x in range(12):
        rain = int(input("enter the amount of rain for all twelve months one at a time: "))
        rainfall.append(rain)
    total = 0
    for x in rainfall:
        total += x 
    average = total / len(rainfall)
    print()
    print(total,"is your total and",average,"is your average")
    print()
    print("your min is", min(rainfall),"and your max is", max(rainfall))
main()