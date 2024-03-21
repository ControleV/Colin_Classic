from imports import *
import json

class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'daily', description= "[User] get your daily prize!")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_Daily(self, interaction: Interaction):
        try:
            await interaction.response.defer()
            usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
            tradutor = ReadLanguages(lingua= usado, command= "Daily")

            with open("Jsons/Daily.json", "r") as ub:
                data = json.load(ub)

            # Verificar se o usuário já usou o comando hoje
            user_id = str(interaction.user.id)
            if user_id in data:
                # Obter a data do último uso do comando pelo usuário
                last_used = datetime.fromisoformat(data[user_id])


                # Verificar se a data é de hoje
                if last_used.date() == datetime.now().date():
                    await interaction.followup.send("Você já usou o comando hoje! Tente novamente amanhã.")
                    return

            # Atualizar os dados do usuário no arquivo JSON
            data[user_id] = datetime.now().isoformat()
            with open("Jsons/Daily.json", "w") as ub:
                json.dump(data, ub)

            stats = Stats()

            stats[str(interaction.user.id)]['laranjas'] += 3200

            DumpStats(data= stats)

            embed = Embed(title= str(tradutor[1]),
                        description= str(tradutor[2]),
                        colour= interaction.user.colour)

            await interaction.followup.send(embed= embed)

        except Exception as e:
            await interaction.followup.send(f"{traceback.format_exc()}")

async def setup(bot):
    await bot.add_cog(Daily(bot))
