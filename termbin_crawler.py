import random
import requests
import string
import time

USER_AGENT = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:80.0) Gecko/20100101 Firefox/80.0",
    "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3"
]

def random_ua(string):
    list_length = len(string)
    agent = random.randrange(list_length)
    random_agent = string[agent]
    return random_agent

def generate_paths(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_link(url):
    headers = {
	    'user-agent': random_ua(USER_AGENT),
	    'referer': 'https://google.com',
    }
    r = requests.get(url, headers=headers)
    return r.status_code
    
def create_delay():
    delays = ['1', '2', '3', '4', '5']
    delay = random.choice(delays)
    return time.sleep(int(delay))

if __name__ == '__main__':
    i = 0
    scrape_history = []
    while i < 5:
        path = generate_paths()
        if path in scrape_history:
            print("Path already scraped: " + path)
            continue
        else:
            url = str('https://termbin.com/' + path)
            print(url + " : " + str(get_link(url)))
        
        scrape_history.append(path)

        # Create a random delay to break up the number of requests
        create_delay()

        i = i + 1
    print("-" * 30)
    print("Total scans completed: " + str(i))
    
