# from turtle import Turtle,Screen
# import turtle
# usman=Turtle()
# usman.color()
# usman.backward(100)
# usman.shape("turtle")
# print(usman)

# screen=Screen()
# print(screen.canvheight)
# screen.exitonclick()


# from turtle import *
# color("blue","yellow")
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("pokemom name",["pikachu", "squirtle", "chamander"]) 
# table.add_column("Type", ["Electric", "Water", "Fire"])
# # table.align="l"
# # print(table)



class usman:
    def __init__(self,name,surname,fatai):
        self.name=name
        self.another=surname
        self.follower=fatai
        self.following=0
    def others(self,usman):
        usman.follower+=1
        self.following+=1
        # print("My name is usman hassan")

        
familyUsman=usman()
familyMariam=usman("abideen", "is_father")
print(familyMariam)


familyUsman.others
print(familyMariam.follower)
print(familyMariam.following)
print(familyUsman.follower)
print(familyUsman.following)

ahmad=usman()
ahmad.name="hassan"

# c

# for _ in range(15):
#     practice.forward(10)
#     practice.penup()
#     practice.forward(10)



# for _ in range(5):
#     practice.forward(60)
#     practice.right(60)
#     practice.forward(60)
# practice.right(120)
# practice.forward(60)




# color=["Blue", "Yellow", "Pink", "Orange","Purple","Green","CornFlowerBlue","wheat", "DeepSkyBlue", "SeaGreen", "IndianRed"]

# def draw_shape(num_sides):
#     angle=360/num_sides
#     for values in range(num_sides):
#         practice.forward(100)
#         practice.right(angle)
# for shape_sides in range(3,11):
#     practice.color(choice(color))
#     draw_shape(shape_sides)




# for _ in range(100):
#     directtions=[0,90,180,270]
#     practice.width(3)
#     practice.speed(0)
#     practice.color(choice(color))
#     practice.forward(20)
#     practice.setheading(choice(directtions))
    
 

# display=Screen()
# def move_forward():
#     practice.forward(52)

# display.listen()
# display.onkey(key="space", fun=move_forward)
# display.exitonclick()


#inheritance
class Animals:
    def __init__(self):
        self.num_eyes=2
    def breathe(self):
        print("inhale, exhale")
class Fish(Animals):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("DOing this on water.")

    def swim(self):
        print("mpving in water")
        

nemo=Fish()
nemo.breathe()
print(nemo.num_eyes)