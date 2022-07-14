
from moviepy.editor import *


clip1 = VideoFileClip("video.mp4")


w1 = clip1.w
h1 = clip1.h

print("Width x Height do clip 1 : ", end = " ")
print(str(w1) + " x ", str(h1))

print("---------------------------------------")

#reduz resolução do vídeo 
#clip2 = clip1.resize(0.20)

#reduz tamanho do vídeo em quantos segundos vc quiser subclipe(inicio, fim)
clip2 = clip1.subclip(0, 3)

#rotaciona o vídeo
#clip2 = clip1.rotate(180)

#diminui o volume do audio
#clip = clip.volumex(0.5)

w2 = clip2.w
h2 = clip2.h

#clip2 = clip1.cutout(x, y)
print("Width x Height of clip 2 : ", end = " ")
print(str(w2) + " x ", str(h2))

print("---------------------------------------")


clip2.ipython_display(width = 280, height = 320)
