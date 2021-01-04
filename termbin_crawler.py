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
    return string[agent]

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
    """ Create a list of seconds to use as delays breaking up the crawl rate
    to help prevent detection as a crawler. """
    delay_timing = ['1', '2', '3', '4', '5']
    delay = random.choice(delay_timing)
    return time.sleep(int(delay))

def header(msg):
    print("-" * 30)
    print(msg)
    print("-" * 30)

def footer(i, r200, r404, end):
    print("-" * 30)
    print("Total scans completed:       " + str(i))
    print("Nunber of 200 links found:   " + str(r200)) 
    print("Nunber of 404 links found:   " + str(r404)) 
    print("Scan completed in (seconds): " + str(end))
    print("-" * 30)

if __name__ == '__main__':
    start = time.time()
    header("Welcome to Termbin Crawler")
    i = 0
    response_200 = 0
    response_404 = 0
    scrape_history = []
    print("Initializing scan. Standby....\n")
    while i < 5:
        path = generate_paths()
        if path in scrape_history:
            print("Path already scraped: " + path)
            continue
        else:
            url = str('https://termbin.com/' + path)
            response_code = get_link(url)
            if response_code == 200:
                print("\33[32m" + str(response_code) + " - " + url + "\33[0m")
                response_200 += 1
            elif response_code == 404:
                print("\33[31m" + str(response_code) + " - " + url + "\33[0m")
                response_404 += 1
 
        scrape_history.append(path)

        create_delay()

        i += 1
    end = (time.time() - start)
    footer(i, response_200, response_404, end)
