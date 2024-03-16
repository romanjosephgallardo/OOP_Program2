from pyfiglet import figlet_format 
import colorama
from fancify_text import monospaced

name = input("Enter your name: ")
dream_job = input("What's your dream job?: ")

print()
print("\033[5m=" * 110)
print(monospaced("----- Your name is -----").center(100))
print(figlet_format(name, font="univers", justify="center", width=100))
print(monospaced("----- and you want to be a -----").center(100))
print(figlet_format(dream_job, font="univers", justify="center", width=110))
print(f"=" * 110)
print()

