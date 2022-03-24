#!/usr/bin/env python3
import os

from dotenv import load_dotenv

from discord.ext import commands

load_dotenv(dotenv_path='config')

bot = commands.Bot(command_prefix='!')
async def on_ready(self):
	print('{self.user.display_name} est connecté !')

@bot.command(name="ping")
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command()
async def print(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)
		
	
bot.run(os.getenv('TOKEN'))