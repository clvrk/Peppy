import discord
from discord.ext import commands
import time
from datetime import datetime

#variable for the bot to know when it started
starttime = time.time()




class Devtools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @command.commands()
    async def uptime(self, ctx)
        #Delta func and more functions to calculate and convert to more neat format

        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        up = discord.Embed(title="The Bot Uptime Is:", description=f"`{seconds}s, {minutes}m, {hours}h, {days}d\n`", color = 0xe67e22)
        await ctx.send(embed=up)
     


def setup(bot):
    bot.add_cog(Devtools(bot))
