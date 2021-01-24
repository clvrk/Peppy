import discord
from discord.ext import commands
from discord.utils import get
import nacl

colors = [0xFFFF33, 0xADFF2F, 0xe67e22]

class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join', aliases=['j', 'connect', 'c'])
    async def p_cmd(self, ctx):
        guild = ctx.guild
        vs = ctx.author.voice ## Voice State
        if vs is None:
            await ctx.send('After you, mate.')
        if vs is not None:
            vc = vs.channel
            await vc.connect()

    @commands.command(name='leave', aliases=['disconnect', 'd', 'l'])
    async def l_cmd(self, ctx):
        guild = ctx.guild
        voice = get(self.bot.voice_clients, guild=guild)
        if voice.is_connected():
            await voice.disconnect()
        elif not voice.is_connected():
            await ctx.send("Can't leave something im not currently in, can i?")


def setup(bot):
    bot.add_cog(music(bot))
