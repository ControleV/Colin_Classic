from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages
from discord import app_commands, Interaction, Embed
from wikipedia import summary, set_lang
from discord.ext import commands
import traceback

class WikipediaComando(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = 'wiki', description = "[Info] Search something on Wikipedia!")
    @app_commands.describe(search = "What should I search for you?")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_wiki(self, interaction: Interaction, search: str):
        try:
            await interaction.response.defer()
            
            usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
            tradutor = ReadLanguages(lingua= usado, command= "Wikipedia")

            set_lang(str(usado))

            info = summary(search)
            info = info[:500]

            embedwiki = Embed(title= f'{tradutor[0]} {search}', description= f'{info}... **{tradutor[1]}**', colour= interaction.user.colour)

            embedwiki.set_author(name='Wikipedia', icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')

            await interaction.followup.send(embed = embedwiki)
            
        except:
            print(traceback.format_exc())

async def setup(bot):
    await bot.add_cog(WikipediaComando(bot))