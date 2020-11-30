"""
DAA.py
Object: Application to Assess Users Cognitive Ability 
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
from playsound import playsound

# Variables

r = 0
g = 0
b = 0
s1 = 0


#Functions

def red():

    global r
    if gavin.color() == ("red","red"):
        r += 1
    else:
        print("Mistake")

def green():

    global g
    if gavin.color() == ("green","green"):
        g += 1
    else:
        print("Mistake")
    
   
def blue():

    global b
    if gavin.color() == ("blue","blue"):
        b += 1
    else:
        print("Mistake")

def sound():

    global s1
    s1 += 1
   
 
# Screen
'''This is a function for generating screen.'''
wn = turtle.Screen()
wn.title("Diligo Psychomotor Assessment by Gavin Kolz ")
wn.bgcolor("black")
wn.setup(600, 600)
wn.tracer(1)

# Welcome note

tian = turtle.Turtle()
tian.hideturtle()
tian.pencolor("white")
tian.write("Welcome to Diligo Psychomotor Assessment", move=False, align="Center", font="Arial")
time.sleep(3)
tian.clear()
time.sleep(2)
tian.write("Determination Test", move=False, align="Center", font="Arial")
time.sleep(2)
tian.clear()
time.sleep(2)

# Introduction to signal
tian.write("When you see ", move=False, align="Left", font="Arial")
time.sleep(2)
tian.clear()

gavin = turtle.Turtle()
gavin.shape("turtle")
gavin.penup()
gavin.setheading(90)
gavin.shapesize(stretch_wid=10, stretch_len=10)
gavin.color("Red")
gavin.showturtle()
time.sleep(3)
gavin.hideturtle()
time.sleep(2)

tian.write("Press R ", move=False, align="Left", font="Arial")
time.sleep(2)
tian.clear()

tian.write("When you see ", move=False, align="Left", font="Arial")
time.sleep(2)
tian.clear()

gavin = turtle.Turtle()
gavin.shape("turtle")
gavin.penup()
gavin.setheading(90)
gavin.shapesize(stretch_wid=10, stretch_len=10)
gavin.color("Green")
gavin.showturtle()
time.sleep(3)
gavin.hideturtle()
time.sleep(2)

tian.write("Press G ", move=False, align="Left", font="Arial")
time.sleep(2)
tian.clear()

tian.write("When you see", move=False, align="Left", font="Arial")
time.sleep(2)
tian.clear()

gavin = turtle.Turtle()
gavin.shape("turtle")
gavin.penup()
gavin.setheading(90)
gavin.shapesize(stretch_wid=10, stretch_len=10)
gavin.color("Blue")
gavin.showturtle()
time.sleep(3)
gavin.hideturtle()
time.sleep(2)

tian.write("Press B", move=False, align="Left", font="Arial")
time.sleep(2)
tian.clear()

tian.write("Get Ready!", move=False, align="Left", font="Arial")
time.sleep(2)
tian.clear()
tian.write("3", move=False, align="Left", font="Arial")
time.sleep(1)
tian.clear()
tian.write("2", move=False, align="Left", font="Arial")
time.sleep(1)
tian.clear()
tian.write("1", move=False, align="Left", font="Arial")
time.sleep(1)
tian.clear()
tian.write("GO!", move=False, align="Left", font="Arial")
time.sleep(1)
tian.clear()

wn.listen()
t1 = time.time()

# Signal
for i in range(0, 20):

    # Event Handling

    wn.onkeypress(red, "r")
    wn.onkeypress(green, "g")
    wn.onkeypress(blue, "b")
    

    

    if 0 < i < 5:
        gavin.hideturtle()
        time.sleep(1)
        gavin.penup()
        gavin.shape("turtle")
        gavin.shapesize(stretch_wid=10, stretch_len=10)
        fi = random.choice(["blue", "green", "red"])
        gavin.color(fi)
        gavin.showturtle()
        time.sleep(3)

    if 5 <= i < 15:
        gavin.hideturtle()
        time.sleep(1)
        gavin.penup()
        gavin.shape("turtle")
        gavin.setheading(90)
        gavin.shapesize(stretch_wid=10, stretch_len=10)
        fi = random.choice(["blue", "green", "red"])
        gavin.color(fi)
        gavin.showturtle()
        time.sleep(1)

    if 15 <= i < 20:
        gavin.hideturtle()
        time.sleep(2)
        gavin.penup()
        gavin.shape("turtle")
        gavin.setheading(90)
        gavin.shapesize(stretch_wid=10, stretch_len=10)
        fi = random.choice(["blue", "green", "red"])
        gavin.color(fi)
        gavin.showturtle()
        time.sleep(2)
        playsound("Censor Beep.mp3")
        wn.onkey(sound,"Down")
        

t2 = time.time() - t1

    


# Scoring

print(r+b+g)
print(s1)
print(t2)

