#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import os
import sys

TOKEN = os.environ.get("DISCORD_TOKEN")
TRICKY_GAME_NAMES = ["Tricky Towers", "trickytowers.x86"]
TRICKY_ROLE_NAME = "Tricky Towers 플레이 중"

client = discord.Client()


@client.event
async def on_ready():
    print(f"[=] We have logged in as {client.user}")
    client_activity = discord.Activity(
        name=TRICKY_GAME_NAMES[0], type=discord.ActivityType.watching
    )
    await client.change_presence(status=discord.Status.online, activity=client_activity)
    print(f"[=] Activity has been updated")

    for guild in client.guilds:
        for member in guild.members:
            await update_tricky_role(member)
    print(f"[=] All members' roles have been updated")


@client.event
async def on_guild_join(guild):
    for member in guild.members:
        await update_tricky_role(member)


@client.event
async def on_guild_available(guild):
    for member in guild.members:
        await update_tricky_role(member)


@client.event
async def on_member_join(member):
    await update_tricky_role(member)


@client.event
async def on_member_update(before, after):
    await update_tricky_role(after)


async def update_tricky_role(member):
    if member == client.user:
        return
    if (
        (member.activity is not None)
        and (member.activity.type == discord.ActivityType.playing)
        and (member.activity.name in TRICKY_GAME_NAMES)
    ):
        await add_tricky_role(member)
        return
    await remove_tricky_role(member)
    return


async def remove_tricky_role(member):
    tricky_role = await get_tricky_role(member.guild.roles)
    if tricky_role in member.roles:
        print(f"[-] {member.name} is not playing {TRICKY_GAME_NAMES[0]}")
        await member.remove_roles(tricky_role)


async def add_tricky_role(member):
    tricky_role = await get_tricky_role(member.guild.roles)
    if tricky_role not in member.roles:
        print(f"[+] {member.name} is playing {TRICKY_GAME_NAMES[0]} now")
        await member.add_roles(tricky_role)


async def get_tricky_role(roles):
    if not roles:
        return None
    for role in roles:
        if role.name == TRICKY_ROLE_NAME:
            return role
    return await roles[0].guild.create_role(name=TRICKY_ROLE_NAME, hoist=True)


if __name__ == "__main__":
    if TOKEN is None:
        print("token is not defined")
        sys.exit(-1)

    if len(TRICKY_GAME_NAMES) < 1:
        print("You should set more than one item for TRICKY_GAME_NAMES")
        sys.exit(-1)

    client.run(TOKEN)
