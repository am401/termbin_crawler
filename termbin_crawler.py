import datetime
import os
import random
import requests
import string
import sys
import time


def read_ua_file(filename):
    """ Allow users to add their random User Agent pool to a file. This function will read in the
    provided file to a list for random_ua() to use."""
    user_agents = []
    try:
        with open(filename, 'r') as f:
            content = f.readlines()
            for line in content:
                remove_new_line = line[:-1]
                user_agents.append(remove_new_line)
        return user_agents
    except IOError as e:
        print("Unable to read from the User Agent file: {}".format(e))
        sys.exit()
            

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


def initiate_request(url):
    """ Add header data to the request and retrieve server response header. A 200 signifies
    content exists while a 404 will indicate no link exists."""
    user_agent_file = read_ua_file('user_agents.txt')
    headers = {
	    'user-agent': random_ua(user_agent_file),
	    'referer': 'https://google.com',
    }
    r = requests.get(url, headers=headers, timeout=5)
    return r
    

def create_delay():
    """ Create a list of seconds to use as delays breaking up the crawl rate
    to help prevent detection as a crawler."""
    delay_timing = ['1', '2', '3', '4', '5']
    delay = random.choice(delay_timing)
    return time.sleep(int(delay))


def save_file(filename, url):
    today = str(datetime.date.today())
    r = initiate_request(url)
    with open('downloads/' + today + '-' + filename, 'wb') as f:
        f.write(r.content)


def header(msg):
    print("-" * 30)
    print(msg)
    print("-" * 30)


def footer(i, r200, r404, end):
    print("-" * 30)
    print("Scan completed on:           " + str(datetime.date.today()))
    print("Total scans completed:       " + str(i))
    print("Nunber of 200 links found:   " + str(r200)) 
    print("Nunber of 404 links found:   " + str(r404)) 
    print("Scan completed in (seconds): " + str(end))
    print("-" * 30)


if __name__ == '__main__':
    """ The script currently requires the downloads directory to be present
        as well as the user_agents.txt file. Check for these and exit if they
        are not present. """
    if not os.path.isdir('downloads'):
        print("The 'downloads' directory does not exist. Please create it and re-run this script.")
        sys.exit()
    if not os.path.isfile('user_agents.txt'):
        print("The 'user_agents.txt' file does not exist. Please create it and re-run this script.")
        sys.exit()
    start_time = datetime.datetime.now()
    header("Welcome to Termbin Crawler")
    i = 0
    response_200 = 0
    response_404 = 0
    scrape_history = []
    print("Initializing scan. Standby....\n")
    while i < 5:
        path = generate_paths()
        if path in scrape_history:
            print("Skipping, already scraped: " + path)
            continue
        else:
            url = str('https://termbin.com/' + path)
            response_code = initiate_request(url).status_code
            if response_code == 200:
                save_file(path, url)
                print(str(i) + ">> \33[32m" + str(response_code) + " - " + url + "\33[0m")
                response_200 += 1
            elif response_code == 404:
                print(str(i) + ">> \33[31m" + str(response_code) + " - " + url + "\33[0m")
                response_404 += 1
            else:
                print("Unable to handle the following request due to unexpected\
                      response code")
                print("\33[33" + str(ressponse_code) + " - " + url + "\33[0m")
 
        scrape_history.append(path)

        create_delay()

        i += 1
    end_time = (datetime.datetime.now() - start_time)
    footer(i, response_200, response_404, end_time)
