# Create a function called get_bot_response(). This function must:
# It should have 1 parameter called user_response, which is a string with the users input.

# It should return a string with the chat bot’s response.

# It should use at least 2 lists to store at least 3 unique responses to different user inputs. For example, if you were building a mood bot and the user entered “happy” for how they were feeling your happy response list could store something like “I’m glad to hear that!”, “Yay!”, “That is awesome!”.

# Use conditionals to decide which of the response lists to select from. For example: if a user entered “sad”, my program would choose a reponse from the of sad response list. If a user entered “happy”, my program would choose a reponse from the of happy response list.

# Use choice() to randomly select one of the three responses. (See example from class.)

# Greet the user using print() statements and explain what the chat bot topic is and what kind of responses it expects.

# Get user input using the input() function and pass that user input to the get_bot_response() function you will write

# Print out the chat bot’s response that is returned from the get_bot_response() function

# Use a while() loop to keep running your chat bot until the user enters "done".
from random import choice

def get_bot_response(user_response):


print("Hi, I am Maiya, Shahir's Assistant\n")

print("I will help you choose the right Tesla model for you!\n")

print("Let's get started!\n")

user = input("What is your name?\n")

bot = print("Nice to meet you", user)

	
lifestyle = input("What type of lifestyle do you have: fast, busy, slow, or chill?")
if "fast" in lifestyle:
    print("You should get a Model 3 or Model S")
elif "busy" in lifestyle:
    print("You should get Model 3")
elif "slow" in lifestyle:
    print("You should get a Model Y or Model X ")
elif "chill" in lifestyle:
    print("Model Y, Model S")
else:
    print("Sorry, but a Tesla is not for you :(")

exit()