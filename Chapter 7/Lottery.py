import random 
def main():
    lottrery = []
    for x in range(7):
        lotnum = random.randint(0,9)
        lottrery.append(lotnum)
    y = len(lottrery)
    for x in range(y):
        print(lottrery[x])
        
main()