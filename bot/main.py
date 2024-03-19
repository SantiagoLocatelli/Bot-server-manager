from keep_alive import keep_alive
import discord
from discord.ext import commands
from api_requests import get_home, get_student, register_student, obtener_aprobados
import json


ROL_ESTUDIANTE = 'Estudiante'
ROL_ADMIN = 'admin'
SERVER_IDS = {
  '1090814357811765248': "Pensamiento Computacional",
  '1128818251510591589': "Santi test"
}

# Configura el prefijo de los comandos del bot
prefix = "!"
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


# Crea una instancia del bot
bot = commands.Bot(command_prefix=prefix, intents=intents)

# Evento que se ejecuta cuando el bot se conecta correctamente


def tiene_rol(author, rol):
  roles = [r.name for r in author.roles]
  return rol in roles


#@bot.command()
async def actualizar_alumnos(ctx):
  servidor = ctx.guild
  if not str(servidor.id) in SERVER_IDS:
    await ctx.send("Offline")
    return
  if not tiene_rol(ctx.author, ROL_ADMIN):
    await ctx.send("No tenes los permisos suficientes")
    return

  usuarios = servidor.members
  for u in usuarios:
    roles_estudiante = [r.name for r in u.roles]
    if (ROL_ESTUDIANTE in roles_estudiante):
      nickname = u.nick
      discord_id = u.id
      response = register_student(nickname, discord_id)
      code = response.get('code', -1)
      if code == 0:
        await ctx.send(f"Se actualizo el alumno {nickname}")
      else:
        await ctx.send(f"Hubo un error al actualizar {nickname}")


@bot.command()
async def online(ctx):
  servidor = ctx.guild
  if not str(servidor.id) in SERVER_IDS:
    await ctx.send("Offline")
    return
  await ctx.send("Estoy Online!")


@bot.command()
async def limpiar_canal(ctx):
  servidor = ctx.guild
  if not str(servidor.id) in SERVER_IDS:
    await ctx.send("Offline")
    return

  if not tiene_rol(ctx.author, ROL_ADMIN):
    await ctx.send("No tenes los permisos suficientes")
    return

  canal_actual = ctx.channel
  cantidad_eliminados = 0
  async for mensaje in canal_actual.history(limit=None):
    await mensaje.delete()
    cantidad_eliminados += 1

  await ctx.send(f"Se eliminaron {cantidad_eliminados} mensajes")


@bot.command()
async def limpiar_canal_attachments(ctx):
  servidor = ctx.guild
  if not str(servidor.id) in SERVER_IDS:
    await ctx.send("Offline")
    return

  if not tiene_rol(ctx.author, ROL_ADMIN):
    await ctx.send("No tenes los permisos suficientes")
    return

  canal_actual = ctx.channel
  cantidad_eliminados = 0
  async for mensaje in canal_actual.history(limit=None):
    if (mensaje.author not in servidor.members
        or tiene_rol(mensaje.author, ROL_ESTUDIANTE)) and mensaje.attachments:
      await mensaje.delete()
      cantidad_eliminados += 1

  await ctx.send(f"Se eliminaron {cantidad_eliminados} mensajes")


#@bot.command()
async def roles(ctx):
  #await member.edit(nick="De prueba")
  servidor = ctx.guild
  if not str(servidor.id) in SERVER_IDS:
    await ctx.send("Offline")
    return
  roles = ctx.guild.roles
  for role in roles:
    await ctx.send(f"roles: {role.name}")

  rol_estudiante = None
  for role in roles:
    if role.name == ROL_ESTUDIANTE:
      rol_estudiante = role

  await ctx.send(f"{rol_estudiante}")


@bot.command()
async def limpiar_todos_estudiantes(ctx):
  servidor = ctx.guild
  if not str(servidor.id) in SERVER_IDS:
    await ctx.send("Offline")
    return

  if not tiene_rol(ctx.author, ROL_ADMIN):
    await ctx.send("No tenes los permisos suficientes")
    return

  usuarios = servidor.members
  for u in usuarios:
    roles_estudiante = [r.name for r in u.roles]
    if (ROL_ESTUDIANTE in roles_estudiante) or len(roles_estudiante) == 1:
      await ctx.guild.kick(u)
      await ctx.send(f"Se saco del servidor al usuario {u.name}")

  await ctx.send("Se termino de sacar a todos los estudiantes del servidor.")


@bot.command()
async def registrarse(ctx, identificador):
  servidor = ctx.guild
  if not str(servidor.id) in SERVER_IDS:
    await ctx.send("Offline")
    return

  member = ctx.author
  if tiene_rol(member, ROL_ESTUDIANTE):
    await ctx.send("Ya tenes el rol de Estudiante")
    return

  await ctx.send("Registrando...")
  response = register_student(identificador, member.id)
  code = response.get('code', -1)
  if code == 0:
    result = response.get('result', {})
    nombre = result.get('nombre', '')
    dni = result.get('identificador', '')
    new_nickname = nombre[0:31]
    await member.edit(nick=new_nickname)
    await ctx.send(f"Se cambió el nick a {new_nickname}.")
    await ctx.send(f"{member.mention} te registraste correctamente.")

    rol_estudiante = discord.utils.get(ctx.guild.roles, name=ROL_ESTUDIANTE)
    await member.add_roles(rol_estudiante)
  elif code != -1:
    await ctx.send(
      response.get(
        'message',
        'Hubo un error, re intenta más tarde. Si el error persiste avisa a alguno de los admins.'
      ))
  else:
    await ctx.send(
      'Hubo un error, re intenta más tarde. Si el error persiste avisa a alguno de los admins.'
    )


@bot.command()
async def limpiar_aprobados(ctx):
  servidor = ctx.guild
  if not str(servidor.id) in SERVER_IDS:
    await ctx.send("Offline")
    return

  if not tiene_rol(ctx.author, ROL_ADMIN):
    await ctx.send("No tenes los permisos suficientes")
    return

  response = obtener_aprobados()
  code = response.get('code', -1)
  if code != 0:
    await ctx.send(response.get('message'))
    return

  alumnos_aprobados = response.get('result', [])
  for alumno in alumnos_aprobados:
    usuario = await bot.fetch_user(int(alumno.get('discord_id')))
    await ctx.guild.kick(usuario)
    await ctx.send(f"Se ha expulsado al usuario con ID {usuario} del servidor."
                   )

  await ctx.send("Se termino de sacar a todos los aprobados del servidor.")


#@bot.command()
async def usuarios(ctx):
  servidor = ctx.guild
  usuarios = servidor.members
  usuarios_nombres = [usuario.name for usuario in usuarios]
  await ctx.send(
    f"Los usuarios del servidor son: {', '.join(usuarios_nombres)}")


# Comando simple para saludar al bot
#@bot.command()
async def hola(ctx):
  await ctx.send("¡Hola! ¡Soy un bot de Discord!")
  await ctx.send(ctx.author.id)


#@bot.command()
async def alumno(ctx, dni):
  response = get_student(dni)
  await ctx.send(json.dumps(response))


bot.run(
  "MTEyODg3MDk2ODMzNzYzNzM3Nw.GBtw50.I0mUSPpF-d_-p7gHEjqp4FQpl-_EXXNYVWeEiE")
