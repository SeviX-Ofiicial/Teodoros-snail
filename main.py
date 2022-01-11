import turtle
import os


#visible=False
pen = turtle.Turtle(visible=False)
import math
pen.color('red', 'yellow')
pen.begin_fill()
pen.speed(9999)

pen.fd(50)
pen.right(90)
pen.fd(50)
pen.home()

pen.right(45)
x = 50 * math.sqrt(2)
pen.fd(50 * math.sqrt(2))
pen.right(90)
pen.fd(50)
pen.home()

pen.right(45)
pen.right(35)
x = math.sqrt((x * x) + (50 * 50))
pen.fd(x)
pen.right(90)
pen.fd(50)
pen.home()


pen.right(45)
pen.right(35)
pen.right(30)
x = math.sqrt((x * x) + (50 * 50))
pen.fd(x)
pen.right(90)
pen.fd(50)
pen.home()

pen.right(45)
pen.right(35)
pen.right(30)
pen.right(26)
x = math.sqrt((x * x) + (50 * 50))
pen.fd(x)
pen.right(90)
pen.fd(50)
pen.home()

pen.right(180)
pen.left(20)
x = math.sqrt((x * x) + (50 * 50))
pen.fd(x)
pen.right(90)
pen.fd(50)
pen.home()

pen.end_fill()

os.system('pause')

'''
x = 50 * math.sqrt(2)
pen.fd(50 * math.sqrt(2))
pen.right(90)
pen.fd(50)
pen.right(90)
pen.fd(50)
pen.home()

pen.right(45)
x = 50 * math.sqrt(2)
pen.fd(50 * math.sqrt(2))
pen.right(90)
pen.fd(50)
pen.right(90)
pen.fd(50)
pen.right(45)
'''
