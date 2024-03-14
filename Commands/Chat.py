from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages
from discord import app_commands, Interaction, File
from PIL import Image, ImageFont, ImageDraw
from discord.ext import commands

class ChooseChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = 'chat', description = '[Fun] Create and customize a themed dialog!')
    @app_commands.describe(rostos = "Choose face!")
    @app_commands.choices(rostos = [
        app_commands.Choice(name = 'DrK', value = 1),
        app_commands.Choice(name = 'Puro', value = 2),
        app_commands.Choice(name = 'Colin', value = 3),
    ])
    @app_commands.describe(texto = "Enter the text that will appear in the dialog box! (90 character limit!)")
    async def on_chat(self, interaction: Interaction, rostos: app_commands.Choice[int], texto: str):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Chat")

        if len(texto) >= 31 and len(texto) <= 61:

            text1 = texto[:30]
            text2 = texto[30:60]

            textfinal = text1 + "\n" + text2

        elif len(texto) > 61 and len(texto) < 91:
            
            text1 = texto[:30]
            text2 = texto[30:60]
            text3 = texto[60:90]

            textfinal = text1 + "\n" + text2 + "\n" + text3


        elif len(texto) >= 90:

            await interaction.response.send_message(str(tradutor[0]).format(interaction.user.name))

        else:
            textfinal = texto    

        img = Image.open("Images/chatchangedbase.png")
        font = ImageFont.truetype("Fonts/upheavtt.ttf", 58)
        draw = ImageDraw.Draw(img)

        avatar = Image.open(f"Images/{rostos.name}face.png")
        avatar = avatar.resize((270, 270))

        img.paste(avatar, (20, 20))
        draw.text((300, 40), textfinal, (255, 255, 255), font = font)
        img.save("Images/chat.png")

        await interaction.response.send_message(file = File("Images/chat.png"))

async def setup(bot):
    await bot.add_cog(ChooseChat(bot))