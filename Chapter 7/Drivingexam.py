def main():
    answers = ["A","C","A","A",'D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
    infile = open('studentanswers.txt', 'r')
    studentanswers = infile.readlines()
    infile.close()
    index = 0
    while index < len(studentanswers):
        studentanswers[index] = studentanswers[index].rstrip('\n')
        index += 1
    print(studentanswers)
    correct = 0
    for y in range(20):
        if answers [0] == studentanswers[0]:
            answers.pop(0)
            correct = correct + 1
        elif answers [0] != studentanswers[0]:
            answers.pop(0)
            correct = correct
        else:
            print('what')
    if correct > 15:
        print("good job you passed")
    else:
        print("YOU FAILED")
    


main()