#Minerva Discord Bot by Kenneth Treadaway was created using the pycord library. Starting on 4/1/2023 at 2:20pm CST. This bot is a work in progress and is not yet complete. I will be adding more features as time goes on. This bot is not yet ready for public use.
# If you would like to use this bot, please contact me at ken cyberresearch (dot) dev. I will be happy to help you get it up and running. I also will be happy to hear any suggestions you may have for this bot. Thank you for your interest in this bot. I hope you enjoy it.

"""
Importing the libraries
Using the command "pip3 install pipreqs" and "pip-tools" to create the requirements.txt file
    """

import os
import random
import discord
# import sys
from dotenv import load_dotenv # used to import the token from the .env file
#import pycord #importing the pycord library
#import asyncio

#print(sys.path)
#defining the global variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#defining the Function for importing the token
@client.event
async def on_ready():
    print("Bot is now online!")
    

@client.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")

@client.user_command(name="Say Hello")
async def hi(ctx, user):
    await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")
    
'''UNCOMMENT THIS CODE TO ENABLE THE BOT TO RESPOND TO MESSAGES gpt
# https://jman4190.medium.com/how-to-build-a-discord-gpt3-chat-bot-with-openai-and-python-14177cd926f0
# MAKE SURE TO UNCOMMENT THE IMPORTS AT THE TOP OF THE FILE
# Make sure also to make this async in its own cog file so it  can hang and be responsive to other commands
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith(‘Hello Mr. Botface’):
    await message.channel.send(‘Howdy Stranger’)
'''

client.run(TOKEN)