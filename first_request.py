import requests
import colorama
import pyfiglet
from termcolor import colored

colorama.init()
msg = "Dad jokes 101"
ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color="green")
print(colored_ascii)

user_input = input("what kind of dad joke are you looking for? \nPlease use one word: ")


if user_input not in data:
		print("Unable able to find what you are looking for, Please try again ")

url = "https://icanhazdadjoke.com/search"
response = requests.get(
	url,
	headers={"Accept": "application/json"},
	
	params={
	"term": user_input, 
	"limit": 1,
	}
)





# print(f"your request to {url} came back w/ status code {response.status_code}")
data = response.json()

print(data["results"])
