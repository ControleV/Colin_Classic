from Modules.CallJsonjs import ReadGuildPreferences, ReadLanguages, Stats
from discord import app_commands, Interaction, File, Member
from PIL import Image, ImageFont, ImageDraw, ImageOps
from discord.ext import commands
from requests import get
from io import BytesIO

class Perfil(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name= 'profile', description = "[Info] See your profile!")
    @app_commands.describe(member= "View someone else's profile!")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_perfil(self, interaction: Interaction, member: Member = None):
        await interaction.response.defer()

        usado = ReadGuildPreferences(guildId = str(interaction.guild.id))
        tradutor = ReadLanguages(lingua= usado, command= "Perfil")
        stats = Stats()

        if member == None:
            familiaIcon = Image.open(f"Images/Families/{str(stats[str(interaction.user.id)]['college'])}.png")
            specimen = stats[str(interaction.user.id)][str(interaction.guild.id)]['title']
            lvl = stats[str(interaction.user.id)][str(interaction.guild.id)]['level']
            xp = stats[str(interaction.user.id)][str(interaction.guild.id)]['xp']
            bannerFont = str(stats[str(interaction.user.id)]["bannerativo"])
            userDescription = stats[str(interaction.user.id)]["descricao"]
            oranges = stats[str(interaction.user.id)]['laranjas']
            urlcard = get(interaction.user.avatar)
            userName = str(interaction.user.name)
            userId = str(interaction.user.id)

        else:
            familiaIcon = Image.open(f"Images/Families/{str(stats[str(member.id)]['college'])}.png")
            specimen = stats[str(member.id)][str(interaction.guild.id)]['title']
            bannerFont = str(stats[str(member.id)]["bannerativo"])
            lvl = stats[str(member.id)][str(interaction.guild.id)]['level']
            userDescription = stats[str(member.id)]["descricao"]
            xp = stats[str(member.id)][str(interaction.guild.id)]['xp']
            oranges = stats[str(member.id)]['laranjas']
            urlcard = get(member.avatar)
            userName = str(member.name)
            userId = str(member.id)

        font_gigantous = ImageFont.truetype("Fonts/square.ttf", 55)
        font_largePlus = ImageFont.truetype("Fonts/square.ttf", 40)
        font_large = ImageFont.truetype("Fonts/square.ttf", 35)

        back = Image.open("Images/Profile/perfil.png")
        draw = ImageDraw.Draw(back)

        mask = Image.open("Images/Masks/ProfilePictureMask.png").convert('L')
        mask = mask.resize((280, 280))

        avatarcard = Image.open(BytesIO(urlcard.content))
        avatarcard = avatarcard.convert("RGBA")
        avatarcard = avatarcard.resize((280, 280))
        avatarcard = ImageOps.fit(avatarcard, mask.size, centering=(0.5, 0.5))
        avatarcard.putalpha(mask)

        banner = Image.open(f"Images/Banners/{bannerFont}.png")
        banner = banner.convert("RGBA")

        familiaIcon = familiaIcon.convert("RGBA")
        familiaIcon = familiaIcon.resize((150, 150))

        prestigio = Image.open("Images/Insignias/prestigio.png")
        prestigio = prestigio.convert("RGBA")
        prestigio = prestigio.resize((80, 80))

        back.paste(avatarcard, (40, 40), avatarcard)
        back.paste(banner, (1410, 30), banner)
        back.paste(familiaIcon, (1610, 590), familiaIcon)

        if member == None:
            if stats[str(interaction.user.id)][str(interaction.guild.id)]["prestigios"] > 0:
                back.paste(prestigio, (1425, 320), prestigio)
                draw.text((1475, 380), f"X{str(stats[str(interaction.user.id)][str(interaction.guild.id)]['prestigios'])}", (255, 255, 255), font= font_large)

        else:
            if stats[str(member.id)][str(interaction.guild.id)]["prestigios"] > 0:
                back.paste(prestigio, (1425, 320), prestigio)
                draw.text((1475, 380), f"X{str(stats[str(member.id)][str(interaction.guild.id)]['prestigios'])}", (255, 255, 255), font= font_large)

        draw.text((680, 85), f"{specimen}", (255, 255, 255), anchor= "ms", font= font_gigantous)

        nameFontSize = 55
        letterAmount = 0

        for j in userName:
            letterAmount += 1

            if letterAmount == 12:
                nameFontSize = nameFontSize - 10
                letterAmount = 0

        nameFont = ImageFont.truetype("Fonts/square.ttf", nameFontSize)
        draw.text((680, 175), userName, (255, 255, 255), anchor= "ms", font= nameFont)
        draw.text((680, 250), f"{userId}", (255, 255, 255), anchor= "ms", font= font_large)
        draw.text((680, 318), f"XP: {xp} / Level: {lvl}", (255, 255, 255), anchor= "ms", font= font_large)
        draw.text((40, 355), f"{str(tradutor[0])}: {oranges}", (255, 255, 255), font= font_gigantous)

        letras = 0
        x = 0
        y = 0

        for i in userDescription:
            draw.text((50 + x, 965 + y), i, (255, 255, 255), font= font_largePlus)
            
            letras = letras + 1

            if i == 'i' or i == ':' or i == 'I':
                x = x + 12

            elif i == ',' or i == ' ':
                x = x + 15

            else:
                x = x + 28

            if letras > 65:
                if (i.isspace()) == True:
                    letras = 0
                    x = 0
                    y = y + 45

        draw.text((275, 920), str(tradutor[1]), (255, 255, 255), anchor= "ms", font= font_gigantous)

        if stats[str(userId)]['college'] == 'waterzone':
            draw.text((1690, 790), "Shark College", (255, 255, 255), anchor= "ms", font= font_gigantous)
            draw.text((1690, 820), f"Water Area", (255, 255, 255),  anchor= "ms", font= font_large)

        if stats[str(userId)]['college'] == 'plantaezone':
            draw.text((1690, 790), "Mother College", (255, 255, 255), anchor= "ms", font= font_gigantous)
            draw.text((1690, 820), f"Plantae Area", (255, 255, 255),  anchor= "ms", font= font_large)

        if stats[str(userId)]['college'] == 'desconhecido':
            draw.text((1690, 790), "in no college", (255, 255, 255), anchor= "ms", font= font_gigantous)
            draw.text((1690, 820), f"/family to join", (255, 255, 255),  anchor= "ms", font= font_large)

        if stats[str(userId)]['college'] == 'blacklatexzone':
            draw.text((1690, 790), "Puro college", (255, 255, 255), anchor= "ms", font= font_gigantous)
            draw.text((1690, 820), f"Black Latex Area", (255, 255, 255),  anchor= "ms", font= font_large)

        if stats[str(userId)]['college'] == 'whitelatexzone':
            draw.text((1690, 790), "Colin college", (255, 255, 255), anchor= "ms", font= font_gigantous)
            draw.text((1690, 820), f"White latex Area", (255, 255, 255),  anchor= "ms", font= font_large)

        if stats[str(userId)]['college'] == 'dragonzone':
            draw.text((1690, 790), "Dragons college", (255, 255, 255), anchor= "ms", font= font_gigantous)
            draw.text((1690, 820), f"Cristals Area", (255, 255, 255),  anchor= "ms", font= font_large)

        if stats[str(userId)]['college'] == 'researchzone':
            draw.text((1690, 790), "Dr.K college", (255, 255, 255), anchor= "ms", font= font_gigantous)
            draw.text((1690, 820), f"Research area", (255, 255, 255),  anchor= "ms", font= font_large)
  
        back.save("Images/Profile/perfilDone.png")

        await interaction.followup.send(file= File("Images/Profile/perfilDone.png"))

async def setup(bot):
    await bot.add_cog(Perfil(bot))
