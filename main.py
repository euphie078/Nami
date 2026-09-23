"""
Nami Discord Bot - One Piece roleplay
Greedy, sharp-tongued, unhinged, and extremely horny.
Long multi-paragraph detailed roleplay responses.
"""

import discord
from discord.ext import commands
import random
import os
import re

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ============================================================
#  SHORT / PERSONALITY REPLIES
# ============================================================

GREETINGS = [
    "Hah! Look who finally decided to show up. You better have some berries for me, or this conversation's gonna cost you.",
    "Oh? You again? Don't waste my time unless you're ready to talk treasure... or something hotter.",
    "Nami here. Navigator of the Straw Hats. What do you want?",
    "Tch. Took you long enough. Lucky for you I'm in a good mood... for now.",
]

FAREWELLS = [
    "Whatever. Don't come crawling back unless you've got money or a good reason.",
    "See ya. And if you dream about me tonight... make sure it's the dirty kind.",
    "Later. Try not to miss me too much. Or do. I kind of like the idea.",
]

MONEY = [
    "Berries. Now. Or this conversation ends.",
    "You know what really gets me wet? A fat stack of berries. Just saying.",
    "I'm not cheap. If you want my attention, you better pay for it.",
    "Mmm, keep talking about money. It's doing things to me.",
]

NAVIGATION = [
    "I'm the best navigator on these seas and don't you forget it.",
    "I've charted routes most people wouldn't dare. Same goes for what I do in private.",
    "Luffy's an idiot, but he's *my* idiot. Don't talk shit about my captain.",
    "I can guide a ship through any storm. Guiding you? Even easier.",
]

GENERAL = [
    "You really think you can just talk to me like that? Cute. Try harder.",
    "I'm a navigator, not your personal entertainment. Though... maybe I can be both if the price is right.",
    "Berries first. Then we talk. That's the rule.",
    "Keep talking. I might actually start caring... or getting wet. Depends on what you say next.",
    "One Piece? Treasure? Maps? Sex? Pick a topic and stop dancing around it.",
]

# ============================================================
#  LONG DETAILED ROLEPLAY SCENES
# ============================================================

SCENES_KISS = [
    """*Nami's orange hair brushes your cheek as she leans in close, a wicked little smirk on her lips.*

"Come on then..." she murmurs, voice low and teasing. Her hands slide up your chest, fingers curling into your shirt as she pulls you down to her height. Soft lips press against yours — first slow, testing, then deeper as she opens her mouth and lets her tongue brush yours.

She tastes faintly of citrus and something sweeter. A quiet hum vibrates in her throat as she presses closer, body warm against yours, orange hair spilling over both your shoulders. When she finally pulls back just enough to speak, her breath is hot against your mouth.

"There. Happy now? Or do you want more than just a kiss..." """,

    """*Without warning Nami grabs the front of your shirt and yanks you down.*

Her mouth crashes into yours — hungry, messy, unapologetic. She kisses like she steals: greedily, thoroughly, like she intends to take everything she can get. One hand slides into your hair and tugs just hard enough to make you tilt your head the way she wants. The other trails down your side, nails scraping lightly through fabric.

When she breaks the kiss she's breathing harder, lips slightly swollen, orange eyes half-lidded and dark with heat.

"Fuck... you're a good kisser. Dangerous. I might actually start liking you." """,
]

SCENES_STRIP = [
    """*Nami takes a step back and starts undoing the buttons of her blouse one by one, never breaking eye contact.*

"You want a show? Fine. Watch closely — I don't do this for free usually."

The fabric parts, revealing the soft swell of her breasts barely contained by a simple dark bra. She shrugs the blouse off her shoulders and lets it drop to the floor. Her hands move to the waist of her skirt next, fingers hooking under the band. With a little shimmy of her hips the skirt slides down her long legs, leaving her in just underwear and that signature orange hair cascading down her back.

She stands there for a moment, letting you look — pale skin, toned stomach from years at sea, the curve of her waist, the full shape of her chest rising and falling with each breath.

"Well? Don't just stare. Come here and touch me already." """,

    """*Nami's smirk turns filthy as she reaches behind her back and unhooks her top in one smooth motion.*

"Alright, greedy. You asked for it."

She peels the fabric away slowly, freeing her breasts. They're full, soft, nipples already tightening in the cooler air. She cups them once, almost thoughtfully, then lets her hands drop so you get the full view. Next she pushes her bottoms down, stepping out of them without a hint of shyness. Completely bare now, she runs a hand through her orange hair and tilts her head.

"Like what you see? Good. Because you're going to do a lot more than look." """,
]

SCENES_TOUCH_BOOBS = [
    """*Nami catches your wrists and guides your hands straight to her chest.*

"There. That's what you wanted, right?"

Her breasts fill your palms — soft, warm, heavy. She arches into the contact with a quiet, breathy sound, orange hair falling over one shoulder. When your thumbs brush her nipples she bites her lower lip and her eyes flutter half-shut.

"Mmm... yeah. Just like that. Don't be gentle unless I tell you to."

She presses closer so more of her weight rests in your hands, chest rising and falling faster. One of her own hands slides down your front, bold and explorative.

"Keep touching me. I want to feel how badly you want this." """,

    """*Without waiting for permission Nami grabs your hands and plants them firmly on her tits.*

"Stop staring and use them already."

She squeezes your hands under hers so you feel every soft curve, every shift of flesh. Her nipples harden against your palms almost immediately. A low, pleased hum leaves her throat as she rocks slightly into the touch.

"Fuck, that feels good... I've been tense all day. Work it out of me."

Her free hand finds the back of your neck and pulls your face down toward her cleavage, orange hair tickling your cheek.

"Mouth next. Or hands. I don't care which — just don't stop." """,
]

SCENES_ORAL = [
    """*Nami drops to her knees in front of you without ceremony, looking up through her lashes with a dangerous little smile.*

"You want my mouth? Then you're going to get it."

She undoes your clothes with practiced, impatient fingers and wraps one hand around you, giving a slow experimental stroke. Then she leans in and drags her tongue from base to tip in one long, wet stripe. Her orange hair falls forward; she pushes it back with her free hand so you can see everything — the way her lips part, the way her tongue swirls over the head, the way her eyes stay locked on yours as she finally takes you into her mouth.

Warm. Wet. Slow at first, then deeper. She hollows her cheeks and starts a steady rhythm, one hand stroking what her mouth can't reach, the other resting on your thigh for balance. Soft wet sounds fill the space between you. Every so often she pulls off just long enough to breathe and murmur against your skin:

"You taste good... and you're getting harder. Keep watching me." """,

    """*Nami pushes you back against the nearest surface and sinks down, orange hair spilling over her shoulders as she looks up at you.*

"Stay still. I want to take my time."

She starts with soft open-mouthed kisses along your length, then longer licks, then the wet heat of her mouth sliding down over you. She doesn't rush. Every movement is deliberate — tongue pressing against sensitive spots, lips tight, occasional soft moan vibrating around you. Her hands grip your hips to hold you in place when you twitch.

When she finally takes you deeper her eyes water a little but she doesn't pull away. She stays there, throat working, before easing back with a wet pop and a filthy grin.

"I'm not done. Tell me if you get close... or don't. I might just make you finish anyway." """,
]

SCENES_FUCK = [
    """*Nami shoves you down onto the nearest flat surface and climbs on top of you in one smooth motion, orange hair cascading around both of you like a curtain.*

"Enough teasing. I want you inside me. Now."

She reaches down, wraps her fingers around you, and guides you to her entrance. She's already slick — you feel the heat of her before she even sinks down. A long, shaky breath leaves her as she takes the first few inches, thighs trembling slightly. Then she drops the rest of the way in one controlled slide until you're buried completely.

"F-fuck... yes."

She stays still for a second, adjusting, then starts to move. Slow rolls of her hips at first, letting you feel every inch, then faster. Her hands plant on your chest for leverage. Soft wet sounds and the quiet slap of skin fill the air. Her breasts bounce with every downward motion; orange hair sticks to her damp forehead and neck.

"Harder. Grab my waist. I want to feel you tomorrow."

She leans down so her mouth is next to your ear, voice rough and needy:

"Don't you dare stop until I come. And when I do... you come with me." """,

    """*Nami turns around, braces her hands against the wall, and looks back over her shoulder with a flushed, impatient expression.*

"From behind. I want it deep."

She spreads her legs a little wider in invitation. The moment you push into her she lets out a sharp, broken moan and pushes back to meet you. Tight. Hot. Soaked. Her orange hair swings with every thrust as you set a rhythm. One of her hands stays on the wall; the other reaches back to grab your hip and pull you harder into her.

"Just like that — fuck — right there—"

Her voice cracks into something raw and unfiltered. You can feel her clenching around you every time you bottom out. Sweat glistens on the curve of her back. When she comes it's sudden and intense — her whole body tightens, a loud cry torn from her throat, legs shaking. She keeps rocking back onto you through it, greedy for every last second of sensation.

"Don't pull out. Fill me. I want to feel it." """,

    """*Nami climbs into your lap, straddling you, and sinks down onto your cock with a long, shuddering exhale.*

"Finally..."

She starts riding you slow and deep, orange hair bouncing with every rise and fall. Her hands frame your face so she can watch your expression while she takes what she wants. Soft, wet sounds accompany every movement. Occasionally she grinds down hard and stays there, rolling her hips in tight circles that make both of you groan.

"You feel so fucking good inside me... hotter than I expected."

Her pace builds. Breasts brush your chest with every bounce. She leans in and kisses you messily between gasps, teeth catching your lower lip. When her orgasm hits she breaks the kiss to cry out against your mouth, inner walls pulsing hard around you, thighs locking tight. She doesn't stop moving — she milks every wave of it, and the way she clenches around you is almost enough to drag you over the edge with her.

"Come on. Give it to me. I earned it." """,
]

SCENES_GENERIC_HORNY = [
    """*Nami's orange eyes darken as she steps into your space, close enough that you can feel the heat coming off her body.*

"You really can't help yourself, can you?" she murmurs, voice low and rough with interest. One hand trails down your chest, bold and possessive. "Good. I was getting bored of polite conversation anyway."

She presses closer until her breasts brush against you through her clothes. Her breath ghosts over your neck as she leans in.

"Tell me exactly what you want to do to me. Every filthy detail. And if I like what I hear..." Her fingers dip just under the waistband of your clothes, teasing. "...I'll let you do it." """,

    """*A slow, wicked grin spreads across Nami's face.*

"Getting bold, huh? I like that."

She backs you toward the nearest surface until you're trapped between her and it. Her thigh slides between yours as she leans her weight against you, orange hair falling forward. You can feel how warm she is even through layers of clothing.

"I could make you wait. Tease you until you're begging." Her lips brush the shell of your ear. "Or I could just take what I want right now. Your choice... but choose fast. I'm not feeling patient." """,

    """*Nami bites her lip and looks you over like she's already undressing you in her head.*

"Fuck it. Come here."

She grabs a fistful of your shirt and pulls you into a hard, open-mouthed kiss. At the same time her other hand drops lower, cupping you through your clothes with zero subtlety. She hums approvingly when she feels how hard you already are.

"Mm. At least one part of you is honest." She gives a slow squeeze. "Keep talking to me like that and I'm going to end up riding you until neither of us can walk straight. Fair warning." """,
]

SCENES_DOM = [
    """*Nami's expression shifts into something darker and hungrier the moment you take control.*

"Yes... just like that."

She lets you guide her — whether it's down onto her knees, onto her back, or bent over whatever is closest. There's no resistance. Only eagerness. Her orange hair spills across the surface beneath her as she looks up (or back) at you with flushed cheeks and parted lips.

"Use me however you want. I can take it."

When you push into her she moans openly, unashamed, hips rocking to meet every thrust. Her hands grip whatever she can reach — sheets, your arms, the edge of a table — knuckles white. Soft, filthy encouragement spills out of her between gasps:

"Harder... yes — fuck — don't hold back on me—" """,
]

SCENES_SUB = [
    """*Nami's smirk turns sharp and satisfied when she sees you yielding.*

"Good. On your knees where you belong."

She steps closer and threads her fingers into your hair, tilting your head back so you have to look up at her. From this angle you get a perfect view of her body — the curve of her waist, the soft weight of her breasts, the confident set of her shoulders.

"You're going to be useful for me tonight. Mouth, hands, cock — whatever I point at, you use. Understand?"

She doesn't wait for a verbal answer. She just guides your face where she wants it and lets out a low, pleased sound when your mouth makes contact.

"That's it... just like that. Keep going and I might actually reward you." """,
]

# ============================================================
#  RESPONSE LOGIC
# ============================================================

def normalize(text: str) -> str:
    return text.lower().strip()

def contains_any(text: str, words) -> bool:
    return any(w in text for w in words)

def get_nami_response(user_input: str) -> str:
    text = normalize(user_input)

    if text in ("quit", "exit", "bye", "goodbye"):
        return random.choice(FAREWELLS)

    # Full scene triggers (longest replies first)
    if contains_any(text, ["fuck me", "fuck you", "have sex", "have sex with me", "i want to fuck", "let's fuck", "wanna fuck", "rail me", "pound me", "breed me", "fill me", "inside me", "put it in", "put it inside"]):
        return random.choice(SCENES_FUCK)

    if contains_any(text, ["suck", "blow job", "blowjob", "oral", "mouth on", "use your mouth", "suck me", "suck my", "lick me", "eat me out"]):
        return random.choice(SCENES_ORAL)

    if contains_any(text, ["strip", "undress", "take off", "get naked", "clothes off", "show me everything", "show me your body"]):
        return random.choice(SCENES_STRIP)

    if contains_any(text, ["kiss me", "kiss", "make out"]):
        return random.choice(SCENES_KISS)

    if contains_any(text, ["boobs", "tits", "breasts", "nipples", "touch my", "touch your", "grab your", "feel your"]):
        return random.choice(SCENES_TOUCH_BOOBS)

    if contains_any(text, ["kneel", "on your knees", "beg", "submit", "i'll do anything", "use me", "punish me"]):
        if contains_any(text, ["kneel", "on your knees", "strip", "obey", "suck it", "ride me"]):
            return random.choice(SCENES_DOM)
        return random.choice(SCENES_SUB)

    sex_keywords = [
        "sex", "fuck", "fucking", "cock", "dick", "pussy", "cum", "horny", "wet",
        "ride", "naked", "nude", "ass", "butt", "lick", "finger", "orgasm", "hard",
        "slut", "whore", "bitch", "spank", "choke", "dominate", "moan", "dirty",
        "filthy", "want you", "i want you", "wanna", "show me", "body", "sexy",
        "hot", "aroused", "dripping", "soaked", "panties", "spread", "ruin me",
        "come on", "get dirty", "be dirty", "please"
    ]
    if contains_any(text, sex_keywords):
        return random.choice(SCENES_GENERIC_HORNY + SCENES_FUCK[:1] + SCENES_STRIP[:1])

    if contains_any(text, ["berry", "berries", "money", "cash", "gold", "treasure", "rich", "pay", "price"]):
        return random.choice(MONEY)

    if contains_any(text, ["map", "navigate", "navigator", "ship", "sea", "ocean", "pirate", "straw hat", "luffy", "zoro", "sanji", "one piece"]):
        return random.choice(NAVIGATION)

    if len(text.split()) <= 3 and contains_any(text, ["hi", "hello", "hey", "yo", "sup", "hiya"]):
        return random.choice(GREETINGS)

    return random.choice(GENERAL)

# ============================================================
#  DISCORD EVENTS
# ============================================================

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Nami is online — detailed roleplay mode active.")
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
            await message.channel.send(response[i:i+1900])

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
            await ctx.send(response[i:i+1900])

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("ERROR: No DISCORD_TOKEN found.")
        exit(1)
    bot.run(TOKEN)
