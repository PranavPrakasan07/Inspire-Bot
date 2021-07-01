import discord
import os
import requests
import json
from keep_alive import keep_alive 

client = discord.Client()
my_secret = os.environ['BOT_TOKEN']

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return quote

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'): 
    #channel = client.get_channel(831211258023772190)

    await message.channel.send("Hello " + f"{message.author.mention}")

  if message.content.startswith('$inspire'):
    await message.channel.send(get_quote())
  

keep_alive()
client.run(my_secret)