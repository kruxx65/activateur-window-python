#importation des modules..
# import os
import os

import colorama
from colorama import Fore, init
from time import sleep

def presentation():
    os.system(" ")
    print(Fore.LIGHTBLUE_EX+f'''
                            ██╗  ██╗███████╗███╗   ██╗    ████████╗ ██████╗  ██████╗ ██╗     
                            ██║  ██║██╔════╝████╗  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                            ███████║███████╗██╔██╗ ██║       ██║   ██║   ██║██║   ██║██║     
                            ██╔══██║╚════██║██║╚██╗██║       ██║   ██║   ██║██║   ██║██║     
                            ██║  ██║███████║██║ ╚████║       ██║   ╚██████╔╝╚██████╔╝███████╗
                            ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                            {Fore.MAGENTA}-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
                            {Fore.MAGENTA}-_-   {Fore.RED}              [1] Activateur Window 10.              {Fore.MAGENTA}         -_-
                            {Fore.MAGENTA}-_-    {Fore.GREEN}                 [2] Désinstalle l'activation.           {Fore.MAGENTA}    -_-
                            {Fore.MAGENTA}-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
    ''')
    mode = input(Fore.WHITE+"                         Mode[>]")
    if mode == '':
        print(Fore.RED+"                         [ERRER] Vous devez préciser un mode le script se relancera dans 3s.")
        sleep(3)
        os.system("cls")
        return presentation()
    if mode not in ["1","2"]:
        print(Fore.RED+f"                         [ERRER]{Fore.GREEN}'{mode}'{Fore.RED} est pas disponible le script se relancera dans 3s.")
        sleep(3)
        os.system("cls")
        return presentation()

    if mode == "2":
        os.system("slmgr.vbs /upk")
        sleep(3)
        os.system("cls")
        return presentation()

    if mode == "1":
        print(Fore.RED+f'''
                            >--------------------------------------------->
                            Version 1.4.4.2 
                                                        Dev by Hassan Wazni
                      {Fore.GREEN}     ┌─────────────────────────────────────────────┐
                           │     Choisi la version de ton window.        │
                           ├─────────────────────────────────────────────┤
                           │       [1]Window 10 Home                     │
                           │       [2]Window 10 Home N                   │
                           │       [3]Window 10 Home Single Language     │
                           │       [4]Window 10 Home Country Specific    │
                           │       [5]Window 10 Professional             │
                           │       [6]Window 10 Professional N           │
                           │       [7]Windpw 10 Education                │
                           │       [8]Window 10 Education N              │
                           │       [9]Window 10 Enterprise               │
                           │      [10]Window 10 Enterprise N             │
                           ├─────────────────────────────────────────────┤
                           │             merci!   │ hassan waz           |
                           └─────────────────────────────────────────────┘''')
    smode = input(Fore.WHITE + "                           Mode[>]")
    if smode not in ["1","2","3","4","5","6",'7','8','9','10']:
        print(
            Fore.RED + f"                         [ERRER]{Fore.GREEN}'{smode}'{Fore.RED} est pas disponible le script se relancera dans 3s.")
        sleep(3)
        os.system("cls")
        return presentation()
    if smode == "1":
        os.system("cls")
        print(Fore.BLUE+f"Vous avez choisi l'option n*1 {Fore.RED}[Window 10 Home]")
        sleep(3)
        os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")

    if smode == "2":
        print(Fore.BLUE + f"Vous avez choisi l'option n*2 {Fore.RED}[Window 10 Home N]")
        sleep(3)
        os.system("slmgr /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM")

    if smode == "3":
        print(Fore.BLUE + f"Vous avez choisi l'option n*3 {Fore.RED}[Window 10 Home Single Language ]")
        sleep(3)
        os.system("slmgr /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH")

    if smode == "4":
        print(Fore.BLUE + f"Vous avez choisi l'option n*4 {Fore.RED}[Window 10 Home Country Specific]")
        sleep(3)
        os.system("slmgr /ipk PVMJN-6DFY6-9CCP6-7BKTT-D3WVR")

    if smode == "5":
        print(Fore.BLUE + f"Vous avez choisi l'option n*5 {Fore.RED}[Window 10 Professional]")
        sleep(3)
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")

    if smode == "6":
        print(Fore.BLUE + f"Vous avez choisi l'option n*6 {Fore.RED}[Window 10 Professional N ]")
        sleep(3)
        os.system("slmgr /ipk MH37W-N47XK-V7XM9-C7227-GCQG9")

    if smode == "7":
        print(Fore.BLUE + f"Vous avez choisi l'option n*7 {Fore.RED}[Education]")
        sleep(3)
        os.system("slmgr /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")

    if smode == "8":
        print(Fore.BLUE + f"Vous avez choisi l'option n*8 {Fore.RED}[Education N]")
        sleep(3)
        os.system("slmgr /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ")

    if smode == "9":
        print(Fore.BLUE + f"Vous avez choisi l'option n*9 {Fore.RED}[Enterprise]")
        sleep(3)
        os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")

    if smode == "10":
        print(Fore.BLUE + f"Vous avez choisi l'option n*10 {Fore.RED}[Enterprise N]")
        sleep(3)
        os.system("slmgr /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4")
presentation()
