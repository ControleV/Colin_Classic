# Importar o que é nescessário para editar videoclips
from moviepy.editor import *



# Carregar o vídeo "Dancing" dentro da variável clip
clip = VideoFileClip("Movies/Dancing.mov")



# diminuir o volume do clipe (volume x 0.8)
clip = clip.volumex(0.8)



# Gerar um clipe de texto.
txt_clip = TextClip("Luifoo depois de\nbaitar mais uma partida", fontsize = 50, color='white', stroke_width = 1, stroke_color = 'black')




# Colocar o texto depois de 3 segundos que o clipe iniciou.
txt_clip = txt_clip.set_pos('center').set_duration(3)





# Compor o vídeo com o texto.
video = CompositeVideoClip([clip, txt_clip])





# Escreve o resultado em um arquivo.
video.write_videofile(filename = "Movies/Done/Dancing_Done.mp4", fps = 30)



