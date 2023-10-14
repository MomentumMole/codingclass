def main():
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    for x in range(2):
        for i in numbers:
            if i <0 or i >100:
                numbers.remove(i)
    print(numbers)
    total = 0
    for x in numbers:
        total += x 
    average = total / len(numbers)
    print(total,"is your total and",average,"is your average")
main()