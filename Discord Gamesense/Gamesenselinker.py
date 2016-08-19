import json
import requests
import jsonposts

#Load the JSON POST data from (see jsonposts.py)
caseSwitch = {
    SETUP: jsonposts.send_discord
    CREATE_EVENT: jsonposts.message_event
    EVENT_DEFAULTS: jsonposts.bind_message_event
    MESSAGE_EVENT: jsonposts.message_event
    MENTION_EVENT: jsonposts.mention_event
}
#Get which exact address we need to POST to
addressSwitch = {
    SETUP:"game_metadata"
    CREATE_EVENT:"register_game_event"
    EVENT_DEFAULTS:"bind_game_event"
    MESSAGE_EVENT:"game_event"
    MENTION_EVENT:"game_event"
}
#load up the config file
def loadConfig():
    with open('config.json') as configfile:
        config=json.load(configfile)
    return config

#For sending pre-defined JSON to Gamesense
def postToGameSense(config,case):
    #open coreProps.json to get the Gamesense port and address
    with open(config[corepropsdir]) as propfile:
        coreprop = json.load(propfile)
    #build the address
    operation=caseSwitch.get(case)
    subaddress=addressSwitch.get(case)
    address = 'http://'+coreprop[address]+'/'+subaddress
    #POST to Gamesense
    session.post(address,json=(operation))

#Setup game and message event with some default settings
def setup(config):
    postToGameSense(config,SETUP)
    postToGameSense(config,CREATE_EVENT)
    postToGameSense(config,EVENT_DEFAULTS)
#Trigger POST event for a message
def messageEvent(config):
    postToGameSense(config,MESSAGE_EVENT)
#Trigger POST event for a mention
def mentionEvent(config):
    postToGameSense(config,MENTION_EVENT)
