

# class Dog():
#
#     def __init__(self, name, age):
#         """Initiated distribute, name and age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Dog sits"""
#         print(self.name.title() + "is now sitting.")
#
#     def roll_over(self):
#         """Dog rolls"""
#         print(self.name.title() + "rolled over!")

# with open('pi_digits.txt') as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())
    # for line in file_object:
    #     print(line.rstrip())
    # lines = file_object.readlines()
# print(lines)
# for line in lines:
#     print(line.rstrip())
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip().strip()
# print(pi_string)
# print(len(pi_string))

# file_name = 'programing.txt'
# with open(file_name, 'a') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love creating new games.\n")
import json

# numbers = [2, 3, 5, 7, 11, 13]
# file_name = 'number.json'
# with open(file_name, 'w') as f_obj:
#     json.dump(numbers, f_obj)
# with open(file_name) as f:
#     numbers = json.load(f)
# print(numbers)

# filename = 'username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What's your name?\n>>> ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print("We'll remember you when you come back, " + username + "!")
# else:
#     print("Welcome back, " + username + "!")











