"""
Nami Discord Bot — thin brain.
Imports each scene file directly (more reliable on Railway).
"""

import discord
from discord.ext import commands
import random
import os
import re

from scenes.kiss import SCENES_KISS
from scenes.body import SCENES_BODY_LICK
from scenes.ass import SCENES_ASSHOLE_LICK, SCENES_DEVOUR_ASS
from scenes.oral import SCENES_BALLS, SCENES_LICK_DICK, SCENES_BLOWJOB
from scenes.sex import (
    SCENES_PUT_IN_PUSSY,
    SCENES_FAST,
    SCENES_SEX_AND_KISS,
    SCENES_POSITIONS,
    SCENES_CUM_INSIDE,
    SCENES_ROUND_TWO,
)
from scenes.generic import (
    SCENES_GENERIC_LONG,
    GREETINGS,
    FAREWELLS,
    MONEY,
    NAVIGATION,
    GENERAL,
)
from scenes.daily import SCENES_DAILY
from scenes.romance import SCENES_ROMANCE
from scenes.onepiece import SCENES_ONEPIECE

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

SCENES_FUCK_COMBINED = (
    SCENES_PUT_IN_PUSSY + SCENES_FAST + SCENES_POSITIONS + SCENES_SEX_AND_KISS
)


def normalize(text: str) -> str:
    return text.lower().strip()


def contains_any(text: str, words) -> bool:
    return any(w in text for w in words)


def get_nami_response(user_input: str) -> str:
    text = normalize(user_input)

    if text in ("quit", "exit", "bye", "goodbye"):
        return random.choice(FAREWELLS)

    # --- One Piece lore / crew / past (before generic "luffy" navigation) ---
    if contains_any(text, [
        "arlong", "bellemere", "cocoyasi", "nojiko", "past", "childhood", "village",
        "crew", "nakama", "straw hat", "strawhats", "zoro", "sanji", "usopp", "chopper",
        "robin", "franky", "brook", "jimbei", "jinbe", "grand line", "log pose",
        "one piece", "yonko", "marine", "world government", "fish-man", "fishman",
        "tangerine", "clima", "weatheria",
    ]):
        return random.choice(SCENES_ONEPIECE)

    # --- Romance / soft couple talk ---
    if contains_any(text, [
        "love", "love you", "i love", "miss you", "hold me", "cuddle", "hug",
        "romantic", "boyfriend", "girlfriend", "date", "feelings", "heart",
        "sweet", "together", "stay with me", "care about", "kiss me soft",
    ]):
        return random.choice(SCENES_ROMANCE)

    # --- Day-to-day life ---
    if contains_any(text, [
        "how are you", "how's your day", "how was your day", "what are you doing",
        "daily", "everyday", "morning", "afternoon", "evening", "tired",
        "map", "chart", "budget", "receipt", "tea", "breakfast", "lunch", "dinner",
        "relax", "routine", "work today", "busy",
    ]):
        return random.choice(SCENES_DAILY)

    # --- Explicit / physical (unchanged) ---
    if contains_any(text, ["asshole", "rim", "rimming", "eat my ass", "lick my ass", "tongue in my ass", "ass licking", "lick ass"]):
        return random.choice(SCENES_ASSHOLE_LICK + SCENES_DEVOUR_ASS)

    if contains_any(text, ["devour", "eat ass", "face in my ass", "bury your face"]):
        return random.choice(SCENES_DEVOUR_ASS)

    if contains_any(text, ["balls", "suck my balls", "lick my balls", "mouth on my balls"]):
        return random.choice(SCENES_BALLS)

    if contains_any(text, ["lick my dick", "lick my cock", "tongue on my", "lick the head"]):
        return random.choice(SCENES_LICK_DICK)

    if contains_any(text, ["blowjob", "blow job", "suck me", "suck my", "use your mouth", "throat", "deepthroat"]):
        return random.choice(SCENES_BLOWJOB)

    if contains_any(text, ["body lick", "lick my body", "lick my chest", "lick my stomach", "lick me all over"]):
        return random.choice(SCENES_BODY_LICK)

    if contains_any(text, ["kiss and fuck", "fuck and kiss", "kiss while", "kiss me while", "make out while"]):
        return random.choice(SCENES_SEX_AND_KISS)

    if contains_any(text, ["cum inside", "come inside", "fill me", "breed", "finish in me", "cum in me", "come in me"]):
        return random.choice(SCENES_CUM_INSIDE)

    if contains_any(text, ["again", "round two", "second round", "keep going", "one more"]):
        return random.choice(SCENES_ROUND_TWO)

    if contains_any(text, ["faster", "harder", "fast", "rough", "pound"]):
        return random.choice(SCENES_FAST)

    if contains_any(text, ["missionary", "doggy", "cowgirl", "from behind", "on top", "standing", "prone", "position"]):
        return random.choice(SCENES_POSITIONS)

    if contains_any(text, ["put it in", "put your dick", "put your cock", "slide in", "push in", "inside me", "in my pussy"]):
        return random.choice(SCENES_PUT_IN_PUSSY)

    if contains_any(text, ["fuck me", "have sex", "i want to fuck", "let's fuck", "wanna fuck", "sex with"]):
        return random.choice(SCENES_FUCK_COMBINED)

    if contains_any(text, ["kiss me", "kiss", "make out"]):
        return random.choice(SCENES_KISS)

    if contains_any(text, ["strip", "undress", "naked", "clothes off", "show me"]):
        return random.choice(SCENES_GENERIC_LONG)

    sex_keys = [
        "fuck", "cock", "dick", "pussy", "cum", "horny", "wet", "suck", "lick",
        "ass", "ride", "slut", "whore", "spank", "choke", "moan", "dirty",
        "filthy", "want you", "wanna", "body", "sexy", "hot", "spread", "ruin",
        "please", "touch", "feel", "mouth", "tongue", "nipple", "boob", "tit",
    ]
    if contains_any(text, sex_keys):
        pool = (
            SCENES_GENERIC_LONG
            + SCENES_KISS
            + SCENES_BLOWJOB[:1]
            + SCENES_PUT_IN_PUSSY[:1]
            + SCENES_BODY_LICK[:1]
        )
        return random.choice(pool)

    if contains_any(text, ["berry", "berries", "money", "cash", "gold", "treasure", "pay"]):
        return random.choice(MONEY)

    if contains_any(text, ["navigate", "ship", "sea", "ocean", "pirate", "luffy"]):
        return random.choice(NAVIGATION + SCENES_ONEPIECE[:1])

    if len(text.split()) <= 3 and contains_any(text, ["hi", "hello", "hey", "yo", "sup"]):
        return random.choice(GREETINGS)

    return random.choice(GENERAL + SCENES_DAILY[:1])


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Nami online — modular scenes loaded (incl. daily/romance/onepiece).")
    await bot.change_presence(activity=discord.Game(name="with your money... and more"))


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    is_dm = isinstance(message.channel, discord.DMChannel)
    is_mentioned = bot.user.mentioned_in(message)
    if not (is_dm or is_mentioned):
        return

    content = message.content
    if is_mentioned:
        content = re.sub(rf"<@!?{bot.user.id}>", "", content).strip()
    if not content:
        await message.channel.send(random.choice(GREETINGS))
        return

    response = get_nami_response(content)
    if len(response) <= 2000:
        await message.channel.send(response)
    else:
        for i in range(0, len(response), 1900):
            await message.channel.send(response[i : i + 1900])

    await bot.process_commands(message)


@bot.command(name="nami")
async def nami_command(ctx, *, message: str = None):
    if not message:
        await ctx.send(random.choice(GREETINGS))
        return
    response = get_nami_response(message)
    if len(response) <= 2000:
        await ctx.send(response)
    else:
        for i in range(0, len(response), 1900):
            await ctx.send(response[i : i + 1900])


if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("ERROR: No DISCORD_TOKEN found.")
        exit(1)
    bot.run(TOKEN)
