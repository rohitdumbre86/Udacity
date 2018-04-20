import turtle


def draw_triangle(x,y, length, initangle) :
  
  tuts = initialize_turtle("turtle","green",initangle)
  
  tuts.begin_fill()
  tuts.setpos(x,y)

  for i in range(1,4):
    tuts.fd(length)
    tuts.left(120)

  tuts.end_fill()

def draw_inverse_triangle(x,y,length,initangle):  
  tuts = initialize_turtle("turtle","white",initangle)
  
  tuts.begin_fill()
  tuts.setpos(x,y)
  tuts.left(60)

  for i in range(1,3):
    tuts.fd(length)
    tuts.left(120)

  tuts.fd(length)
  tuts.end_fill()


def initialize_turtle(shape,color,initangle):
  
  tuts = turtle.Turtle()
  tuts.hideturtle()
  tuts.shape(shape)
  tuts.color(color)
  tuts.hideturtle()
  tuts.left(initangle)
    
  return tuts
    
def draw_fractals(x,y,length,initangle):
    
 draw_triangle(x,y,length, initangle)
 draw_inverse_triangle(x+length/2,y,length/2, initangle)


window = turtle.Screen()
window.bgcolor("white")


draw_fractals(0,0,200,0)
draw_fractals(0,0,100,0)
draw_fractals(0,0,50,0)
draw_fractals(50,0,50,0)
draw_fractals(100,0,100,0)
draw_fractals(100,0,50,0)
draw_fractals(150,0,50,0)




window.exitonclick()


