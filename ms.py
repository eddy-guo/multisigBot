import os, discord, pdb
import announce
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client()

@bot.event
async def on_ready():
    global guild
    guild = discord.utils.get(bot.guilds, name=GUILD)
    global user_messages
    user_messages = {}
    for member in guild.members:
        user_messages[member.name] = "filler"
    print(f"{bot.user} is now connected to {guild.name}.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    ctx = await bot.get_context(message)
    if message.channel.id == 955726679207198741:
        if message.content == "!announce":
            await ctx.send(f"What would you like to announce, <@" + str(message.author.id) + '>?')
    
    for user in user_messages:
        if user_messages[user] == "!announce" and user == message.author.name:
            await announce.announcement(ctx, message.content)
    user_messages[message.author.name] = message.content
    print(user_messages)

bot.run(TOKEN)
