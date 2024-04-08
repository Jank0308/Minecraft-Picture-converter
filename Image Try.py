from PIL import Image
import numpy as np
import turtle

turtle.speed(0)


image = Image.open("/home/jan/Documents/programmes/pixil-frame-0(2).png")


data = np.asarray(image)



for yax in range(0,data.shape[0]):
   
    for xax in range(0,data.shape[1]-1):
        pixelcolor = (float(data[xax][yax][0])/256,float(data[xax][yax][1])/256,float(data[xax][yax][2]/256))
        turtle.color(pixelcolor)
        turtle.penup()
        turtle.setpos(yax,data.shape[1]-xax)
        print(xax,yax)
        turtle.dot(1)
        turtle.pendown()

#test comment
turtle.exitonclick()