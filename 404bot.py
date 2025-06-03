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

# --- 100 Sussy Advices ---
sussy_advices = [
    "Trust no one, especially the pizza delivery guy.",
    "Always carry a rubber chicken for emergencies.",
    "If you hear footsteps behind you, run twice as fast.",
    "Pretend to be asleep to avoid responsibilities.",
    "Forget sunscreen and become a lobster for a day.",
    "Wear socks with sandals to confuse your enemies.",
    "Keep a plant on your desk and name it 'WiFi'.",
    "Talk to your plants. They know your secrets.",
    "Use ketchup as a hair gel for a spicy look.",
    "Replace sugar with salt for an unexpected twist.",
    "Show up to meetings wearing a cape. Instant respect.",
    "Never trust a dog that barks at nothing.",
    "Make your bed with the blanket on the floor.",
    "Dance randomly in public for stress relief.",
    "Hide all your spoons to prevent theft.",
    "Talk in movie quotes only for a whole day.",
    "Pretend your reflection is your evil twin.",
    "Ask your toaster for life advice.",
    "Put googly eyes on everything you own.",
    "Eat dessert first. Life's too short for rules.",
    "Sleep with one eye open, just in case.",
    "Keep a diary of your pet's thoughts.",
    "Shout 'Plot twist!' at random moments.",
    "Carry a spoon everywhere, just in case.",
    "Say 'bless you' to plants when watering them.",
    "Use a banana as a phone to confuse friends.",
    "Pretend your shadow is your bodyguard.",
    "Always wear mismatched shoes for style points.",
    "Make a fort out of pillows and live there.",
    "Turn your umbrella inside out for rain surprise.",
    "Carry a book titled 'How to be normal'.",
    "Call your furniture by pet names.",
    "Speak only in rhymes until someone notices.",
    "Put a 'Do not disturb' sign on your forehead.",
    "Use invisible ink to write your grocery list.",
    "Invent a secret handshake with your reflection.",
    "Wear sunglasses at night to hide your secrets.",
    "Pretend you're on a cooking show while eating.",
    "Tell your plants bedtime stories nightly.",
    "Replace your ringtone with a chicken cluck.",
    "Use a magnifying glass to read cereal boxes.",
    "Keep a paperclip as your lucky charm.",
    "Talk to your shoes before putting them on.",
    "Count how many times you blink per minute.",
    "Make shadow puppets and name them.",
    "Take naps standing up for ultimate power naps.",
    "Write your to-do list in invisible ink.",
    "Call your phone 'the boss'.",
    "Wear a hat made of aluminum foil for protection.",
    "Hide in plain sight by blending with wallpaper.",
    "Invent new words and use them confidently.",
    "Pretend you're a spy and act suspiciously.",
    "Use emojis in real-life conversations only.",
    "Draw smiley faces on all your belongings.",
    "Say 'I'm watching you' to random objects.",
    "Balance a book on your head while walking.",
    "Use your non-dominant hand for everything today.",
    "Make a secret handshake with your shadow.",
    "Use a hairbrush as a microphone and perform.",
    "Talk to your reflection in a different accent.",
    "Wear socks on your hands for a day.",
    "Pretend your pet understands everything you say.",
    "Keep a diary of your weirdest dreams.",
    "Dance like nobody's watching, even when they are.",
    "Say 'Surprise!' before answering the phone.",
    "Make a 'Do not pet' sign for your dog.",
    "Pretend you're from another planet and ask questions.",
    "Use ketchup as paint and decorate your food.",
    "Wear a cape when doing chores for superpowers.",
    "Hide your snacks in the freezer for safekeeping.",
    "Take selfies with random objects and post them.",
    "Pretend to be a statue when someone looks at you.",
    "Invent a secret language and use it today.",
    "Name your shadow and talk to it.",
    "Use a flashlight to read in broad daylight.",
    "Draw a mustache on your hand and talk through it.",
    "Make a list of your top 10 weirdest habits.",
    "Wear pajamas to a formal event virtually.",
    "Use a leaf as a bookmark and pretend it's magic.",
    "Pretend your reflection is your twin sibling.",
    "Balance a spoon on your nose to impress friends.",
    "Talk like a pirate while ordering food.",
    "Take a selfie with your favorite plant.",
    "Make a hat out of paper and wear it proudly.",
    "Pretend your furniture is alive and greet it.",
    "Sing your grocery list instead of saying it.",
    "Use a sock puppet to order pizza.",
    "Write a love letter to your favorite snack.",
    "Hide your keys in a secret spot every day.",
    "Pretend to be invisible in crowded places.",
    "Speak in movie quotes during conversations.",
    "Use a hairdryer as a microphone for karaoke.",
    "Call your pet by different names daily.",
    "Dance in slow motion whenever possible.",
    "Draw funny faces on your fingers and tell stories.",
    "Pretend you're a news anchor reporting life.",
    "Wear sunglasses indoors for mystery points.",
    "Take a bubble bath with a rubber ducky.",
    "Write your name backwards and sign it that way.",
    "Use your phone upside down for a challenge.",
    "Pretend your shoes have superpowers.",
    "Make a tiny hat for your favorite mug.",
    "Use a banana as a phone in serious talks.",
    "Draw your dream vacation and hang it up.",
    "Talk to your pet in a foreign accent.",
    "Pretend you're a statue in a museum.",
    "Write a poem about your favorite food.",
    "Wear mismatched socks to confuse people."
]

# --- 90 Roasts ---
roasts = [
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You have something on your chin... no, the third one down.",
    "You're the reason why the gene pool needs a lifeguard.",
    "You're as useless as the 'g' in lasagna.",
    "You're so dense, light bends around you.",
    "You're proof that evolution can go in reverse.",
    "You're like a software update. Whenever I see you, I think 'Not now.'",
    "You're about as sharp as a marble.",
    "Your secrets are safe with me. I never even listen when you tell me them.",
    "You're like a puzzle with half the pieces missing.",
    "You bring everyone so much joy… when you leave the room.",
    "If I wanted to kill myself, I'd climb your ego and jump to your IQ.",
    "You have something on your chin... no the third one down.",
    "You're the human version of a participation trophy.",
    "Your gene pool could use a lifeguard.",
    "You're as bright as a black hole.",
    "You're the reason the chicken crossed the road—to get away from you.",
    "You're as useless as a screen door on a submarine.",
    "You have something on your chin... no the third one down.",
    "You are like a cloud. When you disappear, it’s a beautiful day.",
    "You're about as useful as a white crayon.",
    "You have the charm and personality of a damp rag.",
    "Your face makes onions cry.",
    "You're the human embodiment of a migraine.",
    "You have the IQ of a rock, but less interesting.",
    "You bring everyone so much joy... when you leave the room.",
    "You have the charisma of a damp sock.",
    "Your secrets are safe with me. I never even listen when you tell me them.",
    "You're like a puzzle with missing pieces.",
    "You have the personality of a wet mop.",
    "You make onions cry.",
    "You're like a cloud. When you disappear, it’s a beautiful day.",
    "You have the charm and personality of a damp rag.",
    "You’re the human version of a participation trophy.",
    "You're as bright as a black hole.",
    "You're the reason the chicken crossed the road—to get away from you.",
    "You're about as useful as a screen door on a submarine.",
    "You're as sharp as a marble.",
    "Your face could scare a hungry lion away.",
    "You're as welcome as a rash in a swimming pool.",
    "You have the personality of stale bread.",
    "You're like a slinky — not really good for anything, but you bring a smile to my face when pushed down the stairs.",
    "You're as useless as a chocolate teapot.",
    "You are the reason why there is a 'No Running' sign at the pool.",
    "Your brain’s so small, it fits in a peanut.",
    "You're like a broken pencil: pointless.",
    "You bring everyone so much joy… when you leave the room.",
    "You have the charisma of a damp rag.",
    "You have the personality of a wet mop.",
    "You're about as bright as a black hole.",
    "You’re the human version of a participation trophy.",
    "You have something on your chin... no, the third one down.",
    "You’re as sharp as a marble.",
    "You're like a software update — whenever I see you, I think ‘Not now.’",
    "You bring everyone so much joy... when you leave the room.",
    "Your secrets are safe with me. I never even listen when you tell me them.",
    "You are like a cloud. When you disappear, it's a beautiful day.",
    "You have the charm and personality of a damp rag.",
    "You're as useless as the 'g' in lasagna.",
    "Your gene pool could use a lifeguard.",
    "You're the human embodiment of a migraine.",
    "You make onions cry.",
    "You have the IQ of a rock, but less interesting.",
    "You have the personality of stale bread.",
    "You're as welcome as a rash in a swimming pool.",
    "You're as useless as a screen door on a submarine.",
    "You have the charisma of a damp sock.",
    "You're like a broken pencil: pointless.",
    "You’re the reason the chicken crossed the road—to get away from you.",
    "You have the charm and personality of a damp rag.",
    "You have something on your chin... no, the third one down.",
    "You're about as sharp as a marble.",
    "Your face could scare a hungry lion away.",
    "You're like a cloud. When you disappear, it’s a beautiful day.",
    "You bring everyone so much joy... when you leave the room.",
    "You're the human version of a participation trophy.",
    "You’re as sharp as a marble.",
    "Your brain’s so small, it fits in a peanut."
]

# --- 100 Insults ---
insults = [
    "You're as sharp as a butter knife in a pillow fight.",
    "If ignorance is bliss, you must be the happiest person alive.",
    "You bring everyone so much joy... when you leave the room.",
    "You're as useless as a screen door on a submarine.",
    "Your secrets are safe with me. I never even listen when you tell me them.",
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You're as bright as a black hole.",
    "You have the charisma of a damp rag.",
    "You're the human version of a participation trophy.",
    "You have something on your chin... no, the third one down.",
    "You're about as sharp as a marble.",
    "Your face could scare a hungry lion away.",
    "You're as welcome as a rash in a swimming pool.",
    "You have the personality of stale bread.",
    "You're like a broken pencil: pointless.",
    "You're the reason the chicken crossed the road—to get away from you.",
    "You bring everyone so much joy… when you leave the room.",
    "You're like a software update. Whenever I see you, I think 'Not now.'",
    "Your gene pool could use a lifeguard.",
    "You're as useless as the 'g' in lasagna.",
    "You have the IQ of a rock, but less interesting.",
    "You make onions cry.",
    "You have the charisma of a damp sock.",
    "Your secrets are safe with me. I never even listen when you tell me them.",
    "You're like a puzzle with missing pieces.",
    "You have the personality of a wet mop.",
    "You're about as bright as a black hole.",
    "You're the human embodiment of a migraine.",
    "You have something on your chin... no, the third one down.",
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You're as sharp as a marble.",
    "You’re the human version of a participation trophy.",
    "You're the reason the chicken crossed the road—to get away from you.",
    "You're as useless as a screen door on a submarine.",
    "You have the charm and personality of a damp rag.",
    "You're like a broken pencil: pointless.",
    "You bring everyone so much joy... when you leave the room.",
    "You have the charisma of a damp sock.",
    "You're the human embodiment of a migraine.",
    "You have the IQ of a rock, but less interesting.",
    "You're about as bright as a black hole.",
    "You make onions cry.",
    "You're as welcome as a rash in a swimming pool.",
    "You're the reason why there is a 'No Running' sign at the pool.",
    "You bring everyone so much joy... when you leave the room.",
    "You're as sharp as a marble.",
    "Your face could scare a hungry lion away.",
    "You have the personality of stale bread.",
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You have something on your chin... no, the third one down.",
    "You're as useless as a chocolate teapot.",
    "You have the charisma of a damp rag.",
    "You bring everyone so much joy… when you leave the room.",
    "You are the reason the chicken crossed the road—to get away from you.",
    "You're like a software update. Whenever I see you, I think 'Not now.'",
    "You're as sharp as a marble.",
    "Your gene pool could use a lifeguard.",
    "You're the human version of a participation trophy.",
    "You make onions cry.",
    "You have the IQ of a rock, but less interesting.",
    "You have the personality of a wet mop.",
    "You're as bright as a black hole.",
    "You bring everyone so much joy... when you leave the room.",
    "You're as useless as the 'g' in lasagna.",
    "You have something on your chin... no, the third one down.",
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "You have the charisma of a damp rag.",
    "You're the human embodiment of a migraine.",
    "You bring everyone so much joy... when you leave the room.",
    "You are the reason the chicken crossed the road—to get away from you.",
    "You're as sharp as a marble.",
    "You have the personality of stale bread.",
    "You're like a broken pencil: pointless.",
    "You bring everyone so much joy... when you leave the room.",
    "You have the charm and personality of a damp rag.",
    "You're the human version of a participation trophy.",
    "You have the IQ of a rock, but less interesting.",
    "You're as useless as a screen door on a submarine.",
    "You make onions cry."
]

# --- Bot and Commands ---

@bot.event
async def on_ready():
    print(f"404Bot is online as {bot.user}")

@bot.slash_command(guild_ids=[GUILD_ID], description="Get a random sussy advice")
async def advice(ctx):
    await ctx.respond(random.choice(sussy_advices))

@bot.slash_command(guild_ids=[GUILD_ID], description="Try to gain respect. Spoiler: You won't.")
async def gainrespect(ctx, user: discord.Member):
    outcome = random.choice([
        f"{user.mention} has 0 IQ. Officially disrespected.",
        f"{user.mention} tried to gain respect... access denied.",
        f"{user.mention} is made of pure trash. No upgrade available.",
        f"{user.mention} has earned... nothing. Still trash-tier.",
        f"{user.mention} is banned from the Respect Hall of Fame."
    ])
    await ctx.respond(outcome)

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

@bot.slash_command(guild_ids=[GUILD_ID], description="Roast yourself")
async def roastme(ctx):
    await ctx.respond(f"{ctx.author.mention}, {random.choice(roasts)}")

@bot.slash_command(guild_ids=[GUILD_ID], description="Trash another user")
async def trashuser(ctx, user: discord.Member):
    await ctx.respond(f"{user.mention}, you're officially trash. 404: Skill Not Found.")

@bot.slash_command(guild_ids=[GUILD_ID], description="Roast a specific user brutally")
async def roast(ctx, user: discord.Member):
    roast_line = random.choice(roasts)
    await ctx.respond(f"{user.mention}, {roast_line}")

@bot.slash_command(guild_ids=[GUILD_ID], description="Rate how roastable a user is")
async def burnlevel(ctx, user: discord.Member):
    level = random.randint(0, 100)
    if level < 30:
        msg = "This one’s safe... for now."
    elif level < 70:
        msg = "Mildly roastable. Could be worse."
    else:
        msg = "🔥 This one’s a walking barbecue!"
    await ctx.respond(f"{user.mention}'s burn level: **{level}%**. {msg}")

@bot.slash_command(guild_ids=[GUILD_ID], description="Scan a user and deliver a personal insult")
async def mirror(ctx, user: discord.Member):
    scan = random.choice(insults)
    await ctx.respond(f"Scanning {user.mention}...\n💀 Mirror says: {scan}")

@bot.slash_command(guild_ids=[GUILD_ID], description="Show available commands and what they do")
async def help(ctx):
    help_msg = """
📜 **404Bot Commands List**

/roast user:@user – Sends a savage insult targeting a user  
/burnlevel user:@user – Rates how roastable a user is  
/mirror user:@user – Scans a user and delivers a custom insult  
/roastme – Roasts you personally  
/insult – Sends a random generic insult  
/advice – Gives suspicious (sussy) advice  
/gainrespect user:@user – Checks if a user has respect or 0 IQ  
/future – Random prediction about your future  
/rickroll – Rickrolls someone or yourself  
/trashuser user:@user – Nicknames someone trash with style  
/help – Shows this help message
"""
    await ctx.respond(help_msg)

# --- Run Bot ---
bot.run(TOKEN)
