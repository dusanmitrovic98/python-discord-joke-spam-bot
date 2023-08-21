import discord
import requests
import asyncio

# Your bot's token
TOKEN = ''

# ID of the target server and channel
SERVER_ID = 114251
CHANNEL_ID = 114278

jokes_api_url = 'https://v2.jokeapi.dev/joke/Any'  # Change 'Any' to a specific category if desired

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
