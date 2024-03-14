from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages
from discord import app_commands, Interaction
from discord.ext import commands
import email.message
import smtplib

class ReportBug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'report_bug', description= "[Preferences] Report bugs or translation failures here!")
    @app_commands.describe(title= "What's the topic? (you can type the command name if you like)")
    @app_commands.describe(description= "Describe exactly what is going wrong or what you think should be done differently")
    @app_commands.checks.cooldown(1, 10, key = lambda i: (i.user.id))
    async def on_ReportBug(self, interaction: Interaction, title: str, description: str):
        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Report")

        await interaction.response.send_message(str(tradutor[0]), ephemeral= True)

        EMAIL_ADDRESS = 'victormotadev@gmail.com'
        EMAIL_PASSWORD = 'gcfhjpujqefbvbbq'

        msg = email.message.Message()
        msg['Subject'] = title
        msg['From'] = 'victormotadev@gmail.com'
        msg['To'] = 'victormotadev@gmail.com'
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(f"{interaction.user} // {interaction.user.id} disse: {description}")

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        s.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        
async def setup(bot):
    await bot.add_cog(ReportBug(bot))