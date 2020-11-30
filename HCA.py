"""
HCA.py
Object: Application to Assess Users HAND/EYE Coordination
Users: General Public
System: Windows/GNU Linux
Interface: GUI
Functional Requirements: Graphics and Audio to Prompt User For Response
						 Input Device, Event Handling
Non-Functional Requirements: Database for User Scores

Expected results: Returns data related hand-eye coordination i.e reaction speed and focus.

NB This assessment in only meant to provide a superficial analyis of user hand/eye coordination and cogitive ability. It does not replace established  psychological tests and serves merely to determine if users are capable of the minimum requirements for employment. THIS ASSESSMENT DOES NOT ASSES FOR MENTAL ILLNESS in any form.
This assessment is not meant to discriminate, only to assist trainers in establishing baseline ability so that relevant resources can be organised for the most effective training experience.

"""
__version__ = "0.1"
__status__ = "prototype"
__maintainer__ = "gavinkolz00@gmail.com"

# Libraries
import random
import time
import turtle

# Screen

'''This is a function for generating screen.'''
wn = turtle.Screen()
wn.title("Diligo Psychomotor Assessment by Gavin Kolz ")
wn.bgcolor("white")
wn.setup(600, 600)
wn.tracer(1)


def f1():
    gavin.setheading(90)
    gavin.forward(10)

def f2():
    gavin.setheading(180)
    gavin.forward(10)


def f3():
    gavin.forward(10)
    gavin.setheading(0)

def f4():
    gavin.setheading(-90)
    gavin.forward(10)






# Welcome note
#
# tian = turtle.Turtle()
# tian.hideturtle()
# tian.pencolor("black")
# tian.write("Welcome to Diligo Psychomotor Assessment", move=False, align="Center", font="Arial")
# time.sleep(3)
# tian.clear()
# time.sleep(2)
# tian.write("Hand-Eye Coordination Test", move=False, align="Center", font="Arial")
# time.sleep(2)
# tian.clear()
# time.sleep(2)
#
# # Introduction to signal
# tian.write("Use the mouse to move the following turtle past the obstacles to its food. ", move=False, align="Left",
#            font="Arial")
# time.sleep(3)
# tian.clear()
# tian.write("Press and Hold LEFT MOUSE BUTTON TO GRAB TURTLE.", move=False, align="Left", font="Arial")
# time.sleep(3)
# tian.clear()
#
# tian.write("Release button when turtle is exactly above it's food.", move=False, align="Left", font="Arial")
# time.sleep(3)
# tian.clear()
# time.sleep(3)
#
# tian.write("Get Ready!", move=False, align="Left", font="Arial")
# time.sleep(2)
# tian.clear()
# tian.write("3", move=False, align="Left", font="Arial")
# time.sleep(1)
# tian.clear()
# tian.write("2", move=False, align="Left", font="Arial")
# time.sleep(1)
# tian.clear()
# tian.write("1", move=False, align="Left", font="Arial")
# time.sleep(1)
# tian.clear()
# tian.write("GO!", move=False, align="Left", font="Arial")
# time.sleep(1)
# tian.clear()


gavin = turtle.Turtle()
gavin.penup()
gavin.hideturtle()
gavin.setposition(-240, -240)
gavin.shape("turtle")
gavin.setheading(90)
gavin.shapesize(stretch_wid=5, stretch_len=5)
gavin.color("green")
gavin.showturtle()



#Enemy1
enemy = turtle.Turtle()
enemy.penup()
enemy.hideturtle()
enemy.setposition(-240, 0)
enemy.shape("square")
enemy.color("black")
enemy.shapesize(stretch_wid=2, stretch_len=10)
enemy.showturtle()

#Enemy2
enemy2 = turtle.Turtle()
enemy2.penup()
enemy2.hideturtle()
enemy2.setheading(90)
enemy2.setposition(100,-240)
enemy2.shape("square")
enemy2.color("black")
enemy2.shapesize(stretch_wid=2, stretch_len=10)
enemy2.showturtle()

# Activate screen
wn.listen()
# Key bindings
wn.onkey(f1,"Up")
wn.onkey(f2,"Left")
wn.onkey(f3,"Right")
wn.onkey(f4,"Down")

# Signal
for i in range(0, 200):

    # Food
    food = turtle.Turtle()
    food.penup()
    food.hideturtle()
    x = random.randint(-240, 240)
    y = random.randint(-240, 240)
    food.setposition(x, y)
    food.shape("circle")
    food.color("green")
    food.shapesize(stretch_len=2, stretch_wid=2)
    food.showturtle()


    # Enemy movement
    enemy.forward(480)
    enemy2.forward(480)
    enemy.backward(480)
    enemy2.backward(480)

    food.hideturtle()





# Event Handling


# Scoring
