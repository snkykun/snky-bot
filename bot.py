import discord
from discord.ext import commands
emoji = '\N{THUMBS DOWN SIGN}'
client = commands.Bot(command_prefix = '.')



annoying = []
@client.command()
async def annoy(ctx, member : discord.Member):
    annoying.append(member.id)
@client.event
async def on_message(message):
    if message.author.id in annoying:
        await message.add_reaction(emoji)



        
# annoying = []
# @client.command()
# async def annoy(ctx, member : discord.Member):
#     annoying.append(member.id)
#     print(annoying)
# @client.event
# async def on_message(message):
#     if message.author.id in annoying:
#         await message.add_reaction(emoji)
# @client.event
# async def on_ready():
#     print('Bot is ready')
# @client.command()
# async def annoy(ctx, member : discord.Member):
#     await member.add_roles(annoying)
# @client.event
# async def on_message(message):
#     if ('annoying') in message.author.roles:
#         await message.add_reaction(emoji)


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge()

client.run('ODAxMTE5NzIxNDA3MTE5NDEx.YAcC4Q.qmAY0UNvK4lndiZh2knfeefKUc8')
