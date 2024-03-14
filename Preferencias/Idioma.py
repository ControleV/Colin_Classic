from discord import app_commands, Interaction
from discord.ext import commands
from json import load, dump

class MudarIdioma(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="language", description="[Preferences] In what language I should speak? ^w^")
    @app_commands.describe(lang_code="You can use 'en', 'pt', 'fr' or 'es' for now!")
    @app_commands.checks.cooldown(1, 5, key = lambda i: (i.guild.id))
    async def set_lang(self, interaction: Interaction, lang_code: str):
        with open("Jsons/Languages.json", "r", encoding='utf-8') as f:
            languagesData = load(f)
        with open("Jsons/PrefJsons/GuildPreferencies.json", "r") as g:
            guildData = load(g)

        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(f"Oops.. **{interaction.user.name}**, It looks like you don't have the necessary permissions <:TOME:1047301334384250910>")

        else:
            if lang_code in languagesData:
                if str(interaction.guild.id) in guildData:
                    guildData[str(interaction.guild.id)]['language'] = str(f"{lang_code}")

                    with open("Jsons/PrefJsons/GuildPreferencies.json", "w") as g:
                        dump(guildData, g)

                else:
                    guildData[str(interaction.guild.id)] = {}
                    guildData[str(interaction.guild.id)]['language'] = str(f"{lang_code}")

                    with open("Jsons/PrefJsons/GuildPreferencies.json", "w") as g:
                        dump(guildData, g)
                
                lingua = languagesData[f"{lang_code}"]["Idioma"][0]
                lingua = str(lingua).format(f"{interaction.user.name}")
                await interaction.response.send_message(f"{lingua}")
            
            else:
                await interaction.response.send_message(f"Oops.. **{interaction.user.name}**, It looks like you entered the wrong code, or there is no translation for this language yet <:triste:1045768010255835246>")

    @commands.Cog.listener()
    async def on_message(self, ctx):
        with open("Jsons/PrefJsons/GuildPreferencies.json", "r") as hg:
                guildData = load(hg)
        
        if str(ctx.guild.id) not in guildData:
            if not ctx.author.bot:
                guildData[str(ctx.guild.id)] = {}
                guildData[str(ctx.guild.id)]['language'] = "en"

                with open("Jsons/PrefJsons/GuildPreferencies.json", "w") as fiai:
                    dump(guildData, fiai)

async def setup(bot):
    await bot.add_cog(MudarIdioma(bot))