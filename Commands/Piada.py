from discord.ext import commands
from discord import app_commands
from discord import Interaction
from random import choice
from os import linesep

class Piada(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="piada", description="[Diversão] Colin lhe dirá uma boa piada (Portuguese only)")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_piada(self, interaction: Interaction):
        listapiada = [f'-Você conhece a piada do Pônei?{linesep}-Pô nei eu', f'-O que o pagodeiro foi fazer na igreja?{linesep}-Cantar Pá God', f'-Você sabe qual é o rei dos queijos?{linesep}-O reiqueijão', 
                              f'-O que o pato falou pra pata?{linesep}-Vem Quá', f'-O que acontece quando chove na inglaterra?{linesep}-Vira Inglalama', f'-O que o tomate foi fazer no banco?{linesep}-Tirar o extrato', 
                              f'-Qual o nome da pessoa que viu Thor de perto?{linesep}-Vi-thor', f'-Por que a galinha atravessou a rua?{linesep}*Esquece essa n dá..*', f'-O que da um crusamento entre uma girafa e um papagaio?{linesep}-Um alto-falante', 
                              f'-O que o jogador de vôlei foi fazer no banco?{linesep}-Fazer um saque', f'-Por que a velhinha não usa relógio?{linesep}-Porque ela é sem hora (senhora)', f'-Por que há uma cama elástica no polo Norte?{linesep}-Para o urso polar', 
                              f'-O que a vaca disse para o boi?{linesep}-Te amuuuuuuuuuuuu', f'-{interaction.user.name}, você sabia que as caixas pretas dos aviões são, na verdade, laranjas?{linesep}-O quê? Não são caixas?', 
                              f'-Por que a água foi presa?{linesep}-Porquê ela matou a sede', f'Um caipira chega a casa de um amigo que está vendo TV e pergunta:{linesep}-E aí, firme?{linesep}-Não, Futebor', 
                              f'-Quero terminar, você é muito imaturo{linesep}-Quem?{linesep}-Você{linesep}-Te perguntou', f'-sabe oq o esqueleto caipira disse pro esqueleto?{linesep}- Ô-sso', f'-Qual o órgão público representado por um anão infértil?{linesep}-O mini-estéril da saúde',
                              f'-Qual a comida q liga e desliga?{linesep}-Strogon-off', f'-Qual o homem q tem muitas expressões faciais?{linesep}-O Fred maiscarinhas', f'-Qual o protetor dos fedidos e dos mal cheirosos?{linesep}-O deus-odorante',
                              f'-Sabe pq todos os imitadores imitam o Silvio Santos?{linesep}-É um transtorno obssesilvio compulsilvio', f'-Vc gosta de café de cavalo?{linesep}-Aquele com pouco pó pouco pó pouco pó...',
                              f'-Qual a pizza q se deve comer sozinho?{linesep}-O prova-alone', f'-Qual o torresmo q nunca tá de bem com a vida?{linesep}-O torresmungando', f'-Qual a ferramenta q vai proteger a todos?{linesep}-A chave, DEFENDA!',
                              f'-Pq aparentemente todos os avôs somem no dia da eleição?{linesep}-Pq todo mundo pergunta: "onde q vovô tá"', f'-Qual o musical preferido dos viciados?{linesep}-O "Lolóland"',
                              f'-Qual a carne preferida do Colin UwU?{linesep}-O filé miownnn 😍', f'-Sabe oq o Faustão foi fazer no parque?{linesep}-Brincadeira bicho']

        listachamada = [f'Se prepara {interaction.user.name}, essa vai doer :3{linesep}', f'Ah, lembrei de uma boa {interaction.user.name}, escuta só..{linesep}', f'Hum talvez.. {interaction.user.name} se liga :3{linesep}', 
                            f'Essa vai doer na alma {interaction.user.name}, uhHum..{linesep}', f'Uhh interessante? {interaction.user.name} segura essa..{linesep}', f'Essa é clássica, {interaction.user.name} vamo lá..{linesep}', 
                            f'Será que eu mando essa?, {interaction.user.name}, éhh..{linesep}', f'Uma clássica também, {interaction.user.name} não entre em convulsão.. por favor <:relaxa:945303087407579216>{linesep}', 
                            f'Essa é do balacobaco {interaction.user.name}, veja só:{linesep}']

        await interaction.response.send_message(choice(listachamada) + choice(listapiada))

async def setup(bot):
    await bot.add_cog(Piada(bot))