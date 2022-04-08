import os, discord, pdb, asyncio, emoji
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command()
async def announcement(ctx, message):
    if message == "!announce":
        await ctx.send('Sorry, you can only announce one message at a time, '
                      f'and only when the previous announcement is finished its evaluation.')
    else:
        global response
        good = emoji.emojize(':check_mark_button:')
        bad = emoji.emojize(':cross_mark:')
        response = await ctx.send('__Please evaluate the following message and decide whether ' 
                                 f'it is appropriate as a server-wide announcement. '
                                 f'Vote by reacting on {good} and {bad} for **in favor** and **against** respectively.__'
                                 f'\n\n{message}')
        await response.add_reaction(good)
        await response.add_reaction(bad)

@bot.command()
async def checkreaction(ctx):
    await asyncio.sleep(5)
    updated = await response.channel.fetch_message(response.id)
    if updated.reactions[0].count > updated.reactions[1].count:
        await ctx.send("**Announcement has been approved by moderators and will be sent to the announcements text channel.**")
    else:
        await ctx.send('**Announcement has been rejected by moderators and will not be sent.**')