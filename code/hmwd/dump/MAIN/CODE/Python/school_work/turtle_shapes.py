import turtle as t
import keyboard 
import pygame
import pyautogui as po
import time,os,subprocess

##

t = t.Turtle()


t.setheading(90)

t.right(90)

speed = 1

angle = 10

while True:
    if keyboard.is_pressed("w"):
        
        t.forward(speed)
    elif keyboard.is_pressed("s"):
        t.forward(-speed)
    if keyboard.is_pressed("d"):
        t.right(angle)
    elif keyboard.is_pressed("a"):
        t.right(-angle)
