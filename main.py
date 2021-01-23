import discord
from discord.ext import commands
import os
from dotenv import load_env


load_env()


bot = commands.AutoShardedBot(command_prefix=True, help_command=None, case_insensitive=True)

@bot.event
async def on_ready():
    print(f"{bot} is online")



bot.run(os.getenv("TOKEN"))
