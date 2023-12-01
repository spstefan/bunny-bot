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
import schedule
import time

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


# ---- EVENTS AND FUNCTIONS ----
@client.event
async def on_ready() -> None:
    print(f'Logged in as {client.user}')

    # Send daily message at set time
    schedule.every().day.at("16:00").do(daily_message(client))


async def daily_message(client) -> None:
    channel = client.get_channel(channel_id)

    if channel:
        await channel.send('Hello')
    else:
        print('Channel not found')


# ---- RUN THE BOT ---- 
client.run(token, log_handler=handler, log_level=logging.DEBUG)