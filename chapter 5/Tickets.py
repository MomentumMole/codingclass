def main():
    A = int(input("how many section A tickets sold: "))
    B = int(input("how many section B tickets sold: "))
    C = int(input("how many section C tickets sold: "))
    TicketsSold(A, B, C)

def TicketsSold(x, y, z):
    Atx = x * 20
    Btx = y * 15
    Ctx = z * 10
    incgen = Atx + Btx + Ctx
    print ("the toatal money generated from ticket sales is", incgen, "dollars")


main()