import discord
import os
from discord.commands import commands
from keep_alive import keep_alive
from discord.commands import Option

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Slash commands on.")


@bot.slash_command(guild_ids=[893076282286436392])
async def hello(ctx):
    """Say hello to the bot""" 
    await ctx.respond(f"Hello {ctx.author}!")


@bot.slash_command(
    name="hi")  # Not passing in guild_ids creates a global slash command (might take an hour to register)
async def global_command(ctx, num: int):
    await ctx.respond(f"This is a global command, {num}!")


@bot.slash_command(guild_ids=[893076282286436392])
async def joined(
    ctx, member: discord.Member = None
):  # Passing a default value makes the argument optional
    user = member or ctx.author
    await ctx.respond(f"{user.name} joined at {discord.utils.format_dt(user.joined_at)}")

@bot.slash_command(guild_ids=[893076282286436392])
async def userid(ctx):
    """Get current command user ID."""  
    await ctx.respond(f"Your user ID is `{ctx.author.id}`.")

@bot.slash_command(guild_ids=[893076282286436392])
@commands.is_owner() 
async def status(ctx, *, msg):
    activity = discord.Game(name=f"{msg}")
    await bot.change_presence(status=discord.Status.do_not_disturb,activity=activity)
    await ctx.respond(f'Made {msg} the status.')

@bot.slash_command(guild_ids=[893076282286436392])
async def hellodetailed(ctx, name: Option(str, "Enter your name"),                                          gender: Option(str, "Choose your gender", choices=["Male", "Female", "Other"]),
    age: Option(int, "Enter your age", required=True, default=18),
):
    await ctx.respond(f"Hello {name}. Your gender is {gender} and you are {age} years old.")

keep_alive()
bot.run(os.getenv('token')) 
