import sys
import json
from urllib.request import urlopen

# Make a resquest to the GitHub API to get the user's events
def make_request(username):
    response = urlopen(f'https://api.github.com/users/{username}/events')
    data = json.loads(response.read().decode('utf-8'))

    '''
    count = 0
    for event in data:
        if event['type'] == "PushEvent":
            count += 1
    print(f"Count of Events: {count}")
    '''
    

def main():
    username = sys.argv[1]
    make_request(username)


if __name__ == "__main__":
    main()