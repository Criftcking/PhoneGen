import random
import pyfiglet
import os
import colorama
from colorama import Fore, Style
colorama.init()


#EStilo



os.system("clear")  # Para sistemas UNIX/Linux
os.system("cls")  # Para sistemas Windows
    
    
font = pyfiglet.Figlet(font='bubble')
art = Fore.BLUE+font.renderText('Phone Generator')+Fore.RESET
print(art)
print(Fore.RED+"By Criftcking_Real | GhostHat_Real"+Fore.RESET)
print()



n = 1
num = int(input(Fore.YELLOW+"Cantidad a Generar---> "))
code = int(input("Area code 3 Digit-----> "))


if len(str(code)) > 3:
    print("Codigo de Area Incorrecto 'Tiene mas de 3 digitos'.")

else:
    while n <= num:
        x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        x1 = (random.choice(x1))
        j2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        j2 = (random.choice(j2))
        r3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        r3 = (random.choice(r3))
        p1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        p1 = (random.choice(p1))
        p2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        p2 = (random.choice(p2))
        p3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        p3 = (random.choice(p3))
        p4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        p4 = (random.choice(p4))
        texto = (f"({code})-{x1}{j2}{r3}-{p1}{p2}{p3}{p4}")
        stt = str(texto)
        n +=1
        with open("Results.txt", 'a') as archivo:
            archivo.write(str(texto+"\n"))
    

print(Fore.BLUE+"El resultado se ha guardado en 'Results.txt' "+Fore.RESET)


