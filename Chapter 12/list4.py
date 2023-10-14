def main():

    unsort = [ 9, 8, 3, 4, 7, 1]
    print(biggest(unsort))
def biggest(y):
    if y[0] < y[1]:
        y.pop(0)
        biggest(y)
        
    elif y[0] > y[1]:
        y.pop(1)
        biggest(y)
    else: 
        len(y) == 1
        return 0
        

main()