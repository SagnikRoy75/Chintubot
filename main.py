import os
from itertools import cycle
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

# import praw

load_dotenv()

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    change_status.start()


status = cycle(['WhiteHatJr SEO', ' with wolf gupta', 'with Lana Rhoades'])


@tasks.loop(seconds=300)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(title=':x: oops! You do not have permission to use this command.',
                              color=discord.Colour.red())
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title=':x:You are missing the required arguements. Please check if your command requires an addition arguement.',
            color=discord.Colour.red())
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandNotFound):
        pass


for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')
        
@bot.command()
async def youtube(ctx,search):


	search_keyword=search
	html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	await ctx.send("https://www.youtube.com/watch?v=" + video_ids[0])


bot.run(os.getenv("TOKEN"))
