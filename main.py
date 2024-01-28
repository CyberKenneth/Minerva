#Minerva Discord Bot by Kenneth Treadaway was created using the pycord library. Starting on 4/1/2023 at 2:20pm CST. This bot is a work in progress and is not yet complete. I will be adding more features as time goes on. This bot is not yet ready for public use.
# If you would like to use this bot, please contact me at ken cyberresearch (dot) dev. I will be happy to help you get it up and running. I also will be happy to hear any suggestions you may have for this bot. Thank you for your interest in this bot. I hope you enjoy it.

import discord
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up Discord bot with intents
intents = discord.Intents.default()
intents.members = True  # Modify as per your bot's functionality
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

# Loading Gears (Extensions)
# Replace 'gears.secure_gear' with your actual Gear file path
bot.load_extension('gears.secure_gear')
# Load additional Gears individually
# bot.load_extension('gears.another_gear')
# bot.load_extension('gears.yet_another_gear')
# Add more as needed

# Run the bot
bot_token = os.getenv('TOKEN')  # Ensure your .env file has the TOKEN variable set
bot.run(bot_token)
