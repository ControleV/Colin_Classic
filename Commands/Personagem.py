from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages
from discord import Interaction, Embed
from discord.ext import commands
from discord import app_commands
from random import randint

class Personagem(commands.Cog):
   def __init__(self, bot):
      self.bot = bot

   @app_commands.command(name="character", description="[Fun] Become one of the characters in Changed!")
   @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
   async def on_personagem(self, interaction: Interaction):
      usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
      tradutor = ReadLanguages(lingua= usado, command= "Personagem")

      escolherpersonagem = randint(1,6)
      foto = 'Placeholder'
      link = 'Placeholder'

      embed = Embed(title= str(tradutor[0]).format(interaction.user.name), description= str(tradutor[escolherpersonagem]).format(interaction.user.name), colour = interaction.user.colour)

      if escolherpersonagem == 1:
         foto = 'https://i.pinimg.com/originals/d4/13/ec/d413ecb9a7cf957ac82c14e083cbd6fb.jpg'
         link = 'https://br.pinterest.com/pin/775393260859257649/'

      elif escolherpersonagem == 2:
         foto = 'https://i.pinimg.com/564x/9a/60/b4/9a60b463eac459099f9e7914053a72cd.jpg'
         link = 'https://br.pinterest.com/pin/434738170289854664/'

      elif escolherpersonagem == 3:
         foto = 'https://i.pinimg.com/564x/db/82/26/db8226aa09b49391c39515155c8b50f7.jpg'
         link = 'https://br.pinterest.com/pin/455074737351806392/'

      elif escolherpersonagem == 4:
         foto = 'https://i.pinimg.com/564x/3a/30/32/3a303266c7841eb96e91bbe5adc2fcfd.jpg'
         link = 'https://br.pinterest.com/pin/389209592806953239/'

      elif escolherpersonagem == 5:
         foto = 'https://i.pinimg.com/564x/8d/98/a9/8d98a936ffeb594d9253e1344d23e700.jpg'
         link = 'https://br.pinterest.com/pin/775393260859572493/'

      elif escolherpersonagem == 6:
         foto = 'https://i.pinimg.com/564x/78/e1/0b/78e10b0a12abf63e80db5dd1d48723bf.jpg'
         link = 'https://br.pinterest.com/pin/623607879657951188/'

      embed.set_image(url= foto)
      embed.set_footer(text= link)
           
      await interaction.response.send_message(embed = embed)

async def setup(bot):
    await bot.add_cog(Personagem(bot))