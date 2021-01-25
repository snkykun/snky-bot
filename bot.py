import discord
import pastas
import ClientID
import emoji
from discord.ext import commands
client = commands.Bot(command_prefix = '.')

## Setup
@client.event
async def on_ready():
    print('Bot is ready')
    custom = discord.Game('snky.cc')
    await client.change_presence(status=discord.Status.online, activity=custom)

## Come correction
@client.listen()
async def on_message(message):
  str = message.content
  if 'come' in str.lower() and message.author.id != 801119721407119411:
    await message.add_reaction(:thumbs_down:)
    await message.channel.send('*cum')

## PASTAS
@client.listen()
async def on_message(message):
  str = message.content
  if 'goat' in str.lower() and message.author.id != 801119721407119411:
    await message.channel.send(pastas.goat)

@client.listen()
async def on_message(message):
  str = message.content
  if 'innit' in str.lower() and message.author.id != 801119721407119411:
    await message.channel.send(pastas.innit)

@client.listen()
async def on_message(message):
  str = message.content
  if 'based' in str.lower() and message.author.id != 801119721407119411 and message.channel.is_nsfw():
    await message.channel.send(pastas.based)

@client.listen()
async def on_message(message):
  str = message.content
  if 'simp' in str.lower() and message.author.id != 801119721407119411:
    await message.channel.send(pastas.simp)

@client.listen()
async def on_message(message):
  str = message.content
  if 'pee' in str.lower() and message.author.id != 801119721407119411:
    await message.channel.send(pastas.pee)
## commands
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

client.run(ClientID.ID)
