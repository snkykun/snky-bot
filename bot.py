import discord
from discord.ext import commands
emoji = '\N{THUMBS DOWN SIGN}'
client = commands.Bot(command_prefix = '.')
annoying = ()
@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def react(ctx, member : discord.Member):
    reacting = member.id
    @client.event
    async def on_message(message):
        if message.author.id == reacting:
            await message.add_reaction(emoji)

client.run('ODAxMTE5NzIxNDA3MTE5NDEx.YAcC4Q.qmAY0UNvK4lndiZh2knfeefKUc8')
