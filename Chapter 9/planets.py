def main():

    radius = {'Io' : '1821.6', 'Europa' : '1560.8', 'Ganymede' : '2634.1', 'Callisto' : '2410.3'}
    surfacegravity = {'Io' : '1.796', 'Europa' : '1.314', 'Ganymede' : '1.428', 'Callisto' : '1.235'}
    orbitalperiod = {'Io' : '1.769', 'Europa' : '3.551', 'Ganymede' : '7.154', 'Callisto' : '16.689'}
    chosenmoon = str(input('input a Galilean moon of Jupiter: '))
    chr = radius.pop(chosenmoon, 'stinky')
    cho = orbitalperiod.pop(chosenmoon, 'stinky')
    chs = surfacegravity.pop(chosenmoon, 'stinky')
    print('the planet raduis surface gravity and orbital period')
    print(chosenmoon,'raduis is',chr)
    print(chosenmoon,'surface gravity is',chs)
    print(chosenmoon,'orbital period is',cho)


main()