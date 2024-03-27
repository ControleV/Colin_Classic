from imports import *

class Movie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= "dance", description= "O que te faz dançar?")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_dance(self, interaction: Interaction, texto: str = None, member: Member = None):
        try:
            await interaction.response.defer()
            
            if texto is None:
                texto = "Placeholder legal"
                
            #Checar se o texto é muito grande, se sim, fatie-o
            texto.strip()

            j = 0
            limite = 15
            a = 0
                        
            for i in texto:
                j += 1
                
                if j > limite and i == ' ':
                    texto = texto[:j] + "\n" + texto[j:]
                                
                    limite += a + 10
                    a = 0
                    
                if j > limite:
                    a += 1
        
        

            # Carregar o vídeo "Dancing" dentro da variável clip
            clip1 = VideoFileClip("Movies/Dancing.mov")



            # diminuir o volume do clipe (volume x 0.8)
            clip1 = clip1.volumex(0.8)



            # Gerar um clipe de texto.
            txt_clip = TextClip(texto, fontsize = 50, color='white', stroke_width = 1, stroke_color = 'black')
            txt_clip = txt_clip.set_pos('center').set_duration(t = clip1.duration)
            
            
            
            #Pegar a foto de perfil do usuário e salvar
            if member == None:
                setimage = get(interaction.user.avatar)
            else:
                setimage = get(member.avatar)
                
            setimage = Image.open(BytesIO(setimage.content))
            setimage = setimage.resize((100, 100))
            setimage.save("Images/Movies/userimage.png")


            #pegar a foto salva e criar um clipe.
            profile_clip = ImageClip("Images/Movies/userimage.png").set_pos(('center', 'center'))
            profile_clip = profile_clip.set_pos((20, 20)).set_duration(t = clip1.duration)


            # Compor o vídeo com o texto.
            video = CompositeVideoClip([clip1, txt_clip, profile_clip])



            # Escreve o resultado em um arquivo.
            video.write_videofile(filename = "Movies/Done/Dancing_Done.mp4", fps=24, remove_temp = True)
            
            
            
            await interaction.followup.send(file = File("Movies/Done/Dancing_Done.mp4"))
        
        except:
            
            await interaction.followup.send("An error has ocurred...")
            print(traceback.format_exc())
    
async def setup(bot):
    await bot.add_cog(Movie(bot))
    