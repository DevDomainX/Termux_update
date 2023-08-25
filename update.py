#!/usr/bin/env python3
from time import sleep
import os
from colorama import init, Fore, Style, Back
init()
logo = Fore.YELLOW+Style.BRIGHT+"""

'##::::'##:'########::'########:::::'###::::'##### ###:'########:
 ##:::: ##: ##.... ##: ##.... ##:::'## ##:::... ##..:: ##.. ...::
 ##:::: ##: ##:::: ##: ##:::: ##::'##:. ##::::: ##:::: ##:::::::
 ##:::: ##: ########:: ##:::: ##:'##:::. ##:::: ##:::: ######:::
 ##:::: ##: ##.......::: ##:::: ##: #########:::: ##:::: ##. ..::::
 ##:::: ##: ##:::::::: ##:::: ##: ##.... ##:::: ##:::: ##:: :::::
. #######:: ##:::::::: ########:: ##:::: ##:::: ##:::: ### #####:
:.......:::..::::::::::..........:::..:::::..:::::..: ::::.......::
:'######:::'######::'########::'####:'########::'# #######:      
'##... ##:'##... ##: ##.... ##:. ##:: ##.... ##:... ##..::      
 ##:::..:: ##:::..:: ##:::: ##:: ##:: ##:::: ##:::: ##::::      
. ######:: ##::::::: ########::: ##:: ########::::: ##::: :      
:..... ##: ##::::::: ##.. ##:::: ##:: ##.....:::::: ##::: :      
'##::: ##: ##::: ##: ##::. ##::: ##:: ##:::::::::::: ##::::      
. ######::. ######:: ##:::. ##:'####: ##:::::::::::: ##::::      
:......::::......:::..::::::..::....::..::::::::::::: :..:::::      



\n\n"""
for i in logo:
    print(i, end="", flush=True)
    
    
title = Fore.CYAN+Style.BRIGHT+"""Antes de comenzar a trabajar, debe escribir el siguiente comando para acceder al almacenamiento del teléfono para instalar las herramientas"""
sleep(3)

for p in title:
        print(p, end='', flush=True)
        sleep(0.1) 

os.system("termux-setup-storage")

print("Waiting....")
sleep(3)

letra = "Estos son comandos esenciales que debe ejecutar antes de comenzar, y de vez en cuando, para actualizar el programa y las herramientas\n"
for i in letra:
        print(i, end='', flush=True)
        sleep(0.1) 

os.system("pkg update && pkg upgrade && apt update && apt upgrade")

p = """Instalar las herramientas necesarias para ejecutar los programas\n"""

for i in p:
        print(i, end='', flush=True)
        sleep(0.1) 

name = "python", "python2", "python3", "git", "ruby", "nmap", "pip", "unzip","nano","root-repo", "php"
update = "pkg install python", "pkg install python2", "pkg install python3", "pkg install git", "pkg install ruby",  "pkg install nmap, pkg install pip", "pkg install unzip", "pkg install nano", "pkg install root-repo", "pkg install x11-repo", "pkg install php"


for e in update:
    os.system(e)
    sleep(2)
        
        



print("\nIntalling Done ! ")