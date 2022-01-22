import os
from os import system
import colorama
from colorama import Fore, init
import requests
import json
import time
from time import sleep
from modules.IpTracker import iptracker
from modules.TokenTool import menu1
from modules.WebhookTool import menu2
import socket
import threading


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


ezbanner = f'''
{Fore.RED}          _                             
{Fore.YELLOW}  ___ ___{Fore.RED}| | ___   __ _  __ _  ___ _ __ 
{Fore.YELLOW} / _ \_  /{Fore.RED} |/ _ \ / _` |/ _` |/ _ \ '__|
{Fore.YELLOW}|  __// /{Fore.RED}| | (_) | (_| | (_| |  __/ |   
{Fore.YELLOW} \___/___{Fore.RED}|{Fore.RED}_|\___/ \__, |\__, |\___|_|   
{Fore.RED}                  {Fore.RED}|___/ |___/ 
'''


ascii_banner = f'''
{Fore.YELLOW}                                                 ╔═╗╔═╗{Fore.RED}╦  ╔═╗╔═╗╔═╗╔═╗╦═╗
{Fore.YELLOW}                                                 ║╣ ╔═╝{Fore.RED}║  ║ ║║ ╦║ ╦║╣ ╠╦╝
{Fore.YELLOW}                                                 ╚═╝╚═╝{Fore.RED}╩═╝╚═╝╚═╝╚═╝╚═╝╩╚═    
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}*{Fore.RED}] {Fore.YELLOW}Options :

{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}1{Fore.RED}] {Fore.YELLOW}Discord Tools
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}2{Fore.RED}] {Fore.YELLOW}Other Tools
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}3{Fore.RED}] {Fore.YELLOW}Exit'''


discordbanner = f'''
{Fore.YELLOW}                                                 ╔═╗╔═╗{Fore.RED}╦  ╔═╗╔═╗╔═╗╔═╗╦═╗
{Fore.YELLOW}                                                 ║╣ ╔═╝{Fore.RED}║  ║ ║║ ╦║ ╦║╣ ╠╦╝
{Fore.YELLOW}                                                 ╚═╝╚═╝{Fore.RED}╩═╝╚═╝╚═╝╚═╝╚═╝╩╚═ 
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}*{Fore.RED}] {Fore.YELLOW}Options :

{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}1{Fore.RED}] {Fore.YELLOW}Token Tools
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}2{Fore.RED}] {Fore.YELLOW}Webhook Tools
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}3{Fore.RED}] {Fore.YELLOW}Server Nuker (soon)
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}4{Fore.RED}] {Fore.YELLOW}Other (soon)
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}5{Fore.RED}] {Fore.YELLOW}Back to menu
'''

otherbanner = f'''
{Fore.YELLOW}                                                 ╔═╗╔═╗{Fore.RED}╦  ╔═╗╔═╗╔═╗╔═╗╦═╗
{Fore.YELLOW}                                                 ║╣ ╔═╝{Fore.RED}║  ║ ║║ ╦║ ╦║╣ ╠╦╝
{Fore.YELLOW}                                                 ╚═╝╚═╝{Fore.RED}╩═╝╚═╝╚═╝╚═╝╚═╝╩╚═ 
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}*{Fore.RED}] {Fore.YELLOW}Options :

{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}1{Fore.RED}] {Fore.YELLOW}IP Tools
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}2{Fore.RED}] {Fore.YELLOW}Proxy scrapper (soon)
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}3{Fore.RED}] {Fore.YELLOW}Port Scanner (soon)
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}4{Fore.RED}] {Fore.YELLOW}Back to menu
'''

ipbanner = f'''
{Fore.YELLOW}                                                 ╔═╗╔═╗{Fore.RED}╦  ╔═╗╔═╗╔═╗╔═╗╦═╗
{Fore.YELLOW}                                                 ║╣ ╔═╝{Fore.RED}║  ║ ║║ ╦║ ╦║╣ ╠╦╝
{Fore.YELLOW}                                                 ╚═╝╚═╝{Fore.RED}╩═╝╚═╝╚═╝╚═╝╚═╝╩╚═ 
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}*{Fore.RED}] {Fore.YELLOW}Options :

{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}1{Fore.RED}] {Fore.YELLOW}IP Tracker
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}2{Fore.RED}] {Fore.YELLOW}IP Logger (soon)
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}3{Fore.RED}] {Fore.YELLOW}IP DOS
{Fore.RED}                                                     [{Fore.LIGHTCYAN_EX}4{Fore.RED}] {Fore.YELLOW}Back to menu
'''



def omenu():
    os.system("cls & title ezlogger - Other Tools")    
    print(otherbanner)
    ochoice = input(f'''
{Fore.RED}┌──[{Fore.LIGHTCYAN_EX}*{Fore.RED}]─[{Fore.LIGHTCYAN_EX}@options~#{Fore.RED}]
{Fore.RED}└───{Fore.YELLOW}$ ''') 

    if ochoice == "4":
        menu()

    if ochoice == "1":
        os.system("cls & title ezlogger - IP Tool")
        print(ipbanner)
        ipchoice = input(f'''
{Fore.RED}┌──[{Fore.LIGHTCYAN_EX}*{Fore.RED}]─[{Fore.LIGHTCYAN_EX}@options~#{Fore.RED}]
{Fore.RED}└───{Fore.YELLOW}$ ''')  

    if ipchoice == "1":
        iptracker()
        input()
        menu()
    
    if ipchoice == "4":
        menu()


            




def dscmenu():
    os.system("cls & title ezlogger - Discord Tools")
    print(discordbanner)    
    dchoice = input(f'''
{Fore.RED}┌──[{Fore.LIGHTCYAN_EX}*{Fore.RED}]─[{Fore.LIGHTCYAN_EX}@options~#{Fore.RED}]
{Fore.RED}└───{Fore.YELLOW}$ ''')

    if dchoice == "5":
        menu()
    
    if dchoice == "1":
        menu1()






def menu():
    os.system("cls & title ezlogger - Menu")
    print(ascii_banner)
    choice = input(f'''
{Fore.RED}┌──[{Fore.LIGHTCYAN_EX}*{Fore.RED}]─[{Fore.LIGHTCYAN_EX}@options~#{Fore.RED}]
{Fore.RED}└───{Fore.YELLOW}$ ''')

    if choice == "1":
        dscmenu()
    if choice == "3":
        sys.exit(f"Thanks for using ezlogger, bye")
    if choice == "2":
        omenu()






menu()