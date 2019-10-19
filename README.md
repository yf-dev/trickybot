TrickyBot - Discord bot for tiny gaming community
===================

[![Invite TrickyBot](https://img.shields.io/static/v1.svg?label=Discord&message=Invite%20TrickyBot&color=7289da&style=flat&logo=discord)](https://discordapp.com/api/oauth2/authorize?client_id=567644412356853770&permissions=268561408&scope=bot)
[![Korean Tricky Towers Union Discord](https://img.shields.io/static/v1.svg?label=Discord&message=Korean%20Tricky%20Towers%20Union&color=7289da&style=flat&logo=discord)](http://bit.ly/kttu-discord)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/yf-dev/trickybot/blob/master/LICENSE)

TrickyBot is a Discord bot for very very tiny gaming community.

This bot will add and remove specific role automatically for members who are playing nice game like [Tricky Towers](http://www.trickytowers.com/) within the same Discord server.

TrickyBot was created for [Korean Tricky Towers Union Discord](http://bit.ly/kttu-discord), but it can be easily applied to other game communities.

## 1. Installation & Configuration

To use TrickyBot, you must first create a Discord bot.
Instructions on how to create a Discord bot can be found at [here](https://discordpy.readthedocs.io/en/latest/discord.html).

1. Clone this repository.

2. Create an `.env` file in repository root and specify Discord token as follows:

```
DISCORD_TOKEN=token_string
```

3. Run the bot with docker-compose

```bash
$ docker-compose up
```

4. If you prefer, you can run the bot directly via pipenv.

```bash
$ pipenv lock --pre
$ pipenv install
$ pipenv run app
```

5. Invite your bot to server and play the game! (When creating an invitation link, do not forget to set the "Manage Roles" permission)

## 2. Change game and role name

You can change game and role name by changing constant `TRICKY_GAME_NAMES` and `TRICKY_ROLE_NAME` on `app.py` file.


## 3. License

MIT
