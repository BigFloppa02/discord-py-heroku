import discord
from discord.ext import commands

TOKEN = "ODM4NzIxMjIxNjQxMjQwNjE2.YI_OAQ.M3dKR83S6x0wBoaeUSs5kmcJc24"

bot = commands.Bot(command_prefix=(':otter:'))
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print("Я даун!")

@bot.command()
async def Пошелнахуй(ctx):
    await ctx.send('Самопошел')


bot.run(TOKEN)
