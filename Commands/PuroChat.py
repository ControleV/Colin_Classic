from imports import *

class PuroChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'purochat', description= "[Fun] Make Puro say something to Colin!")
    @app_commands.describe(texto= 'What should the character say?')
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_procurado(self, interaction: Interaction, texto: str):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "PuroChat")

        #Checar se o texto é muito grande, se sim, fatie-o
        texto.strip()

        j = 0
        limite = 20
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


        img = Image.open("Images/purochatbase.png")
        font = ImageFont.truetype("Fonts/upheavtt.ttf", 50)

        draw = ImageDraw.Draw(img)

        #LUGAR / TEXTO / COR / FONTE
        draw.text((300, 40), texto, (255, 255, 255), font = font)
        img.save("Images/purochat.png")

        await interaction.response.send_message(file = File("Images/purochat.png"))

async def setup(bot):
    await bot.add_cog(PuroChat(bot))