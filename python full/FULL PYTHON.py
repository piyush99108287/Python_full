
''' About the print statement
print("Piyush kumar jha")

print("I am very happy to start this")'''

'''print('This is my journey for
Data Analytics and I will complete this journey 
by learning the new concept and skill')'''

'''print("So, Basically I am exploring \n the different way to use\n the print statement")'''



# How to create a variable

'''a = "Piyush"
print(a)'''

'''even_number = 22
print(even_number)'''

#Data Type

'''Name = input("Enter your name")
print(Name)

age = int(input("Enter your age"))
print(age)

hight = float(input("enter your hight"))
print(hight)

equation = eval(input("Enter the equation :"))
print(equation)'''

# Typecasting and subtypes

'''name = "piyush kumar jha"
age = 20
print(type(name))
print(type(age))

a = 100
b = 1.5
c = a+b
print(c)
print(type(c))'''

'''a = "20"
print(type(a))
b = 44
print(type(b))
a = int(a)
print("after conversion",type(a))
c=a+b
print(c)
print(type(c))'''


#QUESTIONS

# Q1. write a program to display the person name age and address in three different line

'''a = input("Enter the person name : ")
b = input("Enter the age of the person : ")
c = input("Enter the address of the person : ")
print(a,"\n",b,"\n",c)'''

#Q2. Write a program to swap the two varibale

#Method 1
'''x = 10
y = 20
print(x)
print(y)
x,y=y,x
print(x)
print(y)'''

#Method 2
'''x = 30
y = 40
print(x)
print(y)
temp = x
x = y
y = temp
print(x)
print(y)
'''

#Q3. Write a program to convert float into integer

'''a = float(input("Enter a float number :"))
print("Your enterd float number is :",a)
a = int(a)
print(a)
'''
#Q4. take the input from the student for ID card

'''name = input("Enter the name of the student :")
grade = int(input("Enter the grade :"))
roll_no = int(input("Enter the roll number :"))
age = int(input("Enter the age of the student :"))
email = input("Enter the E-mail of the student :")
print("Student ID Card")
print(name)
print(grade)
print(roll_no)
print(age)
print(email)'''

#Q5. Write a program to convert integer into float number
'''x = int(input("Enter the integer number :"))
x = float(x)
print(x)'''



#Operator and Operends


# Arithematic operator
'''print(8%3)
print(8/3)
print(8//3)
print(8*3)
print(8**3)'''

#comparision operator

'''print(3>2)
print(3>8)
print(3==3)
print(3!=3)
print(3>=3)'''

#Logical operator

'''print(3>2 and 3>7)
print(3>2 or 3>7)
print(not(3>2 and 7>3))'''

#Assignment operator

'''a = 50
a +=2
print(a)
a -= 10
print(a)
a *= 2
print(a)'''

#Identity operator
'''a = 1234
b = "1234"
print(a is not b)'''


#Bitwise operator

'''print(bin(15))
a = 10
b = 8
print(a and b) ''' #this will add and covert it into binary
'''a = 10
b = 8
print(a or b)'''
'''a = 10
b = 8
print(a ^ b)'''

# Membership operator

'''a = "hello"
print("e" not in a)
print("e" in a)'''

# Conditional statement

# 1. If statement
'''a = 4
if a>5:
    print("PIYUSH KUMAR JHA")
print("JHA G")'''


#2.If - else

'''var = 1
if var >= 5:
    print("YES")
else:
    print("NO")'''

#3. if-elif-else
'''
marks = 87
if marks >=90:
    print("Trip for You")
elif marks >=80 and marks<=90:
    print("get a new phone")
elif marks >= 70 and marks <80:
    print("Get a new game")
else:
    print("Take the phone")'''

#4 . Nested-If:

'''marks = 96
if marks>=80:
    print("get a new phone")
    if marks >=95:
        print("you go to the trip ")
else:
    print("no phone for a month")'''

#5. Short hand if  statement

'''marks = 97
if marks >=90: print("you will get a new phone")'''

#6. short hand if else statement

'''marks = 87
print("Get a phone") if marks >= 80 else print("no phone for a month")'''


# Question

#1 . write a program to check whether  a number is positive or not

'''a = int(input("ENter a number :"))
if a > 0:
    print("Number is positive ")
else:
    print("Number is negative")
'''

#2. check number is odd or even
'''
a = int(input("Enter a number :"))
if a%2==0:
    print("Number is even number")
elif a%2 != 0:
    print("Number is odd number")'''

#3 . Calculate the area
'''
print("***Area calculator***")
print("""Press 1  to get the area of square
Press 2 to get the area of rectangle
Press 3 to get the area of circle
Press 4 to get the area of triangle""")

choice = int(input("Enter the choice between 1 - 4 : "))

if choice == 1:
    side = float(input("Enter the side of the square"))
    area = side**2
    print("The area of square is :", area)
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area = length * breadth
    print("Area of the rectangle is : " , area)
elif choice == 3:
    radius = float(input("Enter the radius of the circle : "))
    area = radius*3.14*radius
    print("Area of the circle is :", area)
elif choice == 4:
    base = float(input("Enter the the base of the circle : "))
    height = float(input("Enter the height of the circle : "))
    area = (base*height)/2
    print("Area of the triangle is : ",area)
else:
    print("Invalid input")'''

#4 . Check passed letter is vowel or not
'''
letter = input("Enter the letter here : ")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("this is a vowel ")
else:
    print("Letter is not a vowel")'''

#5. Check the number is 2 digit 3 digit 4 digit 5 digit number

'''num = int(input("Enter the number upto 5 digit: "))
if num >=0 and num <=9:
    print("Number is single digit number")
elif num >=10 and num <=99:
    print("Number is double digit number")
elif num >=100 and num <=999:
    print("Number is third digit number ")
elif num >=1000 and num <=9999:
    print("Number is four digit number")
elif num >=10000 and num <=99999:
    print("Number is five digit")'''




#LOOPS

# 1. For Loop

"""for i in range(1,6,2):
    print("PIYUSH KUMAR JHA")
    print(i)"""

"""n = int(input("Enter the number which table you want to print :"))
for i in range (1,11):
    print(n,"*",i,"=",n*i)"""

# 2. While Loop
'''a=0
while a<=10:
    print(a)
    a+=1

n=1
a = int(input("Enter the number to print the table :"))
while n<=10:
    print(a,"*",n,"=",n*a)
    n+=1'''


#3. While True

'''while True:
    print("JHA G")'''

'''while True:
    num1 = int(input("enter  a number :"))
    num2 = int(input("enter  a second number :"))
    print(num1+num2)
    repeat = input("Do you want to repeate a program or not : Type YES or NO only :")
    if repeat == "YES":
        break'''

#4. Nested Loop
'''
for i in range(1,4):
    for j in range(1,11):
        print(j,end ="  ")'''
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()'''



# For loop with conditional statement


'''for i in range(1,11):
    if i == 3:
        print("ADD THIS SONG TO FAVIOURITE")
    else:
        print(i)'''
'''for i in range(1,101):
    if i % 8 ==0 and i % 12==0:
        print(i)
        
'''
'''
n = 1
while n <=10:
    if n ==3:
        print("ADD THIS TO FAVOURITE")
    else:
        print(n)
    n += 1'''


# Break and continue statement

'''for i in range(1,11):
    if(i==5):
        continue
    else:
        print(i)'''

'''for i in range(1,11):
    if (i==7):
        break
    else:
        print(i)
'''

# PROBLEM WITH LOOPS
# Q1. Find sum of even number upto 1 to 50
'''sum = 0
for i in range(1,51):
    if i % 2 == 0:
        sum += i
        
print(sum)'''

#Q2. first 20 number and their square numbers
'''for i in range(1,21):
    SQR = i*i
    print("Square of ",i, "is", SQR)'''

#Q3. Sum of first 100 odd number while

'''sum = 0
n = 0
while n<20:
    if n%2 !=0:
        sum +=n
    n += 1
print(sum)'''

#Q4. check the number is divisble by 8 and 12 upto 100 number

'''for i in range(1,101):
    if (i%8==0) and (i%12==0):
        print(i)'''

#Q5. Write a program to create billing system at super market
'''
while True:
    name = input("Enter Customer Name :")
    total =0

    while True:
        print("Enter amount and quantity :")
        amount = float(input("Enter the amount :"))
        quantity = float(input("Enter the quantity :"))
        total += (amount*quantity)
        repeat = input("do you want to add more iteam ? (yes/no):")
        if repeat =="no" or repeat=="No" or repeat== "NO":
            break
    print("-"*40)
    print("Name",name)
    print("Total amount to be paid",total)
    print("-"*40)
    print("*********HAPPY SHOPPING***********")

    repeat1 = input("Do you want to go to next customer(Yes/No):")
    if repeat1 == "no" or repeat1 =="No" or repeat1 == "NO":
        break'''



# Q6. so we have given a string and we have given some problem statement and we have to write a program one by one

A= "Why fit in, when you are Born to Stand Out !"


# (i) write a program to find the length of the string
'''print(len(A))'''


# (ii) check how many time alphabet o is occuring in A string

#print("Number of time o is occuring is ",A.count("o"))


# (iii) write a program to convert whole string into upper and lower case

'''B = A.lower()
print(B)
C = A.upper()
print(C)'''

# (iv) write the following string into the title
'''
Z = A.title()
print(Z)'''


#(v) write a program to find the index number of "fit in"

''' print(A.find("fit in"))'''

# SOME PATTERN PROBLEMS
'''
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5'''

'''for i in range(1,6): # i is the number of row
    for j in range(1,i+1):   # j is the number of column
        print(j, end = " ")
    print()'''

# solve more question on this topics

# String

a = "piyush kumar jha is a very interesting boy"
'''print(a)
print(type(a))
print(len(a))

print(a.count("jha"))


x = a.lower()
print(x)
y = a.upper()
print(y)

print(a.index("a"))

print(a.capitalize())

print(a.find("jha"))
 
e = "ohh yaahhhh!!! { }"      # go through this

print(a.format(e))


print(a.center(20))

'''


a = "piyush"
b = "123Piyush"
c = "123456"
d = "Piyush"
e = " "
f = "123 Piyush"
g = "1.2234"



# isalnum
'''print(a, a.isalnum())
print(b, b.isalnum())
print(c, c.isalnum())
print(d, d.isalnum())
print(e, e.isalnum())
print(f, f.isalnum())
'''


#isalpha
'''
print(a, a.isalpha())
print(b, b.isalpha())
print(c, c.isalpha())
print(d, d.isalpha())
print(e, e.isalpha())
print(f, f.isalpha())
'''



#isdecimal


'''print(a , a.isdecimal())
print(b , b.isdecimal())
print(c , c.isdecimal())
print(d , d.isdecimal())
print(e , e.isdecimal())
print(f , f.isdecimal())
print(g , g.isdecimal())'''


#isdigit

'''print(a, a.isdigit())
print(b, b.isdigit())
print(c, c.isdigit())
print(d, d.isdigit())
print(e, e.isdigit())
print(f, f.isdigit())
print(g, g.isdigit())'''


#isnumeric

'''print(a, a.isnumeric())
print(b, b.isnumeric())
print(c, c.isnumeric())
print(d, d.isnumeric())
print(e, e.isnumeric())
print(f, f.isnumeric())
print(g, g.isnumeric())
'''

#islower

#check string in lower case or not
'''
print(a, a.islower())
print(b, b.islower())
print(c, c.islower())
print(d, d.islower())
print(e, e.islower())
print(f, f.islower())
print(g, g.islower())
'''


#isupper

#check string is upper
'''
print(a, a.isupper())
print(b, b.isupper())
print(c, c.isupper())
print(d, d.isupper())
print(f, f.isupper())
print(e, e.isupper())
print(g, g.isupper())
'''

#isspace

'''print(a, a.isspace())
print(b, b.isspace())
print(c, c.isspace())
print(d, d.isspace())
print(e, e.isspace())
print(f, f.isspace())
print(g, g.isspace())'''




#istitle

 #check all words in a string first letter is in capital

''' print(a, a.istitle())'''

#endswith()  Return true value
'''a = "Harry potter"
print(a.endswith("r"))
print(a.endswith("t",6,9))'''

#startswith()
'''a = "Harry Potter"
print(a.startswith("H"))
print(a.startswith("P",6,9))'''

#swapcase()  - swaps case ,lower case become upper case and vice versa
'''a = "Harry Potter"
print(a.swapcase())'''


#strip() - Retuern the trimmed version of the string
'''a = "    *******Harry Potter ........      "
print(a)
print(a.strip(".,*, "))'''


#split() - splits the string at the specified separator , and return a list

'''a = "#OOHF#JJSBJ#BJSJBJ#BD"
print(a.split("#"))

b = "HI.I am 23 23. and how aare you"
print(b.split("."))'''


#ljust()

'''a = "harry potter"
x = a.ljust(20,"*")
print(x,"is my movie of the year")'''

#rjust()

'''a = "harry potter"
x = a.rjust(20,"*")
print(x,"is my movie of the year")'''


#replace

'''a = "My name is Piyush. Piyush is a good boy"
print(a)
print(a.replace("Piyush","Bittu"))'''


#rindex()

'''a = "Piyush Kumar Jha"

print(a.rindex("Kumar"))'''

#rfind()
'''
a = "Piyush kumar jha"
print(a.rfind("kumar"))'''


#slicing in string

'''a = "Piyush kumar jha"
print(a)
print(a[0:6])
print(a[7:12])
print(a[:6])
print(a[-4:])'''



# Problem solving

#Q1. get fibonacci series upto 10 number
'''a = 0
b= 1
n = int(input("Enter the number : "))
if n == 1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)'''


#Q2.Number is prime or not

'''num = int(input("Enter a number : "))
if num <=1:
    print("It is not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("NUMBER IS NOT A PRIME NUMBER")
            break
    else:
        print("IT IS A PRIME NUMBER")'''



#Q3. program to find the palindrome of integer

'''num = int(input("Enter the number : "))
temp = num
reverse = 0
while(num>0):
    digit = num%10
    reverse = reverse*10 + digit
    num = num //10
if temp == reverse:
    print("NUMBER IS PALINDROME")
else:
    print("NUMBER IS NOT PALINDROME")'''



#Q4. program to calculate the area of a calculator
'''


their is some problem in this code 
print("***Area calculator***")
while True:
    print("""Press 1  to get the area of square
    Press 2 to get the area of rectangle
    Press 3 to get the area of circle
    Press 4 to get the area of triangle""")

    choice = int(input("Enter the choice between 1 - 4 : "))

    if choice == 1:
        while True:
            side = float(input("Enter the side of the square"))
            area = side ** 2
            print("The area of square is :", area)
            repeat = input("Do you want to repeat with square again?")
            if repeat == "No":
                break
    elif choice == 2:
        while True:
            length = float(input("Enter the length of the rectangle: "))
            breadth = float(input("Enter the breadth of the rectangle: "))
            area = length * breadth
            print("Area of the rectangle is : ", area)
            repeat = input("Do you want to repeat with rectangle again?")
            if repeat == "No":
                break
    elif choice == 3:
        while True:
            radius = float(input("Enter the radius of the circle : "))
            area = radius * 3.14 * radius
            print("Area of the circle is :", area)
            repeat = input("Do you want to repeat with circle again?")
            if repeat == "No":
                break

    elif choice == 4:
        while True:
            base = float(input("Enter the the base of the circle : "))
            height = float(input("Enter the height of the circle : "))
            area = (base * height) / 2
            print("Area of the triangle is : ", area)
            repeat = input("Do you want to repeat with triangle again?")
            if repeat == "No":
                break
    repeat1 = input("DO you want to repeat the menu again ?")
    if repeat1 == "no":
        break'''



a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"

# Q1. write the program to seperate the following string into coma(,)seperated value

'''b = a.split(".")
print(b)'''

#Q2. write a program to sort the string in alphabetically in python
'''a = input("ENTER ANY THING : ")
b = sorted(a)
print(b)'''

#Q3. write a program to remove a given character from a string
'''
a = "PIYUSH KUMAR JHA"
b = a.replace("P","") # we can not delete anything but replace
print(b)'''

#Q4. write a program to remove the dot(.) form the string
'''z = "P.I.Y.U.S.H"
b = z.replace(".","")
print(b)'''

#Q5. Write a program to check the number of occurrence of a substring in a string

'''a = "piyush kumar jha  is has very  is jha's in his life"
b = a.count("is")
print(b)'''


#1. Take a input from the user into string form and then reverse it

'''a = input("Enter anything here : ")
print(a[::-1])'''


#2. write a program to check if a string contain only digits

'''a = input("Enter anything here : ")
print(a.isdigit())
'''

#3. write a program to check string is palindrome

'''a = input("Enter any thing but only one word not string")
rev = a[::-1]
if a == rev:
    print("IT IS PALINDROME")
else:
    print("NOT PALINDROME")'''


#4. write a program to find the number of vowels in a string

'''a = input("Enter the string : ")
vowels = 0
for i in a:
    if i =="a" or i =="e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i =="I" or i == "O" or i =="O" or i == "U":
        vowels += 1
print("number of vowels in string is",vowels )'''


#5. write a program to check if every word in a string begins with a capital letter

'''a = input("Enter any thing you want to know : ")

print(a.istitle())'''


# LISTs

'''
List is the collection of ordered and mutual data
List are written inside the squared brackets
the value inside a list is separated by comma(,)
mutable means once list is created and then can be changed 
multiple datatype can be written indise a list
'''

'''fruits = ["apple","Mango", "banana","12","14.20"]
print(fruits)
print(type(fruits))
'''
#slicing in the list
'''
a = ["Piyush","kumar","jha"]
print(a[0])
print(a[-3])
print(a[1:3])
print(a[:2])
print(a[::1])
print(a[::-1])
print(a[-1:-3:-1])'''


#List Iteration

#interation using for loop

'''a = ["Bittu","is","very","smart"]
for i in a :
    print(i)'''

#interation using for loop with range and length function

'''a = ["Bittu","is","very","smart"]
for i in range(len(a)):
    print(i)
    print(a[i])'''

#iteration using while loop
'''
a = ["Bittu","is","very","smart"]
i = 0
while(i<len(a)):
    print(a[i])
    i +=1
'''

#using short-hand for loop

'''a = ["Bittu","is","very","smart"]
[print (i) for i in a]'''

#LIST FUNCTIONS

'''a = ["PIYUSH","PRINCE","AYUSH","KUMAR","JHA","PIYUSH"]
print(a)'''

#find the length of the string
'''print(len(a))'''

#to count the occurnce of a particular element
'''print(a.count("PIYUSH"))'''

#add element in the list
'''a.append("DIVYANSHU")
print(a) '''

#add element in a list a specific location

'''a.insert(1,"VISHNU G")
print(a)'''

#to remove from the list
'''a.remove("PIYUSH")
print(a)'''

#to remove from a specific location

'''print(a.pop(1))
print(a)'''



'''a = ["PIYUSH","PRINCE","AYUSH","KUMAR","JHA","PIYUSH"]'''

# to create a copy of a list
'''b = []
print(b)
b = a.copy()
print(b)'''

#to access an element

'''print(a.index("JHA"))'''

# to entend the list

'''c = ["VISION","GOOD"]
a.extend(c)
print(a)'''

# to reverse the list
'''
a.reverse()
print(a)
'''

#to sort the list

'''a.sort()
print(a)
'''

#to clear all the data from the list

'''a.clear()
print(a)'''

# LIST COMPREHENSION

l1 = [10,2,45,67,88,76,44,33]

'''l2 = []
for i in l1:
    print(i)
    l2.append(i)
print(l1,"\n",l2)'''

'''l3 = [i for i in l1]
print(l3)'''

# Problem solving on list

'''A = ["Rose","Rachel","Monica","Joe"]'''

#Q1. write program to swap 1st and 4th element
'''print(A)
A[0],A[3]=A[3],A[0]
print(A)'''

#Q2. write a program to add a new value at 2nd postion

'''A.insert(1,"PIYUSH")
print(A)'''

#3. Write a program to delete a value from the second postion

'''A.pop(2)
print(A)'''

B = [13,7,12,10]

#4. write a program to multiply all the B List elements
'''mul = 1
for i in (B):
    mul *=i
print(mul)
'''

#5.write a program to get the largest amd smallest number form the list

'''print(B)
B.sort()
print(B)
print("THE LARGEST VALUE IN THE GIVEN LIST",B[-1])
print("THE SMALLEST VALUE IN THE GIVEN LIST",B[0])'''


# TUPLES

'''
collection of ordered and un-mutable data
for tuple no brackets are mandatory . By choise you can use parenthesis
the values inside seperated by comma(,)
one created can not be changed
multiple data type can be written inside the tuple
'''
'''a = "Apple","banana","Orange",1,23,4,5
print(a)
print(type(a))
b = "JHA",
print(b)
print(type(b))'''

#slicing and iteration in tuples


#slicing
'''a = ("Vivo","apple","oppo","Poco")
print(a[1:4])
print(a[:3])
print(a[2:])
print(a[::2])
print(a[::-1])'''

# Iteration
'''a = ("Vivo","apple","oppo","Poco")'''

#with for loop
'''for i in a:
    print(i)'''

# along with range and length in for loop

'''for i in range(len(a)):
    print(a[i])
'''
#along with while loop
'''i = 0
while i <len(a):
    print(a[i])
    i+=1'''


#Conversion of tuple and tuple function

'''a = ("oneplus","Nokia","redmi")
print(type(a))
a = list(a)
print(type(a))
a.append("SAMSUNG")
print(a)
a = tuple(a)
print(type(a))
print(a)
print(a.count("redmi"))
print(a.index("redmi"))'''



# INTRODUCTION TO DICTIONARIES

"""Dictionary allow user to write the data in the form of key and values
Dictionary are enclosed inside curly brackets{}
key and values are seperated by colon
Every key value pair is seperated by a comma(,)
"""

'''Employee_Data = {"name":"PIYUSH","age":24,"Gender":"Male"}
print(Employee_Data)
print(Employee_Data["age"])'''

#Iteration in dictionary

'''Student = {"Name":"Piyush","Class":"6th","Roll_no":20}'''

#printing all the key name one by one
'''for x in Student:
    print(x)
    '''

#print the value one by one
'''for x in Student:
    print(Student["Roll_no"])'''

#Using value function
'''for x in Student.values():
    print(x)'''

#using the items function
'''for x,y in Student.items():
    print(x,"=",y)'''

'''Student = {"Name":"Piyush","Class":"6th","Roll_no":20}'''

#get
'''x = Student.get("Roll_no")
print(x)'''

#item
'''a = Student.items()
print(a)'''

#keys
'''b = Student.keys()
print(b)'''

#values
'''c = Student.values()
print(c)'''

#copy
'''d = Student.copy()
print(d)'''


#Nested Dictionary

'''Employe = {1:{"Name":"Piyush","Age":21},2:{"Name":"Prince","Age":19},3:{"Name":"Ayush","Age":22}}
print(Employe)
print(Employe[2]["Age"])'''


#Problem Solving

#Q1. write a python program to sort the dictionary by values

'''
a = {"a":12,"b":23,"c":6,"d":91,"e":45}
a = sorted(a.values())
print(a)'''

#Q2. write a python script to print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys

'''a = {}
for i in range(1,16):
    a[i] = i*i
print(a)'''

#3. write a python program to multiply all the items in a dictionary

'''a = {"a":1,"b":2,"c":3,"d":4,"e":5}
product = 1
for i in a:
    product *=a[i]
print(product)'''

#4. Write a python program to sort a dictionary by key

'''a = {12:"a",56:"b",23:"c",48:"d",91:"e"}
a = sorted(a.keys())
print(a)'''


#Introduction to sets

'''
set are the unordered set of data every elements inside the set is unique and mutual 
set are writtrn inside the curly brackets 
the value inside a sets is seperated by comma(,)
nutuale means and once  created they can be changed
'''
'''a = {"Piyush","KUMAR","JHA"}
print(a)
print(type(a))
for x in a:
    print(x)'''

# function of sets

'''a = {"Piyush","KUMAR","JHA"}
b = {"NEHA","MEGHA","SHIVANGI"}
c = {"CAR","BUS","TRUCK"}'''
#add
'''a.add("AYUSH")
print(a)'''

#pop
'''a.pop()
print(a)
'''

#remove
'''a.remove("JHA")
print(a)'''

#discard
'''a.discard("KUMAR")
print(a)'''

#copy
'''b = a.copy()
print(b)'''

#isdisjoint
'''print(a.isdisjoint(b))
print(a.isdisjoint(c))
'''

#issubset

'''print(a.issubset(b))
print(a.issubset(c))'''

#issuperset

'''print(a.issuperset(b))
print(a.issuperset(c))'''

#update

'''a.update(b)
print(a)'''

#clear
'''a.clear()
print(a)'''

#union

'''print(a.union(b))'''

#Difference
'''print(a.difference(b))'''

#difference update

'''a.difference_update(c)
print(a)'''

#intersection

'''print(a.intersection(b))'''

#intersection update

'''a.intersection_update(b)
print(a)'''

#symmetric difference

'''x = a.symmetric_difference(c)
print(x)'''

#symeetric update

'''a.symmetric_difference_update(c)
print(a)'''

#PROBLEM SOLVING

#Q1. write a program to find thr max and min in a set

'''a = {12,4,5,67,86,8,5,7}
maximum = max(a)
minimum = min(a)
print("MINMIMUM VALUE : ",minimum)
print("MAXMIMUM VALUE : ",maximum)'''

#Q2. write a program to find the comman elements in three lists using sets

'''a = [1,5,6,8,2]
b = [4,5,6,7]
c = [1,9,6,2,5]
print(set(a) & set(b) & set(c))'''

#Q3. write a program to find the difeerence between two sets

'''a = {1,5,6,8,2}
b = {1,9,6,2,5}
print(a.difference(b))'''

#Q4. write a program to remove an item from a set of is present in the set

'''a = {1,5,6,8,2}
a.discard(8)
print(a)'''

#Q5. write a program to check if a set is a sub set of another set

'''a = {1,2,3,4,5,6}
b = {2,3,4}
print(b.issubset(a))'''

#Introduction to function

'''
Function are the set of code which once created they can be used throughout the program 
function help break our program into smaller parts and help it look more organized and manageable.
'''

'''def hello():
    print("Hello world")

hello()'''

'''def add():
    x = 56
    y = 23
    print(x+y)
add()'''

#parameters and aruguments

'''def add(x,y):
    print(x + y)

add(12,67)'''

'''def rectangle(length,width):
    print("Area of rectangle is : ",length*width)

rectangle(12,2)'''

'''def hello(*name):
    print("Hello,My  name is", name[2])
hello("PIYUSH","YASH","JHA")'''

#Returnn statement

'''
return keyword in python is used to exit a dunction and return the value of the function
'''

'''def hello():
    return ("Hello world")
print(hello())
'''

'''def add(a,b):
    return (a+b)
print(add(12,4))'''

#Recursion in python
'''
recursion in most com only used mathematical and programming concept
in simple words recursion means a fucntion can call itself giving us a benefits of looping through data in order to get a result
'''

'''def hello():
    print("hello")
    return  hello()
print(hello())'''

'''def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

print(factorial(5))'''

#Lambda function in python
'''
It is used when an anonymous function is required for a short period of time
it can take numerous arguments
it can only have ine expression
'''
'''a = lambda b: b*5
print(a(4))'''

'''x = lambda a,b,c:(a+b)*c
print(x(3,7,2))'''

#Local and Global variable

#--->>Local varibale
'''
local varibale they are restricted to one code of block can not be changed throughout the program 
'''

'''x = 24
print(x)
def xyhello():
    x = 25
    return x
print(xyhello())
print(x)'''
#--->>Global variable
'''
Global variable are not restricted to one block of code and thay can be cahnged throughout the program
'''

'''x = 24
print(x)
def xyhello():
    global x
    x = 25
    return x
print(xyhello())
print(x)'''

# PROBLEM SOLVING ON FUNCTION

#Q1. Write the function to find the maximum of three number in python

'''def max(x,y,z):
    if ((x>y)&(x>z)):
        print(x,"is the gretest")
    elif((y>x)&(y>z)):
        print(y,"is the greatest")
    else:
        print(z,"is the gratest number")
max(8,2,1)'''

#Q2. write a python function to create and print a list where the values are square of number between 1 and 30

'''def create_list():
    l = []
    for i in range(1,31):
        l.append(i*i)
    return l
print(create_list())'''

#Q3. write a python function that takes a number as a parameter and check if the number is prime or not

'''def check_prime(num):
    if num ==1:
        print("NOT A PRIME NUMBER")
    if num == 2:
        print("It is a prime number")
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                print("It is not prime number")
                break
        else:
            print("It is a prime number")

check_prime(37)'''

#Q4. write a python function to sum all the number in a list

#solution 1
'''def add(numbers):
    total = 0
    for i in numbers:
        total = total+i
    return total
print(add([12,4,5,6,7]))'''

#solution 2 using recurssion

'''def add(number):
    if len(number)==1:
        return (number[0])
    else:
        return (number[0])+add(number[1:])
print(add([12,4,5,6,7,8]))'''

#Q5. write a python  program to solve the fibonacci sequence using recursion

'''def fs(num):
    if num ==1:
        return 0
    elif num == 2:
        return 1
    else:
        return (fs(num-1)+fs(num-2))
print(fs(7))'''

#Introduction to Modules
'''
modules are the (.py) files that contain set of function you want to include in your program
'''
#in-built modules
''' these are 3 in-built module
Datetime 
random
Math
'''

#Datetime
'''import datetime
x = datetime.datetime.now()
print(x)'''
'''y = datetime.datetime(2004,12,18)
print(y.strptime("%a"))'''

#rondom
'''import random
l = ["HEADS","TAILS"]
y = random.choice(l)
x=random.randint(1,100)
print(x)
print(y)
'''

#math
'''import math
x = max(9,45,87)
y = min(45,2,66)
print(x)
print(y)
z = pow(2,4)
print(z)
m = math.sqrt(256)
print(m)
n = abs(-311)
print(n)
f = math.floor(12/5)
print(f)
k = math.ceil(2.1)
print(k)
'''

#creation of modules
'''
to create a module we save the file using (.py)
'''
'''import demo_module # import demo_module as d
a = demo.add(5,9)
print(a)'''

'''import demo_module as d
b = d.employee["Name"]
print(b)'''





