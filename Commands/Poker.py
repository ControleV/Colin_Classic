from imports import *

class Poker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'poker', description= "[Fun] Play a game of Poker with server members!")
    @app_commands.describe(friend1= 'Who will be the first participant?')
    @app_commands.describe(friend2= 'Who will be the second participant?')
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_pokerplus(self, interaction: Interaction, friend1: str = None, friend2: str = None):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Poker")
        oranges = Stats()
        nickNames = ReadNickNames()

        if friend1 == None or friend2 == None:
            lista = nickNames["nicks"]
            friend1 = choice(lista)
            friend2 = choice(lista)
          
        acoes = [str(tradutor[0]), str(tradutor[1]), str(tradutor[2]),
                 str(tradutor[3]), str(tradutor[4]), str(tradutor[5]),
                 str(tradutor[6])]

        vencedor= choice([str(friend1), str(friend2), str(interaction.user.name)])

        embed = Embed(title = str(tradutor[8]).format(friend1, friend2, interaction.user.name), description = str(tradutor[7]), colour = interaction.user.colour)
        
        embed.add_field(name= f'**{friend1}**', value=choice(acoes), inline=True)
        embed.add_field(name= f'**{friend2}**', value=choice(acoes), inline=True)
        embed.add_field(name= f'**{interaction.user.name}**', value=choice(acoes), inline=True)
        embed.add_field(name= str(tradutor[9]).format(vencedor), value= str(tradutor[10]), inline=False)
        
        embed.set_thumbnail(url='https://pngimg.com/uploads/poker/poker_PNG19.png')
        
        embed.set_author(name='Poker', icon_url='https://thumbs.gfycat.com/ElegantBothBobolink-size_restricted.gif')
        

        if str(interaction.user.id) in oranges:
            if vencedor == interaction.user.name:
                premio = randint(10, 20)

                embed.add_field(name= f'🍊 {str(tradutor[11])}', value=f'**>>** {premio}', inline=True)

                oranges[str(interaction.user.id)]["laranjas"] = oranges[str(interaction.user.id)]["laranjas"] + premio

                DumpStats(data= oranges)

        await interaction.response.send_message(embed = embed)
           
async def setup(bot):
    await bot.add_cog(Poker(bot))