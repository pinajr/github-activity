# GitHub User Activity

A simple command-line interface (CLI) that fetches and displays the recent activity of a GitHub user using the GitHub API.

This project was built to practice working with APIs, JSON data, command-line arguments, error handling, and Python's standard library.

[View Project](https://github.com/pinajr/github-activity)

## Features

* Accepts a GitHub username as a command-line argument
* Fetches recent user activity from the GitHub API
* Displays activity directly in the terminal
* Handles invalid usernames and API errors
* Uses only Python's standard library
* Requires no external libraries or frameworks

## Requirements

* Python 3.x
* Internet connection

No external Python packages are required.

## Usage

Clone the repository:

```bash
git clone https://github.com/your-username/github-user-activity.git
cd github-user-activity
```

Run the application:

```bash
python3 github-activity.py <username>
```

For example:

```bash
python3 github-activity.py kamranahmedse
```

Example output:

```text
Pushed commits to kamranahmedse/developer-roadmap
Opened an issue in kamranahmedse/developer-roadmap
Starred kamranahmedse/developer-roadmap
```

## How It Works

The application receives a GitHub username from the command line and uses the GitHub Events API to retrieve the user's recent public activity.

The response is returned as JSON, which the application processes to identify and display relevant events in a readable format.

The general flow is:

```text
GitHub username
       ↓
Command-line argument
       ↓
GitHub API request
       ↓
JSON response
       ↓
Event processing
       ↓
Terminal output
```

## API

This project uses the GitHub REST API Events endpoint:

```text
https://api.github.com/users/<username>/events
```

For more information, see the [GitHub REST API documentation](https://docs.github.com/en/rest/activity/events).

## Error Handling

The application handles common errors such as:

* Missing username argument
* Invalid GitHub username
* API request failures
* Unexpected API responses

## Technologies

* Python
* GitHub REST API
* JSON
* Command-line interface

## Project Goals

This project was created as a learning exercise to practice:

* Python functions and control flow
* Command-line interfaces
* HTTP requests
* REST APIs
* JSON data processing
* Error handling
* Working with Python's standard library

## Future Improvements

Possible improvements include:

* Filtering activity by event type
* Supporting additional GitHub API endpoints
* Improving terminal output formatting
* Adding pagination
* Adding caching
* Creating automated tests

## License

This project is available under the MIT License.
