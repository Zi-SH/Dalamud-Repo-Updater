from utils.DalamudTags import tags
from utils.DalamudRepo import readRepo, writeRepo, commitRepo, pushRepo
from utils.DalamudPlugin import retrieveJSON
from utils.json.jsonUtils import jsonRequestDecoder
from conditions.ConditionChecker import checkConditions

validPluginList = []

validRepoList = []
outdatedRepoList = []
invalidRepoList = []

repoFile = "repo_urls.json"

repoList = readRepo(repoFile)

for repo in repoList:
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

    for plugin in repoJSON:
        plugin = {key: value for key, value in plugin.items() if key in tags}

        if checkConditions(plugin):
            plugin = dict(sorted(plugin.items()))
            validPluginList.append(plugin)
        else:
            outdatedRepoList.append(repo)

writeRepo("ffxiv_custom_repo.json", validPluginList)

writeRepo("repo_urls.json", validRepoList)
writeRepo("outdated_repo_urls.json", outdatedRepoList)
writeRepo("invalid_repo_urls.json", invalidRepoList)

commitRepo()
pushRepo()