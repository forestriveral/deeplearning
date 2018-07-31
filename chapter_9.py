
print("=================9-1,4=====================")

# 9-1
class Restaurant(object):
    """A reataurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of restaurant"""
        msg = "This restaurant's name is " + self.name
        msg += "\n" + self.name + " serves woderful" + self.cuisine_type
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant id open."""
        msg = self.name + "is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""
    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super(IceCreamStand, self).__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the following available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']
print(big_one.cuisine_type)
big_one.describe_restaurant()
big_one.show_flavors()

# mean_queen = Restaurant('the mean queen', 'pizza')
# mean_queen.describe_restaurant()
# mean_queen.open_restaurant()
#
# mean_queen.number_served = 430
# print("\nNumber served: " + str(mean_queen.number_served))
# mean_queen.set_number_served(1232)
# print("\nNumber served: " + str(mean_queen.number_served))
# mean_queen.increment_number_served(212)
# print("\nNumber served: " + str(mean_queen.number_served))

print("=================9-3,5=====================")

# 9-3
class User(object):
    """Represent a simple user profile."""
    def __init__(self, first_name, last_name, username, email, age):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name.title() + " " + self.last_name.title())
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("Age: " + self.age)

    def greet_user(self):
        """Display a personalized greeting to user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

eric = User('eric', 'matthes', 'e_matthes',
            'e_matthes@example.com', '29')
eric.greet_user()
eric.describe_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("Login attempts: " + str(eric.login_attempts))
print("Resetting login attempts....")
eric.reset_login_attempts()
print("Login attempts: " + str(eric.login_attempts))

print("======================================")


