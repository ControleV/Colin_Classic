from json import load, dump, dumps

def Stats():
    with open("Jsons/PrefJsons/UserStats.json", "r", encoding= 'utf-8') as a:
        statsData = load(a)
    
    return statsData

def ReadGuildPreferences(guildId):
    with open("Jsons/PrefJsons/GuildPreferencies.json", "r", encoding= 'utf-8') as b:
        guildData = load(b)

    lingua = guildData[str(guildId)]["language"]
    
    return lingua

def ReadLanguages(lingua, command):
    with open("Jsons/Languages.json", "r", encoding= 'utf-8') as c:
        languagesData = load(c)

    usado = languagesData[lingua][command]
    
    return usado

def ReadNickNames():
    with open("Jsons/GenericNickNames.json", "r") as d:
        namesData = load(d)

    return namesData

def ReadArtes():
    with open("Jsons/artes.json", "r") as e:
        artesData = load(e)

    return artesData

def DumpStats(data):
    with open('Jsons/PrefJsons/UserStats.json', 'w') as f:
        dump(data, f, indent= 4)
    
def DumpStatsList(data):
    with open('Jsons/PrefJsons/UserStats.json', 'w') as f:
        dumps(data, f, indent= 4)

def DumpGuildPref(data):
    with open("Jsons/PrefJsons/GuildPreferencies.json", "w") as g:
        dump(data, g, indent= 4)
