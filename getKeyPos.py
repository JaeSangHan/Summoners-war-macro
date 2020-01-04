import pyautogui as pag
import keyboard 
import random, time
import sys


from BtnPos import *
from Opencv import *

while True:
 x, y = pag.position()
 print('x: %s, y: %s' % (x,y))