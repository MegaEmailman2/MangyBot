#! python

import asyncio
import os
import discord
import psutil
from discord.ext.commands import Bot

intents = discord.Intents.default()
Intents.message_content = True

with open("TokenFile.txt", encoding="utf-8") as TokenFile:
        token=TokenFile.read()

client = Bot(command_prefix="!Server", intents=intents)

@client.command(name='start',
                description="Starts a server decided by SE, TC, or (Future Project)",
                brief="Starts a server."
                usage="'!Server start TC' will boot The Center"
                pass_context=True)
async def start(context):
    outstring = "Attempting to start the server now."
    target = context.message_content[13:14]
    if target == "TC":
        os.system(PATH/TO/TC/BAT)   #Fill in
    elif target == "SE":
        os.system(PATH/TO/SE/BAT)   #Fill in
    await context.send(outstring)
    
@client.command(name='stop',
                description="Stops a server decided by SE, TC, or (Future Project)",
                brief="Stops a server."
                usage="'!Server stop TC' will stop The Center"
                pass_context=True)
async def stop(context):
    target = context.message_content[13:14]
    if target == "TC":
        procname = etsuTC   ###Experimental
    elif target == "SE":
        procname = etsuSE   ###Experimental
    for process in psutil.process_iter():
        if procname in process.name():
            process.kill()
    outstring = ("Attempting to stop the server running " + target + ".")
    await context.send(outstring)
    
@client.command(name='update',
                description="Updates the game servers.  Stop them first.",
                brief=""
                usage="!Server update"
                pass_context=True)
async def update(context):
    outstring = "Attempting to update the servers.  Please wait 10 minutes before starting them."
    #Run the update batch file
    await context.send(outstring)
              
    
def startup():
    print("Entering startup!")
    client.run(token)
    
if __name__ == "__main__":
    startup()