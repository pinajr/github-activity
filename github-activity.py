import sys
import json
import re
from urllib.request import urlopen

# Verify if the argument and username are valid to test
def verify_argument():
    try:
        valid_user = sys.argv[1]

        # Verify the quantity of arguments insert in the CLI
        if len(sys.argv) > 2 or len(sys.argv) == 1:
            print("Please, insert a right quantity of argument.")
            sys.exit(1)
        else:
            # Laws to has a GitHub usernames
            if not re.match(r"^[a-zA-Z0-9][a-zA-Z0-9-]{0,37}[a-zA-Z0-9]$", valid_user):
                if len(valid_user) == 1 and valid_user.isalnum():
                    print("Please, insert one more character.")
                    sys.exit(1)
                print("Please, insert a valid user.")
                sys.exit(1)

            if "--" in valid_user:
                print("The '--' is not valid. Please insert a valid username.")
                sys.exit(1)

            return valid_user
    # If don't have any argument to verify
    except IndexError:
        print("Please, insert a username to verify the activity.")
        sys.exit(1)


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
    username = verify_argument()

    make_request(username)


if __name__ == "__main__":
    main()