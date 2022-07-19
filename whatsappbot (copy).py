import pyautogui as pg
import time

time.sleep(10)

txt = open('animals.txt', 'r')

a = "@koome is a "

for i in txt:
    pg.write(a + ' ' + i)
    pg.press("Enter")



import time
import string
import random

import pyautogui as pg

time.sleep(10)

txt = open('animals.txt', 'r')

# Randomly choose a letter from all the ascii_letters
randomLetter = random.choice(string.ascii_letters)
print(randomLetter)

a = "@"
b = "is a"

for i in txt:
    pg.write(a)
    pg.write(randomLetter)
    pg.press("Enter")
    pg.write(a + ' ' + i)
    pg.press("Enter")
