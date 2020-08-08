# Spiral  Helix Pattern in Python
#
# This program uses turtle programming. To install the necessary
# library under Ubuntu, use:
#
# $ sudo apt install python3-tk
#
  
import turtle 
loadWindow = turtle.Screen() 
turtle.speed(2) 
  
for i in range(100): 
    turtle.circle(5*i) 
    turtle.circle(-5*i) 
    turtle.left(i) 
  
turtle.exitonclick()

