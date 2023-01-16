import json
from os import path
from shutil import rmtree
from git import exc, Repo

repository = "https://github.com/Zi-SH/Dalamud-Repo.git"
repoOrigin = "git@github.com:/Zi-SH/Dalamud-Repo.git"
clonePath = "/tmp/dalamud/"

commitMessage = "Automated update of urls"

def readRepo(urlfile: str) -> list:
    if path.exists(clonePath):
        rmtree(clonePath)

    Repo.clone_from(repository, clonePath)

    with open(clonePath + urlfile) as repo_urls:
        repoList = repo_urls.read()
        repoList = json.loads(repoList)

        return repoList

def writeRepo(fileName: str, content: list):
    with open(clonePath + fileName, 'w') as repoList:
        json.dump(content, repoList, indent=4)

def commitRepo():
    repo = Repo(clonePath)

    repo.index.add("ffxiv_custom_repo.json")
    repo.index.add("repo_urls.json")
    repo.index.add("invalid_repo_urls.json")
    repo.index.add("outdated_repo_urls.json")

    repo.index.commit(message=commitMessage)

def pushRepo():
    repo = Repo(clonePath)

    repo.remotes.origin.set_url(repoOrigin)
    repo.git.push('--set-upstream', 'origin', 'main')
    repo.remotes.origin.push()