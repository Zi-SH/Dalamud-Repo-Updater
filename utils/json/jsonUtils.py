import json

def jsonRequestDecoder(response) -> dict:
    try:
        repoJSON = str(response, 'utf-8')
        repoJSON = json.loads(repoJSON)
    except json.decoder.JSONDecodeError as EncoderMismatch:
        ## Malformed Response
        return {}
    except IndexError:
        ## Empty response
        return {}

    return repoJSON