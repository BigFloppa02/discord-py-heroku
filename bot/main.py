import discord
from discord.ext import commands

TOKEN = "ENV_TOKEN"

bot = commands.Bot(command_prefix=(':otter:'))
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print("Я даун!")

@bot.command()
async def Пошелнахуй(ctx):
    await ctx.send('Самопошел')


bot.run(TOKEN)
