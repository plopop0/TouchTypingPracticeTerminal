import random
import msvcrt
import os

character_sheet = [['a', 's', 'd', 'f'],['j', 'k', 'l', ';']]

def asdf():
    typePracticeLoop('asdf')
def jkl_sc():
    typePracticeLoop('jkl;')
    

def typePracticeLoop(keys):
    x = ""
    if keys == 'asdf': chars = character_sheet[0]
    elif keys == 'jkl;': chars = character_sheet[1]

    while True:
        msg = random.choices(chars)[0]
        print(f"type: {msg}")
        while not msvcrt.kbhit():  # Wait for key press
            pass
        x = msvcrt.getch().decode()  # Get the key press
        if x.lower()=='\x1b':break
        print("CORRECT!!!!") if x.lower() == msg else print("DUMBASS KYS BRO YOU SUCK ASS")
    os.system('cls')

while True:
    print("Touch Typing Practice.\nBeginner:\n\
 Type 'asdf' -- familiarizing yourself with asdf keys LH\n\
 Type 'jkl;' -- familiarizing yourself with jkl; keys RH\
          ")


    choose = input()
    if choose == 'asdf':asdf()
    elif choose == 'jkl;':jkl_sc()
    else:continue
    