import os, discord, pdb, asyncio
from dotenv import load_dotenv
from discord.ext import commands
from asyncio import sleep

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command()
async def announcement(ctx, message):
    if message == "!announce":
        await ctx.send(f"You can only announce one message at a time. Please try again.")
    else:
        response = await ctx.send(f"You just sent {message}!")
        moai = '\U0001F5FF'
        money = '\U0001F4B8'
        brain = '\U0001F9E0'
        await response.add_reaction(moai)
        await response.add_reaction(money)
        await response.add_reaction(brain)
        response = await response.channel.fetch_message(response.id)
        print(response.reactions)