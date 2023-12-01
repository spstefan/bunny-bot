"""
Docstring... 
"""

import discord
import os
import logging
import schedule
import time

# Sends logs to a file: 'discord.log'
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Server/app specific environmental variables
token = os.getenv('DISCORD_BOT_TOKEN')
channel_id = os.getenv('CHANNEL_ID')

DAILY_MESSAGE_TIME = time(16, 0, 0)

intents = discord.Intents.default()


client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    # Start the daily message task




client.run(token, log_handler=handler, log_level=logging.DEBUG)
