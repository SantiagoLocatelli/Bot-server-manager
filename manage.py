# -*- coding: utf-8 -*-
from flask.cli import FlaskGroup
from project import app
from dotenv import load_dotenv
import os
from bot import pc_bot
from threading import Thread

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
cli = FlaskGroup(app)
def run():
    pc_bot.bot.run(token) 
    
t = Thread(target=run)
t.start()

if __name__ == "__main__":
    cli()