from imports import *

class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name = 'commands', description = '[Info] See all of my commands!')
    @app_commands.describe(pagina = "choose which page you want to access!")
    @app_commands.choices(pagina = [
        app_commands.Choice(name = 'Interaction', value = 1),
        app_commands.Choice(name = 'Level', value = 2),
        app_commands.Choice(name = 'About Colin', value = 3),
    ])
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_comandosSC(self, interaction: Interaction, pagina: app_commands.Choice[int]):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Comandos")
        
        if pagina.value == 1:
            embeddescription = str(tradutor[0]).format(linesep, linesep, linesep, linesep, linesep, linesep, linesep, linesep, linesep, linesep, linesep, linesep,
                                                    linesep, linesep, linesep, linesep, linesep, linesep, linesep, linesep, linesep, linesep, linesep, linesep)

        if pagina.value == 2:
            embeddescription = str(tradutor[1]).format(linesep, linesep)

        if pagina.value == 3:
            embeddescription = str(tradutor[2]).format(linesep, linesep, linesep, linesep, linesep)

        embed = Embed(title= str(tradutor[3]).format(interaction.user.name), description = embeddescription, colour = interaction.user.colour)

        await interaction.response.send_message(embed = embed, ephemeral = True)

async def setup(bot):
    await bot.add_cog(Comandos(bot))