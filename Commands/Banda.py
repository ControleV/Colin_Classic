from imports import *

class Banda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= "band", description= "[Fun] Create a band with server members!")
    @app_commands.describe(drummer= "First band member")
    @app_commands.describe(guitar_player= "Second band member")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_banda(self, interaction: Interaction, drummer: str = None, guitar_player: str = None):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Banda")

        integrante3 = str(interaction.user.name)

        if drummer == None or guitar_player == None:
            nickNames = ReadNickNames()

            lista = nickNames["nicks"]

            drummer = choice(lista)
            guitar_player = choice(lista)

        nomebanda = drummer[:5]
        arruda = guitar_player[3:]

        abreviacao = randint(1, 2)

        nomebandajunto = integrante3[::abreviacao] + ': ' + nomebanda + arruda

        embed = Embed(title= str(tradutor[0]).format(interaction.user.name), description= str(tradutor[1]).format(drummer, guitar_player, linesep, nomebandajunto.title()), colour= interaction.user.colour)
        embed.set_author(name='Sua banda', icon_url='https://media0.giphy.com/media/LwBTamVefKJxmYwDba/giphy.gif?cid=790b7611e41e344028646a5d3c98b84019b7a15160265190&rid=giphy.gif&ct=s')

        await interaction.response.send_message(embed = embed)

async def setup(bot):
    await bot.add_cog(Banda(bot))