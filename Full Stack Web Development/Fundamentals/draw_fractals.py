import turtle


def draw_triangle(x,y, length) :
  tuts = turtle.Turtle()
  tuts.hideturtle()
  tuts.shape("turtle")
  tuts.color("green")
  tuts.begin_fill()
  tuts.setpos(x,y)
  tuts.fd(length)
  tuts.left(120)
  tuts.fd(length)
  tuts.right(240)
  tuts.fd(length)
  tuts.left(120)
  tuts.end_fill()

def draw_inverse_triangle(x,y,length):  
  tuts = turtle.Turtle()
  tuts.hideturtle()
  tuts.shape("turtle")  
  tuts.color("white")
  tuts.begin_fill()
  tuts.setx(x)
  tuts.left(60)
  tuts.fd(length)
  tuts.left(120)
  tuts.fd(length)
  tuts.left(120)
  tuts.fd(length)
  
  tuts.end_fill()

    
def draw_fractals(x,y,length,originalL):
    
 if (length < originalL/4):
   return

 draw_triangle(0,0,length)
 x = length/2
 length = length/2
 draw_inverse_triangle(x,y,length)

 draw_fractals(x,y,length,originalL)
 draw_fractals(x+x/2,y,length,originalL)
  




    

window = turtle.Screen()
window.bgcolor("white")



draw_fractals(0,0,200,200)
window.exitonclick()


