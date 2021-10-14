import json
import requests
def joke():
  URL = requests.get('https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky')
  JSON_URL = URL.json()
  if JSON_URL["type"] == "twopart":
    print(JSON_URL["setup"])
    print(JSON_URL["delivery"])
  elif JSON_URL["type"] == "single":
    print(JSON_URL["joke"])
  RETRY = input("Do you want to hear another joke?(y/n): ")
  if RETRY == "y":
    joke()
  elif RETRY == "n":
    print("Alright then, have a nice day!")
    exit()
  else:
    exit()
joke()
