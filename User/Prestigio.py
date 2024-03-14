from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages, Stats, DumpStats
from discord import app_commands, Interaction, Embed
from discord.ext import commands

class Prestigio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'prestige', description= "[Preferences] Make the prestige of your level in Colin!")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_Prestigio(self, interaction: Interaction):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Prestigio")

        levels = Stats()

        if levels[str(interaction.user.id)][str(interaction.guild.id)]["level"] > 29:
            levels[str(interaction.user.id)][str(interaction.guild.id)]["xp"] = 0
            levels[str(interaction.user.id)][str(interaction.guild.id)]["level"] = 1
            levels[str(interaction.user.id)][str(interaction.guild.id)]["prestigios"] += 1
            levels[str(interaction.user.id)][str(interaction.guild.id)]["title"] = "Labo rat"

            DumpStats(data= levels)

            embed = Embed(title= str(tradutor[0]), description= str(tradutor[1]).format(interaction.user.name, interaction.guild.name), colour= interaction.user.colour)
            embed.set_thumbnail(url= "https://www.imagensanimadas.com/data/media/1137/diploma-e-formatura-imagem-animada-0004.gif")
            embed.set_footer(text= str(tradutor[2]).format(levels[str(interaction.user.id)][str(interaction.guild.id)]["prestigios"]))
            embed.set_author(name= str(tradutor[3]))

            await interaction.response.send_message(embed= embed)

        else:
            await interaction.response.send_message(str(tradutor[4]).format(interaction.user.name), ephemeral= True)

async def setup(bot):
    await bot.add_cog(Prestigio(bot))