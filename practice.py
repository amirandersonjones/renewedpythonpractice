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

animalDict = {
    "name": "Hope",
    "species": "dog",
    "habitat": "house"
}
print(animalDict)
print(id(animalDict))

animalDict["age"] = 1
print(animalDict)

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
