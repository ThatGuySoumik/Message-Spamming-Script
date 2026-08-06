import pyautogui as pyg
import time
import pygame as pg

pg.mixer.init()


def type_msg(msg):
    pyg.write(msg)
    pyg.press('enter')

time.sleep(4) #run after 8 seconds
i=0
while i<=24: 
    msg = "Good Morning" #enter msg want to send
    type_msg(msg)
    i+=1

pg.mixer.music.load("khatam.mp3")
pg.mixer.music.play()

while pg.mixer.music.get_busy():
    time.sleep(0.1)
    
print("Task Complete")
