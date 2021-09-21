import os
from os import system
import colorama
from colorama import Fore, init
import requests
import json
import time
from time import sleep
from modules.IpTracker import iptracker
from modules.Theme import choice_text
from modules.PhoneTracker import geo_phone
from modules.EmailSpammer import email_spammer


system("")
init()

os.system("cls & title ezlogger - Loading")
print(f"{Fore.LIGHTWHITE_EX}loading [{Fore.LIGHTGREEN_EX}•{Fore.LIGHTWHITE_EX}]")
time.sleep(0.5)
os.system("cls")
print(f"{Fore.LIGHTWHITE_EX}loading [{Fore.LIGHTGREEN_EX}••{Fore.LIGHTWHITE_EX}]")
time.sleep(0.5)
os.system("cls")
print(f"{Fore.LIGHTWHITE_EX}loading [{Fore.LIGHTGREEN_EX}•••{Fore.LIGHTWHITE_EX}]")
time.sleep(0.5)



def menu():
    os.system("cls & title ezlogger - Menu")
    print(choice_text())  
    choice = input(f"\n{Fore.LIGHTWHITE_EX}    > @ezlogger~$ {Fore.LIGHTWHITE_EX}")

    if choice == "1":
        iptracker()
        input()
        menu()
    
    if choice == "3":
        with open("config.json", "r") as config:
            data = json.load(config)
        mail = data["email"]

        with open("config.json", "r") as config:
            data = json.load(config)
        passw = data["password"]        
        email_spammer()

    if choice == "2":
        geo_phone()
        input()
        menu()

    if choice == "4":
        menu()


menu()