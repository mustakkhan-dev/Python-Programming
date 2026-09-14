#1st Program -

marks = [94.8, 85.6, 34.2, 22.4]
print(marks)
print(type(marks))

#2nd Program - 

marks = [97.6, 87.9, 76.4, 56.4, 34.2]
print(len(marks))
print(marks[0])
print(marks[1])
print(marks[4])

#3rd Program -

student = ["Mustak", 97.7, 20, "Chandaneswar"]
print(student)

#4th Program -

str = "Mustak"
print(str[0])        
str[0] = "N"  # Showing error because "STR" is immutable so it cannot change or assign anything! 
print(str)

#5th Program -

str = ["Mustak", 20 , "undergraduated"]
str[0] = "Khan"                             # Execute because 'list' are mutable!
print(str)

#6th Program -

marks = [87, 64, 33, 95, 76]
print(marks[:4])
print(marks[0:len(marks)])
print(marks[-5:])

#7th Program -

num = [96, 86, 76, 66]
print(num[:3])
print(num[-4:len(num)])
print(num[-3:-1])
print(num[0:len(num)])

#8th Program - Use of 'list.append()' method - It means "Adding Value in Ending Position"

list = [2, 1, 3]
list.append(4)
print(list)

# Use of 'list.sort()' method - It means "Ascending Order"

list = [2, 1, 4, 3]
list.sort()
print(list)

# Use of 'list.sort(reverse=True)' method - It means "Descending Order"

list = [2, 1, 3, 4]
list.sort(reverse=True)
print(list)

# Use of 'list.reverse' method - It means "Reverse the Whole List"

list = [2, 1, 3, 4]
list.reverse()
print(list)

# Use of 'list.insert(index,element)' method - It means "Adding Value at Index Position"

list = [2, 1, 3, 4]
list.insert(2,7)
print(list)
list.insert(4,8)
print(list)

# Use of 'list.remove()' method - It means "Removes first occurrence element"

list = [2, 3, 4, 5, 3]
list.remove(3)
print(list)

# Use of 'list.pop(idx)' method - It means "Removes particular element at index position"

list = [2, 3, 4, 9, 8]
list.pop(4)
print(list)


"TUPLES IN PYTHON"

#9th Program - 

list = (32, 44, 55, 32, 45)
list1 = list[0]
print(list1)
list2 = list[4]
print(list2)

#10th Program - 'Single element tuple'

list = (1,)
print(type(list))
print(list)

#11th Program -

# Use of 'tup.count()' method - It means "Find index value/position"

tup = (1, 2, 3, 4, 3)
var1 = tup.index(3)
print(var1)

# Use of 'tup.count()' method - It means "Count elements how many times present"

tup = (1, 2, 4, 5, 2, 1, 2)
tup1 = tup.count(2)
print(tup1)


# Question 1 - WAP to ask the user to enter names of their 3 favourite movies & store them in a list ?

x = input("Enter your first movie name = ")
y = input("Enter your second movie name = ")
z = input("Enter your third movie name = ")

var1 = [x, y, z]
print(var1)

# Same question different process -  

movies = []
movies.append(input("Enter your first movie = "))
movies.append(input("Enter your second movie = "))
movies.append(input("Enter your third movie = "))

print(movies)

# Question 2 - WAP to check if a list contains a palindrome of elements ?

list = [1, 2, 3, 2, 1]

copy_list = list.copy()
copy_list.reverse()

if(list == copy_list):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")


# Question 3 - WAP to count the number of students with the "A" grade in the following tuple ?

#("C", "D", "A", "A", "B", "B", "A") and Store the above values in a list & sort them from "A" to "D"??


tup = ("C", "D", "A", "A", "B", "B", "A")

tup1 = tup.count("A")
print(tup1)

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)