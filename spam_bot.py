import random
import pyautogui as pg
import time

#world(s) to spam
spam_worlds=('lol', 'wake up')

#Some time for choose place where to spam
time.sleep(5)

for i in range(10):
    a=random.choice(spam_worlds)
    pg.write("My spamming worlds are: "+a)
    pg.press('enter')
