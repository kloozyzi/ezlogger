import os
from os import system
import colorama
from colorama import Fore, init
import requests
import json


init()


def iptracker():

        banner = f'''
{Fore.YELLOW}          _                             
{Fore.LIGHTWHITE_EX}  ___ ___{Fore.YELLOW}| | ___   __ _  __ _  ___ _ __ 
{Fore.LIGHTWHITE_EX} / _ \_  /{Fore.YELLOW} |/ _ \ / _` |/ _` |/ _ \ '__|
{Fore.LIGHTWHITE_EX}|  __// /{Fore.YELLOW}| | (_) | (_| | (_| |  __/ |   
{Fore.LIGHTWHITE_EX} \___/___{Fore.YELLOW}|{Fore.YELLOW}_|\___/ \__, |\__, |\___|_|   
{Fore.YELLOW}                  {Fore.YELLOW}|___/ |___/ '''

        os.system("cls & title ezlogger - Enter IP")
        print(banner)
        ip = input(f"{Fore.LIGHTWHITE_EX}[{Fore.YELLOW}>{Fore.LIGHTWHITE_EX}] @target~$ {Fore.YELLOW}")

        os.system("cls & title ezlogger - IP localization")
        r = requests.get(f"http://ip-api.com/json/{ip}")
        r2 = requests.get(f"https://ipinfo.io/{ip}")
        values = json.loads(r.text)
        data = r2.json()
        city = data["city"]
        location = data["loc"].split(",")
        latitude = location[0]
        longitude = location[1]
        hostname = data["hostname"]
        postal =  data["postal"]
        localisation = str(values['lat'])+', '+str(values['lon'])
        infos = ("Localisation", localisation)

        print(f"{Fore.LIGHTWHITE_EX}ezlogger | Author : Kloozy")
        print("")
        print(ip)
        print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}IP{Fore.LIGHTWHITE_EX}]")
        print(f"{Fore.LIGHTWHITE_EX}│  └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] " + ip)
        print(f"{Fore.LIGHTWHITE_EX}│")
        print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}HOSTNAME{Fore.LIGHTWHITE_EX}]")
        print(f"{Fore.LIGHTWHITE_EX}│  └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] " + hostname)
        print(f"{Fore.LIGHTWHITE_EX}│")
        print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}COUNTRY{Fore.LIGHTWHITE_EX}]")
        print(f"{Fore.LIGHTWHITE_EX}│  └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] " + values["country"] + f" [{values['countryCode']}]")
        print(f"{Fore.LIGHTWHITE_EX}│")
        print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}REGION{Fore.LIGHTWHITE_EX}]")
        print(f"{Fore.LIGHTWHITE_EX}│  └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] " + values["regionName"] + f" [{values['region']}]")
        print(f"{Fore.LIGHTWHITE_EX}│")
        print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}POSTAL{Fore.LIGHTWHITE_EX}]")
        print(f"{Fore.LIGHTWHITE_EX}│  └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] " + postal)
        print(f"{Fore.LIGHTWHITE_EX}│")
        print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}CITY{Fore.LIGHTWHITE_EX}]")
        print(f"{Fore.LIGHTWHITE_EX}│  └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] " + city)
        print(f"{Fore.LIGHTWHITE_EX}│")
        print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}TIMEZONE{Fore.LIGHTWHITE_EX}]")
        print(f"{Fore.LIGHTWHITE_EX}│  └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] " + values["timezone"])
        print(f"{Fore.LIGHTWHITE_EX}│")
        print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}ISP{Fore.LIGHTWHITE_EX}]")
        print(f"{Fore.LIGHTWHITE_EX}│  └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] " + values["isp"])
        print(f"{Fore.LIGHTWHITE_EX}│")
        print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}LAT/LON{Fore.LIGHTWHITE_EX}]")
        print(f"{Fore.LIGHTWHITE_EX}│  └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] " + latitude, "|", longitude)
        print(f"{Fore.LIGHTWHITE_EX}│")
        print(f"{Fore.LIGHTWHITE_EX}└──[{Fore.LIGHTGREEN_EX}Maps{Fore.LIGHTWHITE_EX}]")
        print(f"{Fore.LIGHTWHITE_EX}   └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] https://www.google.fr/maps?q="+latitude+","+ longitude)
        print("")
        print("Press [ENTER] for back to menu.")

