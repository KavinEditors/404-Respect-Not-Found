import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# Predefined content from earlier
sussy_advices = [...]
insults = [...]
roasts = [...]

@bot.event
async def on_ready():
    print(f"404Bot is online as {bot.user}")

@bot.slash_command(guild_ids=[GUILD_ID], description="Get a random sussy advice")
async def advice(ctx):
    await ctx.respond(random.choice(sussy_advices))

@bot.slash_command(guild_ids=[GUILD_ID], description="Try to gain respect. Spoiler: You won't.")
async def gainrespect(ctx):
    await ctx.respond("No respect for the one who has 0 IQ.")

@bot.slash_command(guild_ids=[GUILD_ID], description="Ask the bot about your future")
async def future(ctx):
    response = random.choice(["Probably yes.", "No.", "Bruh.", "LMAO nope."])
    await ctx.respond(response)

@bot.slash_command(guild_ids=[GUILD_ID], description="Rickroll someone or yourself")
async def rickroll(ctx):
    await ctx.respond("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@bot.slash_command(guild_ids=[GUILD_ID], description="Get insulted by the 404Bot")
async def insult(ctx):
    await ctx.respond(random.choice(insults))

@bot.slash_command(guild_ids=[GUILD_ID], description="Get roasted")
async def roast(ctx):
    await ctx.respond(random.choice(roasts))

@bot.slash_command(guild_ids=[GUILD_ID], description="Trash another user")
async def trashuser(ctx, user: discord.Member):
    await ctx.respond(f"{user.mention}, you're officially trash. 404: Skill Not Found.")

bot.run(TOKEN)

