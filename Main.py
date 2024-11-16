#! python

import asyncio
import os
import discord
import subprocess
import psutil
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.message_content = True

with open("TokenFile.txt", encoding="utf-8") as TokenFile:
        token=TokenFile.read()

client = Bot(command_prefix="!Server ", intents=intents)

@client.command(name='start',
                description="Starts a server decided by SE, TC, or (Future Project)",
                brief="Starts a server.",
                usage="'!Server start TC' will boot The Center",
                pass_context=True)
async def start(context):
    outstring = "Attempting to start the server now."
    target = context.message.content[14:]
    if target == "TC":
        subprocess.Popen("C:\\Users\\Backup\\Desktop\\Center.bat", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) 
    elif target == "SE":
        subprocess.Popen("C:\\Users\\Backup\\Desktop\\Scorch.lnk", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    await context.send(outstring)
    
@client.command(name='stop',
                description="Stops a server decided by SE, TC, or (Future Project)",
                brief="Stops a server.",
                usage="'!Server stop TC' will stop The Center",
                pass_context=True)
async def stop(context):
    procname=""
    target = context.message.content[13:]
    if target == "TC":
        procname = "Center"   ###Experimental
    elif target == "SE":
        procname = "etsuSE"   ###Experimental
    for process in psutil.process_iter():
        print(procname)
        print(process.name())
        if procname in process.name():
            process.kill()
    outstring = ("Attempting to stop the server running " + target + ".")
    await context.send(outstring)
    
@client.command(name='update',
                description="Updates the game servers.  Stop them first.",
                brief="",
                usage="!Server update",
                pass_context=True)
async def update(context):
    outstring = "Attempting to update the servers.  Please wait 10 minutes before starting them."
    subprocess.Popen("C:\\Users\\Backup\\Desktop\\Update.bat")
    await context.send(outstring)

@client.command(name='test',
		description="Guess.",
		usage="!Server test",
		pass_context=True)
async def test(context):
	await context.send("GG The bot is live.")
              
    
def startup():
    print("Entering startup!")
    client.run(token)
    
if __name__ == "__main__":
    startup()