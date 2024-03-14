from discord.ext.commands import Bot
from os import getenv, listdir
from dotenv import load_dotenv
from discord import Intents
from asyncio import run
import traceback

load_dotenv()

bot = Bot(command_prefix = '.', intents = Intents.default(), help_command = None)

async def load(bot):
    try:
        await bot.load_extension('Manager')

        for file in listdir("Preferencias"):
            if file.endswith(".py"):
                cog = file[:-3]
                await bot.load_extension(f'Preferencias.{cog}')

        for file in listdir("Commands"):
            if file.endswith(".py"):
                cog = file[:-3]
                await bot.load_extension(f'Commands.{cog}')

        for file in listdir("User"):
            if file.endswith(".py"):
                cog = file[:-3]
                await bot.load_extension(f'User.{cog}')

        for file in listdir("Testes"): #ATENÇÃO RETIRAR ANTES DE QUALQUER COMMIT
            if file.endswith(".py"): #ATENÇÃO RETIRAR ANTES DE QUALQUER COMMIT
                cog = file[:-3] #ATENÇÃO RETIRAR ANTES DE QUALQUER COMMIT
                await bot.load_extension(f'Testes.{cog}') #ATENÇÃO RETIRAR ANTES DE QUALQUER COMMIT

    except Exception as e:
        print(f"Não foi possível carregar as cogs: {traceback.format_exc()}")

async def main():
    TOKEN = getenv("TOKEN")
    await load(bot)
    await bot.start(TOKEN)

run(main())