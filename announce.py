import os, discord, pdb
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)
@commands.has_role('testmod')
async def announcement(ctx, message):
    await ctx.send(f"You just sent {message}!")