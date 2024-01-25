#Minerva Discord Bot by Kenneth Treadaway was created using the pycord library. Starting on 4/1/2023 at 2:20pm CST. This bot is a work in progress and is not yet complete. I will be adding more features as time goes on. This bot is not yet ready for public use.
# If you would like to use this bot, please contact me at ken cyberresearch (dot) dev. I will be happy to help you get it up and running. I also will be happy to hear any suggestions you may have for this bot. Thank you for your interest in this bot. I hope you enjoy it.

import discord
import os # default module
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.members = False  # Enable the members intent

bot = discord.Bot(intents=intents) # load all the variables from the env file


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    
@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")
#bot.load_extension('cogs.Greetings') 


#cogs_list = [
 #   'cogs.greeting'  # greeting.py
#]

#or cog in cogs_list:
 #   bot.load_extension(cog) 
bot.run(os.getenv('TOKEN')) # run the bot with the token
