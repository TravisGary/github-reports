#!/usr/bin/env python3
from github import Github
import csv
import getpass

# using an access token
token = getpass.getpass(prompt="github.com personal access token: ", stream=None)
g = Github(token)

r = raw_input("org/repo: ")
repo = g.get_repo(r)

with open("github-teleport-merges.csv", "w") as csvFile:
    fieldnames = ['number', 'closed_at', 'url']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()

    # https://pygithub.readthedocs.io/en/latest/github_objects/PullRequest.html
    pulls = repo.get_pulls(state='closed', sort='created', base='master')


    for pr in pulls:
        writer.writerow({'number' : pr.number, 'closed_at' : pr.closed_at, "url" : pr.url})
