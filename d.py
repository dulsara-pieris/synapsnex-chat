import time
import random
import sys

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from prompt_toolkit import PromptSession
import pyfiglet

console = Console()
session = PromptSession("> ")

# ---------- effects ----------
def typewrite(text, delay=0.015):
    for c in text:
        console.print(c, end="", style="green")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def glitch(text):
    junk = "█▓▒░@#$%"
    return "".join(c if random.random() > 0.12 else random.choice(junk) for c in text)

# ---------- splash ----------
console.clear()
logo = pyfiglet.figlet_format("RETRO CHAT", font="slant")
console.print(logo, style="bold green")
typewrite("CONNECTING TO RETRO-NET NODE 7...")
time.sleep(0.5)

for step in [
    "DIALING 2400 BAUD...",
    "NEGOTIATING PROTOCOL...",
    "HANDSHAKE OK",
    "AUTH ACCEPTED"
]:
    console.print(step, style="green")
    time.sleep(random.uniform(0.4, 1.0))

time.sleep(0.5)

# ---------- chat ----------
messages = [
    "[SYS] WELCOME TO RETRO-NET",
    "[SYS] TYPE /HELP FOR COMMANDS"
]

def render():
    console.clear()
    panel = Panel(
        Align.left("\n".join(messages[-15:])),
        title="RETRO-NET // ONLINE",
        border_style="green",
        width=80
    )
    console.print(panel)

def incoming():
    msgs = [
        "[NODE-3] anyone here?",
        "[NODE-9] hello world",
        "[SYS] latency spike detected",
        "[NODE-5] typing...",
        "[SYS] packet loss 12%"
    ]
    time.sleep(random.uniform(0.8, 2.0))
    return random.choice(msgs)

# ---------- loop ----------
while True:
    render()
    try:
        msg = session.prompt()
    except KeyboardInterrupt:
        break

    if msg == "/quit":
        messages.append("[SYS] DISCONNECTING...")
        render()
        time.sleep(1)
        break

    if msg == "/help":
        messages.append("[SYS] COMMANDS: /help /glitch /quit")
        continue

    if msg == "/glitch":
        messages.append(glitch("[SYS] SIGNAL CORRUPTION DETECTED"))
        continue

    messages.append(f"[YOU] {msg}")

    if random.random() > 0.5:
        messages.append(incoming())
