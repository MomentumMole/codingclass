def main():

    month = int(input('What month is it: '))
    day = int(input('What day is it: '))
    year = int(input('What are the last two digits of the year: '))

    MJ = month * day
    
    if year == MJ:
        print()
        print('Horray your date is magic * * * *')
    else:
        print()
        print('its not magic')

main()    