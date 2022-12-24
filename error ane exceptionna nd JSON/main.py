#fileNotFound
try:
    file=open("dauda.txt")
    dict={"key": "valus"}
    print(dict["djhfjhd"])
except FileNotFoundError:
    file=open("dauda.txt","w")
    file.write("write")
except KeyError as error_message:
    print(f"the key {error_message} does not exist")

else:
    content=file.read()
    print(content)

finally:
    raise TypeError("You have a typeerror")
    


# height=float(input("Height: "))
# weight=int(input("Weight: "))
# if height> 3:
#     raise ValueError("Human heught should not be ocer three meters")
# bmi= weight/height **2
# print(bmi)


# fruits=["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit=fruits[index]
#     except IndexError:
#         print("Fruit pie")
       
#     else:
#         print(fruit+"pie")
      


# make_pie(4)


facebook_posts=[
    {"likes":21,"comment": 2},
    {"likes":13,"comment": 2, "Share": 1},
    {"likes":33,"comment": 8,"Share":3},
    {"comment":4,"shares":2},
    {"comment":1,"shares":1},
    {"likes":19,"comment":3}
]
total_likes=0
for post in facebook_posts:
    try:
        total_likes=total_likes+post["likes"]
    except KeyError:
        print("This is a key error")
        # total_likes+=0
print(total_likes)
  
