#!/usr/bin/env python
# -*- coding: utf-8 -*-

# INVITE URL
# https://discordapp.com/api/oauth2/authorize?client_id=567644412356853770&permissions=268561408&scope=bot

import discord
import os
import sys

TOKEN = os.environ.get("DISCORD_TOKEN")
TRICKY_GAME_NAME = "Tricky Towers"
TRICKY_ROLE_NAME = "Tricky Towers 플레이 중"

client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    for guild in client.guilds:
        for member in guild.members:
            await update_tricky_role(member)


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
    if member.activity is None:
        await remove_tricky_role(member)
        return
    if member.activity.type != discord.ActivityType.playing:
        await remove_tricky_role(member)
        return
    if member.activity.name == TRICKY_GAME_NAME:
        await add_tricky_role(member)
        return


async def remove_tricky_role(member):
    tricky_role = await get_tricky_role(member.guild.roles)
    await member.remove_roles(tricky_role)


async def add_tricky_role(member):
    tricky_role = await get_tricky_role(member.guild.roles)
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

    client.run(TOKEN)
