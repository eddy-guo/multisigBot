import os, discord, pdb
import announce
from dotenv import load_dotenv
from discord.ext import commands
from announce import *

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
    role = discord.utils.get(ctx.guild.roles, name="testmod")

    if message.channel.id == 955726679207198741:
        if message.content == "!announce" and user_messages[message.author.name] == "!announce":
            user_messages[message.author.name] = "filler"
            await announce.announcement(ctx, message.content)
            return
        if message.content == "!announce":
                if role in message.author.roles:
                    await ctx.send(f"What would you like to announce, <@" + str(message.author.id) + '>?')
                else:
                    await ctx.send("**Sorry, you do not have permission to do that.**")

    if user_messages[message.author.name] == "!announce":
        await announce.announcement(ctx, message.content)
        channel = bot.get_channel(955726679207198741)
        list = await channel.history(limit=1).flatten()
        if list[0].content == "**Announcement has been approved by moderators and will be sent to the announcements text channel.**":
            channel = bot.get_channel(961988047409414244)
            await channel.send(message.content)
            await ctx.send("**Announcement was successfully sent!**")

    if role in message.author.roles and message.channel.id == 955726679207198741:
        user_messages[message.author.name] = message.content

bot.run(TOKEN)
