import discord
import random
import os
import re
import sys
import pastas
import botkey
import emoji
import asyncio
import datetime
from discord.ext import commands
from discord import Embed, File
# import google_auth_oauthlib.flow
# import googleapiclient.discovery
# import googleapiclient.errors
# from googleapiclient.discovery import build
client = commands.Bot(command_prefix = '.')

# Setup
# os.chdir(os.path.dirname(sys.argv[0]))
@client.event
async def on_ready():
    oec_gen = client.get_channel(743941628984557711)
    sai_gen = client.get_channel(565401084718481410)
    print('Bot is ready')
    custom = discord.Game('snky.cc')
    await client.change_presence(status=discord.Status.online, activity=custom)
    await oec_gen.send('hello oec nation')
    # await sai_gen.send('Bot is ready, time to post hampters.')
picList = ["floppa", "possum", "cat", "monkey", ""]
benResponse = ['eww.gif', 'laugh.gif', 'no.gif', 'slamphone.gif', 'yes.gif']

#listener
@client.listen()
async def on_message(message):

    if message.author.id != 801119721407119411 and message.channel.id != 885594398669283331:
        msgStr = ((message.content).lower()).split()

        if message.channel.id == 814613616950902834 and len(message.embeds) > 0:
            channel = client.get_channel(565401767416692747)
            embed = discord.Embed.copy(message.embeds[0])
            await channel.send(embed=embed)

        # BEN
        if 'ben' in msgStr:
            if '?' in message.content:
                await message.channel.send(file=File("./data/ben/" + str(benResponse[random.randint(0,4)])))
            elif 'bye' in message.content:
                await message.channel.send(file=File("./data/ben/slamphone.gif"))
                print("triggered ben bye")
            elif 'ben' == (message.content).lower():
                await message.channel.send(file=File("./data/ben/benring.gif"))
                print("triggered ben only")

        # FIX TWITTER
        # if 'https://x.com' or 'https://twitter.com' in message.content:
        #
        #     xcom_pattern = r'https://x\.com/[^\s]+'
        #     twitter_pattern = r'https://twitter\.com/[^\s]+'
        #
        #     xcom_match = re.search(xcom_pattern, message.content)
        #     twitter_match = re.search(twitter_pattern, message.content)
        #
        #     # Replace the matched domain in the link
        #     if xcom_match:
        #         await message.channel.send(re.sub(r'https://x\.com/', 'https://fxtwitter.com/', xcom_match.group()))
        #     elif twitter_match:
        #         await message.channel.send(re.sub(r'https://twitter\.com/', 'https://fxtwitter.com/', twitter_match.group()))



        # PASTAS
        for x in pastas.triggers:
            if x in msgStr:
                index = pastas.triggers.index(str(x))
                if './data/' in pastas.triggerResponse[index]:
                    await message.channel.send(file=File(pastas.triggerResponse[index]))
                else:
                    message = await message.channel.send(pastas.triggerResponse[index])
                if 'counter' == pastas.triggerResponse[index]:
                    await message.add_reaction('👍')

#-------deprecated-------#
        # if 'goats' in msgStr:
        #     await message.channel.send(pastas.goat)
        #
        # if 'ninja' in msgStr:
        #     await message.channel.send(pastas.ninja)
        #
        # if 'innit' in msgStr:
        #     await message.channel.send(pastas.innit)
        #
        # if 'kephrii' in msgStr:
        #     await message.channel.send(pastas.kephrii)
        #
        # if 'based' in msgStr:
        #     await message.channel.send(pastas.based)
        #
        # if 'simp' in msgStr:
        #     await message.channel.send(pastas.simp)
        #
        # if 'pee' in msgStr:
        #     await message.channel.send(pastas.pee)
        #
        # if 'furry' in msgStr:
        #     await message.channel.send(pastas.furry)
        #
        # if 'cringe' in msgStr:
        #     await message.channel.send(pastas.cringe)
        #
        # if 'flashy' in msgStr:
        #     await message.channel.send(pastas.flashy)
        #
        # if 'what are you doing' in msgStr:
        #     await message.channel.send('YO MAMA')
        # old leave join shit
        #
        # if message.channel.id == 743941744927834133:
        #     str = message.content
        #
        #     if 'gone' in str.lower():
        #         await message.add_reaction('<:peepoSad:820015915676336180>')
        #     else:
        #         await message.add_reaction('<:Pog:820015969966751815>')
        # if message.author.id == 390308146293243904:
        #     await message.add_reaction('🐒')
        # if message.author.id == 274656834315616256:
        #     await message.add_reaction('<:cryingcat:796506331523055686>')
        # if 'cum' in msgStr:
        #     # await message.add_reaction('👎')
        #     await message.channel.send('cum')
        # if 'shadowplay' in msgStr:
        #         await message.channel.send(file=File("./data/chadowplay.mp4"))
        # if 'scort' in msgStr and message.author.id != 355144450437021697:
        #         await message.channel.send(file=File("./data/Retard-lf8zQN6agAw.mp4"))
        # if 'mercy montage' in msgStr:
        #         await message.channel.send(file=File("./data/MercyMontage-nMTj67b_Boc.mp4"))
        # if 'peak' in msgStr:
        #         await message.channel.send(file=File("./data/KW2fX8VRPVwcPYUC.mp4"))
        # if 'hampter' in msgStr:
        #     await message.channel.send('https://tenor.com/view/hampter-gif-20240312')
        # if message.author.id == 66056020786425856:
        #     await message.channel.send('this you? https://cdn.discordapp.com/avatars/66056020786425856/dfa93feb88c85a0183eac633d95e3007.webp?size=2048')

## commands
@client.command()
async def submit(ctx, code=None, link=None):
    msg = ctx.message.content
    if ctx.channel.id == 746754347764809869:
        if 'https' in link.lower() and code != None:
            await ctx.send('Thank you for your submission, a mod will approve/remove your frag shortly! Other members may vote by reacting to the submission with the corresponding emojis.')
            await ctx.message.add_reaction('✔️')
            await ctx.message.add_reaction('❌')
        else:
            await ctx.send(ctx.message.author.mention + ' Submit a frag by typing `.submit <replay code> <video link>`')

@client.command()
async def possum(ctx):
    async with ctx.channel.typing():
        await ctx.channel.send(file=File("./data/possum/" + random.choice(os.listdir("./data/possum"))))

@client.command()
async def floppa(ctx):
    async with ctx.channel.typing():
        await ctx.channel.send(file=File("./data/floppa/" + random.choice(os.listdir("./data/floppa"))))

@client.command()
async def cat(ctx):
    async with ctx.channel.typing():
        await ctx.channel.send(file=File("./data/cat/" + random.choice(os.listdir("./data/cat"))))

@client.command(aliases=['monkey', 'monki', 'monke'])
async def _monkey(ctx):
    async with ctx.channel.typing():
        await ctx.channel.send(file=File("./data/monkey/" + random.choice(os.listdir("./data/monkey"))))

@client.command()
async def ym(ctx):
    await ctx.channel.send('YO MAMA')
    await ctx.message.delete()

@client.command()
async def real(ctx):
    await ctx.channel.send('real')
    await ctx.message.delete()

@client.command()
async def say(ctx):
    msg = ctx.message.content
    await ctx.channel.send(msg[4:])
    await ctx.message.delete()

@client.command()
async def fym(ctx):
    if (ctx.message.mentions[0]).id == 801119721407119411:
        embed = discord.Embed(
        description = "**Snky** fucks **" + ctx.message.author.display_name + "'s** mother"
        )
        embed.set_footer(text="you cannot fuck Snky's mother")
        embed.set_image(url='https://c.tenor.com/GryShD35-psAAAAC/troll-face-creepy-smile.gif')
        await ctx.channel.send(embed=embed)
    elif (ctx.message.mentions[0]).id == 818622709655273532:
        await ctx.channel.send("no")
        await ctx.channel.send(file=File('./data/JdKRgS-6boMbY9nZ.mp4'))
    else:
        embed = discord.Embed(
        description = "**" + ctx.message.author.display_name + "** fucks **" + (ctx.message.mentions[0]).display_name + "'s** mother"
        )
        embed.set_footer(text='and everyone clapped..')
        embed.set_image(url='https://c.tenor.com/Ftt4ZlVWDUwAAAAC/mom-your-mom.gif')
        await ctx.channel.send(embed=embed)

# for pics in picList:
#     @client.command()
#     async def pics(ctx):
#         await ctx.channel.send(file=File("./data/" + str(pics) + "/" + random.choice(os.listdir("./data/" + str(pics)))))

@client.command(aliases=['freestyle', 'dof', 'reshade', 'greenscreen'])
async def _freestyle(ctx):
    await ctx.channel.send('Nvidia Freestyle in Overwatch guide https://youtu.be/lAEkQdQGRNA Text version: https://github.com/snkykun/Overwatch-Freestyle')

@client.command(aliases=['dolly', 'cam', 'dollycam'])
async def _dolly(ctx):
    await ctx.channel.send('Creating an HLAE style dolly cam inside overwatch with AHK https://github.com/snkykun/Overwatch-Dolly')

@client.command()
@commands.has_role('Frag Approver')
async def approve(ctx):
    channel = client.get_channel(790682495167234080)
    await channel.send(ctx.message.reference.resolved.content + " hit by " + ctx.message.reference.resolved.author.mention)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def servers(ctx):
  servers = list(client.guilds)
  await ctx.send(f"Connected on {str(len(servers))} servers:")
  await ctx.send('\n'.join(guild.name for guild in servers))

client.run(botkey.key)

# @client.command()
# async def edit(ctx, *, source=None):
#     if source == 'source':
#         await ctx.send('Videos are sourced from this playlist here: https://www.youtube.com/playlist?list=PL-qDtdxHx3uLL7QVV3hXh08tKJU5PHy-5')
#     else:
#         vid_link = 'https://www.youtube.com/watch?v=' + str(random.choice(YoutubeAPI.vid_ids))
#         await ctx.send(vid_link)

# @client.listen()
# @commands.has_role('Frag Approver')
# async def on_message(msg):
#   if msg.author.id != 801119721407119411 and msg.channel.id == 803087684779114516:
#       await msg.channel.send('1')
