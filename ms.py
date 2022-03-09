import os, discord, pdb
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    global guild
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f"{bot.user} is now connected to {guild.name}.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    ctx = await bot.get_context(message)
    await ctx.send("Hi!")

bot.run(TOKEN)