import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.AutoShardedBot(command_prefix='pp!', help_command=None, case_insensitive=True)

colors = [0xFFFF33, 0xADFF2F]

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online")


extensions = ['Commands.music']


if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)


bot.run(os.getenv("TOKEN"))
