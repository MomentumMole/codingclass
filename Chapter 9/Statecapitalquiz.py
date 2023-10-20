import random
def main():
    val = 0
    no = 'no'
    while val != no:
        print('you will be quized on your states')
        statefun()
        val = str(input("Again? "))
    

def statefun():
    for x in range(1):
        statecap = {'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix',
                    'Arkansas':'Little Rock','California':'Sacramento','Colorado':'Denver',
                    'Connecticut':'Hartford','Delaware':'Dover','Florida':'Tallahassee ',
                    'Georgia':'Atlanta','Hawaii':'Honolulu','Idaho':'Boise','Illinois':'Springfield',
                    'Indiana':'Indianapolis','Iowa':'Des Moines','Kansas':'Topeka',
                    'Kentucky':'Frankfort','Louisiana':'Baton Rouge','Maine':'Augusta',
                    'Maryland':'Annapolis','Massachusetts':'Boston','Michigan':'Lansing',
                    'Minnesota':'Saint Paul','Mississippi':'Jackson','Missouri':'Jefferson City',
                    'Montana':'Helena','Nebraska':'Lincoln','Nevada':'Carson City',
                    'New Hampshire':'Concord','New Jersey':'Trenton','New Mexico':'Santa Fe',
                    'New York':'Albany','North Carolina':'Raleigh','North Dakota':'Bismarck',
                    'Ohio':'Columbus','Oklahoma':'Oklahoma City','Oregon':'Salem',
                    'Pennsylvania':'Harrisburg','Rhode Island':'Providence','South Carolina':'Columbia',
                    'South Dakota':'Pierre','Tennessee':'Nashville','Texas':'Austin',
                    'Utah':'Salt Lake City','Vermont':'Montpelier','Virginia':'Richmond',
                    'Washington':'Olympia' ,'West Virginia':'Charleston','Wisconsin':'Madison',
                    'Wyoming':'Cheyenne',}
        statelist = list(statecap)
        x = 49
        randindex = random.randint(1,x)
        x -= 1
        chosenst = statelist[randindex]
        statequiz = statecap.pop(chosenst, 'stinky')
        print()
        print('what is the capital of',chosenst,'? ')
        Quiziegquess = input()
        if Quiziegquess == statequiz:
            print("you're right the capittal of", chosenst,"is ",statequiz)
        else:
            print(Quiziegquess, 'is not the capittal of', chosenst)
    
main()