from typing import Text
from unicodedata import category
from discord.ext import commands
import discord
from discord_buttons_plugin import *
import asyncio

bot = commands.Bot(command_prefix = "!") #YOUR PREFIX HERE
buttons = ButtonsClient(bot)
token = "YOUR TOKEN HERE"

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Streaming(name="TOURNAMENT", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")) #YOUR BOT ACTIVITY HERE
	print("The bot is ready!")



@buttons.click
async def member_count(ctx):
    await ctx.reply(f"members in {ctx.guild.name} = {ctx.guild.member_count}", flags = MessageFlags().EPHEMERAL)


@bot.command()
async def member_count(ctx):
	await ctx.channel.purge(limit=1)
	await buttons.send(
		content = "Member Count Menu", 
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					emoji = {
								"id": None,
								"name": "👥",
								"animated": False
							},
					label="Member Count", 
					style=ButtonType().Secondary, 
					custom_id="member_count"         
				)
			]),
			
		]
	)


bot.run(token)
