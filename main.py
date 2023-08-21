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

    server = client.get_guild(SERVER_ID)
    if server is None:
        print(f"Error: Couldn't find server with ID {SERVER_ID}")
        return

    channel = server.get_channel(CHANNEL_ID)
    if channel is None:
        print(f"Error: Couldn't find channel with ID {CHANNEL_ID} in server {server.name}")
        return

    while True:
        response = requests.get(jokes_api_url)
        joke_data = response.json()
        
        if 'joke' in joke_data:
            joke = joke_data['joke']
            await channel.send(joke)
        elif 'setup' in joke_data and 'delivery' in joke_data:
            setup = joke_data['setup']
            delivery = joke_data['delivery']
            await channel.send(f"{setup}\n{delivery}")
            await channel.send(f"===================================================")
        
        await asyncio.sleep(1)

client.run(TOKEN)

import discord
import requests
import asyncio
