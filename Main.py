#! python

import asyncio
import discord
import subprocess
import psutil
import os
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.message_content = True

with open("TokenFile.txt", encoding="utf-8") as TokenFile:
        token=TokenFile.read()

client = Bot(command_prefix="!Server ", intents=intents)

@client.command(name='start',
                description="Starts a server decided by SE, TC, or (Future Project)",
                brief="Starts a server.  Check specific help for map codes",
                usage="'!Server start TC' will boot The Center",
                pass_context=True)
async def start(context):
    outstring = "```Attempting to start the server now.```"
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
     for process in psutil.process_iter(['pid', 'name', 'cmdline']):
         if procname in str(process.info['cmdline']):
             process.kill()
     outstring = ("```Attempting to stop the server running " + target + ".```")
     await context.send(outstring)

@client.command(name='update',
                description="Updates the game servers.  Stop them first.",
                brief="",
                usage="!Server update",
                pass_context=True)
async def update(context):
    outstring = "```Attempting to update the servers.  Please wait 10 minutes before starting them.```"
    subprocess.Popen("C:\\Users\\Backup\\Desktop\\Update.bat")
    await context.send(outstring)
    
@client.command(name='Admin',
                description='Don't worry about it.',
                brief='',
                usage='!Admin'
                pass_context=True)
async def Admin(context):
    if os.path.exists('C:\\Users\\Backup\\Desktop\\AdminOn.txt'):
        result = subprocess.run(context.message.content[14:], capture_output=True, text=True, check=True)
        await context.send(result.stdout)
    else:
        await context.send("And stay out!  Or ask Paul to enable the permissions.")
        
def startup():
    print("Entering startup!")
    client.run(token)
    
if __name__ == "__main__":
    startup()