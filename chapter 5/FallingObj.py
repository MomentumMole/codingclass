def main():
    z = 0
    for x in range(10):
        z = z + 1
        falling_distance(z)

def falling_distance(t):
    g = 9.8
    d = g/2 * (t * t)
    d = int(d * 10)/10
    print(d)


main()