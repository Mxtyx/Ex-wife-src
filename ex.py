import discord
import random
from discord.ext import commands
import asyncio
import datetime
import typing
import aiohttp
from discord import Embed
from discord.ui import View, Button
import datetime
import pytz
from typing import Optional
from discord import Webhook

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='.', help_command=None, self_bot=True, intents=discord.Intents.all())

OWNER_ONLY = YOUR ID HERE
CLEAN = "<:clean:1080250547497615401>"
BETA = "<:betaa:1080518165701873754>"
WARNING = "<:warningg:1080251493858418818>"
NEW = "<:neww:1080250027886252155>"

def is_allowed_user(ctx):
    return ctx.message.author.id == OWNER_ONLY

@bot.event
async def on_connect():
  await bot.change_presence(activity = discord.Streaming(name = 
  "ILY", url = "https://www.twitch.tv/ex"))   

@bot.command()
@commands.check(is_allowed_user)
async def lock(ctx):
    channel = ctx.channel
    new_permissions = channel.overwrites_for(ctx.guild.default_role)
    new_permissions.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=new_permissions)
    em = discord.Embed(title="", color=0x2f3136)
    em.add_field(name="", value=f"```{channel} has been locked```")
    await channel.send(embed=em)

@bot.command()
@commands.check(is_allowed_user)
async def unlock(ctx):
    channel = ctx.channel
    new_permissions = channel.overwrites_for(ctx.guild.default_role)
    new_permissions.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=new_permissions)
    em = discord.Embed(title="", color=0x2f3136)
    em.add_field(name="", value=f"```{channel} has been unlocked```")
    await channel.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def clown(ctx, member: discord.Member):
    if bot.user in ctx.message.mentions:
        em = discord.Embed(title="", color=0x2f3136)
        em.add_field(name="", value=f"```You really are a fucking retarted monkey i wont clown myself```")
        await ctx.reply(embed=em)
    else:
        roasts = ["There is someone out there for everyone. For you, it’s a therapist.", "I would smack you, but I’m against animal abuse.", "If I wanted to kill myself, I would simply jump from your ego to your IQ.", "Whoever told you to be yourself, gave you a bad advice", "I don’t hate you, but if you were drowning, I would give you a high five.", "If I throw a stick, will you leave me too?", "Sorry I can’t think of an insult dumb enough for you to understand.", "It is hilarious how you are trying to fit your entire vocabulary into one sentence.", "I would call you an idiot, but it would be an insult for stupid people.", "I told my therapist about you; she didn’t believe me.", "The last time I saw something like you, it was behind metal grids.", "If I had a dollar every time you shut up, I would give it back as a thank you.", "You were so happy for the negativity of your Covid test, we didn’t want to spoil the happiness by telling you it was IQ test.", "You are like a software update. every time I see you, I immediately think “not now”.", "You are the reason why there are instructions on shampoo bottles.", "I look at you and think what a waste of two billion years of the evolution.", "It would be a great day If you used a glue stick instead of Chapstick.", "You are the reason why God is not talking to us anymore.", "You can’t imagine how much happiness you can bring… by leaving the server.", "It’s all about balance… you start talking, I stop listening.", "Everyone is allowed to act stupid once, but you… you are abusing that privilege.", "Cry me a river, then drown yourself in it.", "Ola soy Dora. Can you help me find where we asked?", "Somewhere tree is producing oxygen for you. I’m sorry for it.", "Everyone has purpose in this life, yours is to become an organ donor.", "I am jealous of people who didn’t meet you.", "Why are you rolling your eyes? Are you looking for your brain?", "What is wrong with you? Have you had too many drugs in mental hospital today?", "I am not ignoring you; I am just giving you a time to understand what you just said.", "Every time I think you can’t get any dumber, you are proving me wrong."]
        roast = random.choice(roasts)
        await ctx.send(f"{member.mention}, {roast}")

@commands.cooldown(1, 3, commands.BucketType.user)
@bot.command()
async def pfp(ctx, user: typing.Union[discord.User, discord.Member] = None):
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f"{user.display_name}'s avatar", color=0x2f3136)
    embed.set_image(url=user.avatar.url)
    await ctx.reply(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def suck(ctx, member: discord.Member):
    if not member:
        await ctx.reply(f"{ctx.author.mention}, you cant suck yourself can you?")
    elif member == ctx.author:
        await ctx.reply(f"{ctx.author.mention}, you cant suck yourself you dumb retarded monkey.")
    elif bot.user in ctx.message.mentions:
        await ctx.reply(f"{ctx.author.mention}, i dont have a dick")
    else:
        await ctx.send(f"{member.mention}, you got your dick sucked by {ctx.author.mention}")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def fuck(ctx, member: discord.Member = None):
    if not member:
        await ctx.reply(f"{ctx.author.mention}, you cant fuck yourself can you?")
    elif member == ctx.author:
        await ctx.reply(f"{ctx.author.mention}, you cant fuck yourself you dumb retarded monkey.")
    elif bot.user in ctx.message.mentions:
        await ctx.reply(f"{ctx.author.mention}, only ex can fuck me")
    else:
        await ctx.send(f"{member.mention}, you just got fucked by {ctx.author.mention}.")

@commands.cooldown(1, 3, commands.BucketType.user)
@bot.command(pass_context=True, aliases=['help'])
async def cmd(ctx):
    pages = [
        discord.Embed(title="<:fight:1080250765974704170> Ex Slave's - Fun Commands", color=0x2f3136)
        .add_field(name="**.suck <mentioned_user>**", value="```Makes you suck some users dick```", inline=False)
        .add_field(name="**.fuck <mentioned_user>**", value="```Makes you fuck a user```", inline=False)
        .add_field(name="**.clown <mentioned_user>**", value="```Bot roasts the mentioned user```", inline=False)
        .add_field(name="**.webhook **", value="```Bot lets you save a webhook where you can then send a message to```", inline=False)
        .add_field(name="**.sendwebhook <message>**", value="```Bot lets you send a message to your webhook```", inline=False),
        discord.Embed(title="<:info:1080251547646185473> Ex Slave's - Info commands", color=0x2f3136)
        .add_field(name="**.pfp <mentioned_user>**", value="```Sends yours/users pfp```", inline=False)
        .add_field(name="**.banner <mentioned_user>**", value="```Sends yours/users banner```", inline=False)
        .add_field(name="**.server **", value="```Sends the servers info```", inline=False)
        .add_field(name="**.ui <mentioned_user>**", value="```Sends the users info```", inline=False)
        .add_field(name="**.invites **", value="```Sends a list of invites from the server```", inline=False)
        .add_field(name="**.getinvite <bot_id>**", value="```Sends an invite link for the bots id mentioned in the msg```", inline=False),
        discord.Embed(title="<:modshield:1080250575582670981> Ex Slave's - Moderation commands", color=0x2f3136)
        .add_field(name="**.lock <channel>**", value="```Locks the mentioned channel```", inline=False)
        .add_field(name="**.unlock <channel>**", value="```Unlocks the mentioned channel```", inline=False)
        .add_field(name="**.kick <mentioned_user>**", value="```Kicks the mentioned user```", inline=False)
        .add_field(name="**.ban <mentioned_user>**", value="```Bans the mentioned user```", inline=False)
        .add_field(name="**.clear <amount_msgs>**", value="```Deletes the amount of messages mentioned```", inline=False)
        .add_field(name="**.cleanup <amount_msgs>**", value="```Deletes the amount of bot messages mentioned```", inline=False),
    ]
    page_number = 0
    message = await ctx.reply(embed=pages[page_number])
    reactions = ["<:left:1080249990489841775>", "<:right:1080249928930054316>"]
    for reaction in reactions:
        await message.add_reaction(reaction)
    while True:
        try:
            reaction, user = await bot.wait_for(
                "reaction_add",
                timeout=60.0,
                check=lambda r, u: u == ctx.author and str(r.emoji) in reactions and r.message.id == message.id
            )
        except asyncio.TimeoutError:
            for reaction in reactions:
                await message.remove_reaction(reaction, bot.user)
            break
        else:
            if str(reaction.emoji) == "<:left:1080249990489841775>":
                page_number = (page_number - 1) % len(pages)
                await message.edit(embed=pages[page_number])
            elif str(reaction.emoji) == "<:right:1080249928930054316>":
                page_number = (page_number + 1) % len(pages)
                await message.edit(embed=pages[page_number])
            await message.remove_reaction(reaction, user)

@bot.command()
@commands.check(is_allowed_user)
async def status(ctx, status_type: str, *, status: str):
    if status_type.lower() == "playing":
        await bot.change_presence(activity=discord.Game(name=status))
        await ctx.reply(f"Bot status changed to 'Playing {status}'")
    elif status_type.lower() == "listening":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
        await ctx.reply(f"Bot status changed to 'Listening to {status}'")
    elif status_type.lower() == "watching":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await ctx.reply(f"Bot status changed to 'Watching {status}'")
    elif status_type.lower() == "streaming":
        await bot.change_presence(activity=discord.Streaming(name=status, url="https://twitch.tv/ex"))
        await ctx.reply(f"Bot status changed to 'Streaming {status}'")
    else:
        em = discord.Embed(title="", color=0x2f3136)
        em.add_field(name=f"{WARNING} **Invalid status type**", value=f"```Please choose from 'Playing', 'Listening', 'Watching', or 'Streaming'.```", inline=False)
        await ctx.reply(embed=em)

@bot.command()
@commands.check(is_allowed_user)
async def servers(ctx):
    embed = discord.Embed(title="Servers", color=0x2f3136)
    for guild in bot.guilds:
        embed.add_field(name=guild.name, value=f"ID: `{guild.id}`", inline=False)
    await ctx.reply(embed=embed)

@bot.command()
@commands.check(is_allowed_user)
async def leave(ctx, guild_id: int):
    guild = bot.get_guild(guild_id)
    if guild is None:
        em = discord.Embed(title=f"{WARNING}Error", color=0x2f3136)
        em.add_field(name="", value=f"```Can't find a server with ID {guild_id}```", inline=False)
        await ctx.reply(embed=em)
        return
    await guild.leave()
    em = discord.Embed(title="", color=0x2f3136)
    em.add_field(name="Left the server", value=f"```{guild.name} | {guild_id}```", inline=False)
    await ctx.reply(embed=em)

@bot.command()
@commands.check(is_allowed_user)
async def name(ctx, *, new_name: str):
    old_name = bot.user.name
    try:
        await bot.user.edit(username=new_name)
        em = discord.Embed(title="", color=0x2f3136)
        em.add_field(name="**Bots name changed**", value=f"```{old_name} to {new_name} ```", inline=False)
        await ctx.reply(embed=em)
    except discord.HTTPException as e:
        em = discord.Embed(title="", color=0x2f3136)
        em.add_field(name=f"{WARNING} **Error**", value=f"```{e}```", inline=False)
        await ctx.reply(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases= ['bn'])
async def banner(ctx, *, user:commands.UserConverter=None):
    if user == None:
        member = ctx.author
    else:
        member = user
    usr = await bot.fetch_user(member.id)
    if usr.banner:
        banner = usr.banner.url
        bannerEmbed=discord.Embed(
            title='',
            description=f"**[banner]({banner})**",
            color=0x2f3136
        )
        bannerEmbed.set_author(name=f'{usr.name}#{usr.discriminator}', icon_url=usr.display_avatar.url)
        bannerEmbed.set_image(url=banner)
        await ctx.reply(embed=bannerEmbed)
    elif usr.accent_color:
        uc = str(usr.accent_color).format(hex).strip('#')
        colorEmbed=discord.Embed(
            title='',
            description=f"**[banner]({f'https://singlecolorimage.com/get/{uc}/400x100'})**",
            color=0x2f3136
        )
        colorEmbed.set_author(name=f'{usr.name}#{usr.discriminator}', icon_url=usr.display_avatar.url)
        colorEmbed.set_image(url=f'https://singlecolorimage.com/get/{uc}/400x100')
        await ctx.reply(embed=colorEmbed)
    else:
        bnerrEmbed=discord.Embed(
            title='',
            description='banner/color not assigned',
            color=0x2f3136
        )
        bnerrEmbed.set_author(name=f'{usr.name}#{usr.discriminator}', icon_url=usr.display_avatar.url)
        await ctx.reply(embed=bnerrEmbed)
@banner.error
async def need_mention(ctx, error):
    if isinstance(error, ):
        await ctx.reply("user not found")
    else:
        print(error)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases= ['s'])
async def server(ctx):
    guild = ctx.guild
    owner = guild.owner
    member_count = guild.member_count
    boost_count = guild.premium_subscription_count
    icon_url = guild.icon.url
    embed = discord.Embed(title=f"Server Info", color=0x2f3136)
    embed.set_thumbnail(url=icon_url)
    embed.add_field(name="**Owner**", value=f"```{owner}```")
    embed.add_field(name="**Members**", value=f"```{member_count}```")
    embed.add_field(name="**Boosts**", value=f"```{boost_count}```")
    await ctx.reply(embed=embed)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(pass_context=True, aliases= ['inv'])
async def invites(ctx):
    invites = await ctx.guild.invites()
    sorted_invites = sorted(invites, key=lambda x: x.uses, reverse=True)
    num_pages = (len(sorted_invites) // 10) + 1
    page_num = 1
    start_index = 0
    end_index = 10
    em = create_invites_embed(sorted_invites[start_index:end_index], page_num, num_pages)
    message = await ctx.reply(embed=em)
    if num_pages > 1:
        await message.add_reaction('<:left:1080249990489841775>')
        await message.add_reaction('<:right:1080249928930054316>')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['<:left:1080249990489841775>', '<:right:1080249928930054316>']
        while True:
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
                if str(reaction.emoji) == '<:right:1080249928930054316>' and page_num < num_pages:
                    page_num += 1
                    start_index = end_index
                    end_index += 10
                    em = create_invites_embed(sorted_invites[start_index:end_index], page_num, num_pages)
                    await message.edit(embed=em)
                elif str(reaction.emoji) == '<:left:1080249990489841775>' and page_num > 1:
                    page_num -= 1
                    end_index = start_index
                    start_index -= 10
                    em = create_invites_embed(sorted_invites[start_index:end_index], page_num, num_pages)
                    await message.edit(embed=em)
                await reaction.remove(user)
            except asyncio.TimeoutError:
                break
    else:
        return
def create_invites_embed(invites, page_num, num_pages):
    em = discord.Embed(title=f'**Server Invites** (Page {page_num}/{num_pages})', color=0x2f3136)
    for invite in invites:
        user = invite.inviter
        uses = invite.uses
        code = invite.code
        em.add_field(name=f'Invite by {user.name}#{user.discriminator}', value=f'**Code:** `{code}`\n**Uses:** {uses}')
    return em

@bot.command(pass_context=True, aliases= ['cu'])
@commands.check(is_allowed_user)
async def cleanup(ctx, amount=5):
    if not ctx.author.guild_permissions.manage_messages:
        em = discord.Embed(title=f"{WARNING} Error", color=0x2f3136)
        em.add_field(name="", value=f"```You don't have permission to use this command.```", inline=False)
        return await ctx.reply(embed=em)
    try:
        amount = int(amount)
    except ValueError:
        em = discord.Embed(title=f"{WARNING} Error", color=0x2f3136)
        em.add_field(name="", value=f"```Please enter a valid number of bot messages to clear.```", inline=False)
        return await ctx.reply(embed=em)
    def is_bot_message(message):
        return message.author == bot.user
    deleted = []
    async for message in ctx.channel.history(limit=None):
        if len(deleted) == amount:
            break
        if is_bot_message(message):
            deleted.append(message)
            await message.delete()
    em = discord.Embed(title="", color=0x2f3136)
    em.add_field(name=f"{CLEAN} Cleaned", value=f"```Deleted {len(deleted)} bot messages.```", inline=False)
    await ctx.reply(embed=em)

@bot.command(pass_context=True, aliases= ['c'])
@commands.check(is_allowed_user)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    em = discord.Embed(title="", color=0x2f3136)
    em.add_field(name=f"{CLEAN} Cleaned", value=f" ```Deleted {amount} messages```", inline=False)
    await ctx.send(embed=em)

@bot.command()
@commands.check(is_allowed_user)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        em = discord.Embed(title="", color=0x2f3136)
        em.add_field(name=f"{member.name}#{member.discriminator} has been kicked", value=f"```Reason: {reason}```", inline=False)
        await ctx.send(embed=em)
    except:
        em = discord.Embed(title=f"{WARNING} Error", color=0x2f3136)
        em.add_field(name=f"", value=f"```Failed to Kick {member.name}#{member.discriminator}```", inline=False)
        await ctx.reply(embed=em)

@bot.command()
@commands.check(is_allowed_user)
async def ban(ctx, member: discord.Member, delete_messages: Optional[bool]=False, *, reason=None):
    try:
        if delete_messages:
            await ctx.guild.ban(member, reason=reason, delete_message_days=7)
        else:
            await member.ban(reason=reason)
        em = discord.Embed(title="", color=0x2f3136)
        em.add_field(name=f"{member.name}#{member.discriminator} has been banned from the server", value=f"```Reason: {reason}```", inline=False)
        await ctx.reply(embed=em)
    except discord.Forbidden:
        em = discord.Embed(title=f"{WARNING} Error", color=0x2f3136)
        em.add_field(name=f"", value=f"```Failed to Ban {member.name}#{member.discriminator}```", inline=False)
        await ctx.reply(embed=em)

class UserButton(discord.ui.Button):
    def __init__(self, member: discord.Member):
        super().__init__(style=discord.ButtonStyle.grey, label="profile", url=f"https://discord.com/users/{member.id}")

class ProfileView(discord.ui.View):
    def __init__(self, member: discord.Member):
        super().__init__()
        self.add_item(UserButton(member))

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def ui(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    roles = [role.mention for role in member.roles if role != ctx.guild.default_role]
    roles_str = ", ".join(roles) if roles else "None"
    boost_status = "Yes" if member.premium_since is not None else "No"
    embed = discord.Embed(title=f"{BETA}", color=0x2f3136)
    embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.display_avatar)
    embed.set_thumbnail(url=member.display_avatar)
    embed.add_field(name="dates", value="**joined: **" + member.joined_at.strftime("%b %d, %Y") + "\n" + "**created: **" + member.created_at.strftime("%b %d, %Y") + "\n" + "**boosted: **" + boost_status, inline=False)
    embed.add_field(name="others", value=f"**status: **{member.status}\n**platform: **{'<:pc:1080254748743192658>' if member.desktop_status else '<:mobile:1080254717982163066>'}" + "\n" + "**roles: **" + roles_str, inline=False)
    embed.set_footer(text=f"ID: {member.id}")
    view = ProfileView(member=member)
    await ctx.send(embed=embed, view=view)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def getinvite(ctx, bot_id: int):
    bot = await ctx.bot.fetch_user(bot_id)
    if bot.bot:
        em = discord.Embed(title="invite the bot", url=f"https://discord.com/api/oauth2/authorize?client_id={bot_id}&permissions=8&scope=bot%20applications.commands", color=0x2f3136)
        await ctx.reply(embed=em)
    else:
        em = discord.Embed(title=f"{WARNING} Error", color=0x2f3136)
        em.add_field(name="", value=f"```That isnt a bot id```", inline=False)
        await ctx.reply(embed=em)

@bot.command()
@commands.check(is_allowed_user)
async def mute(ctx, member: discord.Member, *, reason=None):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        muted_role = await ctx.guild.create_role(name="Muted")
        for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role, send_messages=False)
    await member.add_roles(muted_role, reason=reason)
    em = discord.Embed(title="", color=0x2f3136)
    em.add_field(name=f"{member.name}#{member.discriminator} has been muted", value=f"```Reason: {reason}```", inline=False)
    await ctx.reply(embed=em)

@bot.command()
@commands.check(is_allowed_user)
async def unmute(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if muted_role in member.roles:
        await member.remove_roles(muted_role)
        em = discord.Embed(title=f"", color=0x2f3136)
        em.add_field(name="", value=f"```{member.name}#{member.discriminator} has been unmuted```", inline=False)
        await ctx.reply(embed=em)
    else:
        em = discord.Embed(title=f"{WARNING} Error", color=0x2f3136)
        em.add_field(name="", value=f"```{member.name}#{member.discriminator} is not muted```", inline=False)
        await ctx.reply(embed=em)

@bot.command()
@commands.check(is_allowed_user)
async def massban(ctx, time_window: int):
    ban_count = 0
    time_cutoff = datetime.datetime.now(pytz.utc) - datetime.timedelta(seconds=time_window)
    for member in ctx.guild.members:
        if member.joined_at and member.joined_at >= time_cutoff:
            try:
                await member.ban(reason="Massban")
                ban_count += 1
            except discord.errors.Forbidden:
                pass
    em = discord.Embed(title="<:modshield:1080250575582670981> Massban", color=0x2f3136)
    em.add_field(name=f"Members", value=f"```Banned {ban_count} members```", inline=False)
    em.add_field(name=f"Time", value=f"```{time_window} seconds```", inline=False)
    await ctx.reply(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def uptime(ctx):
    now = datetime.datetime.utcnow()
    delta = now - bot.start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    uptime_str = f"{days}d, {hours}h, {minutes}m, {seconds}s"
    em = discord.Embed(title="<:time:1080531316736544808> Uptime", color=0x2f3136)
    em.add_field(name=f"", value=f"``` {uptime_str}```", inline=False)
    await ctx.reply(embed=em)

bot.start_time = datetime.datetime.utcnow()
@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def webhook(ctx):
    em = discord.Embed(title=f"Check your DMs", color=0x2f3136)
    em.add_field(name="", value=f"```Enter the webhook in DMs```", inline=False)
    await ctx.reply(embed=em)
    em = discord.Embed(title=f"Send your webhook url", color=0x2f3136)
    em.add_field(name="", value=f"```NOTE: just send the webhook dont add anything else```", inline=False)
    await ctx.author.send(embed=em)
    response = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    webhook_url = response.content
    file_name = f"{ctx.author.id}.txt"
    try:
        with open(file_name, 'x') as file:
            file.write(webhook_url)
    except FileExistsError:
        em = discord.Embed(title=f"{WARNING} ERROR", color=0x2f3136)
        em.add_field(name="", value=f"```You already have a webhook saved. Do you want to replace it? (yes/no)```", inline=False)
        await ctx.author.send(embed=em)
        response = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        if response.content.lower() == "yes":
            with open(file_name, 'w') as file:
                file.write(webhook_url)
            em = discord.Embed(title=f"Webhook updated successfully", color=0x2f3136)
            em.add_field(name="", value=f"```You can now use the .sendwebhook command```", inline=False)
            await ctx.author.send(embed=em)
        else:
            em = discord.Embed(title=f"", color=0x2f3136)
            em.add_field(name="", value=f"```No changes were made to your webhook```", inline=False)
            await ctx.author.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def sendwebhook(ctx, *, message):
    file_name = f"{ctx.author.id}.txt"
    try:
        with open(file_name, 'r') as file:
            webhook_url = file.read().strip()
    except FileNotFoundError:
        em = discord.Embed(title=f"{WARNING} ERROR", color=0x2f3136)
        em.add_field(name="", value=f"```You need to save a webhook to use this command. Use *.webhook* to save your webhook```", inline=False)
        await ctx.reply(embed=em)
    else:
        async with aiohttp.ClientSession() as session:
            async with session.post(webhook_url, json={'content': message}) as response:
                if response.status == 204:
                    em = discord.Embed(title=f"Message sent to your webhook", color=0x2f3136)
                    em.add_field(name="", value=f"```{message}```", inline=False)
                    await ctx.reply(embed=em)
                else:
                    em = discord.Embed(title=f"{WARNING} ERROR", color=0x2f3136)
                    em.add_field(name="", value=f"```Failed to send message to your webhook```", inline=False)
                    await ctx.reply(embed=em)
bot.run('TOKEN HERE')

#CREDITS TO EX | ! ex#9999