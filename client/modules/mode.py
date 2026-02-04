if is_public_ip(SERVER_IP):
        MODE = "GLOBAL"
        VISIBILITY = "PUBLIC"
else:
        MODE = "LOCAL"
        VISIBILITY = "PRIVATE"

print(CYAN + "[CONNECTED TO RELAY NODE]" + RESET)
print(YELLOW + f"[MODE: {MODE} CHAT]" + RESET)
print(f"[RELAY IP: {SERVER_IP}]")
print(f"[RELAY VISIBILITY: {VISIBILITY}]")
print("[TYPE /help FOR COMMANDS]\n")

threading.Thread(target=listen, daemon=True).start()
