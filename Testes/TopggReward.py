from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages, Stats, DumpStats
from discord import app_commands, Interaction, Embed
from Modules.ggChecker import GG
from discord.ext import commands

class TopggReward(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= "vote", description= "[User] Receive prizes for voting for me!")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_dbl_vote(self, interaction: Interaction):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Topgg")
        stats = Stats()

        gg_token = ""
        bot_id = 956589806622756894
        user_id = interaction.user.id

        bot = GG(gg_token, bot_id, user_id)
        check = bot.has_voted()
        
        if check == True:
            title = f"{str(tradutor[0])} <a:RepostToVibe:994272960166772858>"
            description = str(tradutor[1])

            stats[str(interaction.user.id)]["laranjas"] += 3200

            DumpStats(data= stats)

        else:
            title = "Oops.."
            description = f"{str(tradutor[2])} \nhttps://top.gg/bot/956589806622756894"

        embed = Embed(title= title, description= description, colour= interaction.user.colour)
        embed.set_author(name= "Top.gg", url= 'https://top.gg/bot/956589806622756894', icon_url= 'https://cdn.discordapp.com/attachments/1047528676864032818/1054798089891889163/colin_new_face2.png')
        embed.set_thumbnail(url= 'https://cdn.discordapp.com/attachments/1047528676864032818/1055480276387639397/ghfghfh.png')

        if check == True:
            embed.add_field(name= f"🍊 {str(tradutor[3])}", value= ">> 3200", inline= True)

        await interaction.response.send_message(embed= embed)

async def setup(bot):
    await bot.add_cog(TopggReward(bot))