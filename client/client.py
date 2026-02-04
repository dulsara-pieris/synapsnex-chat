import socket
import threading
import time
import readline
import ipaddress
import sys
from pyfiglet import Figlet
import shutil
from rich.progress import track
from rich.syntax import Syntax
from rich.console import Console
from datetime import datetime
from modules.time import save_login, last
from modules.ip import is_public_ip
import random
from rich.text import Text

print('')
print('')
print('')
for i in track(range(20), description='Processing...'):
        time.sleep(0.05)
print('')
print('')

console = Console()
exec(open('modules/colors.py').read())
exec(open('modules/banner.py').read())
exec(open('modules/join.py').read())
exec(open('modules/recive.py').read())
exec(open('modules/mode.py').read())



while True:
        timestamp = time.strftime('%H:%M')
        save_login()
        try:
                text = input('> ').strip()
        except KeyboardInterrupt:
                break

        if not text:
                continue

        if text == '/exit':
                print('disconnecting...')
                break

        if text == '/help':
                print('''
                /help                show commands
                /exit                quit chat
                /me <msg>        action message
                /time           shows last 3 time stamps logged in
                ''')
                continue
        if text == '/time':
            last()
            continue

        if text.startswith('/code '):

                        code = text[len('/code '):]
                        code = code.replace('\\n', '/n')
                        syntax = Syntax(code, 'python', theme='monokai', line_numbers=True)
                        console.print(syntax)

        if text.startswith('/me '):
                msg = f'[{timestamp}] * {username} {text[4:]}'
        else:
                msg = f'[{timestamp}] {username}> {text}'

        try:
                sock.send(msg.encode())
        except:
                print('connection lost')
                break

sock.close()
print('bye Hacker')