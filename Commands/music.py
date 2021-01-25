import discord
from discord.ext import commands
from discord.utils import get
import nacl
import youtube_dl
import os

colors = [0xFFFF33, 0xADFF2F, 0xe67e22]

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['p', 'play'])
    async def p_cmd(self, ctx, url: str):
        vs = ctx.author.voice
        if vs is not None:
            existing_song = os.path.isfile("song.mp3")
            try:
                if existing_song:
                    os.remove("song.mp3")
            except PermissionError:
                await ctx.send("Music is not queued, use pp!end and play a different song.")
                return

            vc = vs.channel
            await vc.connect()
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                await ctx.send("Downloading.. may take some time.", delete_after=5)
                ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
            try:
                await voice.play(discord.FFmpegPCMAudio("song.mp3"))
            except:
                pass

        elif vs is None:
            await ctx.send("Join a voice channel first.")

    @commands.command(name='join', aliases=['j', 'connect', 'c'])
    async def c_cmd(self, ctx):
        guild = ctx.guild
        vs = ctx.author.voice ## Voice State
        if vs is None:
            await ctx.send('Join a voice channel first.')
        elif vs is not None:
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

    @commands.command(name='pause', aliases=['stop', 's'])
    async def pause_cmd(self, ctx):
        guild = ctx.guild
        voice = get(self.bot.voice_clients, guild=guild)
        if voice.is_playing():
            await voice.pause()
        elif not voice.is_playing():
            await ctx.send("There is nothing to pause.")

    @commands.command(name='resume', aliases=['r'])
    async def res_cmd(self, ctx):
        guild = ctx.guild
        voice = get(self.bot.voice_clients, guild=guild)
        if voice.is_paused():
            await voice.resume()
        elif not voice.is_paused():
            await ctx.send("Do you mean `pp!replay?` the music is currently playing or has ended.")

    @commands.command(name='end', aliases=['e'])
    async def e_cmd(self, ctx):
        guild = ctx.guild
        voice = get(self.bot.voice_clients, guild=guild)
        if voice.is_playing():
            await voice.stop()
        elif not voice.is_playing():
            await ctx.send("There is no music to stop playing currently.")

def setup(bot):
    bot.add_cog(music(bot))
