import discord
from discord.ext import commands
import time
from datetime import datetime
import random

#variable for the bot to know when it started
starttime = time.time()


colors = [0xFFFF33, 0xADFF2F, 0xe67e22]


class Devtools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.launch_time = datetime.utcnow()

    @commands.command()
    async def Uptime(self, ctx):
        uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        up = discord.Embed(
            title="Uptime",
            description=f"`I have been online for {days}d, {hours}h, {minutes}m`",
            color=random.choice(colors)
        )
        if ctx.author.id == 461287425625554950 or 513351917481623572:
            await ctx.send(embed=up)

    @commands.command()
    async def ping(self, ctx):
        if ctx.author.id == 461287425625554950 or 513351917481623572:
            before = time.monotonic()
            msg = await ctx.send('Pinging...')
            ping = (time.monotonic() - before) * 1000

            if ping < 200:
                color = 0x35fc03
            elif ping < 350:
                color = 0xe3f51d
            elif ping < 500:
                color = 0xf7700f
            else:
                color = 0xf7220f

            mbed = discord.Embed(
                title="Ping Stats",
                color=color
            )
            mbed.add_field(name="Latency", value=f'{int(ping)}ms')
            mbed.add_field(name="API", value=f'{round(self.bot.latency * 1000)}ms')
            mbed.set_thumbnail(url=self.bot.user.avatar_url)
            await msg.edit(content=None, embed=mbed)



def setup(bot):
    bot.add_cog(Devtools(bot))
