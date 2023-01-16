from utils.DalamudTags import tags
from utils.DalamudRepo import readRepo, writeRepo
from utils.DalamudPlugin import retrieveJSON
from utils.json.jsonUtils import jsonRequestDecoder
from conditions.ConditionChecker import checkConditions

invalidRepoList = []

validRepoFile = "repo_urls.json"
invalidRepoFile = "invalid_repo_urls.json"
outdatedRepoFile = "outdated_repo_urls.json"

recheckList = readRepo(invalidRepoFile)

validRepoList = readRepo(validRepoFile)
outdatedRepoList = readRepo(outdatedRepoFile)

for repo in recheckList:
    response = retrieveJSON(repo)
    if response is None:
        invalidRepoList.append(repo)
        continue

    repoJSON = jsonRequestDecoder(response)
    if len(repoJSON) == 0:
        invalidRepoList.append(repo)
        continue
    else:
        validRepoList.append(repo)

    plugin = {key: value for key, value in repoJSON.items() if key in tags}

    if checkConditions(plugin):
        validRepoList.append(repo)
    else:
        outdatedRepoList.append(repo)

writeRepo("repo_urls.json", validRepoList)
writeRepo("outdated_repo_urls.json", outdatedRepoList)
writeRepo("invalid_repo_urls.json", invalidRepoList)
