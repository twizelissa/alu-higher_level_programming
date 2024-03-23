#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to oldest) of a given repository by the user.
Usage: ./100-github_commits.py [repository name] [owner name]
"""

import requests
import sys

def list_commits(repository, owner):
    # GitHub API endpoint for listing commits
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    # Make a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        commits = response.json()

        # Print the list of commits
        for commit in commits[:10]:  # Get the first 10 commits
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        # Print an error message if the request was not successful
        print(f"Error: Failed to fetch commits. Status code: {response.status_code}")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py [repository name] [owner name]")
        sys.exit(1)

    # Get the repository name and owner name from command line arguments
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # List commits for the given repository and owner
    list_commits(repository_name, owner_name)
