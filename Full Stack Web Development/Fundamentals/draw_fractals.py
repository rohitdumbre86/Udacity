import turtle


def draw_triangle(x,y, length, tuts) :
  
  tuts.begin_fill()
  tuts.setpos(x,y)

  for i in range(1,4):
    tuts.fd(length)
    tuts.left(120)

  tuts.end_fill()

def draw_inverse_triangle(x,y,length, tuts):
  
  tuts.begin_fill()
  tuts.left(60)

  tuts.setpos(x,y)

  for i in range(1,3):
    tuts.fd(length)
    tuts.left(120)

  tuts.fd(length)
  tuts.end_fill()


def initialize_turtle(shape,color):
  
  tuts = turtle.Turtle()
  tuts.shape(shape)
  tuts.color(color)
  tuts.hideturtle()  
  return tuts
    
def draw_fractals(x,y,length, initangle=0, initlength=0):

  

  tutsG = initialize_turtle("turtle","green")
  tutsW = initialize_turtle("turtle","white")

  if initangle > 0 and initlength > 0 :
    tutsG.left(initangle)
    tutsG.fd(initlength)
    tutsG.left(300)
    tutsW.left(initangle)
    tutsW.fd(initlength)
    tutsW.left(300)
    x = x + tutsG.pos()[0]
    y = y + tutsG.pos()[1]

  draw_triangle(x,y,length,tutsG)
  draw_inverse_triangle(x+length/2,y,length/2, tutsW)


window = turtle.Screen()
window.bgcolor("white")




draw_fractals(0,0,50)
draw_fractals(50,0,50)
draw_fractals(100,0,50)
draw_fractals(150,0,50)

draw_fractals(0,0,50,60,50)
draw_fractals(100,0,50,60,50)

draw_fractals(0,0,50,60,100)
draw_fractals(50,0,50,60,100)

draw_fractals(0,0,50,60,150)


window.exitonclick()


