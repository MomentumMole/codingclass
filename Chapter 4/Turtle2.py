def main():
    import turtle
    turtle.speed(1000)
    turtle.hideturtle()
    turtle.penup()
    turtle.forward(339)
    turtle.right(90)
    turtle.forward(315)
    turtle.pendown()
 
    turtle.left(90)
    z = 5
    y = z

    for x in range(129):

        for x in range(2):
            turtle.forward(y)
            turtle.right(90)
        y = y + z
        for x in range(1):
            for x in range(2):
                turtle.forward(y)
                turtle.right(90)

    Y = y - z
    turtle.forward(y)
    turtle.right(90)
    turtle.forward(Y)
    turtle.right(90)
    turtle.forward(z)
    turtle.left(90)
    turtle.forward(z)
    
    
    

    turtle.exitonclick()
main()