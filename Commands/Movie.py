from imports import *

class Movie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= "dance", description= "O que te faz dançar?")
    @app_commands.checks.cooldown(1, 2, key = lambda i: (i.user.id))
    async def on_dance(self, interaction: Interaction, texto: str = None):
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
            clip = VideoFileClip("Movies/Dancing.mov")



            # diminuir o volume do clipe (volume x 0.8)
            clip = clip.volumex(0.8)



            # Gerar um clipe de texto.
            txt_clip = TextClip(texto, fontsize = 50, color='white', stroke_width = 1, stroke_color = 'black')




            # Colocar o texto depois de 3 segundos que o clipe iniciou.
            txt_clip = txt_clip.set_pos('center').set_duration(5)





            # Compor o vídeo com o texto.
            video = CompositeVideoClip([clip, txt_clip])





            # Escreve o resultado em um arquivo.
            video.write_videofile(filename = "Movies/Done/Dancing_Done.mp4", fps = 30)
            
            
            
            await interaction.followup.send(file = File("Movies/Done/Dancing_Done.mp4"))
        
        except:
            
            await interaction.followup.send("An error has ocurred...")
            print(traceback.format_exc)
    
async def setup(bot):
    await bot.add_cog(Movie(bot))
    