def main():

    DY = int(input("how many days are you working? "))
    CurDY = 1
    Money = 0.01
    
    print("Days\tMoney")
        
       
    
    for CurDY in range(CurDY, DY):
        print(CurDY, '\t', Money)
        Money = Money * 2
        CurDY = CurDY + 1
        
        
main()    