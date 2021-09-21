import colorama
import phonenumbers
from colorama import Fore, init
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import os
from os import system


init()




def geo_phone():
    os.system("cls & title ezlogger - Enter Phone number")
    banner = f'''
{Fore.RED}          _                             
{Fore.LIGHTWHITE_EX}  ___ ___{Fore.RED}| | ___   __ _  __ _  ___ _ __ 
{Fore.LIGHTWHITE_EX} / _ \_  /{Fore.RED} |/ _ \ / _` |/ _` |/ _ \ '__|
{Fore.LIGHTWHITE_EX}|  __// /{Fore.RED}| | (_) | (_| | (_| |  __/ |   
{Fore.LIGHTWHITE_EX} \___/___{Fore.RED}|{Fore.RED}_|\___/ \__, |\__, |\___|_|   
{Fore.RED}                  {Fore.RED}|___/ |___/ '''    
    print(banner)
    number = input(f"{Fore.LIGHTWHITE_EX}[{Fore.RED}>{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}@phone~$ {Fore.RED}")
   
    phone = phonenumbers.parse(number)
    service_provider = phonenumbers.parse(number)
    key = "491b2357ea594bb3b9f8cded1a4c2490"
    geo = OpenCageGeocode(key)
    results = geo.geocode(geocoder.description_for_number(phone, "en"))    
    lat = str(results[0]['geometry']['lat'])
    lng = str(results[0]['geometry']['lng'])     
    
    os.system("cls & title ezlogger - Phone Localization")
    print(f"{Fore.LIGHTWHITE_EX}ezlogger | Author : Kloozy")
    print("")
    print(number)
    print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}COUNTRY{Fore.LIGHTWHITE_EX}]")
    print(f"{Fore.LIGHTWHITE_EX}│  └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] " + geocoder.description_for_number(phone, "en"))
    print(f"{Fore.LIGHTWHITE_EX}│")    
    print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}ISP{Fore.LIGHTWHITE_EX}]")
    print(f"{Fore.LIGHTWHITE_EX}│  └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] " + carrier.name_for_number(service_provider, "en"))
    print(f"{Fore.LIGHTWHITE_EX}│")      
    print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}TIMEZONE{Fore.LIGHTWHITE_EX}]")
    print(f"{Fore.LIGHTWHITE_EX}   └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] " + timezone.time_zones_for_number(number))   
    print("Press [ENTER] for back to menu.") 