import discord
import GameSenseLinker as gsl
from discord.ext import commands
import time


tracker=discord.client()
config=gsl.loadConfig()
#setup Gamesense using loaded config data
@tracker.event
async def on_ready():
    gsl.setup(config)
#main method to check various conditions of a message
@tracker.event
async def on_message(collect):
    #Ignore if the message comes from you
    if collect.author.id != config["User_Id"] :
        #Find member info based off User_Id
        user=tracker.get_member(config["User_Id"])
        if user.mentioned_in(collect):
            gsl.mentionEvent(config)
            while user.status == 'idle':
                time.sleep(15)
                gsl.mentionEvent()
        elif config["Alert_on_active"]:
            gsl.messageEvent(config)
            while user.status == 'idle':
                time.sleep(15)
                gsl.messageEvent()

tracker.run(config["token"])
