from steam_client.steam import Steam

# reading game file contents, reading stored data in autosensdata.csv
def fileReader():
    pass

# write to files
def fileWriter():
    pass

# write to autosensdata.csv to add games to the list
def updateStoredData():
    pass

# find steam's file path
def getSteamInstall():
    pass

#find all steam games listed using steam-client library
def getSteamGames():
    gamesList = dict()

    # On Windows, auto-detect path from registry:
    from steam_client.utils import steam_from_registry
    steam = steam_from_registry()

    for game in steam.library.games():
        gamesList[game.appid] = game.name

    print(gamesList)

# check steam file paths from steam
def getFilePaths():
    pass

# obtain a new games multiplier from the internet
def getNewGameMultiplierValue():
    pass




getSteamGames()

