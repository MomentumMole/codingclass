def main():

    Cpeople = int(input("How many people are coming to the cookout? :"))
    Cdawgs = int(input('how many hot dogs will people have? :'))
    Hpack = 10
    Hbun = 8
    Htotal = Cpeople * Cdawgs
    print(Htotal)
    Hbneeded = int(Htotal / Hbun)
    print (Hbneeded)
    N = Hbneeded + 1
    N = int(N * 10) / 10
    if Hbneeded <= N:
        
        print("you need", N, "pack of hot dog buns")
    
    Hpneeded = int(Htotal / Hpack)
    print(Hpneeded)
    X = Hpneeded + 1
    X = int(X * 10) / 10
    if Hpneeded <= X:
        
        print("you need", X, "pack of hot dogs")

main()