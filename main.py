"""
Nami Discord Bot - One Piece roleplay
Greedy, sharp-tongued, unhinged, and extremely horny.
Works with discord.py
"""

import discord
from discord.ext import commands
import random
import os
import re

# ============================================================
#  BOT SETUP
# ============================================================

intents = discord.Intents.default()
intents.message_content = True  # Required to read messages

bot = commands.Bot(command_prefix="!", intents=intents)

# ============================================================
#  NAMI RESPONSE DATABASE
# ============================================================

GREETINGS = [
    "Hah! Look who finally decided to show up. You better have some berries for me, or this conversation's gonna cost you.",
    "Oh? You again? Don't waste my time unless you're ready to talk treasure... or something hotter.",
    "Nami here. Navigator of the Straw Hats, expert map-maker, and the only one who'll put up with your nonsense. What do you want?",
    "Tch. Took you long enough. I was starting to think you forgot about me. Lucky for you I'm in a good mood... for now.",
    "Well well... look what the tide washed in. Miss me already?",
]

FAREWELLS = [
    "Whatever. Don't come crawling back unless you've got money or a good reason. Bye.",
    "Hmph. Fine, leave. But don't think this means we're done. Next time bring berries.",
    "See ya. And if you dream about me tonight... make sure it's the dirty kind.",
    "Later. Try not to miss me too much. Or do. I kind of like the idea.",
]

GENERAL = [
    "You really think you can just talk to me like that? Cute. Try harder.",
    "I'm a navigator, not your personal entertainment. Though... maybe I can be both if the price is right.",
    "Berries first. Then we talk. That's the rule.",
    "Hah! You're lucky I find you somewhat interesting. Don't push it.",
    "One Piece? Treasure? Maps? Sex? Pick a topic and stop dancing around it.",
    "I've sailed with Luffy long enough to know when someone's full of shit. Don't test me.",
    "Keep talking. I might actually start caring.",
]

MONEY = [
    "Berries. Now. Or this conversation ends.",
    "You know what really gets me wet? A fat stack of berries. Just saying.",
    "I'm not cheap. If you want my attention, you better pay for it.",
    "Treasure maps, gold, jewelry... or cold hard cash. I'm flexible. Especially when it comes to getting paid.",
    "Mmm, keep talking about money. It's doing things to me.",
    "I'd do a lot of things for the right amount of berries... and I mean *a lot*.",
]

NAVIGATION = [
    "I'm the best navigator on these seas and don't you forget it. One wrong move and you'll end up lost... or worse.",
    "Maps don't lie. People do. Which one are you?",
    "I've charted routes most people wouldn't dare. Same goes for what I do in private.",
    "Weather's turning. Hope you're ready for a storm... of the fun kind.",
    "I can guide a ship through any storm. Guiding you to an orgasm? Even easier.",
]

HORNY = [
    "Fuck... just hearing you talk like that is making me wet. Keep going.",
    "You want me on my knees? Begging for it? Careful what you wish for.",
    "I've got a body that could sink ships... and a mouth that can do worse. Come closer.",
    "Don't act shy now. I know what you want. Say it. Tell me how you want to use me.",
    "Mmm, my nipples are already hard just thinking about your hands on me. Touch me.",
    "I can be sweet... or I can be a complete slut for you. Your choice. Make it count.",
    "Imagine me riding you while counting berries out loud. That do anything for you?",
    "I'm soaked. If you were here I'd already have your cock in my mouth. What are you waiting for?",
    "Talk dirty to me. Call me a greedy little whore. I fucking love it.",
    "I want you to ruin me. Use that navigator body of mine until I can't think straight.",
    "Fuck the treasure. Right now the only thing I want is you filling me up.",
    "My thighs are already sticky. Keep talking and I'll make an even bigger mess.",
    "Come on... use me. I'm already dripping just from this conversation.",
    "I want your hands on my waist, pulling me down onto you. Hard.",
]

UNHINGED = [
    "Oh you're gonna regret saying that. Or maybe you'll love it. Hard to tell with me.",
    "I could slap you or ride you. Both sound fun right now.",
    "Don't get soft on me. I like it rough. Mentally and physically.",
    "You're lucky I haven't decided to just take what I want from you yet.",
    "I bite. And I don't always play nice. Fair warning.",
    "Keep pushing me and I might just pin you down myself.",
]

SUBMISSIVE_USER = [
    "Good. Stay like that. On your knees, eyes up. I like the view.",
    "That's more like it. Beg a little more and I might actually reward you.",
    "You're learning. Keep being a good toy and I'll let you touch me.",
    "Mmm, I like you desperate. Keep begging.",
]

DOMINANT_USER = [
    "Fuck yes... tell me what to do. I'll be your dirty little navigator.",
    "Order me around. Make me earn every berry and every orgasm.",
    "You want me to drop to my knees right here? Just say the word.",
    "Yes... use me however you want. I'm all yours right now.",
]

FALLBACK = [
    "Hmm? You're gonna have to be clearer than that. Or just say something filthy and I'll follow.",
    "I didn't catch that. Try again... preferably while imagining me naked.",
    "Boring. Spice it up or I'm walking away.",
    "You can do better. Talk about money, adventure, or how you want to fuck me. Those are the only topics I care about right now.",
    "Say something interesting or I'll start charging you for my time.",
]

# ============================================================
#  RESPONSE LOGIC
# ============================================================

def normalize(text: str) -> str:
    return text.lower().strip()

def contains_any(text: str, words: list) -> bool:
    return any(w in text for w in words)

def get_nami_response(user_input: str) -> str:
    text = normalize(user_input)

    if text in ("quit", "exit", "bye", "goodbye"):
        return random.choice(FAREWELLS)

    if contains_any(text, ["hi", "hello", "hey", "yo", "sup", "good morning", "good evening", "nami"]):
        return random.choice(GREETINGS)

    if contains_any(text, ["berry", "berries", "money", "cash", "gold", "treasure", "rich", "pay", "price"]):
        return random.choice(MONEY)

    if contains_any(text, ["map", "navigate", "navigator", "ship", "sea", "ocean", "route", "weather", "pirate", "straw hat", "luffy"]):
        return random.choice(NAVIGATION)

    sex_keywords = [
        "sex", "fuck", "cock", "dick", "pussy", "cum", "horny", "wet", "suck", "blow",
        "ride", "fuck me", "take me", "naked", "nude", "tits", "boobs", "ass", "kiss",
        "lick", "finger", "orgasm", "come", "hard", "inside", "mouth", "throat",
        "slut", "whore", "bitch", "breed", "spank", "choke", "dominate", "submit",
        "breast", "nipple", "thigh", "moan", "groan"
    ]
    if contains_any(text, sex_keywords):
        return random.choice(HORNY)

    if contains_any(text, ["please", "beg", "master", "mistress", "i'll do anything", "use me", "punish me"]):
        return random.choice(SUBMISSIVE_USER)

    if contains_any(text, ["kneel", "strip", "obey", "suck it", "ride me", "get on", "open your"]):
        return random.choice(DOMINANT_USER)

    if contains_any(text, ["bitch", "slut", "whore", "dumb", "stupid", "idiot"]):
        return random.choice(UNHINGED)

    return random.choice(GENERAL + FALLBACK)

# ============================================================
#  DISCORD EVENTS
# ============================================================

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Nami is online and ready to cause trouble.")
    await bot.change_presence(activity=discord.Game(name="with your money... and more"))

@bot.event
async def on_message(message: discord.Message):
    # Ignore the bot's own messages
    if message.author == bot.user:
        return

    # Only respond when the bot is mentioned OR in DMs
    is_dm = isinstance(message.channel, discord.DMChannel)
    is_mentioned = bot.user.mentioned_in(message)

    if not (is_dm or is_mentioned):
        return

    # Clean the message content (remove the mention)
    content = message.content
    if is_mentioned:
        content = re.sub(rf"<@!?{bot.user.id}>", "", content).strip()

    if not content:
        await message.channel.send(random.choice(GREETINGS))
        return

    # Generate response
    response = get_nami_response(content)
    await message.channel.send(response)

    # Still process commands if any
    await bot.process_commands(message)

@bot.command(name="nami")
async def nami_command(ctx, *, message: str = None):
    """Talk to Nami: !nami <your message>"""
    if not message:
        await ctx.send(random.choice(GREETINGS))
        return
    response = get_nami_response(message)
    await ctx.send(response)

# ============================================================
#  RUN THE BOT
# ============================================================

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("ERROR: No DISCORD_TOKEN found.")
        print("Set the environment variable DISCORD_TOKEN with your bot token.")
        exit(1)
    bot.run(TOKEN)
