import discord
from discord.ext import commands
import os
from dotenv import load_env


load_env()


bot = commands.AutoShardedBot(command_prefix=True, help_command=None, case_insensitive=True)


@bot.event
async def on_ready():
    print(f"{bot} is online\n\n{bot} is in {len(bot.guilds)} servers\n\n{len(bot.users)} users")


    
@bot.command()
async def blah_blah_blah(ctx):
    await ctx.send("ok.")


bot.run(os.getenv("TOKEN"))
