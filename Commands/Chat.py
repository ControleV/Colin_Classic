from imports import *

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
    async def on_chat(self, interaction: Interaction, rostos: app_commands.Choice[int], texto: str = None):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Chat")
        
        if texto is None:
            texto = "Lorem Impsum Dolor Sit Amet"

        #Checar se o texto é muito grande, se sim, fatie-o
        texto.strip()

        j = 0
        limite = 30
        a = 0
                        
        for i in texto:
            j += 1
                
            if j > limite and i == ' ':
                texto = texto[:j] + "\n" + texto[j:]
                                
                limite += a + 10
                a = 0
                    
            if j > limite:
                a += 1


        if len(texto) >= 90:

            await interaction.response.send_message(str(tradutor[0]).format(interaction.user.name))
            return

        img = Image.open("Images/chatchangedbase.png")
        font = ImageFont.truetype("Fonts/upheavtt.ttf", 50)
        draw = ImageDraw.Draw(img)

        avatar = Image.open(f"Images/{rostos.name}face.png")
        avatar = avatar.resize((270, 270))

        img.paste(avatar, (20, 20))
        draw.text((300, 40), texto, (255, 255, 255), font = font)
        img.save("Images/chat.png")

        await interaction.response.send_message(file = File("Images/chat.png"))

async def setup(bot):
    await bot.add_cog(ChooseChat(bot))