import turtle
 
def drawSnake(rad,angle,len,neckrad):
 
  colors = ["red","orange","yellow","green","cyan","blue"]
  for i in range(len):
    turtle.color(colors[i])
    turtle.circle(40,80)
    turtle.circle(-40,80)
 
  turtle.color("purple")
  turtle.circle(40,80/2)
  turtle.fd(rad)
  turtle.circle(neckrad+1,180)
  turtle.fd(40*2/3)
 
def main():
  turtle.setup(2300,800,200,200)
  pythonsize = 30
  turtle.pensize(pythonsize)
  turtle.seth(-40)
  drawSnake(40,80,6,pythonsize/2)
 
main()
