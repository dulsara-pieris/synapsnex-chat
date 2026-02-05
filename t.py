import os, sys

def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

clear()
WIDTH  = 80
HEIGHT = 24

screen = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

def box(x, y, w, h, title=""):
    for i in range(w):
        screen[y][x+i] = "-"
        screen[y+h-1][x+i] = "-"
    for i in range(h):
        screen[y+i][x] = "|"
        screen[y+i][x+w-1] = "|"

    screen[y][x] = "+"
    screen[y][x+w-1] = "+"
    screen[y+h-1][x] = "+"
    screen[y+h-1][x+w-1] = "+"

    if title:
        for i, c in enumerate(title[:w-4]):
            screen[y][x+2+i] = c
box(0, 0, 80, 3, " RETRO COMM TERMINAL ")
box(0, 3, 80, 18, " MESSAGES ")
box(0, 21, 80, 3, " INPUT ")
def render():
    clear()
    for row in screen:
        print("".join(row))
messages = []
MAX_MSG = 16

def add_msg(user, text):
    messages.append(f"{user}: {text}")
    if len(messages) > MAX_MSG:
        messages.pop(0)

def draw_messages():
    y = 4
    for msg in messages:
        for i, c in enumerate(msg[:76]):
            screen[y][2+i] = c
        y += 1
while True:
    screen[:] = [[" "]*WIDTH for _ in range(HEIGHT)]

    box(0, 0, 80, 3, " RETRO COMM TERMINAL ")
    box(0, 3, 80, 18, " MESSAGES ")
    box(0, 21, 80, 3, " INPUT ")

    draw_messages()
    render()

    msg = input("> ")
    if msg == "/exit":
        break
    add_msg("YOU", msg)
