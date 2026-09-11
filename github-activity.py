import sys
import json
import re
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from typing import Optional

def parse_argument() -> Optional[str]:
    # Retrieve the raw CLI argument, or None if invalid.
    if len(sys.argv) != 2:
        print("The correct command is 'github-activity.py <username>'"
        "\nPlease try again.")
        return None
    return sys.argv[1]
    

def validate_username(valid_user) -> Optional[str]:
    # Checks if the username complies with GitHub's regex rules.
    if not re.fullmatch(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*", valid_user):
        print("Please insert a valid user.")
        return None
    return valid_user


def exit_if_none(value, exit_code=1):
    # End the program if the value be None
    if value == None:
        sys.exit(exit_code)


def fetch_events(username):
    # Make a resquest to the GitHub API to get the user's events.
    # Handling HTTP and network errors.
    url = f'https://api.github.com/users/{username}/events'

    try:
        response = urlopen(url, timeout=5)
    except HTTPError as e:
        print(f"Error retrieving activities for '{username}': {e.code} {e.reason}")
        return None
    except URLError as e:
        print(f"Could not connect to GitHub: {e.reason}")
        return None

    data = json.loads(response.read().decode('utf-8'))
    return data


def format_event(events):
    pass

'''
count = 0
for event in data:
    if event['type'] == "PushEvent":
        count += 1
print(f"Count of Events: {count}")
'''


def main():
    argument = parse_argument()
    exit_if_none(argument)

    username = validate_username(argument)
    exit_if_none(username)

    events = fetch_events(username)
    exit_if_none(events)


if __name__ == "__main__":
    main()