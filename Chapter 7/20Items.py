def main():

    series = []
    for x in range(12):
        rain = int(input("enter all 20 items one at a time: "))
        series.append(rain)
    total = 0
    for x in series:
        total += x 
    average = total / len(series)
    print()
    print(total,"is your total and",average,"is your average")
    print()
    print("your lowest number is", min(series),"and your biggest number is", max(series))
main()