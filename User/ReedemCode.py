from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages, Stats, DumpStatsList, DumpStats
from discord import app_commands, Interaction, Embed
from discord.ext import commands

class Redeem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'redeem_code', description= "[Preferences] Have you discovered any new code yet? type it here!")
    @app_commands.describe(code= "Don't know any codes yet? Join our server and find out about everyone!")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_Redeem(self, interaction: Interaction, code: str):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Redeem")

        stats = Stats()

        avaiblecodes = ['tyjinvid92933475b,23pod-ik34yub8d7y674bnn wslpod91-3uif hg3tgd0o9aks-094ijk34o']

        codeExists = False

        for i in avaiblecodes:
            if code == i:
                if code in stats[str(interaction.user.id)]['banners']:
                    pass

                else:
                    codeExists = True
                    lista = [f"{code}"]

                    stats[str(interaction.user.id)]['banners'] = stats[str(interaction.user.id)]['banners'] + lista

                    DumpStats(data= stats)

                break

        if codeExists == True:
            embed = Embed(title= str(tradutor[0]), description= str(tradutor[1]).format(code), colour= interaction.user.colour)

        else:
            embed = Embed(title= 'Oops..', description= str(tradutor[2]).format(code), colour= interaction.user.colour)

        await interaction.response.send_message(embed= embed)

async def setup(bot):
    await bot.add_cog(Redeem(bot))