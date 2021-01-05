import random
import requests
import string
import time


def read_ua_file(filename):
    """ Allow users to add their random User Agent pool to a file. This function will read in the
    provided file to a list for random_ua() to use."""
    user_agents = []
    with open(filename, 'r') as f:
        content = f.readlines()
        for line in content:
            remove_new_line = line[:-1]
            user_agents.append(remove_new_line)
    return user_agents
            
def random_ua(string):
    """ Randomize the list of User Agents provided to reduce the likelihood of script detection
    or ability to block a specific User Agent. For a list of UA's: https://tinyurl.com/y2ry65rw."""
    list_length = len(string)
    agent = random.randrange(list_length)
    return string[agent]


def generate_paths(size=4, chars=string.ascii_lowercase + string.digits):
    """ This function generates the four character alpha numeric string that termbin.com
    uses to store its content."""
    return ''.join(random.choice(chars) for _ in range(size))


def get_link(url):
    """ Add header data to the request and retrieve server response header. A 200 signifies
    content exists while a 404 will indicate no link exists."""
    user_agent_file = read_ua_file('user_agents.txt')
    headers = {
	    'user-agent': random_ua(user_agent_file),
	    'referer': 'https://google.com',
    }
    r = requests.get(url, headers=headers)
    return r.status_code
    

def create_delay():
    """ Create a list of seconds to use as delays breaking up the crawl rate
    to help prevent detection as a crawler."""
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
    while i < 50:
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
