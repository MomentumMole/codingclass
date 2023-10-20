def main():

    unsort = [ 9, 8, 3, 4, 7, 1]
    print(biggest(unsort))
def biggest(y):
    if len(y) > 2:
        if y[0] < y[1]:
            y.remove(y[0])
            biggest(y)
        elif y[0] > y[1]:
            y.remove(y[1])
            biggest(y)
        else: 
            len(y) == 1
            print("Done")
    else:
        if y[0] > y[1]:
            print(y[0])
        else:
            print(y[1])
main()