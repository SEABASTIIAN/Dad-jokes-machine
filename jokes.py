import requests
import colorama
import pyfiglet
from termcolor import colored
from random import choice

colorama.init()


art = pyfiglet.figlet_format("Dad jokes 3000")
color = colored(art, color="green")
print(color)


user_input = input("What kind of joke do you what to hear? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
	url,
	headers={"Accept": "application/json"},
	params={"term": user_input}

).json()

num_jokes = res["total_jokes"]
results = res["results"]

if num_jokes > 1:
	print(f"I found {num_jokes} about {user_input}. Here's one: ")
	print(choice(results)["joke"])
elif num_jokes	== 1:
	print(f"I found one joke about {user_input}")
	print(results [0]["joke"])
else:
	print(f"Sorry, could't not find a joke with your term: {user_input}")