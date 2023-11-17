# turtle race project 
# turtle race project
import turtle

from turtle import Turtle,Screen
import random
width,height=600,600
def user_input():# this fn is to get a correct user input for the race
    user_int = 0
    while True:
        user_int = int(input("Enter how many turtles do you want in the race (2-10):"))
        if 2<=user_int<=10:
            return user_int # return the input to the fn call
        else:
            print("Try to give the values in the range betweem 2 to 10 ")

def race():
    is_race=True
    while is_race:
        for t in turtle_list:
            distance = random.randint(1, 20)
            t.forward(distance) # we are moving the turtle at random dist
            x,y =t.pos() # it returns the pos of the turtle
            if y >= (height // 2)-20:
                print(f" THE WINNER IS {t.pencolor()} TURTLE")
                is_race = False

turtles = user_input()

s1=Screen()
s1.setup(600,600)
x_position=width//(turtles+1)
colors=['red','yellow','blue','green','pink','blue violet','coral',"orange","brown","black"]
turtle_list=[]
for i in range(1,turtles+1): # looping through user input
    speed_turtle = random.randint(0,10)
    new_turtle=Turtle() #creating obj
    new_turtle.shape("turtle")
    new_turtle.left(90)
    new_turtle.color(colors[i-1])
    new_turtle.penup()
    new_turtle.goto(-width//2 + (i*x_position),-height//2+20) # simple formula to set turtles in even space
    turtle_list.append(new_turtle) # appending all obj into a list
race()
s1.exitonclick()