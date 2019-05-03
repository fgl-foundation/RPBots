
Serverid=573555922996297728



def GetAccessToken(id):
    import json
    return json.loads(open('AccessToken.json','r').read())[str(id)]
    
def GetBotNames():
    import json
    return list(json.loads(open('AccessToken.json','r').read()).keys())