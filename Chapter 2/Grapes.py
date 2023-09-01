def main():
    
    R = int(input('how long is the row: '))
    S = int(input('how much space is inbetween the vines: '))
    E = int(input('how much space is used by end post assembly: '))
    V = (R - (2 * E)) / S
    print(V)
main()    