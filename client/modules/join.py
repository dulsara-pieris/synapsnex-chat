import socket
import sys
import os
import subprocess


def is_docker():
         return os.path.exists('/.dockerenv')
         print(" no rick role fun")

def get_host_ip():
         try:
                  result = subprocess.run(
                                ["ip", "route", "show", "default"],
                                capture_output=True,
                                text=True
                  )
                  return result.stdout.split()[2]
         except:
                  return "172.17.0.1"

username = input("Username> ").strip()

if not username:
         print("Username required!")
         sys.exit(1)


if is_docker():
         default_server = get_host_ip()
         print(f"using docker no rick role fun")
else:
         default_server = "127.0.0.1"

SERVER_IP = input(f"Press Enter for {default_server}> ").strip() or default_server
PORT = 5555

print(f"Connecting to {SERVER_IP}:{PORT}...")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
         sock.connect((SERVER_IP, PORT))
except Exception as e:
         print("Connection failed:", e)
         print(f"Tried connecting to: {SERVER_IP}:{PORT}")
         print("Tip: Make sure the relay server is running on the host machine!")
         sys.exit(1)

print("[CONNECTED TO RELAY NODE]")
