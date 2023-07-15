import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()

# Configura el prefijo de los comandos del bot
prefix = "!"

# this is necessary depending on the version od discord.py
# intents = discord.Intents.default()
# intents.message_content = True

# Crea una instancia del bot
bot = commands.Bot(command_prefix=prefix)

# Evento que se ejecuta cuando el bot se conecta correctamente
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user.name}")
    print("------")

@bot.event
async def on_connect():
    print(f"Me conecte a un servidor")

# @bot.event
# async def on_message(message):
#     print(f"mandaron un mensaje {message}")

# Comando simple para saludar al bot
@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola! ¡Soy un bot de Discord!")

@bot.command()
async def ayuda(ctx):
    await ctx.send("AYUDAAAA")

# Comando para sumar dos números
@bot.command()
async def suma(ctx, num1: int, num2: int):
    resultado = num1 + num2
    await ctx.send(f"La suma de {num1} y {num2} es {resultado}")

token = os.getenv("DISCORD_TOKEN")
bot.run(token)