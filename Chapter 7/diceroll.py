import random
def main():
    dice = []
    number_of_throws = int(input("how many throws? "))
    for x in range(number_of_throws):
        numbers = random.randint(1,6)
        dice.append(numbers)
    dice.sort()
    print(dice)


main()