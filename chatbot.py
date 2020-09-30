from random import choice


def get_bot_response(user_response):
    print("I will help you choose the right Tesla model for you!\n")
    fast_response = ["Model 3", "Model S"]
    slow_response = ["Model Y", "Model X"]
    busy_response = ["Model 3", "Model Y"]
    chill_response = ["Model Y", "Model S"]
    if "fast" == user_response:
        return choice(fast_response)
    elif "busy" == user_response:
        return choice(busy_response)
    elif "slow" == user_response:
        return choice(slow_response)
    elif "chill" == user_response:
        return choice(chill_response)
    else:
        return "Sorry, but a Tesla is not for you :(!"

    print("Let's get started!\n")


user = input("What is your name?\n")

bot = print("Nice to meet you", user)

while True:
    life_style = input(
        "What type of lifestyle do you have: fast, busy, slow, or chill?")
    results = get_bot_response(life_style)
    print(results)
    if life_style == "done":
        break

