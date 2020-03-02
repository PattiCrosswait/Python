import turtle
def draw_square(t, size):
   for i in range(4):
       t.forward(size)
       t.left(90)

def drawSquares(numSquares):

    patti = turtle.Turtle()
    patti.color("hotpink")
    patti.pensize(3)
    sizevar = 20

    for i in range(numSquares):
        draw_square(patti, sizevar)
        sizevar += 20
        patti.penup()
        patti.backward(10)
        patti.right(90)
        patti.forward(10)
        patti.left(90)
        patti.pendown()

def main():
    numSquares = int(input("Enter the number of squares: "))
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    #patti = turtle.Turtle()
    #sizevar = 20
    #draw_square(patti, sizevar)
    drawSquares(numSquares)
    wn.exitonclick()

main()