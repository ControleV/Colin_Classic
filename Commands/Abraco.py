from imports import *

class Abraco(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= "hug", description= "[Fun] Hug someone affectionately UwU")
    @app_commands.describe(friend= "Who are you going to hug? ^w^")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_abracoplus(self, interaction: Interaction, friend: str = None):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Abraco")

        if friend == None:
            nickNames = ReadNickNames()

            lista = nickNames["nicks"]
            friend = choice(lista)

        image = "Placeholder"
        footer = "Placeholder"

        escolherabracomigo = randint(1,3)
        embeddescription = [str(tradutor[0]).format(interaction.user.name, friend), str(tradutor[1]).format(friend, interaction.user.name), str(tradutor[2]).format(interaction.user.name, friend)]

        if escolherabracomigo == 1:
            image = "https://i.pinimg.com/564x/aa/a5/a1/aaa5a16eda0911aeb15445d52836b747.jpg"
            footer = "https://br.pinterest.com/pin/595038169527644926/"

        elif escolherabracomigo == 2:
            image = "https://i.pinimg.com/564x/14/d8/57/14d85755a6926d61c74122f6498c6c4b.jpg"
            footer = "https://br.pinterest.com/pin/139470919700367897/"

        elif escolherabracomigo == 3:
            image = "https://pbs.twimg.com/media/FFVQ9PjXIAgMtj7?format=png&name=240x240"
            footer = "https://mobile.twitter.com/Enderma88701889/status/1465166269016064011"

        embed = Embed(description= choice(embeddescription), colour= interaction.user.colour)
        embed.set_image(url= image)
        embed.set_footer(text= footer)
                
        await interaction.response.send_message(embed = embed)

async def setup(bot):
    await bot.add_cog(Abraco(bot))