import os
from moviepy.editor import VideoFileClip

# Ruta del video original
path = "/Users/tiago/Documents/GitHub/HelicopTourSite/assets/imagenes/fondoVideo.mp4"

# Obtener el directorio y el nombre del archivo original
directory, filename = os.path.split(path)
name, ext = os.path.splitext(filename)

# Definir la ruta de salida del video comprimido
output_path = os.path.join(directory, f"{name}_comprimido.mp4")

try:
    # Cargar el video
    clip = VideoFileClip(path)

    # Comprimir el video especificando el códec
    clip.write_videofile(output_path, codec='libx264', bitrate="3000k")
    print(f"Video comprimido guardado en: {output_path}")
except Exception as e:
    print(f"Ocurrió un error durante la compresión: {e}")
