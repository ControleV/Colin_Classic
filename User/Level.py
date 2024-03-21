from imports import *

#colocar cargo em quem sobe de nível
level = ["Labo rat", "Specimen", "Latex cristal", "Latex GOO", "Latex creature", "Biohazard Furry"]

level_num = [4, 9, 14, 19, 24, 29]

class Level(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #isso vai aumentar o xp do usuário toda vez que ele falar
    @commands.Cog.listener()
    async def on_message(self, ctx):
        usado = ReadGuildPreferences(guildId = str(ctx.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Level")

        if not ctx.author.bot:
            levels = Stats()

            if str(ctx.author.id) in levels:
                if str(ctx.guild.id) in levels[str(ctx.author.id)]:
                    xp = levels[str(ctx.author.id)][str(ctx.guild.id)]['xp']
                    lvl = levels[str(ctx.author.id)][str(ctx.guild.id)]['level']

                    increased_xp = xp+25
                    new_level = int(increased_xp/100)

                    levels[str(ctx.author.id)][str(ctx.guild.id)]['xp'] = increased_xp

                    DumpStats(data = levels)

                    #User upou
                    if new_level > lvl:

                        levels[str(ctx.author.id)][str(ctx.guild.id)]['level'] = new_level
                        levels[str(ctx.author.id)][str(ctx.guild.id)]['xp'] = 0
                                
                        #Dá um título ao usuário
                        if lvl == 5: levels[str(ctx.author.id)][str(ctx.guild.id)]['title'] = 'Lab rat'
                        if lvl == 9: levels[str(ctx.author.id)][str(ctx.guild.id)]['title'] = 'Specimen'
                        if lvl == 14: levels[str(ctx.author.id)][str(ctx.guild.id)]['title'] = 'Latex cristal'
                        if lvl == 19: levels[str(ctx.author.id)][str(ctx.guild.id)]['title'] = 'Latex GOO'
                        if lvl == 24: levels[str(ctx.author.id)][str(ctx.guild.id)]['title'] = 'Lab creature'
                        if lvl >= 29: levels[str(ctx.author.id)][str(ctx.guild.id)]['title'] = 'Biohazard Furry'

                        DumpStats(data = levels)

                else:
                    levels[str(ctx.author.id)][str(ctx.guild.id)] = {}
                    levels[str(ctx.author.id)][str(ctx.guild.id)]['xp'] = 0
                    levels[str(ctx.author.id)][str(ctx.guild.id)]['level'] = 1
                    levels[str(ctx.author.id)][str(ctx.guild.id)]['prestigios'] = 0
                    levels[str(ctx.author.id)][str(ctx.guild.id)]['title'] = str(tradutor[0])

                    DumpStats(data = levels)

            else:
                levels[str(ctx.author.id)] = {}
                levels[str(ctx.author.id)]["laranjas"] = 0
                levels[str(ctx.author.id)]["descricao"] = "Lorem Impsum dolor sit amet :)"
                levels[str(ctx.author.id)]["banners"] = ["default"]
                levels[str(ctx.author.id)]["bannerativo"] = "default"
                levels[str(ctx.author.id)]["college"] = "desconhecido"
                levels[str(ctx.author.id)][str(ctx.guild.id)] = {}
                levels[str(ctx.author.id)][str(ctx.guild.id)]['xp'] = 0
                levels[str(ctx.author.id)][str(ctx.guild.id)]['level'] = 1
                levels[str(ctx.author.id)][str(ctx.guild.id)]['prestigios'] = 0
                levels[str(ctx.author.id)][str(ctx.guild.id)]['title'] = str(tradutor[0])

                DumpStats(data = levels)

    @app_commands.command(name= "leaderboard", description= "[Level] Shows the XP leaderboard!")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def leader(self, interaction: Interaction):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Level")

        await interaction.response.send_message(str(tradutor[3]))

async def setup(bot):
    await bot.add_cog(Level(bot))