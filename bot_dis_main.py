# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
import os

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        rand = random.randint(1,2)
        if rand == 1:
            await ctx.send(f'Нет, {ctx.subcommand_passed} это не круто')
        elif rand == 2:
            await ctx.send(f'Да, {ctx.subcommand_passed} это круто')


@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def ask(ctx):



bot.run('TOKEN')
