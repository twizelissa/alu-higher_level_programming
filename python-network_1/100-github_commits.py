#!/usr/bin/env python3
"""
This script lists 10 commits (from the most recent to oldest)
of a specified repository by the specified owner.
"""

import requests
import sys
import time

def get_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        return commits
    elif response.status_code == 403:  # Rate limit exceeded
        print("Rate limit exceeded. Waiting for one minute...")
        time.sleep(60)
        return get_commits(repo, owner)
    else:
        print(f"Error: {response.status_code}")
        return []

def main():
    if len(sys.argv) != 3:
        print("Usage: ./script.py <repository name> <owner name>")
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]

    commits = get_commits(repo, owner)
    if commits:
        for commit in commits[:10]:  # Print only the first 10 commits
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")
    else:
        print("No commits found.")

if __name__ == "__main__":
    main()