

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? \n>>>"
#
# name = input(prompt)
# print("\nHello, " + name + "!")

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# current_number = 0
# while current_number <= 10:
#     current_number +=1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# unconfirmed_users = ['alice', 'brain', 'candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_users = unconfirmed_users.pop()
#     print("Verifying user: " + current_users.title())
#     confirmed_users.append(current_users)
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nWhat is your name? \n>>>")
#     response = input("Which mountain would you like to climb someday? \n>>>")
#     responses[name] = response
#     repeat = input("Would you like to let another person respond? (yes/no) \n>>>")
#     if repeat =='no':
#         polling_active = False
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name + " Would like to climb " + response + ".")

# def greet_user(username):
#     """Show simple greetings"""
#     print("Hello, " + username.title() + "!")
# greet_user('Jesse')

# def describe_pet(animal_type, pet_name):
#     """Show the details of pets"""
#     print("\nI have a " + animal_type + ".")
#     print("My" + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')
# describe_pet(animal_type='cat', pet_name='jerry')

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return clear full name"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician_1 = get_formatted_name('john', 'hooker', 'lee')
# print(musician_1)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("Printing model: ", current_design)
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     print("\nThe following models have printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['iphone case', 'roboot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

def make_pizza(size, *args):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for arg in args:
        print("- ", arg)
make_pizza(16, 'pepperoni')
make_pizza(16, 'pepperoni', 'mushroom', "green peppers", "extra cheese")










