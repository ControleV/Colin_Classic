from imports import *

class FurryOMeter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'furryometer', description= "[Fun] See how furry you or someone else is!")
    @app_commands.describe(someone= "Who will be next in the test?")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_FurryOMeter(self, interaction: Interaction, someone: str = None):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Furryometer")

        img = Image.open("Images/FurryOMeter/base.png")

        if someone == None: sujeito = interaction.user.name
        else: sujeito = someone

        contador = randint(0, 101)

        font_small = ImageFont.truetype('Fonts/square.ttf', 30)
        font_large = ImageFont.truetype('Fonts/digital.ttf', 112)

        draw = ImageDraw.Draw(img)
        draw.text((490, 90), str(tradutor[0]).format(sujeito), anchor= 'ms', font= font_small, fill= (255, 255, 255), stroke_width= 2, stroke_fill= (0, 0, 0))
        draw.text((490, 180), f"{contador}% Furry", anchor= 'ms', font= font_large, fill= (143, 206, 0), stroke_width=2, stroke_fill= (0, 0, 0))

        img.save("Images/FurryOMeter/MeterDone.png")
        
        await interaction.response.send_message(file= File("Images/FurryOMeter/MeterDone.png"))

async def setup(bot):
    await bot.add_cog(FurryOMeter(bot))