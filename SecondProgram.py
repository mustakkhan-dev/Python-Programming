"STRING"

#1st Program -

str1 = "Mustak Khan"
str2 = 'Mustak Khan'
str3 = '''Mustak Khan'''

#2nd Program -

str1 = "I am mustak khan and now learning book's"
print(str1)

#3rd Program - (Concatenation Process)

str1 = "Mustak"
str2 = "Khan"
print(str1 + str2)

#4th Program -

str1 = "hello"
str2 = "world"
print(str1+str2)

#5th Program -

str1 = "Mustak"
len1 = len(str1)
str2 = "Khan"
len2 = len(str2)
print(len1)             #Use of len operations which counting length of str
print(len2)
final_str = (str1 +" "+ str2)
len3 = len(final_str)
print(len3)
print(final_str)

#6th Program -

var1 = input("Enter your name :")
var2 = int(input("Enter your age :"))
var3 = input("Where are you from :")
var4 = input("Enter your university name :")
var5 = input("Enter your college name :")
var6 = input("Enter your school name :")
print("Welcome!", var1)
print("You are now",var2,"years old")
print("You are from",var3)
print("You are currently pursing B.Tech at",var4)
print("You have completed your higher education from",var5)
print("You have completed your matriculation from",var6)

#7th Program -

str1 = "Mustak Khan"
str2 = "I am from Balasore"
len1 = len(str1)
len2 = len(str2)
print(len1)
print(len2)
final1 = (str1 + str2)
print(final1)

#8th Program  -

str = "Mustak-Khan"
chr = str[4]
print(chr)

#9th Program -

str = "Python-Programming"
print(str[4])


"SLICING IN PYTHON"

#10th Program -

str = "Mustak Khan"
print(str[0:6])

#11th Program -

str = "Apna College"
print(str[:len(str)])
print(str[:4])
print(str[1:len(str)])
print(str[0:6])

#12th Program - 'Negative Slicing'-

str = "apple"
print(str[-3:-1])
str = "Iam Mustak"
print(str[-6:])    

#13th Program - Use to find ending chr are same or not ?

str = "I am now studying python for Apna College"
print(str.endswith("ege"))  # True statement
print(str.endswith("ega"))   # False statement

#14th Program -  Use for change first letter are capital ?

a = "mustak khan"
print(a.capitalize())

#15th program - Use of changing old values to new values ?

str = "I am now learning python programming"
print(str.replace("python","java"))
str = "I am mustak khan"
print(str.replace("m","n"))


#Question - WAP to input User's name & print its length ?

str = input("Enter your name : ")
len1 = len(str)
print(len1)

#Question - WAP to find the occurrence of '$' in a String ?

str = "$Hi, I am a $ symbol and use $899.9"
print(str.count("$"))

"Conditional Statement"

#16th Program -

age = 24

if(age >= 18):
    print("Can vote")
    print("Can Drive")

#17th Program -

age = 16 
if(age >= 18):
    print("Can apply for license")     # O/P is Nothing because check condition is false.

#18th Program - 

light = "green"

if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Ready")
elif(light == "green"):
    print("Go")

#19th Program -

num = 5
if(num > 3):
    print("Greater than 3")
if(num > 2):
    print("Greater than 2")

#20th Program -

light = "Pink"

if(light == "Red"):
    print("Stop")
elif(light == "Yellow"):
    print("Ready")
elif(light == "Green"):
    print("Go")

else:
    print("Light is broken!")

#21th Program -

age = 17

if(age > 18):
    print("You can vote now!")
else:
    print("Sorry, you cannot vote now!")

#22th Program - 

x = input("Enter your name : ")
y = int(input("Enter your marks : "))
print(x)

if(y >= 90):
    print("Grade is A")
elif((y > 90) or (y >= 80)):
    print("Grade is B")
elif((y > 80) or (y >= 70)):
    print("Grade is C")
else:
    print("Grade is D")

"NESTING"

#23th Program -

age = 19

if(age >= 18):
    if(age >= 80):
        print("Cannot Drive!")
    else:
        print("Can Drive!")
else:
    print("Cannot Drive!")

# Same Program -

age = 92

if(age >= 18):
    if(age >= 82):
        print("Cannot Drive Anything!")
    else:
        print("Can Drive!")
else:
    print("Cannot Drive Bike")


# Question - WAP to check if a number entered by the user is odd or even ?

x = int(input("Enter your number = "))
if(x % 2 == 0):
    print("Number is Even")
else:
    print("Number is Odd")

# Same question -

x = int(input("Enter your number = "))
num1 = x % 2

if(num1 == 0):
    print("Number is Even!")
else:
    print("Number is Odd!")


# Question - WAP to find the greatest of 3 numbers entered by the user ?

x = int(input("Enter your first number = "))
y = int(input("Enter your second number = "))
z = int(input("Enter your third number = "))

if((x > y) and (x > z)):
    print("First number is greatest!")
elif((y > z) and (y > x)):
    print("Second number is greatest!")
else:
    print("Third number is greatest!")

# Question - WAP to check if a number is a multiple of 7 or not ?

x = int(input("Enter your number = "))

if(x % 7 == 0):
    print("Number is multiple of 7")
else:
    print("Number is not multiple of 7")