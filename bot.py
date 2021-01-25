import discord
import pastas
import botkey
import emoji
import asyncio
import datetime
from discord.ext import commands
client = commands.Bot(command_prefix = '.')

## Setup
@client.event
async def on_ready():
    print('Bot is ready')
    custom = discord.Game('snky.cc')
    await client.change_presence(status=discord.Status.online, activity=custom)


## Pastas
@client.listen()
async def on_message(message):
  str = message.content
  if message.author.id == 235751410979962892:
      await message.add_reaction('<:cringe:585938141496475673>')
  if message.author.id == 274656834315616256:
      await message.add_reaction('<:cryingcat:796506331523055686>')
  if 'come' in str.lower() and message.author.id != 801119721407119411:
    await message.add_reaction('👎')
    await message.channel.send('*cum')

  if 'goat' in str.lower() and message.author.id != 801119721407119411:
      await message.channel.send(pastas.goat)

  if 'innit' in str.lower() and message.author.id != 801119721407119411:
    await message.channel.send(pastas.innit)

  if 'based' in str.lower() and message.author.id != 801119721407119411 and message.channel.is_nsfw():
    await message.channel.send(pastas.based)

  if 'simp' in str.lower() and message.author.id != 801119721407119411:
    await message.channel.send(pastas.simp)

  if 'pee' in str.lower() and message.author.id != 801119721407119411:
    await message.channel.send(pastas.pee)

## commands
@client.command()
async def submit(ctx):
    msg = ctx.message.content
    if ctx.channel.id == 746754347764809869:
        if 'https' in msg.lower():
            await ctx.send('Thank you for your submission, a mod will approve/remove your frag shortly!')
        elif msg[7:] == "":
            await ctx.send(ctx.message.author.mention + ' Submit a frag by typing `.submit <replay code> <video link>`')
        else:
            await ctx.send(ctx.message.author.mention + ' You need a link displaying the frag you are submitting! Record it and upload to a site like streamable or youtube, then resubmit with `.submit <replay code> <video link>`')

@client.command()
@commands.has_role('Frag Approver')
async def approve(ctx):
    channel = client.get_channel(790682495167234080)
    await channel.send(ctx.message.reference.resolved.content[6:] + " hit by " + ctx.message.reference.resolved.author.mention)



# @client.listen()
# @commands.has_role('Frag Approver')
# async def on_message(msg):
#   if msg.author.id != 801119721407119411 and msg.channel.id == 803087684779114516:
#       await msg.channel.send('1')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

client.run(botkey.key)
