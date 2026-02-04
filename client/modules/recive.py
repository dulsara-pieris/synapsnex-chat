from time import sleep

def typer(text):
        for i in text:
                print(i, end = "")
                sleep(.5)

def listen():
        while True:
                try:
                        msg = sock.recv(4096).decode()
                        if not msg:
                                continue
                        else:
                                print(GREEN + BOLD + msg + RESET)

                except:
                        print(f'{RED}{BOLD}Connection lost{RESET}')
                        break