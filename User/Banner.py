from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages, Stats, DumpStats
from discord import app_commands, Interaction, Embed
from discord.ext import commands
from typing import List

class Banner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def banner_autocomplete(self, interaction: Interaction, current: str) -> List[app_commands.Choice[str]]:
        stats = Stats()
        choices = []
        for i in stats[str(interaction.user.id)]["banners"]:
            choices.append(i)
        return [app_commands.Choice(name= choice, value= choice) for choice in choices if current.lower() in choice]

    @app_commands.command(name= "banner", description= "See all your banners!")
    @app_commands.describe(choices= "Choose the banner you want on your profile")
    @app_commands.autocomplete(choices= banner_autocomplete)
    async def on_Banner(self, interaction: Interaction, choices:str):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Banner")

        embed = Embed(title= str(tradutor[0]), description= str(tradutor[1]).format(choices), colour= interaction.user.colour)
        
        stats = Stats()
        stats[str(interaction.user.id)]["bannerativo"] = str(choices)

        DumpStats(data= stats)

        await interaction.response.send_message(embed= embed)

async def setup(bot):
    await bot.add_cog(Banner(bot))