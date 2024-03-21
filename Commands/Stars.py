from imports import *

class Stars(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name = 'stars', description = "[Fun] Introducing Resident Evil, but with server members!")
    @app_commands.describe(captain = 'Who is the team captain?')
    @app_commands.describe(berry = 'Who is Berry on the team?')
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_starsplus(self, interaction: Interaction, captain: str = None, berry: str = None):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Stars")

        if captain == None or berry == None:
            nicknames = ReadNickNames()

            lista = nicknames["nicks"]
            captain = choice(lista)
            berry = choice(lista)

        embedstars = Embed(title= str(tradutor[0]), description= str(tradutor[1]).format(captain, berry, interaction.user.name), colour= interaction.user.colour)
        embedstars.set_thumbnail(url="https://64.media.tumblr.com/8d74d284cb2f7b525c52488caa828f6d/tumblr_nskeddWV9h1sbbfwho1_250.png")
        embedstars.set_author(name='Umbrella Corps.', icon_url="https://static.wikia.nocookie.net/residentevil/images/5/50/UmbrellaCorporation3.png/revision/latest/top-crop/width/360/height/360?cb=20130206014840")
        embedstars.set_image(url="https://static.wixstatic.com/media/a0aa22_cb9312970984498aaf39cfa774384c1c~mv2.gif")
        
        await interaction.response.send_message(embed = embedstars)

async def setup(bot):
    await bot.add_cog(Stars(bot))