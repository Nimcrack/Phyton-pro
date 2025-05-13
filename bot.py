import discord
import aiohttp
import os
import random
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def saludo(ctx):
    await ctx.send(f"Hola {ctx.author.name}, bienvenido a la grasa")

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def add(ctx, num1: int, num2: int):
    """Adds two numbers together."""
    await ctx.send(f"La suma de {num1} y {num2} es {num1 + num2}")

@bot.command()
async def mem(ctx):
    with open('imagenes/meme1.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def mem1(ctx):
    imagenes = os.listdir('imagenes')
    with open(f'imagenes/{random.choice(imagenes)}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)    

@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")

@bot.command()
async def anime(ctx, *, nombre):
    url = f"https://kitsu.io/api/edge/anime?filter[text]={nombre}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                try:
                    anime = data["data"][0]["attributes"]
                    title = anime["canonicalTitle"]
                    synopsis = anime["synopsis"]
                    image_url = anime["posterImage"]["original"]
                    embed = discord.Embed(title=title, description=synopsis[:300] + "...")
                    embed.set_image(url=image_url)
                    await ctx.send(embed=embed)
                except IndexError:
                    await ctx.send("No encontré resultados para ese anime.")
            else:
                await ctx.send("Hubo un error al consultar la API.")

@bot.command()
async def animales(ctx):
    animales = ['imagenes/gato.jpg', 'imagenes/gato2.webp', "imagenes/perro.jpg" , "imagenes/lechuza.jpg" ]
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable
    # A continuación, podemos enviar este archivo como parámetro.
    random_animal = random.choice(animales)
    with open(random_animal, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"""
    Hola, soy un bot {bot.user}!
    """)# esta linea saluda
    await ctx.send("Quieres hablar de la contaminacion?")
    # Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content == 'si':
            await ctx.send("""La contaminación ambiental es la presencia de sustancias o elementos dañinos para los seres humanos y los ecosistemas (seres vivos)""")   
        else:
            await ctx.send("Está bien, si alguna vez necesitas saber sobre que es la contaminación, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
 
    await ctx.send("Quieres conocer algunos ejemplos de contaminación, responde 'sí' o 'no'.")
    def check1(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response1 = await bot.wait_for('message', check=check1)
    if response1:
        if response1.content == "si":
            await ctx.send("1. contaminación del aire") 
            await ctx.send("2. contaminación del suelo") 
            await ctx.send("3. contaminación acustica")
            await ctx.send("4. contaminación termica") 
        else:
            await ctx.send("Está bien, si alguna vez necesitas conocer los tipos de contaminación, me avisas.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Deseas ver una imagen sobre un ejemplo de contaminación?")
    def check2(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response2 = await bot.wait_for('message', check=check2)
    if response2:
        if response2.content == "si":
            with open('imagenes/contamincaion.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
                picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=picture)
        else:
            await ctx.send("Esta bien!")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

@bot.command()
async def skibiditoilet(ctx):
    await ctx.send(f"""
    Hola, soy un bot {bot.user}!
    """)# esta linea saluda
    await ctx.send("Quieres hablar de los skibidis?")
    # Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content == 'si':
            await ctx.send("""El origen de su nombre o su historia no tiene origen claro, traducido al español, ‘Skibidi Toilet’ significa ‘Humanos con cabeza de váter’. Aunque suele ser consumida principalmente por niños, muchos padres están en contra de su contenido, pues suele tener sustos repentinos, además de violencia en los enfrentamientos que se presentan en la trama.
https://www.milenio.com/virales/skibidi-toilet-que-significa-en-espanol-es-para-ninos""")   
        else:
            await ctx.send("que mal que no quieras saber de los skibidis, muy buena serie")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
 
    await ctx.send("Quieres conocer los personajes de la serie de skibidi toilet?")
    def check1(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response1 = await bot.wait_for('message', check=check1)
    if response1:
        if response1.content == "si":
            await ctx.send("1. El Titán Speakerman es el segundo titán que aparece en la serie Skibidi Toilet, haciendo su debut en el Episodio 26, donde apareció en escena mientras explotaba el Balaclava Skibidi Toilet y jugaba a (La mayor parte de la libertad y del placer.)") 
            await ctx.send("2. Los inodoros Skibidi (estilizados como ΣΚΙΒΙΔΙ) (romanizados: SKIBIDI) fueron los principales antagonistas titulares de la serie Skibidi Toilet creada por DaFuq!? ¡Auge! en YouTube. Fueron los principales adversarios de La Alianza antes de unirse a ellos para superar a los Astro Toilets (los principales antagonistas actuales después del comienzo del Astro Arc) y convertirse en el tetagonista de la serie.") 
            await ctx.send("3. El Verdugo Speakerman, indistintamente llamado Ejecutor, es un gigantesco guerrero Speakerman que debutó en el baño 78 de Skibidi, donde comandó la armada de Speakerman y demostró sus poderosas habilidades.")
            await ctx.send("4. Buzzsaw Skibidi Mutant 3.0, también llamado Hugo Boss, es la versión mejorada de Buzzsaw Skibidi Mutant 2.0. Es un mutante Skibidi afiliado a Skibidi Toilets y sus aliados The Alliance, sirviendo como el protagonista principal del Episodio 78, donde participó en una operación de rescate, antes de convertirse en uno de los primeros testigos del debut de Speakermen 3.0.") 
        else:
            await ctx.send("Está bien, si alguna vez necesitas conocer los tipos de contaminación, me avisas.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Deseas ver una imagen sobre un ejemplo de skibidi toilet?")
    def check2(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response2 = await bot.wait_for('message', check=check2)
    if response2:
        if response2.content == "si":
            with open('imagenes/skibidi toilet.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
                picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=picture)
        else:
            await ctx.send("Esta bien!")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
