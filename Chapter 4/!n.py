def main():

    n = int(input("pick any integer: "))
    n = n ** 2
    n = n ** .5
    n = int(n)
    print(n)
    num =1 

    
    while n > 1:
        num *= (n)
        n = n - 1
    
    print(num)
        

main()    