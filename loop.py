"""i = 1

while i < 7 :
    print(i)
    i += 1

fruits = ["grapes","berries","oranges"]

for x in fruits:
    print(x)
#Nested For loop
colors = ["green","yellow","red"]
fruits = ["banana","apple","oranges"]  

for x in colors:
    for y in fruits:
        print(x,y)

#Break statement (stop the loop) 

i = 1

while i < 8:
    print(i)
    if i==4:
        Break
    i += 1    

# continue statement
i = 0

while i < 8:
    i += 1
    if i==4:
        continue 
    print(i)

fruits = ["grapes","berries","oranges"]

for x in fruits:
    print(x)
    if x == "berries":
        break  

 # for loop and Cont,

fruits = ["grapes","berries","apple"] 

for x in fruits:
    if x == "berries":
        continue
    print (x)  """

#For loop and else statement

for x in range(8):
    print(x)
else:
    print("loop is over.bye")    