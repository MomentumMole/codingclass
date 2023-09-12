def main():

    Choice = int(input('Please input a number on the roulet wheel ranging form 0-36: '))
    
    green = 0
    # red1 = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    # black1 = [2, 4, 6, 8, 10, 11, 13 ,15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    evens1 = (Choice / 2)
    print(evens1)
    evens2 = int(evens1)
    evens2 = int(evens2 * 10) / 10
    print(evens2)
    if evens2 < evens1:
        Odd = Choice
        print(Odd)
    else:
        evens1 == evens2
        even = Choice
        print(even)
    
    if Choice == green:
        print("the pocket is green")
    elif Choice < 0:
        print("Not a number on the wheel")
    elif Choice > 36:
        print("not a number on the wheel")
    elif Odd == Choice:
        if Choice == 1:
            print("the pocket is red")
        elif Choice <= 10:
            print("the pocket is red")
        elif Choice <= 18:
            print("the pocket is red")
        elif Choice <= 28:
            print("the pocket is red")
        else:
            Choice <= 36
            print("the pocket is red")
    else:
        even == Choice
        if Choice <=10:
            print("the pocket is black")
        elif Choice <= 18:
            print("the pocket is black")
        elif Choice <= 28:
            print("the pocket is black")
        else:
            Choice <= 36
            print("the pocket is black")
    
    print(Choice)
   
   
    
    # if Choice == green:
    #     print("the pocket is green")
    # elif Choice < 0:
    #     print("Not a number on the wheel")
    # elif Choice > 36:
    #     print("not a number on the wheel")
    # elif Choice in black1:
    #     print("the pocket is black")
    # else:
    #     Choice in red1
    #     print("the pocket is red")
main()    