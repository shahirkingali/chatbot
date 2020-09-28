from random import choice

def get_bot_response(user_response):
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
    print("Sorry, but a Tesla is not for you :(!")

exit()