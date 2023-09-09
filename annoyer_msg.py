import random
import pyautogui as pg

import time

wish=('Dasu','Bobo','Anu')
time.sleep(10)
for i in range(100):
    x=random.choice(wish)
    pg.write('Good afternoon '+x)
    pg.press('enter')