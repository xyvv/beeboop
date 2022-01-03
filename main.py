import discord, os
from discord.ext import commands

import music

client = commands.Bot(command_prefix="&", intent = discord.Intents.all())
token = os.environ['beeboop-token']

cogs = [music]
for i in range(len(cogs)):
  cogs[i].setup(client)


client.run(token) 

