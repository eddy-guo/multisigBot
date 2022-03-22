import os, discord, pdb
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
    print(f"{bot.user} is now connected to {guild.name}.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.channel.id == 955726679207198741:
        ctx = await bot.get_context(message)
        await ctx.send("Hi!")
    await bot.process_commands(message)

@bot.command(pass_context=True)
@commands.has_role('testmod')
async def modcheck(ctx):
    await ctx.send("Hello moderator")

bot.run(TOKEN)
