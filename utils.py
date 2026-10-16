from steam_client.steam import Steam
from steam_client.utils import steam_from_registry
import csv

# reading game file contents, reading stored data in autosensdata.csv
def getFromFile(columnToGet, gameId):
    with open("autosensdata.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == gameId:
                return row[columnToGet]
        return "game not found"

def getGameTitleById(gameId):
    return getFromFile(1, gameId) # column 1 in the csv file contains game name

def getMultiplierById(gameId):
    return getFromFile(2, gameId) # column 2 in the csv file contains game's sensitivity multiplier from base
    
def getFilePathById(gameId):
    return getFromFile(3, gameId) # column 3 in the csv file contains filepaths
    



# write to files
def fileWriter():
    pass

# write to autosensdata.csv to add games to the list
def updateStoredData():
    pass

# find steam's file path
def getSteamInstall():
    pass

#find all steam games currently installed using steam-client library
def getSteamGames():
    gamesList = dict()

    from steam_client.utils import steam_from_registry
    steam = steam_from_registry()

    for game in steam.library.games():
        gamesList[game.appid] = game.name

    return gamesList


# check steam file paths from steam
def getFilePaths():
    pass

# obtain a new games multiplier from the internet
def getNewGameMultiplierValue():
    pass



