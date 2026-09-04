"1st Program"

print("My name is Mustak Khan.")
print("I am 20 years old.")

print("I am Mustak Khan", "I am 20 years old")     #Print in same line process.

"2nd Program"

name = "Mustak Khan"
age = 20
price = 243

print(name)
print(age)
print(price)

"3rd Program"
name = "Mustak Khan"
age = 20
print("The name is :", name)
print("Iam years old", age)

"4th Program"
name = "Mustak Khan"
age = 20
price = 3.4
r = True
box = None 

print(type(name))
print(type(age))
print(type(r))
print(type(box))
print(type(price))

"5th Program"
a = 190
b = 90
sum = (a + b)
diff = (a - b)

print(sum)
print(diff)

"6th Program - Arithmetic Operator:"
a = 5
b = 8
print(a + b) # Sum of Numbers
print(a - b) # Substraction of Num
print(a / b) # Division of Num
print(a % b) # Modulus use for find reminder
print(a // b) #Floor Division use for num like 2.67 but o/p show only 2 not show point value
print(a * b) # Multiplication of Num
print(a ** b) # Exponential of num like 5 to the power 8

"7th Program - Relational Operator:"
a = 6
b = 12
print(a == b) #Equal to 
print(a != b) #Not equal to
print(a > b) #Greater than 
print(a >= b) #Greater than equal to
print(a < b) #Less than
print(a <= b) #Less than equal too

"8th Program - Assignment Operator:"
num = 10
num += 5   # Means:- num= 10+5 = 15
print(num)

"9th Program"
num = 10
num -= 5
print(num)  #Means: num = 10-5 = 5

"10th Program - Logical Operator"
'''Use of not operator (Means Opposite)''' 

print(not True)  # o/p comes False because use 'not' operator 
print(not False)

a = 10
b = 5
print(not (a > b))  #Statement is 'TRUE' but comes 'FALSE' because use of 'not' statement
print(not(a < b))   #Statement is 'FALSE' but comes 'TRUE' 

"Use of and Operator:"

val1 = True
val2 = True
print(val1 and val2)

a = True
b = False
print(a and b)

a = 10
b = 20
print(a and b)

"Use of or Operatior"

val1 = True
val2 = False
print(val1 or val2)


val1 = False
val2 = False
print(val1 or val2)

a = 8
b = 6
print((a==b) or (a>b))

"Type Conversion"

a = 2        # Python automatically change to float
b = 4.25
sum = (a + b)
print(sum)

a = int("2") # Change str to int value (Casting Type)
b = 4.25
print(a + b)

a = 4.5
b = float("2") # Change str to float value (Casting Type)
print(a + b)

"INPUT in Python"

x = input("Enter your name : ")
y = input("Enter your age : ")                 # Use str input values
print("Welcome!" ,x )
print("You are now",y,"years old!")

x = int(input("Enter your first number :" ))
y = int(input("Enter your second number :"))     # Use int input values
sum = x + y
print("Your total number is = ",sum)

a = float(input("Enter your first number ="))
b = float(input("Enter your second number ="))
print("First number = ",a)                           # Use float input values
print("Second number = ",b)
sum = a + b
print("Sum of total numbers = ",sum)

# Question 1 - WAP to input 2 numbers & print their sum ?

x = int(input("Enter your first number = "))
y = int(input("Enter your second number = "))
print("First number = ",x)
print("Second number =",y)
sum = x + y
print("Sum of two numbers =",sum)

# Question 2 - WAP to input side of a square & print its area?

a = int(input("Enter your square side = "))
val = a * a
print("Area of square is = ",val)


# Same question some step changes -

a = int(input("Enter your square side = "))
val = a ** 2
print("Area of square is = ",val)

# Question 3 - WAP to input 2 floating point numbers & print their average ?

a = float(input("Enter your first number = "))
b = float(input("Enter your second number = "))
val1 = ((a+b)/2)
print("Total average = ", val1)

# Question 4 - WAP to input 2 int numbers , a and b.
               #print True if a is greater than or equal to b. If not print False?

a = int(input("Enter your first number = "))
b = int(input("Enter your second number = "))
if(a >= b):
 print("Statement is TRUE")
else:
 print("Statement is FALSE")
