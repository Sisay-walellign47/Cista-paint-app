import turtle
import tkinter
from tkinter.ttk import Label 


screen = turtle.Screen()
screen.setup(700,500)
screen.title('Cista sketcher app')
screen.bgcolor('#eeeedd')
screen.update()
screen.colormode(200)

help = turtle.Turtle()
help.color("#5209da")
help.hideturtle()
help.speed(10)
help.penup()
help.goto(780,380)
help.pendown()
help.write("Help!!", align= "right" , font = ["Cambria" , 25 , "bold"])


pen = turtle.Turtle()
pen.shapesize(stretch_len = 3, stretch_wid =3)

def pen_up():
    y = pen.ycor()
    y += 20
    pen.sety(y)

def pen_down():
    y = pen.ycor()
    y -= 20
    pen.sety(y)

def pen_right():
    x = pen.xcor()
    x += 20
    pen.setx(x)

def pen_left():
    x = pen.xcor()
    x -= 20
    pen.setx(x)

def pen_up_right():
        pen.left(45)

def pen_up_left():
        pen.left(135)

def pen_down_left():
       pen.right(135)

def pen_down_right():
        pen.right(45)



def pen_up_rightf():
        pen.forward(20)

def pen_up_leftf():
        pen.forward(20)

def pen_down_leftf():
       pen.forward(20)
       
def pen_down_rightf():
        pen.forward(20)



while True:
    shape= input("type the shape of the turtle(turtle, triangle , arrow, square, circle,classic) ")
    if shape == "turtle":
        pen.shape("turtle")
    elif shape == "square":
       pen.shape("square")
    elif shape == "arrow":
        pen.shape("arrow")
    elif shape == "triangle":
        pen.shape("triangle")
    elif shape == "circle":
        pen.shape("circle")
    elif shape == "classic":
        pen.shape("classic")
    else:
        print("You must choose from turtle, triangle , arrow, square, circle,classic")
        continue

    color= input("type the line color for the " + shape +": ")
    if color == "lime":
        pen.color("lime")
    elif color == "yellow":
        pen.color("yellow")
    elif color == "red":
        pen.color("red")
    elif color == "blue":
        pen.color("blue")
    elif color == "cyan":
        pen.color("cyan")
    elif color == "deeppink":
        pen.color("deeppink")
    elif color == "green":
        pen.color("green")
    elif color == "skyblue":
        pen.color("skyblue")
    elif color == "orange":
        pen.color("orange")
    elif color == "black":
        pen.color("black")
    elif color == "white":
        pen.color("white")
    elif color == "violet":
        pen.color("violet")
    elif color == "indigo":
        pen.color("indigo")
    elif color == "brown":
        pen.color("brown")
    elif color == "darkblue":
        pen.color("darkblue")
    elif color == "pink":
        pen.color("pink")
    elif color == "purple":
        pen.color("purple")
    else:
        print('Choose from lime,yellow,red,blue,cyan,deeppink,green,skyblue,orange,black,white,violet,indigo,brown,darkblue,pink and purple')
        continue

    colors= input("write the background color for the screen: ")
    if colors == "lime":
        screen.bgcolor("lime")
    elif colors == "yellow":
        screen.bgcolor("yellow")
    elif colors == "red":
        screen.bgcolor("red")
    elif colors == "blue":
        screen.bgcolor("blue")
    elif colors == "cyan":
        screen.bgcolor("cyan")
    elif colors == "deeppink":
        screen.bgcolor("deeppink")
    elif colors == "green":
        screen.bgcolor("green")
    elif colors == "skyblue":
        screen.bgcolor("skyblue")
    elif colors == "orange":
        screen.bgcolor("orange")
    elif colors == "black":
        screen.bgcolor("black")
    elif colors == "white":
        screen.bgcolor("white")
    elif colors == "violet":
        screen.bgcolor("violet")
    elif colors == "indigo":
        screen.bgcolor("indigo")
    elif colors == "brown":
        screen.bgcolor("brown")
    elif colors == "darkblue":
        screen.bgcolor("darkblue")
    elif colors == "pink":
        screen.bgcolor("pink")
    elif colors == "purple":
        screen.bgcolor("purple")
    else:
        print('Choose from lime,yellow,red,blue,cyan,deeppink,green,skyblue,orange,black,white,violet,indigo,brown,darkblue,pink and purple')
        continue

    def helps(x,y):
        root = tkinter.Tk()
        root.title("help")
        root.resizable(False,False)
        root.geometry("200x200")
        Label(root ,text= "press y to go up ,\nb to go down , \ng to go left , \nh to go right &  \nu ad n to turn 45 degrees & \nv and t to turn 135 degrees" , font= ["Cambria" , 12 ,"normal"]).pack()
        root.mainloop()

    screen.listen()
    screen.onkeypress(pen_right, "h")

    screen.listen()
    screen.onkeypress(pen_left, "g")

    screen.listen()
    screen.onkeypress(pen_up, "y")

    screen.listen()
    screen.onkeypress(pen_down, "b")

    screen.listen()
    screen.onkeypress(pen_down_right, "n")
    screen.onkeypress(pen_down_rightf, "m")

    screen.listen()
    screen.onkeypress(pen_up_left, "t")
    screen.onkeypress(pen_up_leftf, "r")

    screen.listen()
    screen.onkeypress(pen_up_right, "u")
    screen.onkeypress(pen_up_rightf, "i")

    screen.listen()
    screen.onkeypress(pen_down_left, "v")
    screen.onkeypress(pen_down_leftf, "c")

    screen.listen()
    screen.onclick(helps)


    turtle.done()
