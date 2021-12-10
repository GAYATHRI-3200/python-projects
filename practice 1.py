print("hello world!")
#i=input("Enter your Name: ")
#print("Hello nice to hear "+ i);
#find position
"""
abc=("i like to play guitar and i am huge fan of sungha jung and he play very good guitar")
x=(abc.find("play"))
y=(abc.find("play",x+1))
print(y)#answer should be 62, not getting!(-1)
print(abc[62:])
"""
####program2
"""print("Hello Hope you're doing good!!")
i=input("How can i help you, please enter your name:")
print(i +" the length of your name is " +str(len(i)))
i1=input("May i know your age:")
print("you will be age " +str(int(i1)+1) +" in a year")
print('Thank you.......!!!!')"""
"""  
print("Hello world!, Sum of two digits")
a=input("enter a number:")
b=input("enter a number:")
#c=a+b
print("sum og two digits is ",  str(int(a)+int(b)))"""

#Procedure Defining
"""
def sub(a,b):
    return a-b
print(sum(10,10))"""
#Make own program on procedure
#sum of 2 numbers
"""
def sum(a,b):
    return a+b
x=input("enter 1st number:")
#x1=int(x)
y=input("enter 2nd number:")
#y1=int(y)
#c=str(x1+y1)
c=(sum(int(x),int(y)))
print(c)   """
#square
"""
def square(a):
    return a*a
x=input("enter a number:")
x1=(square(int(x) ))
print(x1)  """
#stringsconcatenation via def
"""def strings(a,b):
    return a+b
print(strings("Hello", " All"))"""
#find 2nd pos of string
"""
def pos1(variable1, element1):
    a=(variable1.find(element1)) 
    return (variable1.find(element1,a+1))"""
"""
x= "i like to play guitar and i am learning guitar"
a=(x.find("guitar"))
b=(x.find("guitar",a+1))
#print((pos1(x,"guitar"))) 
print(b) 
print(x[40:]) """  
#If-else Number guessing game
"""x=input("enter a number from 1 to 10:")
x=int(x)
if(x!=4):
    print("Oops, your guess is wrong")
else:
    print("your guess is right")"""
#If-else---Greatest
"""x=input("enter a number:")
x=int(x)
y=input("enter a number:")
y=int(y)
if(x>y):
    print(str(x) +("is greater"))
else:
    print(str(y) +("is greater"))"""
#def to greatest    
"""def greatest1(a,b):
    if(a>b):
        return a
    else:
        return b
x=input("enter a number:")
y=input("enter a number:")        
z=(greatest1(int(x),int(y)))
print(str(z) + (" is greatest"))"""
#Name from A/a is true else False
"""def name(i):

    if(i[0]=='A' or i[0]=='a'):
        print(i +(" is True"))
    else:
        print(i +(" is False"))   
x=input("enter your name:")
y=(name(str(x)))
print(str(y))"""
#Nested if-else
# largest of 3 numbers
"""def large1(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else: 
            return c
    else:
        if(b>c):
            return b
        else:
            return c
""""""
x1=input("enter a number:")
y1=input("enter a number:") 
z1=input("enter a number:")
#x=(large1(int(x1),int(y1),int(z1)))  
print(max(x1,y1,z1)) """ 
#while loop
"""i=1
while(i!=10):
    i=i+1      
    print(i)"""
#series, factorial, A.p Series using while loop
#Number Series
"""def num1(a):
    i=1
    while(i<=a):
        print(i)
        i=i+1
x=input("enter a number:")
x1=num1(int(x))       
print(x1)"""
#Factorial
"""def factorial(i):
    fact=1
    while(i>=1):
        fact=fact*i
        i=i-1
    return fact    
x=input("enter a number:")
x1=factorial(int(x)) 
print(x1) """
#A.P Series
"""def AP(a,d,l):
    while(a<=l):
        print(a)
        a=a+d
a=int(input("enter 1st term of AP:"))
d=int(input("enter difference of AP:")) 
n=int(input("enter last term:"))  
l=(a +(n*d)  -d)   
z=(AP(a,d,l))
print(z)"""
#Infinite Loop, break,continue & Password program.
"""#loop
def print_numb(x):
    i=1
    while(i<=x):
        print(i)
        i=i+1
print(print_numb(10))  """    
"""#Infiniteloop
def print_numb(x):
    i=1
    while True:#Infiniteloop
        if(i>x):# break
            break
        print(i)
        i=i+1
print(print_numb(10))    """
"""#Password & Continue stmt
while True:
    x= str(input("your name?."))
    if(x!="alex"):
        continue
    y=str(input("Hi Alex, your password?."))
    if(y=="Alex123"):
        break
print("Welcome Alex, Acess is granted!!!")  """  
#Basics of seo
x=("hi")
if x:
    print("not empty:")
else:
    print("it's empty")        