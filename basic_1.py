

# age = 23
# message = "Happy " + str(age) + "rd Birthday"
# print(message)
# num_1 = 123
# num_2 = 321
# print(num_1 + num_2)
# import this

# motorcycle = ['honda', 'yamaha', 'suzuki']
# print(motorcycle)
# del motorcycle[0]
# print(motorcycle)
# del motorcycle[1]
# print(motorcycle)
# popped_motorcycle = motorcycle.pop()
# print(motorcycle)
# print(popped_motorcycle)
# lasted_owned = motorcycle.pop()
# motorcycle.remove('honda')
# print(motorcycle)
# motorcycle.insert(2, 'ducati')
# print(motorcycle)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse = True)
# print(cars)
# print(sorted(cars,reverse = True))
# print(cars)
# print(len(cars))

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ","
#                              "that was a great trick!")
#     print("I can't wait to see your next trick, " +
#           magician.title() + ".\n")
# print("Thank you! Everyone!")

# for value in range(1, 5):
#     print(value)
# numbers = list(range(1, 20, 3))
# print(numbers)
# squares = []
# for value in range(1, 11):
#     squares.append(value**2)
#     print(squares)
# print(squares)

# squares = [value**2 for value in range(1, 11)]
# print(squares)

# players = ['charles', 'martina', 'michael',
#            'florence', 'eli']
# print(players[0:3])
# print(players[-3:])
# athletes = players
# players.append('john')
# athletes.append('mike')
# print(players)
# print(athletes)

# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# print((22 >= 21) and (18 >= 21))
# requested_toppings = ["mushroom", "green peppers"]
# if requested_toppings:
#     for requested_topping in  requested_toppings:
#         print("Adding " + requested_topping + ".")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# print(favorite_languages.keys())
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for talking the poll.")
#
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#
#     if name in friends:
#         print("  Hi " + name.title() +
#               ", I see your favorite languages is " +
#               favorite_languages[name].title() + "!")

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

aliens = []

for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# for alien in aliens[:5]:
#     print(alien)
# print("......")
# print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0:5]:
    print(alien)
print("......")






