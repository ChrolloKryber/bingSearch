import os
import time
import datetime
from pynput.keyboard import Key, Controller
import subprocess
import random

with open("private_keywords.txt", "r") as keywords:
    queries = keywords.readlines()

keyboard = Controller()


def search_bar():
    keyboard.press(Key.ctrl)
    keyboard.press("l")
    keyboard.release(Key.ctrl)
    keyboard.release("l")


def press_enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def bing_search(word):
    search_bar()
    time.sleep(2)
    keyboard.type(word)
    time.sleep(2)
    press_enter()


def launch_edge():
    with open(os.devnull, "w") as devnull:
        subprocess.Popen(["microsoft-edge-stable"], stdout=devnull, stderr=devnull)


def close_edge():
    os.system("pkill -f stable")

for i in range(8):
    print(f"Start Time : {datetime.datetime.now().time()}")

    launch_edge()

    time.sleep(3)
    
    for i in range(4):
        words = random.choice(queries)
        print(f"Query {i + 1}: {words}", end="")
        bing_search(words)
        time.sleep(12)

    close_edge()
    print(f"Kill Time : {datetime.datetime.now().time()}")

    time.sleep(900)

