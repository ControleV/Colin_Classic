from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages, ReadNickNames
from discord import Interaction, Embed, app_commands
from discord.ext import commands
from os import linesep as line
from random import choice

class PtCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #COMANDOS
    @app_commands.command(name= "uwu", description= "[Fun] Gift someone OwO")
    @app_commands.describe(friend= "Who will you give the gift to?")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_uwu(self, interaction: Interaction, friend: str = None):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Ptcommands")

        if friend == None:
            nickNames = ReadNickNames()

            lista = nickNames["nicks"]
            friend = choice(lista)

        embed = Embed(description= str(tradutor[0]).format(interaction.user.name, friend, line, friend), colour= 8007909)

        await interaction.response.send_message(embed = embed)

    @app_commands.command(name= "secret", description= "[Fun] Make the BOT tell you a little secret.. (turn on direct messages)")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_segredo(self, interaction: Interaction):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Ptcommands")

        mensagem = [str(tradutor[1]).format(interaction.user.name, line), str(tradutor[2]).format(interaction.user.name)]
        aenviar = choice(mensagem)

        await interaction.user.send(aenviar)
        await interaction.response.send_message(str(tradutor[3]))

    @app_commands.command(name= "ping", description= "[Info] Shows client latency")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_ping(self, interaction: Interaction):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Ptcommands")
        
        botping = str(self.bot.latency)
        botping = botping[:4]

        await interaction.response.send_message(f'🏓 Pong! ' + str(tradutor[4]).format(line, botping))

    @app_commands.command(name= "pong", description= "[Info] Shows client latency")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_pong(self, interaction: Interaction):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Ptcommands")
        
        botping = str(self.bot.latency)
        botping = botping[:4]

        await interaction.response.send_message(f'🏓 Ping! ' + str(tradutor[4]).format(line, botping))

    @app_commands.command(name= "help", description= "[Info] A little help for beginners ^w^")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_help(self, interaction: Interaction):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Ptcommands")

        embedhelp = Embed(description= str(tradutor[5]).format(interaction.user.name, line))

        await interaction.response.send_message(embed = embedhelp)

    @app_commands.command(name= "press_f", description= "[Fun] Pay respects")
    @app_commands.checks.cooldown(1, 5, key = lambda i: (i.guild_id))
    async def on_f(self, interaction: Interaction):
        await interaction.response.send_message(f'**{interaction.user.name}** *pressed F to pay respects*')

    @app_commands.command(name= "choose", description= "[Fun] Make the BOT choose between two options")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_escolha(self, interaction: Interaction, opçao1: str, opçao2: str):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Ptcommands")

        lista = [opçao1, opçao2]
        resposta = choice(lista)

        await interaction.response.send_message(str(tradutor[6]).format(opçao1, opçao2, resposta))

    @app_commands.command(name= "heads_or_tails", description= "[Fun] Make heads or tails")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_caracoroa(self, interaction: Interaction):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Ptcommands")

        lista = [f"🗿 {tradutor[7]}", f"👑 {tradutor[8]}"]
        resposta = choice(lista)

        await interaction.response.send_message(str(tradutor[9]).format(resposta))

async def setup(bot):
    await bot.add_cog(PtCommands(bot))