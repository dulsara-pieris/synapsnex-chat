import socket
import threading
import time

clients = []

def broadcast(msg, sender):
        for c in clients:
                if c != sender:
                        try:
                                c.send(msg)
                        except:
                                pass

def handle_client(conn, addr):
        clients.append(conn)
        print(f"[+] Connected: {addr}")

        while True:
                try:
                        data = conn.recv(1024)
                        if not data:
                                break
                        broadcast(data, conn)
                except:
                        break

        clients.remove(conn)
        conn.close()
        print(f"[-] Disconnected: {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen()

print("=== RETRO RELAY NODE ONLINE ===")
print("PORT: 5555")

while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
