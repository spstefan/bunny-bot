"""
BunnyBot sends a message at set time every day asking users to report their mood using reactions. 
At midnight, the reactions are tallied up and saved to a file. Using this data, the bot can create
visualisations with Altair which users can retrieve with a command. 

In order to set up the bot in your server you will have to set environmental variables in the environment
the bot will run on. The names of these variables can be found (or modified) under the section 'SETUP'. 
"""

import discord
import os
import logging
from discord.ext import tasks
import datetime

# ---- SETUP ---- 
# Sends logs to a file: 'discord.log'
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Server/app specific environmental variables
token = os.getenv('DISCORD_BOT_TOKEN')
channel_id = os.getenv('CHANNEL_ID')

# Permissions for the bot
intents = discord.Intents.default()

# Initialize client
client = discord.Client(intents=intents)

# Time to send the daily message
daily_message_time = datetime.time(hour=22, minute=45, second=0) 


# ---- EVENTS AND FUNCTIONS ----
@client.event
async def on_ready() -> None:
    print(f'Logged in as {client.user}')

    if not daily_message.is_running():
        daily_message.start() #If the task is not already running, start it.
        print(f"Daily message function ran {datetime.date.now()}")


@tasks.loop(time=daily_message_time) 
async def daily_message(client) -> None:
    channel = client.get_channel(channel_id)

    if channel:
        message = await channel.send('Hello')
        message_id = message.id
        print(f'Daily message sent at {datetime.datetime.now()}')
    else:
        print('Channel not found')


# ---- RUN THE BOT ---- 
client.run(token, log_handler=handler, log_level=logging.DEBUG)