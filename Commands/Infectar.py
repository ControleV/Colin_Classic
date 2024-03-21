from imports import *

class Infectar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= "infect", description= "[Fun] Infect a server member!")
    @app_commands.describe(victim= "Who will be your next victim?")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_infect(self, interaction: Interaction, victim: str = None):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Infectar")

        fera = [str(tradutor[0]), str(tradutor[1]), str(tradutor[2]), str(tradutor[3])]
        feraescolhida = choice(fera)
        probabilidade = randint(0, 20)

        footer = "Placeholder"

        if victim == None:
            nickNames = ReadNickNames()

            lista = nickNames["nicks"]
            victim = choice(lista)

        if probabilidade <= 10:
            embeddescription = str(tradutor[5]).format(interaction.user.name, victim, interaction.user.name)
            thumb = 'https://staff-cdn.siege.gg/org-632-bonk.png'
            footer = 'F no chat'

        else:
            if feraescolhida == fera[0]:
                embeddescription = str(tradutor[6]).format(interaction.user.name, victim, feraescolhida)
                thumb = 'https://i.pinimg.com/originals/3a/50/2c/3a502c2223de3fde2ec90ddbd579177a.jpg'
                footer = 'https://br.pinterest.com/pin/326370304254738816/'

            if feraescolhida == fera[1]:
                embeddescription = str(tradutor[6]).format(interaction.user.name, victim, feraescolhida)
                thumb = 'https://i.pinimg.com/564x/fc/5b/0b/fc5b0b0c481a38e01e8fb1dfc2318309.jpg'
                footer = 'https://br.pinterest.com/pin/579557045779865501/'

            if feraescolhida == fera[2]:
                embeddescription = str(tradutor[6]).format(interaction.user.name, victim, feraescolhida)
                thumb = 'https://i.pinimg.com/originals/ff/35/4d/ff354d122caf099cbdd901cb84562023.jpg'
                footer = 'https://br.pinterest.com/pin/51158145757540122/'

            if feraescolhida == fera[3]:
                embeddescription = str(tradutor[6]).format(interaction.user.name, victim, feraescolhida)
                thumb = 'https://i.pinimg.com/originals/09/7b/1a/097b1acb8b229c3b124b4297e92cd924.png'
                footer = 'https://br.pinterest.com/pin/51158145757540122/'

        embed = Embed(title=str(tradutor[4]).format(interaction.user.name), description= embeddescription)
        embed.set_author(name='Changed', icon_url='https://static.wikia.nocookie.net/changed1449/images/e/ef/Puro.png/revision/latest/top-crop/width/360/height/450?cb=20210630204745')
        embed.set_image(url= thumb)
        embed.set_footer(text= footer)

        await interaction.response.send_message(embed = embed)

async def setup(bot):
    await bot.add_cog(Infectar(bot))