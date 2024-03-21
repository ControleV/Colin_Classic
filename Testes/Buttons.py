from imports import *

class InviteButtons(ui.View):
    def __init__(self):
        super().__init__()

    @ui.button(label= 'Botão fofo', style= ButtonStyle.green)
    async def fofoBtn(self, interaction: Interaction, button: ui.Button):
        await interaction.response.edit_message(content= 'Bete boquete banana nana confetti')

class Buttons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'buttons', description= "[Teste] Button Test")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_ButtonTest(self, interaction: Interaction):
        await interaction.response.defer()

        await interaction.followup.send("Clique no botão!", view= InviteButtons())

async def setup(bot):
    await bot.add_cog(Buttons(bot))