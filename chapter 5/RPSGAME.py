import random

numgames = 1
def main():
    game()

def random_number():
        Challenger = random.randint(1 , 3)
        return Challenger
def game():
    Player = str(input("please chose rock paper or scissors: "))
    Opponet = random_number()
    if Player == "rock":
        Player = 1
    elif Player == "paper":
        Player = 2
    else:
        Player = 3

    if Player == Opponet:
        print ("TIE! play agin to detrmine a winner")
        main()
    elif Player > Opponet:
        #player = 3 opponet = 2
        #player = 2 opponet = 1
        #player = 3 oppnnet = 1
        Opponet = Opponet + 1
        if Player == Opponet:
            if Player == 3:
                print("Scissors cuts paper.")
            else:
                print("Paper wraps rock")
        else:
            print("Rock smashes scissors.")
    else:
        Player < Opponet
            #player = 1 opponent = 2
            #player = 1 opponet = 3
            #player = 2 oppent = 3
        Opponet = Opponet - 1
        if Player == Opponet:
            if Player == 1:
                print("Paper wraps rock")
            else:
                print("Scissors cuts paper.")
        else:
            print("Rock smashes scissors.")
    Again = str(input("Play again? yes? no? "))
    if Again == "yes":
        play_again()
    else:
        print("thanks for playing")
        
  
def play_again():
    numgames = numgames + 2 
    print("best of", numgames)
    main()

main()