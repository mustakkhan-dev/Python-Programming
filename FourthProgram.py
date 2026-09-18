"DICTIONARY IN PYTHON"

# 1st Program -

info = {
    "name" : "Mustak Khan",
    "age" : 20,
    "from" : "Balasore",
    "study" : "Centurion",
    "sec" : "A",
    "subject" : ("Architecture", "Security", "DevOps"),
    "marks" : [94.09, 88.08, 92.90]
}

print(info)
print(type(info))

# 2nd Program -

dict = {
    "name" : "Mustak Khan",
    "age" : 20,
    "from" : "Balasore",
    "cgpa" : 8.55,
    "marks" : [96, 89, 76]
}

print(dict["name"])
print(dict["cgpa"])         # This method use to print only this line.
print(dict["age"])

# 3rd Program -

dict = {
    "name" : "Mustak",
    "age" : 20,
    "from" : "Balasore"
}

dict["name"] = "Khan"      # Change old name to new name 
dict["surname"] = "MK"     # Add on dictionary new line

print(dict)
print(dict["name"])
print(dict["from"])

# Question 1 - We can print null dictionary? Then add one value ?

null_dict = {}
print(null_dict)

null_dict = {}

null_dict["name"] = "Mustak Khan"
print(null_dict)

# 4th Program - Nested Dictionaries

student = {
    "name" : "Mustak Khan",
    "score" : {
        "chem" : 98,
        "phy" : 99,
        "math" : 88
    }
}

print(student)

# 5th Program -

student = {
    "name" : "Khan",
    "score" : {
        "chem" : 98,
        "phy" : 99,
        "math" : 88
    }
}

print(student["score"]["chem"])       # Use for knowing that topic/subject     
print(student["score"]["math"])

# 6th Program -

dict = {
    "name1" : "Mustak Khan",
    "name2" : "Muskan Khatun",
    "name3" : "Halima Bibi",
    "name4" : "Ramjan Khan",
    "age1" : 20,
    "age2" : 16,
    "age3" : 32,
    "age4" : 37,
    "work" : {
        "Mustak" : "Student",
        "Muskan" : "Student",
        "Halima" : "House Wife",
        "Ramjan" : "Chef"
    }
}

print(dict)
print(dict["name1"])
print(dict["work"])
print(dict["work"]["Ramjan"])
print(dict["name4"])

dict["name1"] = "Khan Mustak"
print(dict["name1"])

dict["name4"] = "Khan Ramjan"
print(dict["name4"])

dict["name3"] = "Bibi Halima"
print(dict["name3"])

dict["name2"] = "Khatun Muskan"
print(dict["name2"])


# 7th Program - Use of "myDict.keys()" method - It means returns all keys.

student = {
    "name" : "Mustak Khan",
    "subject" : {
        "phy" : 98,
        "chem" : 99,
        "math" : 80
    }
}
print(student.keys())    

print(list(student.keys()))  # Typecasting means 'dict_keys' convert to 'list' format.

print(len(student.keys()))   # Use for know length of 'dict_keys'.

print(len(list(student.keys()))) # Use for know the length of list.


# Use of 'myDict.values()' method - It means returns all values.

student = {
    "name" : "Mustak Khan",
    "subject" : {
        "phy" : 98,
        "chem" : 99,
        "math" : 80
    }
}
print(student.values())
print(list(student.values()))

# Use of 'myDict.items()' - It means returns all '(key,val)' pairs as tuple.

student = {
    "name" : "Mustak",
    "score" : {
        "first" : 9,
        "second" : 8,
        "third" : 10
    }
}
print(student.items())

print(list(student.items()))

pairs = list(student.items())  # We can access single by single tuple to convert in list form.
print(pairs[0])
print(pairs[1])

# Use of 'myDict.get("Key")' - It means returns key according to value.

student = {
    "name" : "Mustak Khan",
    "age" : 20
}

print(student["name"])   # Give same o/p like 'student.get("key")' but difference are ?
print(student.get("name"))

# # Difference are -

print(student["name2"])  # It gives error.

print(student.get("name2"))  # But it gives None.

# Use of 'myDict.update(newDict)' - It basically pass additional dictionary or (key,value) use of '{}'.

student = {
    "name" : "Mustak Khan",
    "age" : 20
}

print(student.update({"from":"BBSR"}))  # Direct Process for assigning.
print(student)

# Same problem -

student = {
    "name" : "Mustak Khan",
    "age" : 20
}

#new_dict = {"from":"BBSR", "sub":"Eng"}    # Assigning variable.

new_dict = {"name":"MK"}    # Changing name also.

student.update(new_dict)
print(student)


"SET IN PYTHON"

# 8th Program -

collection = {1, 2, 3, 4}

print(collection)
print(type(collection))

# 9th Program -

student = {1, 2, 2, 3, "Mustak", "World"}

print(student)           # Set ignores duplicate values.
print(len(student))

# 10th Program -

var = {1, 2, "Mustak", "hello", 4, 5, "khan"}

print(var)         # Value positions are different because 'set' are unordered.
print(len(var))

# 11th Program - Question 1 - Can print empty set ??

var1 = set()
print(var1)


# 12th Program - Use of 'set.add(el)' method - It means adding values in set.

student = {1, 2, 3}
student.add(4)
print(student)

student = set()

student.add(1)
student.add(2)
student.add(7)
student.add("Mustak")
student.add((1, 2, 3))

print(student)

# Use of 'set.remove(el)' method - It means removes elements in set.

var1 = {1, 2, 3, "Mustak"}

var1.remove("Mustak")
var1.remove(2)
print(var1)

var = set()

var.add(1)
var.add(2)
var.add("Mustak")
var.add("Khan")
var.add("Muskan")
var.add("Annie")

var.remove("Khan")
var.remove(1)
var.remove(2)
print(var)

# Use of 'set.clear()' method - It means clear/empty to the set.

student = {1, 2, 3, 5}

student.clear()
print(student)
print(len(student))

# Use of 'set.pop()' method - It means removes value randomly.

var1 = {"Mustak", "Khan", "Mk", "Annie"}

var1.pop()
print(var1)

# Use of 'set.union(set2)' method - It means union of 2 sets.

set1 = {1, 2, 3}
set2 = {2, 3, 4}

var = set1.union(set2)
print(var)
print(set1)
print(set2)

# Use of 'set.intersection(set2)' method - It means intersection of 2 sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

var = set1.intersection(set2)
print(var)


# Question 1 - Store following word meaning in a python dictionary ?

dict = {
    "table" : ("a piece of furniture", "list of facts & figures"),
    "cat" : "a small animal"
}

print(dict)

# Question 2 - You are given list of subjects and assume how many classroom required ?

subjects = {
    "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
} 

print(subjects)
print(len(subjects))   # This line to know how many class are required.

# Question 3 - WAP to enter marks of 3 subjects from the user and store them in a dictionary ?

marks = {}

x = int(input("Enter your first subject marks = "))
marks.update({"first":x})

x = int(input("Enter your second subject marks = "))
marks.update({"second":x})

x = int(input("Enter your third subject marks = "))
marks.update({"third":x})

print(marks)

# Question 4 - Figure out a way to store 9 & 9.0 as separate values in the set ?

values = {
    ("float", 9.0),
    ("int", 9)
}

print(values)