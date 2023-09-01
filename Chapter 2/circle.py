def main():
    pi = float(3.14159)
    R = float(input("input radius: "))
    area = pi * (R ** 2)
    circumference = 2 * pi * R
    print(area, 'is the area')
    print(circumference, 'is the circumference')


main()