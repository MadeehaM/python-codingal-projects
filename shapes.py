import turtle

turtle.Screen().bgcolor("white")
turtle.screensize(1000,300)
turtle.title("Shapes")
board=turtle.Turtle()
board.speed('slow')
board.pencolor('blue')

for i in range(3):
    board.forward(200)
    board.left(120)
    i=i+1