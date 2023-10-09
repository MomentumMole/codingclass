def main(): 
    M = int(input("enter object mass: "))
    V = int(input("enter object volicity: "))
    kenetic_energy(M, V)

def kenetic_energy(m , v):
    KE = (m * (v * v)) / 2
    print(KE)


main()