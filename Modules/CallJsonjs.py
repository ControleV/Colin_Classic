import json

def Stats():
    with open("Jsons/PrefJsons/UserStats.json", "r", encoding= 'utf-8') as a:
        statsData = json.load(a)

    return statsData

def ReadGuildPreferences(guildId):
    with open("Jsons/PrefJsons/GuildPreferencies.json", "r", encoding= 'utf-8') as b:
        guildData = json.load(b)

    lingua = guildData[str(guildId)]["language"]

    return lingua

def ReadLanguages(lingua, command):
    with open("Jsons/Languages.json", "r", encoding= 'utf-8') as c:
        languagesData = json.load(c)

    usado = languagesData[lingua][command]

    return usado

def ReadNickNames():
    with open("Jsons/GenericNickNames.json", "r") as d:
        namesData = json.load(d)

    return namesData

def ReadArtes():
    with open("Jsons/artes.json", "r") as e:
        artesData = json.load(e)

    return artesData

def DumpStats(data):
    with open('Jsons/PrefJsons/UserStats.json', 'w') as f:
        json.dump(data, f, indent= 4)
    
def DumpStatsList(data):
    with open('Jsons/PrefJsons/UserStats.json', 'w') as f:
        json.dumps(data, f, indent= 4)

def DumpGuildPref(data):
    with open("Jsons/PrefJsons/GuildPreferencies.json", "w") as g:
        json.dump(data, g, indent= 4)
