import time
import string
import random

import pyautogui as pg

time.sleep(10)

txt = open('animals.txt', 'r')

# Randomly choose a letter from all the ascii_letters
randomLetter = random.choice(string.ascii_letters)
print(randomLetter)

b = ""

for i in txt:
    pg.write('You are a ' + i)
    pg.press("Enter")