from discord import app_commands, Interaction, Embed
from discord.ext import commands
from asyncio import sleep

class ReactionTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'reaction', description= "[Teste] Reaction Test")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_ReactionTest(self, interaction: Interaction):
        await interaction.response.defer()
        await interaction.followup.send("Esolha algum emoji")

        await sleep(2)

        await interaction.edit_original_response(content= 'knkfjnbkln')

async def setup(bot):
    await bot.add_cog(ReactionTest(bot))