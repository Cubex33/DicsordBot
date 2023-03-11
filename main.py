import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def привет (ctx):
 await ctx.channel.send(f'привет')

@bot.event
async def on_ready():
    print("I am connected!")

@bot.event
async def on_message_edit(before, after):
    if before.content == after.content:
        return
    await before.channel.send(f"Сообщении было изменено!\n{before.content} -> {after.content}")
 
bot.run('OTgwNDk5OTMzNzg0MzMwMjYw.Gfhxee.5gjAHruUcDw2R-eRh7Cu1jzW-vNz8cVRAxqQ7M')
