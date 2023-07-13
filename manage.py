# -*- coding: utf-8 -*-
from flask.cli import FlaskGroup
from project import app
from dotenv import load_dotenv
from bot import pc_bot
import os
load_dotenv()

cli = FlaskGroup(app)
token = os.getenv("DISCORD_TOKEN")

pc_bot.bot.run(token)
if __name__ == "__main__":
    cli()