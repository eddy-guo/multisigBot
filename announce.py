import os, discord, pdb
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command()
async def announcement(ctx, message):
    if message == "!announce":
        await ctx.send(f"You can only announce one message at a time. Please try again.")
    else:
        await ctx.send(f"You just sent {message}!")