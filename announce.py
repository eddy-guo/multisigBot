import os, discord, pdb, asyncio, emoji
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command()
async def announcement(ctx, message):
    if message == "!announce":
        await ctx.send('You can only announce one message at a time, and only when the previous announcement is finished its evaluation.')
    else:
        global response
        response = await ctx.send(f"You just sent {message}!")

        good = emoji.emojize(':check_mark_button:')
        bad = emoji.emojize(':cross_mark:')

        await response.add_reaction(good)
        await response.add_reaction(bad)

@bot.command()
async def checkreaction(ctx):
    await asyncio.sleep(5)
    updated = await response.channel.fetch_message(response.id)
    if updated.reactions[0].count > updated.reactions[1].count:
        await ctx.send("Announcement is good to send!")
    else:
        await ctx.send('Announcement is not approved.')