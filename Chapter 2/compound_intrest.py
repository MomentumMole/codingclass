def main(): 

    N = int(input('Number of times compunded for a year: '))
    R = float(input('Anual intrest rate:'))
    P = float(input('Priniciple amount in account: '))
    T = int(input('Years'))
    A = P * ((1 + (R / N)) ** (N * T))
    print(A)

main()    