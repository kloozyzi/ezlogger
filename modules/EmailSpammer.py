import os, colorama, time, smtplib, ssl
from os import system
from colorama import init, Fore
from time import sleep
import json


init()



def email_spammer():
    os.system("cls & title ezlogger - enter Email Spammer informations")
    banner = f'''
{Fore.LIGHTMAGENTA_EX}          _                             
{Fore.LIGHTWHITE_EX}  ___ ___{Fore.LIGHTMAGENTA_EX}| | ___   __ _  __ _  ___ _ __ 
{Fore.LIGHTWHITE_EX} / _ \_  /{Fore.LIGHTMAGENTA_EX} |/ _ \ / _` |/ _` |/ _ \ '__|
{Fore.LIGHTWHITE_EX}|  __// /{Fore.LIGHTMAGENTA_EX}| | (_) | (_| | (_| |  __/ |   
{Fore.LIGHTWHITE_EX} \___/___{Fore.LIGHTMAGENTA_EX}|{Fore.LIGHTMAGENTA_EX}_|\___/ \__, |\__, |\___|_|   
{Fore.LIGHTMAGENTA_EX}                  {Fore.LIGHTMAGENTA_EX}|___/ |___/ '''

    print(banner)
    emailspamm = input(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}>{Fore.LIGHTWHITE_EX}] @emailspam~$ {Fore.LIGHTMAGENTA_EX}")
    message = input(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}>{Fore.LIGHTWHITE_EX}] @message~$ {Fore.LIGHTMAGENTA_EX}")

    os.system("cls & title ezlogger - Spam Email")
    print(f"{Fore.LIGHTWHITE_EX}ezlogger | Author : Kloozy")
    print("")
    print(emailspamm)
    print(f"{Fore.LIGHTWHITE_EX}│──[{Fore.LIGHTGREEN_EX}SPAM{Fore.LIGHTWHITE_EX}]")    
    
    mailcount = int(500)
    sendmsg = 0
    port = 587
    email = mail
    password= passw
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', port)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email, password)
        while 1:
            smtp.sendmail(email, emailspamm, message)
            sendmsg +=1
            print(f"{Fore.LIGHTWHITE_EX}│  └──"f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTWHITE_EX}] {Fore.LIGHTBLUE_EX}Message send") 
    except:
        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}] {Fore.LIGHTRED_EX}Google stopped the process")  
