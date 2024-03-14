from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages, Stats, DumpStats
from discord import app_commands, Interaction, Embed
from discord.ext import commands

class Family(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'family', description= "[Preferences] Join a faction!")
    @app_commands.describe(families= "Choose one of the families to be a part of")
    @app_commands.choices(families = [
        app_commands.Choice(name = 'Black Latex College', value = 1),
        app_commands.Choice(name = 'White Latex College', value = 2),
        app_commands.Choice(name = 'Dragon College', value = 3),
        app_commands.Choice(name = 'Plantae College', value = 4),
        app_commands.Choice(name = 'Research College', value = 5),
        app_commands.Choice(name = 'Water College', value = 6)
    ])
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_Family(self, interaction: Interaction, families: app_commands.Choice[int]):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Families")

        stats = Stats()

        if families.value == 1: stats[str(interaction.user.id)]["college"] = 'blacklatexzone'
        if families.value == 2: stats[str(interaction.user.id)]["college"] = 'whitelatexzone'
        if families.value == 3: stats[str(interaction.user.id)]["college"] = 'dragonzone'
        if families.value == 4: stats[str(interaction.user.id)]["college"] = 'plantaezone'
        if families.value == 5: stats[str(interaction.user.id)]["college"] = 'researchzone'
        if families.value == 6: stats[str(interaction.user.id)]["college"] = 'waterzone'

        DumpStats(data= stats)

        embed = Embed(title= str(tradutor[0]).format(families.name), description= str(tradutor[1]), colour = interaction.user.colour)

        await interaction.response.send_message(embed= embed)

async def setup(bot):
    await bot.add_cog(Family(bot))