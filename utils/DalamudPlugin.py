import urllib.error
from urllib.request import Request, urlopen

def retrieveJSON(url: str):
    repoRequest = Request(url, headers={'User-Agent': 'Scions/7.0'})
    repoResponse = None

    try:
        repoResponse = urlopen(repoRequest, timeout=10).read()
    except urllib.error.HTTPError as HTTPError:
        if "404" in HTTPError:
            return None

    return repoResponse