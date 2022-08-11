# temperature = 20
# name = "Batman"

# -----IF,ELIF----

# if temperature > 30:
#     print("It's not that bad outside")
#     if temperature < 50:
#         print("it could be warmer")
#     elif temperature > 50:
#         print("Thats what we cann nice weather in Minnesotta")

# elif temperature > 20:
#     if temperature < 32:
#         print("Its still freezing outside")
#     elif temperature > 32:
#         print("well, at least snow will melt!")

# elif temperature < 10:
#     if temperature < 0:
#         print("Why do I live here")
#         print("Like no joke, on time it went from -60 to 40 degrees in one night")
#         print("That's a 100 degree swing in one day, man Texas is looking good right now")

# elif temperature == 20:
#     print("Gee Willkers" + name + ", why do people live in Minnesota")

# else:
#     print("This line is used to catch errors")

# count_list = list(range(1,27, 2))
# print(count_list)

# ------FOR LOOPS----
# animals = ["dog", "cat", "snake", "goat"]
# print(len(animals))

# for animal in animals:
#     print(animal)

# for i in range(len(animals)):
#     print(i, animals[i])

# print(animals[2])

# animals.append("mouse")
# print(animals)
# animals.insert(1,"mouse")
# print(animals)

# while "mouse" in animals:
#     animals.remove("mouse")
#     print(animals)
# # print(animals)

# list = ["thing1","thing2","thing3"]
# for item in list:
#     print(f" This {item} is in my list")

# portList= ["Interface g0/0", "Interface, g0/1", "Interface g0/2"]
# deviceList = ["Catalyst 3650", "Catalyst 3750", "Catalyst 3850"]

# for port in portList:
#     for device in deviceList:
#         print(f"{device}\n {port}\n shut\n")

# names = ["Kali", "George", "Bob", "Mack"]
# for i in range(len(names)):
#     print(i, names[1])

# evens_list = list(range(0,10, 2))
# print(evens_list)
# print(len(evens_list))

# smoresIngredients = ["Chocolate", "Marshmellows", "Graham Crackers"]
# for ingredient in smoresIngredients:
#     if ingredient == "Marshmellows":
# #         continue
# #     print(ingredient)

# smoresIngredients = ["Chocolate", "Marshmellows", "Graham Crackers"]
# for ingredient in smoresIngredients:
#     if ingredient == "Marshmellows":
#         break
#     print(ingredient)


# print("end")

# ------WHILE LOOPS-------

# number = 5

# while number < 20:
#     print(f"This {number} is less than 10")
#     number +=1

#     if number == 15:
#         break

# login = input("Enter a login name ")

# while len(login) < 8:
#     print("Your login must be longer than 8 characters")
#     login = input("Enter a login name")

# print(f"Your login name is {login}")

# check = bool(2+1==2)
# print(check)

# smoresIngredients = ["Chocolate", "Marshmellows", "Graham Crackers"]
# for i in range(len(smoresIngredients)):
#     print(i, smoresIngredients[i], len(smoresIngredients))


# ----iterate through the pizzalist and if the value is cheese add it to the liked_list and then count how many cheese pizzas are liked.

# pizzalist = ["sausage", "sausage", "pepperoni", "cheese", "cheese"]

# liked_list = []
# amount_cheese = 0

# for pizza in pizzalist:
#     if pizza == "cheese":
#         liked_list.append(pizza)
#         amount_cheese +=1
# print(f"{liked_list}, the amount of cheese is: {amount_cheese}")


# pythonList = ["name", 8490, 57, 9]
# new_list = pythonList[::-1]
# print(new_list)


# tenList = ["zero", "one", "two", "three", "four",
#            "five", "six", "seven", "eight", "nine", "ten"]
# print(len(tenList))
# print(tenList[len(tenList)-1])

# ------LIST SLICING----
# print(tenList[1:7])
# print(tenList[:5])
# print(tenList[5:])

# print(tenList[0:10:2])
# print(tenList[0::2])

# print(tenList[4::2])

# more_numbers = ["eleven", "twelve", "thirteen", "fourteen", "fifteen"]

# tenList.extend(more_numbers)
# print(tenList)
# tenList.insert(0, "zeroth")
# print(tenList)

# numbers_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(min(numbers_list))
# print(max(numbers_list))
# numbers_list.pop()
# print(numbers_list)
# numbers_list.pop(0)
# print(numbers_list)
# numbers_list.remove(5)
# print(numbers_list)

# numbers_list=[1, 2, 3, 4, 5, 10, 7, 8, 9, 6]
# numbers_list.sort()
# print(numbers_list)

# ----TUPLES, WHY USE THEM???------
# 1.) tuples are not Mutable
# 2.) data Integrity
# 3.) key-value pairs

# smoresIngredients= ("Chocolate", "Marshmellows", "Graham Crackers")
# print(len(smoresIngredients))
# print(min(smoresIngredients))
# print(max(smoresIngredients))
# moreIngredients=("Mushrooms")
# smoresIngredients.append(moreIngredients) #tuples are not mutable so we can't change them, will get an error message.

# ----DICTIONARIES---
# an unordered list of key-value pairs

# dictExample= {"key":"Value","key2":"Value2", "key3":"Value3"}
# print(dictExample['key'])

# myDict = {
#     "name": "Barry",
#     "species": "bird",
#     "habitat": "tree"
# }

# print(myDict["name"])

# mynewDict =[
#     {"name": "Barry", "species": "bird", "habitat": "tree"},
#     {"name": "Hope", "species": "dog", "habitat": "house"},
#     {"name": "Mosses", "species": "cat", "habitat": "house"}

# ]

# print(mynewDict[1])
# print(mynewDict[1]["species"])

# print(myDict["name"])

# ----ADDING KEYS TO A DICTIONARY----

# animalDict = {
#     "name": "Hope",
#     "species": "dog",
#     "habitat": "house"
# }
# print(animalDict)
# print(id(animalDict))

# animalDict["age"] = 1 #adding age to animalDict
# print(animalDict)
# print(id(animalDict))

# if we use animalDict.get("age", "Error wrong input"), if we make a mistake it will return None and continue to run our program instead of crashing.

# ----REMOVING KEYS FROM DICTIONARY-----

# animalDict = {
#         "name": "Hope",
#         "species": "dog",
#         "habitat": "house",
#         "age": 1
#     }
# print(animalDict)

# del animalDict["age"]
# print(animalDict)

# friendDict = {
#     "friend1": "Kellie",
#     "friend2": "Mary",
#     "friend3": "Gussie",
#     "friend4": "Billie"
# }

# print(friendDict)
# popped_friend = friendDict.pop("friend3")
# print(friendDict)


# animalDict = {
#         "name": "Hope",
#         "species": "dog",
#         "habitat": "house",
#         "age": 1
#     }

# -----get the keys from the dictionary---
# print(animalDict.keys())

# -------turn the keys of a dictionary into a list----
# animaldictkeys = list(animalDict.keys())
# print(animaldictkeys)
# print(animaldictkeys[2])

# -----get the values from the dictionary---
# print(animalDict.values())
# animaldictvalues = list(animalDict.values())
# print(animaldictvalues)
# print(animaldictvalues[3])


# -----OBJECT ORIENTED PROGRAMMING-----

# class Student:
#     pass

# student1 = Student()
# student1.name = "Amir" #this is an attribute
# student1.grade = 100 #this is an attribute

# student2 = Student()
# student2.name = "Kellie"  # this is an attribute
# student2.grade = 110  # this is an attribute

# print(student1.name)
# print(student2.grade)


# animalDict = {
#     "name": "Hope",
#             "species": "dog",
#             "habitat": "house",
#             "age": 1
# }

# print(animalDict.keys())

# listanimaldict = list(animalDict.keys())
# print(listanimaldict)
# print(listanimaldict[2])
# valuelist = list(animalDict.values())
# print(valuelist)

# print(animalDict.items())
# animalList = list(animalDict.items())
# print(animalList[2])
# print(animalList[2][1])

# ITERATING OVER DICTIONARIES
# animalDict = {
#     "name": "Hope",
#     "species": "dog",
#     "habitat": "house",
#     "age": 1,
#     "weight": "20lbs"
# }

# for printoutkeys in animalDict.keys():
#     print(printoutkeys)

# for printoutvalues in animalDict.values():
#     print(printoutvalues)

# for item in animalDict.items():
#     print(item)

# for k,v in animalDict.items():
#     print(k)

# for key, value in animalDict.items():
#     print(f"The key is {key}, the value is {value}")

# for key in sorted(animalDict.keys()):
#     print(key)

# ----COMBINING 2 DICTIONARIES-----
# pizzaPrices = {"Jacks":4, "Digiorno": 7, "Red Baron":6}
# beerPrices= {"Paulaner":12, "Heineken":10, "Blue Moon": 8}
# pizzBeerList = {**pizzaPrices, **beerPrices}
# print(pizzBeerList)

# -------SETS---------
# 1.) sets are unordered
# 2.) unique
# 3.) mutable
# 4.) there are frozen sets if we don't want them changed {a,b,c}

# deviceName = {"Cisco", "Aruba", "CiscoXE"}
# print(deviceName, type(deviceName))

# ingredientList = {"hot dogs", "burgers", "buns"}
# print(id(ingredientList))

# ingredientList.add("mustard")
# print(ingredientList)
# print(id(ingredientList))

# ingredientList.remove("mustard")
# print(ingredientList)

# ingredientList.pop()
# print(ingredientList)

# numberSet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# numberSet.pop()
# print(numberSet)
# numberSet.pop()
# print(numberSet)
# numberSet.pop()
# print(numberSet)


# european_floor = input("What is the number of the european floor?: ")
# us_floor = int(european_floor) + 1
# print(f'The european floor you entered was {european_floor}, That is equal to us floor {us_floor}')

# ingredientList1 = {'Marshmellow', 'Chocolate', 'Graham Crackers'}
# ingredientList1.add('Roast')
# print(ingredientList1)
# ingredientList1.remove('Roast')
# print(ingredientList1)

# ingredientList1 = {'Marshmellow', 'Chocolate', 'Graham Crackers'}
# ingredientList2 = {'Marshmellow', 'Hershey Bar', 'Graham Crackers'}
# print(ingredientList1 - ingredientList2)
# print(ingredientList1.difference(ingredientList2))

# combine 2 sets:
# combinedList = ingredientList1.union(ingredientList2)
# print(combinedList)

# intersectionList = ingredientList1.intersection(ingredientList2)
# print(intersectionList)

# -------------------FUNCTIONS-------------------
# functions-always returns something. Default return will always be None

# import netmiko #3rd party

# print("argument") #built-in

# Custom
# def function1(argument1):
#     print(argument1)


# function1("team fox")

# Bank account
# bankAccount = 0.0

# def deposit(argument1):
#     global bankAccount
#     bankAccount = bankAccount + argument1
#     print(bankAccount)

# def withdraw(argument):
#     global bankAccount
#     bankAccount = bankAccount - argument
#     print(bankAccount)

# deposit(140)
# withdraw(70)
# withdraw(30)

# def addValues(argument1, argument2):
#     sumVar = argument1 + argument2
#     print(sumVar)

# def subtractValues(argument1, argument2):
#     diffVar = argument1 - argument2
#     print(diffVar)

# addValues(55,23)

# Name Generator
# from random import randrange

# firstName = ['adam', 'Becky','Charlie', 'Eggbert', 'Fransine' ]
# lastName = ['Adams', 'Becker', 'Chara', 'Davenport', 'Eggelkrout', 'Franco']

# print(randrange(6))

# def randomName():
#     firstName = ['adam', 'Becky', 'Charlie', 'Eggbert', 'Fransine']
#     lastName = ['Adams', 'Becker', 'Chara', 'Davenport', 'Eggelkrout', 'Franco']

#     print(f"{firstName[randrange(6)]} {lastName[randrange(6)]}")

# randomName()

# A better way to do the above function:

# firstName = ['adam', 'Becky', 'Charlie', 'Eggbert', 'Fransine']
# lastName = ['Adams', 'Becker', 'Chara','Davenport', 'Eggelkrout', 'Franco']

# def randomName(argument1, argument2):


#     print(f"{argument1[randrange(6)]} {argument2[randrange(6)]}")


# randomName(firstName, lastName)


# -----------VARIABLE LENGTH ARGUMENTS---------------

# def addingNumbers(*number):
#     sum = 0
#     for n in number:
#         sum = sum + n
#     print(sum)

# addingNumbers(3,4,5,6)

# ---------------KEYWORD ARGUMENTS = KWARGS--------------------
# def printArguments(*args):
#     for argument in args:
#         print(f"Argument {argument} was passed in")

# printArguments("dominic", "simonetti")

# def printArguments(**kwargs): #defines the function with the special character kwargs
#     for key, value in kwargs.items(): #seperates key-values into key/value categories using the .items()
#         print(f"Argument key is {key} was passed in with the value {value}")

# printArguments(firstName="dominic", lastName="simonetti")

# ---------------INTRODUCTION TO MODULES------------

# from random import randrange

# import sys
# print(sys.path)

# sysList=sys.path
# for path in sysList:
#     print(path)

# 3 places to find libraries you can download from python:
# 1.) standard library
# 2.) third party (pip)
# 3.) local imports (files we wrote and import from our own machine to use in our code.)

# for i in range(10):
#     print(i)

# from random import randrange

# randomNumber = randrange(11)
# print(randomNumber)

# ------------RETURNING MULTIPLE VALUES----------

# def basicMath(argument1, argument2):
#     addedMath = argument1 + argument2
#     multipliedMath = argument1 * argument2
#     subtractMath = argument1 - argument2

#     return addedMath, multipliedMath, subtractMath

# print(basicMath(7, 5))


# x,y,z = basicMath(7,5)
# print(x)
# print(y)
# print(z)

# ---------SCOPE------------
# 1.) Enclosing-functions inside of Functions(inner function)
# 2.) Built-in- available to use anywhere in python
# 3.) Local scope- available inside of the function/local to the function.idented inside of function
# 4.) Global-defined outside of a function.not available inside of the function unless called into it.

# -------------FUNCTIONAL PROGRAMMING-------------
# -Python is known as an object oriented programming language
# -objects have properties and methods
# -methods change the object(use the . to change for example name.lower() is a method)
# -Functional programming is for our use of functions

# ------------------COMPREHENSIONS------------------
# groceryList = ["kwickade", "kwickice", "Monster", "kwickpizza", "Ellisworth Cheese Curds"]
# kwickList = []

# for groceryitem in groceryList:
#     if groceryitem.startswith("kwick"):
#         kwickList.append(groceryitem)
# print(kwickList)

# structure= <nameofnewlist>[<list><iteration><conditional>]
# kwickList = [groceryitem for groceryitem in groceryList if groceryitem.startswith("kwick")]
# print(kwickList)

# friendsList = ["Jeannette", "Kirby", "Brown", "Jace", "Jerry", "Jack", "Queen"]
# jfriendList = []

# for friend in friendsList:
#     if friend.startswith("J"):
#         jfriendList.append(friend)
# print(jfriendList)

# jfriendlist=[friend for friend in friendsList if friend.startswith("J")]
# print(jfriendlist)

# numberslist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# newlist = []
# for num in numberslist:
#     if num % 2 == 0:
#         newlist.append(num)
# print(newlist)

# newlist = [num for num in numberslist if num % 2 == 0]
# print(newlist)

# ------------------KEY:VALUE COMPREHENSIONS------------------

# ageList = {"Jeremy":26, "Beth":19, "Michael":24, "Andy":20, "Danny":26}

# legalDrinking = {key:value for (key, value) in ageList.items() if value > 21}
# print(legalDrinking)


# ------------------LAMBDA FUNCTIONS------------------
# 1.) Intent is to be used only once and keep code short!
# 2.) Single line code.
# 3.) Lambda functions do not have to be name(so they are called anonymous functions).
# 4.) Regular functions return None by default but Lambda functions return @ least one value.

# def basicadd(argument1, argument2):
#     sum = argument1 + argument2
#     return sum

# answer = basicadd(5, 7)
# print(answer)

# addUp = lambda argument1, argument2: argument1 + argument2
# print(addUp(5,7))

# exponential = lambda x: x**2
# print(exponential(8))

# exponential = lambda x, y=2: x ** y
# print(exponential(9))
# print(exponential(9, 3))

# def canDrink(argument1):
#     if argument1 > 20:
#         print("You can drink")
#     else:
#         print("You are not of legal age to drink!")

# canDrink(21)

# reachAge = lambda age: "you can drink" if age > 20 else "you cannot drink"
# print(reachAge(21))


# ------------------MAP FUNCTIONS------------------
# 1.) The map function takes in 2 arguments
# 2.) The first argument is the function you want to use and the second it what you want it to iterate on.

# numberList = [1, 2, 3, 4, 5]

# def cubed(argument1):
#     return argument1 ** 3

# print(cubed(5))

# newnumberList = map(cubed, numberList)
# print(newnumberList)
# print(list(newnumberList))

# numberList = [1, 2, 3, 4, 5]
# newNumberList = list(map(lambda x: x ** 3, numberList))
# print(newNumberList)

# friendList = ["Jeannette", "Kirby", "brown", "jace", "Jerry", "Jack", "Queen"]
# newNameList = list(map(lambda name: name.capitalize(), friendList))
# print(newNameList)

# numberslist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# newlist = []
# for num in numberslist:
#     if num % 2 == 0:
#         newlist.append(num)
# print(newlist)

# newlist = [num for num in numberslist if num % 2 == 0]
# print(newlist)

# agedict = {"Jeremy":26, "Beth":19, "Michael":24, "Andy":20, "Danny":26}
# # for key, value in agedict.items():
# #     print(key, value)

# newdict = {key:value for key, value in agedict.items() if value > 21}
# print(newdict)

# timesTwo = lambda x: x * 2
# print(timesTwo(4))
# def timesTwo(argument1):
#     print(argument1 * 2)

# numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list(map(timesTwo, numberList)))


# ------------------TEXT FILES------------------
# help(open)
# textfile = open('textfile.txt')
# print(textfile)
# textfile.close()

# AUTOMATICALLY OPEN AND CLOSE FILE
# with open('textfile.txt') as f:
#     print("Test")

# with open('textfile.txt') as f:
#     output = f.read()
# print(output)

# with open('textfile.txt') as f:
#     output1 = f.readline()
#     print(output1)

# with open('textfile.txt') as f:
#     output1 = f.readline()
#     print(output1)
#     output1 = f.readline()
#     print(output1)

# with open('textfile.txt') as f:
#     output1 = f.readlines()
#     print(output1)

#     print(output1[1])

# with open('textfile.txt', 'w') as f:
#     # vaName = 'Amir'
#     # f.write(vaName)
#     f.write('Amir\nJones')
#     # f.write('Jones')

# with open('textfile.txt', 'w') as f:
#     friendList = ["Jeannette\n", "Kirby\n", "brown\n","jace\n", "Jerry\n", "Jack\n", "Queen"]
#     f.writelines(friendList)

# with open('textfile.txt', 'r') as old, open('newtextfile.txt', 'w') as new:
#     text = old.readlines()
#     for line in text:
#         new.write(line.upper())

# with open('textfile.txt', 'a') as f:
#     f.write("\nNew Text")

# ------------------Pulling and Writing Files------------------
# import netmiko

# with open('ciscoConfigs.txt', 'w') as f:

#     connection = netmiko.ConnectHandler(
#         ip = 'sandbox-iosxe-latest-1.cisco.com',
#         device_type = 'cisco_xe',
#         username = 'developer',
#         password = 'C1sco12345'
#     )

#     f.write(connection.send_command("show run"))

# ------------GITHUB COMMANDS--------------

# git checkout {file number}-goes back to the file before current head
# (git switch -) -will switch back from the git checkout or git checkout {file number}
# git dif- will show changes that have been added to file
# git log- will show the log of commits
# git log --oneline- will show a shortened version of commit history
# git diff {first file} {second file}- shows the difference between two files. git log-will show you the numbers to put in.
# git status- shows the status of current commits
# git commit --ammend

# ------------OBJECT ORIENTED PROGRAMMING--------------
#An object = something like a person
#An object has properties to it such as height, weight, color, = ATTRIBUTES
#Objects can also have things they do = METHODS

# class PartyAnimal:
#     x = 0
#     def party(self):
#         self.x = self.x + 1
#         print("So far", self.x)

# an = PartyAnimal()
# an.party()
# an.party()
# an.party()

# print(dir(an))


