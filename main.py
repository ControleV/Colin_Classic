from imports import *

load_dotenv()

bot = Bot(command_prefix = '.', intents = Intents.all(), help_command = None)

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

        for file in listdir("Testes"):
            if file.endswith(".py"):
                cog = file[:-3]
                await bot.load_extension(f'Testes.{cog}')

    except Exception as e:
        print(f"Não foi possível carregar as cogs: {traceback.format_exc()}")

async def main():
    Token = os.getenv("TOKEN")
    await load(bot)
    await bot.start(Token)

run(main())
