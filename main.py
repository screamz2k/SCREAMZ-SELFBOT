import datetime
import json
import requests
import time
import datetime
import random
import string
from os import system

import discord
from colorama import Fore, init
from discord.ext import commands

system("title " + "SCREAMZ SNIPER [github.com/screamz2k]")
banner1 = (Fore.BLUE + """
\t\t\t\t.|'''|                                              
\t\t\t\t||                                                  
\t\t\t\t`|'''|, .|'', '||''| .|''|,  '''|.  '||),,(|,  '''/
 \t\t\t\t.   || ||     ||    ||..|| .|''||   || || ||   //
 \t\t\t\t|...|' `|..' .||.   `|...  `|..||. .||    ||. /...""")
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
with open('config.json') as f:
    file = json.load(f)
    token = file["token"]
    prefix = file["prefix"]
    spam_msg = file["spam_msg"]
init()

# config
color = 1752220
log = []

# Global vars
stop = True
nuker = False


def update_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


def main():
    print(banner1)
    print(Fore.GREEN + "\t\t\t\t\t\t\tLoading...")


bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    activity = discord.Game(name="SCREAMZ SELFBOT", type=3)
    await bot.change_presence(activity=activity)
    system("cls")
    print(banner1)
    print("\t\t\t\t\t Started Selfbot as: " + bot.user.name)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="SCREAMZ SELFBOT",
                          description="https://github.com/screamz2k",
                          color=color,
                          timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Fun", value=f"{prefix}fun", inline=True)
    embed.add_field(name="Utility", value=f"{prefix}utility", inline=True)
    embed.add_field(name="Admin", value=f"{prefix}admin", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/876076455405187132/876733846102638642/Logo.png")
    await ctx.message.channel.send(embed=embed)


# admin
@bot.command()
async def admin(ctx):
    embed = discord.Embed(title="Admin Commands",
                          description="https://github.com/screamz2k",
                          color=color,
                          timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Ban", value=f"{prefix}ban [user] [reason]", inline=True)
    embed.add_field(name="Kick", value=f"{prefix}kick [user] [reason]", inline=True)
    embed.add_field(name="Create Text Channel", value=f"{prefix}create_text_channel [name]",
                    inline=False)
    embed.add_field(name="Create Voice Channel", value=f"{prefix}create_voice_channel [name]",
                    inline=False)
    embed.add_field(name="Create Role", value=f"{prefix}create_role [name]", inline=True)
    embed.add_field(name="Give Role", value=f"{prefix}give_role [user] [role]", inline=True)
    embed.add_field(name="Change Nick", value=f"{prefix}nick name [optional user]", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/876076455405187132/876733846102638642/Logo.png")
    await ctx.message.channel.send(embed=embed)


# ban
@bot.command()
async def ban(ctx, user: discord.Member = "", *, reason=None):
    if user == ctx.message.author:
        embed = discord.Embed(title="You cant ban urself dumbo!", colour=color)
        await ctx.send(embed=embed)
        pass
    if user == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}ban @test smells bad", colour=color)
        await ctx.send(embed=embed)
        return
    try:
        await ctx.guild.ban(user=user, reason=reason)
        embed = discord.Embed(title=f"Created {user} succesfully", color=color)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)


# kick
@bot.command()
async def kick(ctx, user: discord.Member, *, reason=None):
    if user == ctx.message.author:
        embed = discord.Embed(title="You cant kick urself dumbo!", colour=color)
        await ctx.send(embed=embed)
        pass
    if user == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}kick @test smells bad", colour=color)
        await ctx.send(embed=embed)
        return
    else:
        try:
            await ctx.guild.kick(user=user, reason=reason)
            embed = discord.Embed(title=f"Kicked {user} succesfully", color=color)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
            await ctx.send(embed=embed)


# Create Text Channel
@bot.command()
async def create_text_channel(ctx, name=""):
    if name == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}create_text_channel lounge", colour=color)
        await ctx.send(embed=embed)
        return
    try:
        await ctx.guild.create_text_channel(name=name)
        embed = discord.Embed(title=f"Created {name} succesfully", color=color)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)


# Create Voice Channel
@bot.command()
async def create_voice_channel(ctx, name=""):
    if name == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}create_voice_channel lounge", colour=color)
        await ctx.send(embed=embed)
        return
    try:
        await ctx.guild.create_voice_channel(name=name)
        embed = discord.Embed(title=f"Created {name} succesfully", color=color)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)


# Create role
@bot.command()
async def create_role(ctx, name=""):
    if name == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}create_role king", colour=color)
        await ctx.send(embed=embed)
        return
    try:
        await ctx.guild.create_role(name=name)
        embed = discord.Embed(title=f"Created {name} succesfully", color=color)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)


# Give role
@bot.command()
async def give_role(ctx, user: discord.Member = "", role=""):
    if user == "" or role == "":
        embed = discord.Embed(title=f"Use command like this: {prefix}give_role @screamz admin", colour=color)
        await ctx.send(embed=embed)
        return
    given_role = discord.utils.get(ctx.guild.roles, name=role)
    if given_role is None:
        discord.utils.get(ctx.guild.roles, name=role)
        embed = discord.Embed(title="Role doesnt exist", color=color)
        await ctx.send(embed=embed)
        return
    try:
        await user.add_roles(given_role)
        embed = discord.Embed(title=f"Gave {user} the role {role}", color=color)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)


# Change nickname
@bot.command()
async def nick(ctx, user: discord.Member = None, *, name=""):
    if name == "" or user is None:
        embed = discord.Embed(title=f"Use command like this: {prefix}nick @screamz king", colour=color)
        await ctx.send(embed=embed)
        return
    try:
        await user.edit(nick=name)
        embed = discord.Embed(title=f"Changed name of {user} to {name}", color=color)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="You don't have the right Permissions!", colour=color)
        await ctx.send(embed=embed)


# Fun
@bot.command()
async def fun(ctx):
    embed = discord.Embed(title="Fun",
                          description="https://github.com/screamz2k",
                          color=color,
                          timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Flip a Coin:coin:", value=f"{prefix}flip", inline=True)
    embed.add_field(name="Blackjack:black_joker:", value=f"{prefix}bj", inline=True)
    embed.add_field(name="Roll a Dice", value=f"{prefix}dice", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/876076455405187132/876733846102638642/Logo.png")
    await ctx.message.channel.send(embed=embed)


# Utility
@bot.command()
async def utility(ctx):
    embed = discord.Embed(title="Utility",
                          description="https://github.com/screamz2k",
                          color=color,
                          timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Webhookspammer", value=f"{prefix}webspam [webhook] [count] [message]", inline=True)
    embed.add_field(name="Nuke:bomb:", value=f"{prefix}test (to hide the command)", inline=True)
    embed.add_field(name="Nitro Snipe", value=f"{prefix}snipe", inline=True)
    embed.add_field(name="Generate random Nitro Codes", value=f"{prefix}gen [webhook] [count]", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/876076455405187132/876733846102638642/Logo.png")
    await ctx.message.channel.send(embed=embed)


# WEBHOOK NITRO
@bot.command()
async def gen(ctx, webhook="", amount=0):
    await ctx.message.delete()
    if webhook == "" or amount == 0:
        embed = discord.Embed(title=f"Use command like this: {prefix}gen https://discord.com/api/webhooks 20",
                              colour=color)
        await ctx.send(embed=embed)
        return
    orig_embed = discord.Embed(description="Webhook Spammer", color=color)
    orig_embed.add_field(name="Messages sent:", value=f"{0}")
    info = await ctx.send(embed=orig_embed)
    success = True
    counter = 0

    def sent():
        global success
        success = True
        res = requests.post(webhook, data=data)
        new_embed = discord.Embed(description="Nitro Gen", color=color)
        new_embed.add_field(name="Codes sent:", value=f"{counter}")
        try:
            time.sleep(res.json()["retry_after"] / 1000)
        except:
            success = False
        return new_embed

    for i in range(amount):
        counter += 1
        code_gen = (random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=16))
        code = ""
        for char in code_gen:
            code += char
        start = "https://discord.gift/" + code + "\n"

        data = {
            "content": start
        }
        embed = sent()
        await info.edit(embed=embed)
    last_embed = discord.Embed(description="Nitro Gen", color=color)
    last_embed.add_field(name="Finished", value=f"Sent {amount} codes")
    await info.edit(embed=last_embed)


# WEBHOOK
@bot.command()
async def webspam(ctx, webhook="", count: int = 0, *, message):
    await ctx.message.delete()
    if webhook == "" or count == 0:
        embed = discord.Embed(title=f"Use command like this: {prefix}webspam https://discord.com/api/webhooks 20 msg",
                              colour=color)
        await ctx.send(embed=embed)
        return
    orig_embed = discord.Embed(description="Webhook Spammer", color=color)
    orig_embed.add_field(name="Messages sent:", value=f"{0}")
    info = await ctx.send(embed=orig_embed)
    data = {
        "content": message
    }
    success = True
    counter = 0

    def sent():
        global success
        success = True
        res = requests.post(webhook, data=data)
        new_embed = discord.Embed(description="Webhook Spammer", color=color)
        new_embed.add_field(name="Messages sent:", value=f"{counter}")
        try:
            time.sleep(res.json()["retry_after"] / 1000)
        except:
            success = False
        return new_embed

    for i in range(count):
        embed = sent()
        await info.edit(embed=embed)
        if success:
            counter += 1
    last_embed = discord.Embed(description="Webhook Spammer", color=color)
    last_embed.add_field(name="Finished", value=f"Sent {counter} messages")
    await info.edit(embed=last_embed)  #


# NUKE
def nuke_ui():
    print(Fore.CYAN + "Commands:")
    print(Fore.MAGENTA + f"""|nuke / spam / role_spam /clear  |
    |ping_spam / mass_kick / mass_ban|
    |stop                              |""")
    print("Log:")
    for event in log:
        print(event)


@bot.command()
async def test(ctx):
    global nuke
    await ctx.message.delete()
    for i in range(2):
        print("\n")
    print(Fore.GREEN + "Activated Nuke mode hehe")
    print(Fore.CYAN + "Commands:")
    print(Fore.MAGENTA + f"""|nuke / spam / role_spam /clear  |
    |ping_spam / mass_kick / mass_ban|
    |stop / clear_log                    |""")
    nuke = True


# Nuke:)
@bot.command()
async def nuke(ctx):
    global stop
    if nuker:
        print(Fore.BLUE + f"[{update_time()}] Nuke attack started hehe")
        await ctx.message.delete()
        for i in range(5):
            await ctx.message.channel.create_invite(max_age=300)
        print(Fore.BLUE + f"[{update_time()}] Created invites!")
        for role in ctx.message.guild.roles:
            try:
                await role.delete()
            except:
                pass
        print(Fore.BLUE + f"[{update_time()}] Deleted all roles!")
        for member in ctx.message.guild.members:
            try:
                await member.edit(nick="nuked lmao")
            except:
                pass
        await ctx.message.guild.edit(name="nuked by 1takeluca on tt")
        for channel in ctx.message.guild.voice_channels:
            await channel.delete()
            if not stop:
                stop = True
                break
        for channel in ctx.message.guild.text_channels:
            await channel.delete()
            if not stop:
                stop = True
                break
        print(Fore.BLUE + f"[{update_time()}] Deleted all channels")
        print(Fore.BLUE + f"[{update_time()}] Creating channels")
        while True and stop:
            await ctx.message.guild.create_text_channel("nuked by github.com/screamz2k")
            await ctx.message.guild.create_voice_channel("discord.gg/toolstown")
        else:
            stop = True


# Delete all channels
@bot.command()
async def clear(ctx):
    if nuke:
        global stop
        await ctx.message.delete()
        for channel in ctx.message.guild.channels:
            await channel.delete()
            if not stop:
                stop = True
                break
        ch = await ctx.message.guild.create_text_channel("finished")
        await ch.send("Cleared successfully")
        print(Fore.BLUE + f"[{update_time()}] Cleared successfully")


# Spam every channel
@bot.command()
async def spam(ctx):
    if nuke:
        global stop
        await ctx.message.delete()
        print(Fore.BLUE + f"[{update_time()}] Started spamming!")
        for channel in ctx.message.guild.text_channels:
            if not stop:
                stop = True
                break
            if channel.type == discord.ChannelType.voice:
                continue
            for i in range(10):
                await channel.send("got nuked lmao @everyone")
                await channel.send(spam_msg)
        print(Fore.BLUE + f"[{update_time()}] Restarting Spam!")
        for channel in ctx.message.guild.text_channels:
            if not stop:
                stop = True
                break
            if channel.type == discord.ChannelType.voice:
                continue
            for i in range(10):
                await channel.send("got nuked lmao @everyone")
                await channel.send(spam_msg)
        print(Fore.BLUE + f"[{update_time()}] Stopped spamming!")


# Spam pings
@bot.command()
async def ping_spam(ctx):
    if nuke:
        global stop
        await ctx.message.delete()
        print(Fore.BLUE + f"[{update_time()}] Started pinging!")
        for channel in ctx.message.guild.channels:
            if not stop:
                stop = True
                break
            if channel.type == discord.ChannelType.voice:
                continue
            for i in range(10):
                await channel.send("@everyone @here")
        for channel in ctx.message.guild.channels:
            if not stop:
                stop = True
                break
            if channel.type == discord.ChannelType.voice:
                continue
            for i in range(10):
                await channel.send("@everyone @here")


# Spam roles
@bot.command()
async def role_spam(ctx):
    if nuke:
        global stop
        await ctx.message.delete()
        print(Fore.BLUE + f"[{update_time()}] Started mass creating roles")
        while True and stop:
            await ctx.message.guild.create_role(name="screamz2k", colour=discord.Colour.blue())
        else:
            stop = True


# Ban all members
@bot.command()
async def mass_ban(ctx):
    if nuke:
        global stop
        await ctx.message.delete()
        print(Fore.BLUE + f"[{update_time()}] Started mass banning!")
        count = 0
        for user in ctx.message.guild.members:
            if user == ctx.message.author:
                continue
            try:
                await user.ban(reason="Got nuked lmao", delete_message_days=7)
                count += 1
            except PermissionError:
                continue
            if not stop:
                stop = True
                break
        print(Fore.BLUE + f"[{update_time()}] Successfully kicked {count} members")


# Kick all members
@bot.command()
async def mass_kick(ctx):
    if nuke:
        global stop
        await ctx.message.delete()
        print(Fore.BLUE + f"[{update_time()}] Started mass kicking!")
        count = 0
        for user in ctx.message.guild.members:
            if user == ctx.message.author:
                continue
            try:
                await user.kick(reason="Got nuked lmao")
                count += 1
            except:
                pass
            if not stop:
                stop = True
                break
            print(Fore.BLUE + f"[{update_time()}] Successfully kicked {count} members")


@bot.command()
async def stop(ctx):
    global stop
    await ctx.message.delete()
    stop = False
    print(Fore.BLUE + f"[{update_time()}] Stopped current operation")


main()
bot.run(token, bot=False)
