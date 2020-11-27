import os

import discord
from dotenv import load_dotenv
from mcstatus import *
from datetime import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
server = MinecraftServer.lookup("142.44.135.67:25575")
status = server.status()

motd = [ motdtext['text'] for motdtext in status.raw['description']['extra']]
#print(usersConnected)

@client.event
async def on_ready():
    status = server.status()
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your commands."))
    #print(status.raw)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'sninfo':
        status = server.status()
        try:
            usersConnected = [ user['name'] for user in status.raw['players']['sample'] ]
        except KeyError:
            usersConnected = ["None"]
        auth = str(message.author).split("#")
        dt = str(datetime.now()).split()
        embed = discord.Embed(title="Server Info",colour=discord.Colour.red())
        embed.add_field(name="Server IP",value="`142.44.135.67:25575`",inline=False)
        embed.add_field(name="# of Players Online",value="`"+str(status.players.online)+"/"+str(status.players.max)+"`",inline=False)
        embed.add_field(name="Players Online",value="`"+"`, `".join(usersConnected)+"`",inline=False)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/775408277616853075/779091594955587584/logoisgood.gif")
        embed.set_footer(text=str(auth[0])+" • "+str(dt[0]))
        await message.channel.send(embed=embed)
    elif message.content == 'pplonline':
        status = server.status()
        try:
            usersConnected = [ user['name'] for user in status.raw['players']['sample'] ]
        except KeyError:
            usersConnected = ["None"]
        auth = str(message.author).split("#")
        dt = str(datetime.now()).split()
        embed = discord.Embed(title="People Online",colour=discord.Colour.red())
        embed.add_field(name='~~~~~~~~~~~~~~~~~~~~',value="`"+"`, `".join(usersConnected)+"`",inline=False)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/775408277616853075/779091594955587584/logoisgood.gif")
        embed.set_footer(text=str(auth[0])+" • "+str(dt[0]))
        await message.channel.send(embed=embed)
    elif message.content == 'snversion':
        status = server.status()
        auth = str(message.author).split("#")
        dt = str(datetime.now()).split()
        embed = discord.Embed(title="Server Version",colour=discord.Colour.red())
        embed.add_field(name='~~~~~~~~~~~~~~~~~~~~',value="`"+str(status.version.name)+"`",inline=False)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/775408277616853075/779091594955587584/logoisgood.gif")
        embed.set_footer(text=str(auth[0])+" • "+str(dt[0]))
        await message.channel.send(embed=embed)
    elif message.content == 'snmotd':
        status = server.status()
        auth = str(message.author).split('#')
        dt = str(datetime.now()).split()
        embed = discord.Embed(title="Server MOTD",colour=discord.Colour.red())
        embed.add_field(name='~~~~~~~~~~~~~~~~~~~~',value="`"+str(motd[0])+"`",inline=False)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/775408277616853075/779091594955587584/logoisgood.gif")
        embed.set_footer(text=str(auth[0])+" • "+str(dt[0]))
        await message.channel.send(embed=embed)



client.run(TOKEN)
