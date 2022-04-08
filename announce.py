import os, discord, pdb, asyncio, emoji
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
        global response
        response = await ctx.send(f"You just sent {message}!")

        good = emoji.emojize(':check_mark_button:')
        bad = emoji.emojize(':cross_mark:')

        await response.add_reaction(good)
        await response.add_reaction(bad)
        response = await response.channel.fetch_message(response.id)

@bot.command()
async def checkreaction():
    print(response.content)
    print(response.reactions)