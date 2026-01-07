import subprocess, os, time, platform,threading,socket,random
import tkinter
from tkinter import *






def math_questions(arg):
    amount_q = 14
    amount_q = amount_q - 1
    questions_and_answers = [
        {"question": "23 + 85", "answer": "108"},           #1
        {"question": "10 / 6 as a decimal to 3 significant figures", "answer": "1.67"}, #2
        {"question": "999 X 2", "answer": "1998"}, #3
        {"question": "15 + 47", "answer": "62"}, #4
        {"question": "42 - 19", "answer": "23"}, #5
        {"question": "8 * 7", "answer": "56"}, # 6
        {"question": "100 / 4", "answer": "25"}, #7
        {"question": "45 + 32", "answer": "77"}, #8
        {"question": "81 - 36", "answer": "45"}, #9
        {"question": "7 * 9", "answer": "63"}, #10
        {"question": "144 / 12", "answer": "12"}, #11
        {"question": "12 / 5 as a decimal to 2 significant figures", "answer": "2.4"}, #12
        {"question": "375 + 625", "answer": "1000"}, #13
        {"question": "what has no value yet is so vital?", "answer": "0"} #14
    ]





    ran = random.randint(0,amount_q)



    ren = questions_and_answers[ran]

    return ren







