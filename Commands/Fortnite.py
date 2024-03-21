from imports import *

class Fortnite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name= "fortnite", description= "[Fun] Play a game of Fortnite with someone!")
    @app_commands.describe(opponent= "Who will be your opponent?")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_fortnite(self, interaction: Interaction, opponent: str = None):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Fortnite")

        dano = str(randint(10, 200))
        ganhou = randint(0, 22)

        local = ['LOGJAM LUMBERYARD', 'SHIFTY SHAFTS', 'SLEEPY SOUND', 'COMMAND CAVERN', 'THE FORTRESS', 'CONEY CROSSROADS', 'THE DAILY BUGLE',
                 'CAMP CUDDLE', 'TILTED TOWERS', 'SANCTUARY', 'GREASY GROVE', 'ROCKY REELS', 'THE JONESES', 'SYNAPSE STATION', "CHONKER'S SPEEDWAY", 'CONDO CANYON']

        arma = ['COMMON AUTO SHOTGUN', 'UNCOMMON AUTO SHOTGUN', 'RARE AUTO SHOTGUN', 'EPIC AUTO SHOTGUN', 'LEGENDARY AUTO SHOTGUN', 'COMMON DRUM SHOTGUN', 
                'UNCOMMON DRUM SHOTGUN', 'RARE DRUM SHOTGUN', 'EPIC DRUM SHOTGUN', 'LEGENDARY DRUM SHOTGUN', 
                'COMMON STRIKER PUMP SHOTGUN', 'UNCOMMON STRIKER PUMP SHOTGUN', 'RARE STRIKER PUMP SHOTGUN', 'EPIC STRIKER PUMP SHOTGUN', 
                'LEGENDARY STRIKER PUMP SHOTGUN', 'EXOTIC THE DUB', 'COMMON RANGER SHOTGUN', 'UNCOMMON RANGER SHOTGUN',
                'RARE RANGER SHOTGUN', 'EPIC RANGER SHOTGUN', 'LEGENDARY RANGER SHOTGUN', 'EPIC THERMAL SCOPED ASSAULT RIFLE', 'LEGENDARY THERMAL SCOPED ASSAULT RIFLE', 'EXOTIC STORM SCOUT', 
                'COMMON MK-SEVEN ASSAULT RIFLE', 'UNCOMMON MK-SEVEN ASSAULT RIFLE', 'RARE MK-SEVEN ASSAULT RIFLE', 'EPIC MK-SEVEN ASSAULT RIFLE', 'LEGENDARY MK-SEVEN ASSAULT RIFLE', "MYTHIC THE FOUNDATION'S MK-SEVEN ASSAULT RIFLE", 
                'COMMON RANGE ASSAULT RIFLE', 'UNCOMMON RANGE ASSAULT RIFLE', 'RARE RANGE ASSAULT RIFLE', 'EPIC RANGE ASSAULT RIFLE', 'LEGENDARY RANGE ASSAULT RIFLE', 'COMMON STRIKER BURST RIFLE', 
                'UNCOMMON STRIKER BURST RIFLE', 'RARE STRIKER BURST RIFLE', 'EPIC STRIKER BURST RIFLE', 'LEGENDARY STRIKER BURST RIFLE', 'HARVESTING TOOL..']

        if opponent == None:
            nickNames = ReadNickNames()

            lista = nickNames["nicks"]
            opponent = choice(lista)

        resultado = [str(tradutor[0]).format(interaction.user.name, opponent), str(tradutor[1]).format(opponent, interaction.user.name)]
        
        embed = Embed(title= str(tradutor[2]), description= str(tradutor[3]).format(interaction.user.name, opponent), colour= interaction.user.colour)
        embed.set_author(name='Fortnite', icon_url="https://i.pinimg.com/originals/e1/71/09/e171098d2797260e90e1b170063c079e.png")
        embed.set_thumbnail(url="https://cdn2.unrealengine.com/battlepass-battlestar-277x252-579065405.png")
        
        if ganhou >= 10: embed.add_field(name= str(tradutor[4]), value= resultado[0], inline=False)
        else: embed.add_field(name= str(tradutor[4]), value= resultado[1], inline=False)
        
        embed.add_field(name= str(tradutor[5]), value=dano, inline=True)
        embed.add_field(name= str(tradutor[6]), value=choice(local), inline=True)
        embed.add_field(name= str(tradutor[7]), value=choice(arma), inline=True)
        
        if ganhou >= 10:
            oranges = Stats()

            if str(interaction.user.id) in oranges:

                premio = randint(10, 20)

                embed.add_field(name= f'🍊{str(tradutor[8])}', value= str(tradutor[9]).format(premio), inline=True)

                oranges[str(interaction.user.id)]["laranjas"] = oranges[str(interaction.user.id)]["laranjas"] + premio

                DumpStats(data= oranges)
                    
        await interaction.response.send_message(embed= embed)

async def setup(bot):
    await bot.add_cog(Fortnite(bot))