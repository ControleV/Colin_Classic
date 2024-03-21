from discord.ext import commands
import discord

class InviteButtons(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label= 'Botão fofo', style= discord.ButtonStyle.green)
    async def fofoBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content= 'Bete boquete banana nana confetti')

class ButtonTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name= 'buttons', description= "[Teste] Button Test")
    @discord.app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_ButtonTest(self, interaction: discord.Interaction):
        await interaction.response.defer()

        await interaction.followup.send("Clique no botão!", view= InviteButtons())

async def setup(bot):
    await bot.add_cog(ButtonTest(bot))