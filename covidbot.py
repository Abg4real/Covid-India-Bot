# bot.py
import os
import requests
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


def get_corona_update():
    url = 'https://api.covid19india.org/data.json?'
    response = requests.get(url)
    data = response.json()
    active = str(int(data["statewise"][0]["active"]))
    confirmed = str(int(data["statewise"][0]["confirmed"]))
    deaths = str(int(data["statewise"][0]["deaths"]))
    recovered = str(int(data["statewise"][0]["recovered"]))
    return_data = "Cofirmed cases: " + confirmed + \
        "\nActive: " + active + "\nDeaths: " + deaths + "\nRecovered: " + recovered
    return(str(return_data))


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    channel = message.channel
    content = message.content

    if content == '.covid-update':
        update = get_corona_update()
        await channel.send(update)

client.run(TOKEN)
