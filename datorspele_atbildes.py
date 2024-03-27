from time import sleep
from os import system

print("Spēle Jums uzdos 5 jautājumus.")
print("Ja uz kādu jautājumu atbildi nepareizi tad sāc no jauna.")
print("Atbildes raksti ar mazajiem burtiem.")
print("")
print("1. Kas ir CPU?")
pirmais = input("Tava atbilde: ")
if pirmais == "procesors":
    system("CLS")
    print
