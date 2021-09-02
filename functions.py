"""def sum(x,y):
    print(x + y)
#calling fungtions   

sum(4,5)

def sum (x,y):
    return x + y

print(sum(4,5))
print(sum(8,4))

#Return Value

def students_names(names="Bagas"):
    print("hello "+ names)
students_names()
students_names("jhon") 
students_names("jane") 

#fungci argument

def more_num(a, b=7, c=10):
    print("a is",a, "and b is",b,"while c is",c)

more_num(3,7) 
more_num(23,c=17)
more_num(c=40,a=80)

def greeting():
    def say_hello():
        return "hello"
    return say_hello

hello = greeting()   
print(hello())  

def mynum(x):
    return x + 1

num = mynum 

print(num(7))
print(mynum(8))

#global and local variabel scope
#global variabel scope

x= 10

def my_numbers():
    global x
    print(x)
    x = 7
    print("my fav number is", x )

my_numbers() 
print(x)  

#nesting function

def mynum(a):
    def num(a):
        return a + 1
    result = num(a) 
    return result 

print(mynum(4)) 

#nesting func acces variabel scope

def display_message(message):
    "hello"
    def message_sender():
        "nested function"
        print(message)
    message_sender()   

display_message("show me the money")
#Pass Fuctions

def dream_home():
    Pass

def mynum(b):
    return b + 1
def addnum(c):
    newnum = 7
    return c(newnum)  

print(addnum(mynum)) """ 

def total_numbers(a=7, *numbers,**phonebook):
    print("my fav number is", a)

    for num in numbers:
        print("num", num)
    for name, phone_number in phonebook.items():
        print(name, phone_number) 

total_numbers(7,1,2,3,jane=2222, jhon=4444,Angela=5555)          




