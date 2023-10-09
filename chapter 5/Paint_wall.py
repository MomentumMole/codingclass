def main():

    SAwall = int(input("how big is your wall in feet squared? "))
    Paintex = int(input("how much per gallon of paint in dollars? "))
    Cost(SAwall, Paintex)

def Cost(x, Y):
    
    x = x / 112
    galpaint = x
    print("you will need", galpaint, "gallons of paint")
    Time = x * 8
    print("it will take", Time, "hours")
    TCharge = Time * 35
    print("the labor charges will be ", TCharge," dollars")
    TotalCost = TCharge + (galpaint * Y)
    print("the toatal cost for painting the wall will be", TotalCost," dollars")


main()