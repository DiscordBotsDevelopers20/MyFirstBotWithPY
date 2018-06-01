import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

bot = discord.Client()
bot_prefix= "<"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    await bot.change_presence(game=discord.Game(name="HELP | {} Users ".format(len(set(bot.get_all_members()))),type=3))



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot:
        return
    elif message.content.startswith('<test'):
        await bot.send_message(message.channel ,"Done !")
    

bot.run(process.env.BOT_TOKEN)
