import gameLog
import os
from colorama import init, Fore, Style

init(autoreset=True)


gameLoop=True
while gameLoop:
   
    choice =input("Do you want to play War? Y/N ")
    choice = choice.upper()
    if choice=='Y':
        os.system('cls' if os.name == 'nt' else 'clear') 
        gameLog.gameStart()
    elif choice=='N':
        print(Fore.RED +"You missed your chance bye!!")
        gameLoop=False
    else:
        print("Please Enter a valid choice")