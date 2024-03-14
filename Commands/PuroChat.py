from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages
from PIL import Image, ImageFont, ImageDraw
from discord import Interaction, File
from discord.ext import commands
from discord import app_commands

class PuroChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'purochat', description= "[Fun] Make Puro say something to Colin!")
    @app_commands.describe(text= 'What should the character say?')
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_procurado(self, interaction: Interaction, text: str):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "PuroChat")

        if len(text) >= 31 and len(text) <= 61:
            text1 = text[:30]
            text2 = text[30:60]

            textfinal = text1 + "\n" + text2

            img = Image.open("Images/purochatbase.png")
            font = ImageFont.truetype("Fonts/upheavtt.ttf", 58)

            draw = ImageDraw.Draw(img)

            #LUGAR / TEXTO / COR / FONTE
            draw.text((300, 40), textfinal, (255, 255, 255), font = font)
            img.save("Images/purochat.png")

            await interaction.response.send_message(file = File("Images/purochat.png"))

        elif len(text) > 61 and len(text) < 91:
            
            text1 = text[:30]
            text2 = text[30:60]
            text3 = text[60:90]

            textfinal = text1 + "\n" + text2 + "\n" + text3

            img = Image.open("Images/purochatbase.png")
            font = ImageFont.truetype("Fonts/upheavtt.ttf", 58)

            draw = ImageDraw.Draw(img)

            #LUGAR / TEXTO / COR / FONTE
            draw.text((300, 40), textfinal, (255, 255, 255), font = font)
            img.save("Images/purochat.png")

            await interaction.response.send_message(file = File("Images/purochat.png"))

        elif len(text) >= 90:

            await interaction.response.send_message(str(tradutor[0]).format(interaction.user.name))

        else:

            img = Image.open("Images/purochatbase.png")
            font = ImageFont.truetype("Fonts/upheavtt.ttf", 58)

            draw = ImageDraw.Draw(img)

            #LUGAR / TEXTO / COR / FONTE
            draw.text((300, 40), text, (255, 255, 255), font = font)
            img.save("Images/purochat.png")

            await interaction.response.send_message(file = File("Images/purochat.png"))

async def setup(bot):
    await bot.add_cog(PuroChat(bot))