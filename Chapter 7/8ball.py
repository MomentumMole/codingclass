import random
def main():
    question = str(input("please give me a yes or no question and I will advise you: "))
    infile = open('8_ball_responses.txt', 'r')
    querryresult = infile.readlines()
    infile.close()
    index = 0
    while index < len(querryresult):
        querryresult[index] = querryresult[index].rstrip('\n')
        index += 1
    ballchoice = 0
    #random.randint(0,11)
    answer = querryresult[ballchoice]
    print(answer)
main()