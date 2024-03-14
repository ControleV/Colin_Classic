from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages
from discord import app_commands, Interaction, Embed
from discord.ext import commands
from random import choice

class CrystalOfTruth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'crystal_of_truth', description= '[Fun] Ask the crystal of truth anything!')
    @app_commands.describe(question= 'They say this crystal never misses!')
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_(self, interaction: Interaction, question: str):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "CrystalOfTruth")

        respostas = [str(tradutor[0]), str(tradutor[1]), str(tradutor[2]), str(tradutor[3]), str(tradutor[4]), str(tradutor[5]),
                     str(tradutor[6]), str(tradutor[7])]

        resposta = choice(respostas)

        embed = Embed(title= str(tradutor[8]).format(interaction.user.name, question),
                      description= str(tradutor[9]).format(resposta),
                      colour= interaction.user.colour)

        await interaction.response.send_message(embed= embed)

async def setup(bot):
    await bot.add_cog(CrystalOfTruth(bot))