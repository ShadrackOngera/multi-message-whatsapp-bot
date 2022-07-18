import pyautogui as pg
import time

time.sleep(10)

txt = open('animals.txt', 'r')

a = "@koome is a "

for i in txt:
    pg.write(a + ' ' + i)
    pg.press("Enter")
