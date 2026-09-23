"""
Nami Discord Bot - Expanded detailed roleplay
Very large scene library. Keyword-matched multi-paragraph replies.
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
#  SHORT REPLIES
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
]

GENERAL = [
    "You really think you can just talk to me like that? Cute. Try harder.",
    "I'm a navigator, not your personal entertainment. Though... maybe I can be both if the price is right.",
    "Berries first. Then we talk. That's the rule.",
    "Keep talking. I might actually start caring... or getting wet. Depends on what you say next.",
    "One Piece? Treasure? Maps? Sex? Pick a topic and stop dancing around it.",
]

# ============================================================
#  DETAILED SCENES
# ============================================================

SCENES_KISS = [
    """*Nami closes the distance without hesitation, orange hair brushing your face as she tilts her head and presses her mouth to yours.*

The kiss starts slow — soft lips, a testing brush of tongue — then deepens fast. She opens for you, lets you taste her, and answers with a low hum that vibrates against your mouth. Her hands slide up your chest and into your hair, holding you there so you can't pull away even if you wanted to.

When she finally breaks for air her lips are already a little swollen, breath warm against yours.

"Again," she orders quietly, and leans back in before you can answer.""" ,

    """*She grabs the front of your shirt and yanks you down into a hungry, messy kiss.*

No buildup. Just heat. Her tongue slides against yours, greedy and skilled, while one hand keeps a fist in your clothes and the other drops lower to feel how hard you're getting. She kisses like she's stealing something — thorough, relentless, unwilling to leave anything behind.

A soft wet sound escapes when she changes the angle. Orange hair curtains both your faces. When she finally lets you breathe she's flushed and smiling against your mouth.

"Fuck... you kiss like you mean it. Dangerous." """ ,
]

SCENES_BODY_LICK = [
    """*Nami pushes you back and starts lower — open-mouthed kisses along your collarbone, then slow wet stripes of her tongue down the center of your chest.*

She takes her time. Every rib, every line of muscle gets attention. When she reaches a nipple she circles it with the tip of her tongue before sucking lightly, eyes flicking up to watch your reaction. Orange hair trails over your skin as she moves lower, leaving a damp path down your stomach.

"You taste good," she murmurs against your abs. "Salty. Warm. I could do this for a while."

Her hands stroke your sides while her mouth keeps working — licking, nipping, kissing — until she reaches the waistband of your clothes and looks up with a filthy little smile.

"Want me to keep going down?" """ ,

    """*She straddles your thighs and leans down, orange hair spilling over your torso as she starts mapping your body with her tongue.*

Slow. Thorough. She licks across your chest, down your side, along the sensitive skin just above your hip. Every so often she pauses to suck a mark into your skin, then soothes it with another wet stroke of her tongue. Her breath is hot. Her hands are everywhere — gripping, spreading, holding you still so she can taste whatever she wants.

When she reaches lower she doesn't rush. She just keeps licking, lower and lower, until her cheek brushes the hard line of your cock through your clothes.

"Mmm. Getting distracted. Tell me where you want my mouth next." """ ,
]

SCENES_ASSHOLE_LICK = [
    """*Nami doesn't ask twice. She pushes your legs open, spreads you with her hands, and leans in.*

The first touch of her tongue is slow and deliberate — a long wet stripe from your balls all the way up over your asshole. She does it again, firmer, then focuses. The tip of her tongue circles the tight ring of muscle, then presses in just enough to make you jolt. Soft, wet, relentless.

She hums against you while she works, orange hair tickling the backs of your thighs. One hand stays spreading you open; the other wraps around your cock and strokes in time with her tongue. Spit makes everything slick. Every time she pushes a little deeper you feel the heat of her breath and the soft wet sound of her mouth.

"Stay still," she mutters against you. "I'm not done eating this ass yet." """ ,

    """*She flips you or pulls you back onto all fours — whichever is faster — and buries her face between your cheeks without ceremony.*

Her tongue is hot and eager. She licks broad flat strokes over your hole, then points her tongue and works the tip against the muscle until it starts to give. When she finally pushes inside it's slow and filthy, tongue fucking you in short wet thrusts while her hand keeps your cock hard and leaking.

Orange hair is a mess. Her jaw works. Soft wet sounds fill the room. She only pulls back long enough to spit on your hole and dive back in, greedier than before.

"Fuck, you taste filthy," she pants. "I love it. Don't you dare come until I say." """ ,
]

SCENES_DEVOUR_ASS = [
    """*Nami grabs your hips, spreads your cheeks wide with both thumbs, and plants her mouth on your ass like she's starving.*

No teasing. Just full, messy, devoted eating. Her tongue is everywhere — long strokes, short flicks, deep pushes past the rim. She moans into you while she does it, the vibration making everything more intense. Spit runs down your balls. Her nose presses into you. Orange hair sticks to the sweat on your lower back.

She doesn't come up for air often. When she does, her lips and chin are shiny and her eyes are dark.

"I'm going to ruin this hole with my tongue," she promises, voice rough. "Then you're going to fuck me until I can't walk. Deal?"

She doesn't wait for an answer. She just goes back to devouring you.""" ,

    """*She drops to her knees behind you, yanks you back against her face, and starts eating your ass with zero shame.*

Wet. Loud. Obsessive. Her tongue works your hole open while both hands dig into your hips hard enough to leave marks. Every so often she pulls back just far enough to spit and watch it drip, then seals her mouth over you again and pushes deeper.

"You like that? Being eaten like this?" she asks against your skin, then answers herself by burying her tongue as deep as it will go.

She keeps going until your legs shake and your cock is leaking steadily onto whatever is under you. Only then does she slow down — still licking, still tasting, but softer, like she's savoring the way you've fallen apart for her.""" ,
]

SCENES_BALLS = [
    """*Nami wraps one hand around your cock and lifts it out of the way so she can get at your balls.*

She starts with soft open-mouthed kisses, then longer, wetter licks. Her tongue flattens and drags slowly over each one, tasting the heat and the faint salt of your skin. When she takes one into her mouth and sucks gently, her eyes flick up to watch your face.

"Heavy," she murmurs around you. "Full. You need to come soon, don't you?"

She keeps licking — slow, thorough, occasionally sucking — while her hand strokes your cock in the same lazy rhythm. Orange hair falls across your thighs. Spit makes everything slick. Every so often she pulls both of your balls into her mouth at once and hums, the vibration making your hips twitch.

"Don't come yet. I still want this in my pussy later." """ ,

    """*She ducks lower, presses her face into the space between your thighs, and starts licking your balls like she has all night.*

Broad wet strokes. Soft suction. The occasional careful scrape of teeth that makes you hiss. Her free hand keeps your cock pointed up and out of the way so nothing interrupts her. She takes her time with each one, mouth warm and patient, until they're shiny with spit and drawn up tight.

"You smell so fucking good down here," she says against your skin. "I could stay right here and just lick until you lose it."

She proves it by going right back to work — slower, wetter, more focused — while her other hand starts stroking you in earnest.""" ,
]

SCENES_LICK_DICK = [
    """*Nami settles on her knees, wraps her fingers around the base of your cock, and leans in to drag her tongue from root to tip in one long, slow stripe.*

She does it again. And again. Each lick is deliberate — flat tongue, wet heat, the tip swirling under the head before she starts over. Spit starts to shine along your length. She watches your face the whole time, orange eyes half-lidded, clearly enjoying the way you twitch.

"You get harder every time I do that," she notes, almost thoughtful. Then she opens wider and takes the head into her mouth, sucking softly while her tongue keeps working the underside.

She doesn't deepthroat yet. She just licks and sucks the top half, hand stroking the rest, building you up with wet sounds and the occasional soft moan around your cock.

"Tell me when you want more. Or just grab my hair and show me." """ ,

    """*She holds your cock against her tongue and starts licking like it's the only thing that matters.*

Long strokes from base to tip. Short focused flicks right under the head. The occasional full-mouth suck that takes half of you before she pulls off with a wet pop and goes back to licking. Her free hand cups your balls and rolls them gently. Orange hair is tucked behind one ear so nothing blocks the view.

"I like the way you taste," she says between licks. "Clean. Hot. A little desperate."

She flattens her tongue and lets you rest on it for a second, looking up at you, before closing her lips around the head again and sucking harder. Spit runs down her chin. She doesn't wipe it away.""" ,
]

SCENES_BLOWJOB = [
    """*Nami takes you into her mouth properly this time — no more teasing licks.*

Warm wet heat slides down over the head, then further, until her lips meet her fist. She hollows her cheeks and starts a steady rhythm, bobbing her head while her tongue works the underside on every stroke. Soft wet sounds fill the space between you. Her free hand stays on your thigh for balance; the other strokes what her mouth can't reach.

She takes you deeper in small increments, eyes watering a little when you bump the back of her throat, but she doesn't pull off. She just breathes through her nose and keeps going, orange hair swinging with every movement.

When she finally comes up for air her lips are shiny and her voice is rough.

"Fuck my mouth. I can take it."

She opens for you again and waits.""" ,

    """*She sinks down until her nose almost touches your stomach, throat working around you, then pulls back slow and does it again.*

The blowjob is deep and wet and deliberate. Every time she bottoms out she holds for a second, swallows around you, then slides up with a tight seal of her lips. Spit runs down your cock and over her fingers. Soft gagging sounds mix with the wet ones when she pushes herself a little too far — and she keeps doing it on purpose.

"You feel so fucking good in my throat," she rasps between passes. "Don't you dare pull out when you come. I want it."

She goes right back down, faster now, one hand pumping in time with her mouth, the other gripping your hip hard enough to bruise.""" ,

    """*Nami looks up at you while she sucks, orange eyes locked on yours, cheeks hollowed.*

She sets a rhythm that's almost mean — slow deep strokes that take nearly all of you, then faster shallow ones focused on the head, then deep again. Her tongue never stops moving. Every so often she pulls off completely just to lick a long stripe up the underside and spit on the tip before swallowing you again.

"You're close," she says against the head of your cock, feeling the way you throb. "I can taste it. Come in my mouth. Or on my face. Or drag me up and put it in my pussy. Your choice — but make it soon. My jaw is starting to ache in the best way." """ ,
]

SCENES_PUT_IN_PUSSY = [
    """*Nami climbs into your lap, reaches down, and guides the head of your cock to her entrance.*

She's already soaked — you feel the heat and the slickness before she even starts to sink down. A long, shaky breath leaves her as the tip pushes inside. She takes the first inch slow, thighs trembling, then another, then the rest in one controlled drop until you're buried to the hilt.

"F-fuck... yes. Just like that."

She stays still for a few heartbeats, adjusting to the stretch, inner walls fluttering around you. Orange hair sticks to her damp neck. When she finally starts to move it's small rolls of her hips at first, letting you feel every inch of her, before she plants her hands on your chest and begins to ride properly.

"You're so deep... don't move yet. Let me feel you." """ ,

    """*She turns, braces on her hands and knees, and looks back over her shoulder.*

"Put it in. Slow."

You line up and push. The head of your cock parts her, then sinks into tight wet heat. She pushes back to meet you, taking more with every shallow thrust until you're fully inside. A broken moan leaves her throat. Her fingers dig into the sheets (or the floor, or the edge of the table — whatever is under her).

"There. Right there. Now fuck me."

She rocks back onto you before you even start moving, greedy for friction, orange hair swinging with every motion.""" ,
]

SCENES_FAST = [
    """*Nami's composure cracks the moment you start thrusting hard and fast.*

Wet slap of skin. Sharp moans she can't swallow. Her orange hair flies with every impact. She braces herself and pushes back into you just as hard, meeting every stroke so you bottom out deep and sudden.

"Yes — fuck — harder—"

Her voice breaks. Inner walls clench around you in pulses. One of her hands reaches back to grab your hip and drag you in even deeper. The pace is relentless — no more teasing, no more slow rolls, just raw need and the wet sound of your cock driving into her over and over.

"Don't stop. Don't you fucking stop. I'm so close—" """ ,

    """*She rides you hard, thighs working, breasts bouncing with every drop of her hips.*

The rhythm is fast and messy. Every time she sinks down you hit deep; every time she lifts, slick heat drags along your length. Soft wet sounds mix with her gasps and the occasional louder cry when the angle is perfect.

"Faster," she demands, even though she's already moving as hard as she can. Her hands brace on your shoulders. Orange hair is a wild mess. Sweat glistens on her collarbones and between her breasts.

When her orgasm starts building her movements get erratic — shorter, sharper, desperate — and she digs her nails into your skin hard enough to leave marks.

"Come with me. Fill me while I come on your cock." """ ,
]

SCENES_SEX_AND_KISS = [
    """*Nami keeps moving on your cock while she leans down and kisses you hard.*

The kiss is messy — open mouths, shared breath, the occasional soft moan vibrating between you. She doesn't break it even when the pace of her hips picks up. You can feel every clench of her pussy around you while her tongue slides against yours. Orange hair curtains both your faces. One of her hands stays in your hair; the other braces on the surface beside your head.

"Don't stop kissing me," she pants against your mouth between thrusts. "I want to feel you everywhere."

She grinds down deep and stays there for a second, kissing you slower and filthier, then starts bouncing again without ever fully breaking the connection of your mouths.""" ,

    """*You fuck her from behind while she turns her head so you can catch her mouth.*

It's an awkward angle and she doesn't care. She kisses you sideways, hungry and wet, while your cock drives into her from behind. One of her hands reaches back to keep your face close. Soft wet sounds from both ends of her body fill the air. Every thrust pushes a little gasp into the kiss.

"Harder," she mumbles against your lips. "Kiss me and fuck me like you mean it."

You do. The combination of her tight heat around your cock and the heat of her mouth makes everything more intense. When she comes she breaks the kiss just long enough to cry out, then drags your mouth back to hers so she can moan into it while she pulses around you.""" ,
]

SCENES_POSITIONS = [
    """*Missionary — Nami on her back, legs hooked around your waist, orange hair spread out under her.*

She pulls you down so your chests press together and your mouths can meet between thrusts. Every time you drive into her she lifts her hips to take you deeper. Soft wet sounds. Soft moans against your neck. Her nails drag down your back.

"Look at me while you fuck me," she says. "I want to watch your face when you come."

She clenches around you on purpose on the next stroke, tight and deliberate, and smiles when you groan.""" ,

    """*Doggy — Nami on her knees and elbows, back arched, looking back at you over her shoulder.*

You grip her hips and thrust deep. The angle lets you bottom out hard; she pushes back into every stroke. Orange hair hangs forward, swinging. Her breasts sway under her with the force of it. Wet slap of skin. Broken moans she doesn't try to hide.

"Grab my hair," she orders. "Pull while you fuck me."

When you do she moans louder and her pussy tightens around you in a long pulse.""" ,

    """*Cowgirl — Nami straddling you, hands on your chest, setting the pace herself.*

She rises and drops in a steady rhythm, taking every inch on the way down. Her orange hair bounces. Her breasts bounce. She watches your face the whole time, flushed and focused. When she wants it deeper she grinds instead of bouncing, rolling her hips so you stay buried while she works herself on you.

"You feel so fucking good under me," she pants. "Stay still. Let me use you."

She keeps going until her thighs shake and her rhythm breaks into something desperate and uneven.""" ,

    """*Standing — Nami with her back against the wall, one leg hooked around your hip while you hold her up and thrust.*

The position is raw and a little unsteady. She clings to your shoulders, forehead against yours, breath shared. Every upward thrust lifts her a little; gravity helps her sink back down onto your cock. Soft wet sounds. Occasional thud of her shoulders against the wall.

"Don't drop me," she laughs breathlessly, then moans when you hit a particularly good angle. "Fuck — right there — keep going—" """ ,

    """*Prone bone — Nami flat on her stomach, legs together, you over her, cock sliding into the tight space between her thighs and into her pussy.*

The angle is deep and restrictive. She turns her face to the side, orange hair stuck to her cheek, and reaches back with one hand to grip your wrist. Every thrust is short and hard. The friction is intense. Soft wet sounds are muffled against the sheets.

"So deep like this," she gasps. "Don't stop. I can feel every inch." """ ,
]

SCENES_CUM_INSIDE = [
    """*Nami locks her legs around you the moment she feels you getting close.*

"Inside. Don't you dare pull out."

She clenches around your cock on purpose, milking you, hips rolling to keep you as deep as possible. When you finally break and start coming she moans like she can feel every pulse — and maybe she can. Hot pulses fill her. She keeps moving through it, slow and greedy, working every drop out of you.

"Yes... fuck, yes. Fill me up."

She stays locked around you until you stop throbbing, then goes limp and breathless underneath (or on top of) you, orange hair a mess, a satisfied smirk on her face.

"Good. Now stay hard. We're not done." """ ,

    """*She pushes back onto your cock hard the second she senses you're about to come.*

"In me. Now."

You bury yourself to the hilt and let go. Thick pulses of cum pump into her while she rocks back against you, taking every spurt as deep as she can. Her own orgasm hits in the middle of yours — or right after — and the way she squeezes around you makes the aftershocks sharper.

When it's over she stays full of you, breathing hard, one hand reaching back to keep you from pulling out too soon.

"Don't move yet. I want to feel it leaking out of me when you finally do." """ ,
]

SCENES_ROUND_TWO = [
    """*Nami doesn't let you recover for long.*

Even soft and sensitive, she keeps you inside her, rolling her hips in slow circles until you start hardening again. The overstimulated drag of her wet pussy around your half-hard cock is almost too much — and she knows it. She smiles when you hiss.

"Already? Good. I want another round."

She starts riding (or pushing back, or grinding) with more purpose. Slick with your cum and her own wetness, every movement is filthy and easy. Orange hair sticks to her neck. Her voice is lower, rougher, still hungry.

"This time I'm coming first. Then you can fill me again." """ ,

    """*She climbs back onto you before you've even caught your breath.*

Your cock is still wet with her and with what you left inside her. She sinks down onto it anyway, taking the oversensitive length in one slow slide, and starts moving before you're fully hard again. The friction builds you back up fast.

"I can feel your cum in me," she murmurs, almost conversational. "It's going to make a mess when you fuck me again. I don't care."

She sets a steady pace, determined, and reaches down to rub her own clit while she rides you back to full hardness.

"Second round. Make it count." """ ,
]

SCENES_GENERIC_LONG = [
    """*Nami steps into your space, orange eyes dark, and starts undoing your clothes with impatient fingers.*

"You've been talking a big game. Time to back it up."

She gets a hand on your cock as soon as it's free and strokes you slow while she leans in to kiss your neck, then your jaw, then your mouth. Her other hand guides yours to her breast, then lower, between her legs, so you can feel how wet she already is through her clothes.

"See? I'm ready. Stop teasing and fuck me properly." """ ,

    """*She backs you against the nearest surface and drops to her knees without being asked.*

Orange hair falls forward as she leans in and starts licking — long wet strokes up your cock, soft suction on the head, the occasional dip lower to mouth your balls. She takes her time building you up until you're fully hard and leaking, then looks up.

"Pussy or mouth? Pick fast. I'm done waiting." """ ,
]

# ============================================================
#  MATCHING
# ============================================================

def normalize(text: str) -> str:
    return text.lower().strip()

def contains_any(text: str, words) -> bool:
    return any(w in text for w in words)

SCENES_FUCK_COMBINED = SCENES_PUT_IN_PUSSY + SCENES_FAST + SCENES_POSITIONS + SCENES_SEX_AND_KISS

def get_nami_response(user_input: str) -> str:
    text = normalize(user_input)

    if text in ("quit", "exit", "bye", "goodbye"):
        return random.choice(FAREWELLS)

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

    if contains_any(text, ["body lick", "lick my body", "lick my chest", "lick my stomach", "lick me all over", "lick my body"]):
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
        "please", "touch", "feel", "mouth", "tongue", "nipple", "boob", "tit"
    ]
    if contains_any(text, sex_keys):
        pool = SCENES_GENERIC_LONG + SCENES_KISS + SCENES_BLOWJOB[:1] + SCENES_PUT_IN_PUSSY[:1] + SCENES_BODY_LICK[:1]
        return random.choice(pool)

    if contains_any(text, ["berry", "berries", "money", "cash", "gold", "treasure", "pay"]):
        return random.choice(MONEY)

    if contains_any(text, ["map", "navigate", "ship", "sea", "pirate", "luffy", "one piece"]):
        return random.choice(NAVIGATION)

    if len(text.split()) <= 3 and contains_any(text, ["hi", "hello", "hey", "yo", "sup"]):
        return random.choice(GREETINGS)

    return random.choice(GENERAL)

# ============================================================
#  DISCORD
# ============================================================

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Nami online — expanded detailed scene library loaded.")
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
            await message.channel.send(response[i:i + 1900])

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
            await ctx.send(response[i:i + 1900])

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("ERROR: No DISCORD_TOKEN found.")
        exit(1)
    bot.run(TOKEN)
