import random 
import colorama 
from colorama import init, Fore

init()


text1 = f'''
{Fore.LIGHTBLACK_EX}▄███▄   ▄▄▄▄▄▄   {Fore.LIGHTWHITE_EX}█    ████▄   ▄▀    ▄▀  ▄███▄   █▄▄▄▄ 
{Fore.LIGHTBLACK_EX}█▀   ▀ ▀   ▄▄▀   {Fore.LIGHTWHITE_EX}█    █   █ ▄▀    ▄▀    █▀   ▀  █  ▄▀ 
{Fore.LIGHTBLACK_EX}██▄▄    ▄▀▀   ▄▀ {Fore.LIGHTWHITE_EX}█    █   █ █ ▀▄  █ ▀▄  ██▄▄    █▀▀▌  
{Fore.LIGHTBLACK_EX}█▄   ▄▀ ▀▀▀▀▀▀   {Fore.LIGHTWHITE_EX}███▄ ▀████ █   █ █   █ █▄   ▄▀ █  █  
{Fore.LIGHTBLACK_EX}▀███▀            {Fore.LIGHTWHITE_EX}    ▀       ███   ███  ▀███▀     █   
                                     {Fore.LIGHTWHITE_EX}            ▀ 

{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTWHITE_EX}1{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}ip loockup
{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTWHITE_EX}2{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}phone loockup
{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTWHITE_EX}3{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}refresh menu'''

text2 = f'''
{Fore.LIGHTRED_EX}                      /$$                                                  
{Fore.LIGHTRED_EX}                     | $$                                                  
{Fore.LIGHTBLACK_EX}  /$$$$$$  /$$$$$$$${Fore.LIGHTRED_EX} | $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
{Fore.LIGHTBLACK_EX} /$$__  $$|____ /$$/{Fore.LIGHTRED_EX} | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
{Fore.LIGHTBLACK_EX}| $$$$$$$$   /$$$$/ {Fore.LIGHTRED_EX} | $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
{Fore.LIGHTBLACK_EX}| $$_____/  /$$__/  {Fore.LIGHTRED_EX} | $$| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      
{Fore.LIGHTBLACK_EX}|  $$$$$$$ /$$$$$$$${Fore.LIGHTRED_EX} | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
{Fore.LIGHTBLACK_EX} \_______/|________/{Fore.LIGHTRED_EX} |__/ \______/  \____  $$ \____  $$ \_______/|__/      
                                   {Fore.LIGHTRED_EX} /$$  \ $$ /$$  \ $$                    
                                  {Fore.LIGHTRED_EX} |  $$$$$$/|  $$$$$$/                    
                                   {Fore.LIGHTRED_EX} \______/  \______/

{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTRED_EX}1{Fore.LIGHTBLACK_EX}] {Fore.LIGHTRED_EX}ip loockup
{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTRED_EX}2{Fore.LIGHTBLACK_EX}] {Fore.LIGHTRED_EX}phone loockup
{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTRED_EX}3{Fore.LIGHTBLACK_EX}] {Fore.LIGHTRED_EX}refresh menu'''

text3 = f'''
{Fore.LIGHTBLACK_EX}      :::::::::: :::::::::                                            
{Fore.LIGHTBLACK_EX}     :+:             :+:                                              
{Fore.LIGHTBLACK_EX}    +:+            +:+                                                
{Fore.LIGHTBLACK_EX}   +#++:++#      +#+                                                  
{Fore.LIGHTBLACK_EX}  +#+          +#+                                                    
{Fore.LIGHTBLACK_EX} #+#         #+#                                                      
{Fore.LIGHTBLACK_EX}########## #########                                                  
{Fore.LIGHTMAGENTA_EX}      :::        ::::::::   ::::::::   ::::::::  :::::::::: ::::::::: 
{Fore.LIGHTMAGENTA_EX}     :+:       :+:    :+: :+:    :+: :+:    :+: :+:        :+:    :+: 
{Fore.LIGHTMAGENTA_EX}    +:+       +:+    +:+ +:+        +:+        +:+        +:+    +:+  
{Fore.LIGHTMAGENTA_EX}   +#+       +#+    +:+ :#:        :#:        +#++:++#   +#++:++#:    
{Fore.LIGHTMAGENTA_EX}  +#+       +#+    +#+ +#+   +#+# +#+   +#+# +#+        +#+    +#+    
{Fore.LIGHTMAGENTA_EX} #+#       #+#    #+# #+#    #+# #+#    #+# #+#        #+#    #+#     
{Fore.LIGHTMAGENTA_EX}########## ########   ########   ########  ########## ###    ### 

{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTMAGENTA_EX}1{Fore.LIGHTBLACK_EX}] {Fore.LIGHTMAGENTA_EX}ip loockup
{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTMAGENTA_EX}2{Fore.LIGHTBLACK_EX}] {Fore.LIGHTMAGENTA_EX}phone loockup
{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTMAGENTA_EX}3{Fore.LIGHTBLACK_EX}] {Fore.LIGHTMAGENTA_EX}refresh menu'''

text4 = f'''
{Fore.LIGHTBLACK_EX}d88888b d88888D                                  
{Fore.LIGHTBLACK_EX}88'     YP  d8'                                  
{Fore.LIGHTBLACK_EX}88ooooo    d8'                                   
{Fore.LIGHTBLACK_EX}88~~~~~   d8'                                    
{Fore.LIGHTBLACK_EX}88.      d8' db                                  
{Fore.LIGHTBLACK_EX}Y88888P d88888P                                  
                                                 
{Fore.LIGHTBLUE_EX}db       .d88b.   d888b   d888b  d88888b d8888b. 
{Fore.LIGHTBLUE_EX}88      .8P  Y8. 88' Y8b 88' Y8b 88'     88  `8D 
{Fore.LIGHTBLUE_EX}88      88    88 88      88      88ooooo 88oobY' 
{Fore.LIGHTBLUE_EX}88      88    88 88  ooo 88  ooo 88~~~~~ 88`8b   
{Fore.LIGHTBLUE_EX}88booo. `8b  d8' 88. ~8~ 88. ~8~ 88.     88 `88. 
{Fore.LIGHTBLUE_EX}Y88888P  `Y88P'   Y888P   Y888P  Y88888P 88   YD

{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTBLUE_EX}1{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLUE_EX}ip loockup
{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTBLUE_EX}2{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLUE_EX}phone loockup
{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTBLUE_EX}3{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLUE_EX}refresh menu'''


text5 = f'''
{Fore.LIGHTBLACK_EX}_______ ______ {Fore.LIGHTYELLOW_EX}        _____   ______  ______ _______  ______
{Fore.LIGHTBLACK_EX}|______  ____/ {Fore.LIGHTYELLOW_EX}|      |     | |  ____ |  ____ |______ |_____/
{Fore.LIGHTBLACK_EX}|______ /_____ {Fore.LIGHTYELLOW_EX}|_____ |_____| |_____| |_____| |______ |    \_

{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTYELLOW_EX}1{Fore.LIGHTBLACK_EX}] {Fore.LIGHTYELLOW_EX}ip loockup
{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTYELLOW_EX}2{Fore.LIGHTBLACK_EX}] {Fore.LIGHTYELLOW_EX}phone loockup
{Fore.LIGHTBLACK_EX}    [{Fore.LIGHTYELLOW_EX}3{Fore.LIGHTBLACK_EX}] {Fore.LIGHTYELLOW_EX}refresh menu'''

def choice_text():
    text = [text1, text2, text3, text4, text5]
    return(random.choice(text))