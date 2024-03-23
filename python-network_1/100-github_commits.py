#!/usr/bin/python3
"""Fetches and lists commits from a GitHub repository."""

import sys
import requests

def get_commits(repo_name, owner_name):
    """Fetches and lists 10 commits from the specified GitHub repository."""
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Failed to fetch commits. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    get_commits(repo_name, owner_name)