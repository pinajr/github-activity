import sys
import json
import re
from urllib.request import urlopen

def parse_argument():
    # Retrieve the raw CLI data to valid it and prevents an IndexError.
    try:        
        if len(sys.argv) > 2:
            print("The correct command is 'github-actitivy.py <username>'"
            "\nPlease try again.")
            return None
        return sys.argv[1]
    except IndexError:
        print("Please insert a <username> to verify the activity.")
        return None
    

def validate_username(valid_user):
    # Checks if the username complies with GitHub's regex rules.
    if not re.fullmatch(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*", valid_user):
        print("Please, insert a valid user.")
        sys.exit(1)
    return valid_user


def make_request(username):
    # Make a resquest to the GitHub API to get the user's events.
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
    parse_argument()


if __name__ == "__main__":
    main()