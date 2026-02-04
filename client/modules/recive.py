
current_process = None
stop_flag = False

def ascii(endpoint):
    global current_process, stop_flag
    try:
        url = f"https://ascii.live/{endpoint}"
        
        current_process = subprocess.Popen(['curl', '-s', url])

        while current_process.poll() is None:
            if stop_flag:
                current_process.terminate()
                current_process.kill()
                stop_flag = False
                print(f"\n{GREEN}{BOLD}Stopped! Back to chat...{RESET}\n")
                break
            time.sleep(0.1)
        
        current_process = None
        
    except FileNotFoundError:
        print(f'{RED}{BOLD}curl not found. Install: sudo apt install curl{RESET}')
    except Exception as e:
        pass
    finally:
        current_process = None

def listen():
    global stop_flag
    
    while True:
        try:
            msg = sock.recv(4096).decode()
            if not msg:
                continue
            elif '/rickrole' in msg:
                t = threading.Thread(target=ascii, args=("rick",), daemon=True)
                t.start()
                continue
            else:
                print(GREEN + BOLD + msg + RESET)
        except KeyboardInterrupt:
            stop_flag = True
            time.sleep(0.3)
            continue
        except Exception as e:
            print(f'{RED}{BOLD}Connection lost: {e}{RESET}')
            break