def main():
    x = int(input("enter a number: "))
    y = int(input("eneter a number: "))
    print(reapeat(x, y))
    
def reapeat(Num1, counter):
    if counter > 0:
        return Num1 + reapeat(Num1 ,counter - 1)
    else:
        return 0

main()