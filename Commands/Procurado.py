from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages
from discord import app_commands, Interaction, Attachment, File
from PIL import Image, ImageFont, ImageDraw
from discord.ext import commands
from random import randint
from requests import get
from io import BytesIO

class Procurado(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'wanted', description= "[Fun] Dr.K is looking for someone, how much will he pay for his head?")
    @app_commands.describe(image= "What does the wanted person look like?")
    @app_commands.describe(name= "What is the name of the wanted person?")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_Procurado(self, interaction: Interaction, image: Attachment = None, name: str = None):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Wanted")

        if name == None:
            name = str(interaction.user.name)

        elif len(name) >= 12:
            await interaction.response.send_message(str(tradutor[0]).format(interaction.user.name), ephemeral= True)
            return

        if image == None:
            newimage = get(interaction.user.avatar)
            newimage = Image.open(BytesIO(newimage.content))
            newimage = newimage.resize((365, 365))
            newimage.save("Images/Wanted/userimage.png")
        
        else:
            await image.save("Images/Wanted/userimage.png")

        newImage = Image.open("Images/Wanted/userimage.png")
        newImage = newImage.resize((365, 365))
        newImage.save("Images/Wanted/userimage.png")
        
        back = Image.open("Images/Wanted/wanted.png")
        draw = ImageDraw.Draw(back)

        back.paste(newImage, (175, 242))

        font = ImageFont.truetype("Fonts/Insanibu.ttf", 58)
        fontGrande = ImageFont.truetype("Fonts/Insanibu.ttf", 80)
        fontWanted = ImageFont.truetype("Fonts/Insanibu.ttf", 105)
        fontReason = ImageFont.truetype("Fonts/Insanibu.ttf", 32)

        numbers = randint(1, 100)
        wantedText = str(tradutor[1])
        reasonText = str(tradutor[2])

        draw.text((350, 660), name, (0, 0, 0), anchor= "ms", font= font)
        draw.text((350, 740), str(numbers) + f",000,00", (0, 0, 0), anchor="ms", font= fontGrande)
        draw.text((350, 130), wantedText, (0, 0, 0), anchor="ms", font= fontWanted)
        draw.text((351, 180), reasonText, (0, 0, 0), anchor="ms", font= fontReason)

        back.save("Images/Wanted/wanteddone.png")

        await interaction.response.send_message(file = File("Images/Wanted/wanteddone.png"))

async def setup(bot):
    await bot.add_cog(Procurado(bot))