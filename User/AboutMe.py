from imports import *

class AboutMe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'about_me', description= "[Preferences] Change your 'about me'!")
    @app_commands.describe(text= "Put here what people need to know about you ^w^ (250 character limit)")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_AboutMe(self, interaction: Interaction, text: str):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "AboutMe")

        if len(text) > 250:
            title = "Oops.."
            description = str(tradutor[0])

        else:
            stats = Stats()
            stats[str(interaction.user.id)]["descricao"] = text
            DumpStats(data= stats)

            title = str(tradutor[1])
            description = text

        embed = Embed(title= title, description= description, colour= interaction.user.colour)
        await interaction.response.send_message(embed= embed, ephemeral= True)

async def setup(bot):
    await bot.add_cog(AboutMe(bot))