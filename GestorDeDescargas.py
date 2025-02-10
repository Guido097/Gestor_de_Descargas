import os
import shutil
import time

# Rutas
DESCARGAS = os.path.expanduser("C:\\Users\\guido\\Downloads")
CARPETAS = {
    "Imágenes": [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"],
    "Documentos": [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"],
    "Audio": [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac", ".aiff", ".alac", ".dsd", ".ogg", ".opus", ".pcm", ".tta", ".wv"],
    "Instaladores": [".exe", ".msi"],
    "Comprimidos": [".zip", ".rar", ".tar.gz"],
}
LOG_FILE = os.path.join(DESCARGAS, "log_movimientos.txt")

def obtener_nombre_unico(ruta_destino, nombre_archivo):
    nombre_base, extension = os.path.splitext(nombre_archivo)
    contador = 1
    nuevo_nombre = nombre_archivo
    while os.path.exists(os.path.join(ruta_destino, nuevo_nombre)):
        nuevo_nombre = f"{nombre_base} ({contador}){extension}"
        contador += 1
    return nuevo_nombre

def registrar_log(mensaje):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {mensaje}\n")

def organizar_descargas():
    for archivo in os.listdir(DESCARGAS):
        ruta_archivo = os.path.join(DESCARGAS, archivo)
        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1].lower()
            for carpeta, extensiones in CARPETAS.items():
                if extension in extensiones:
                    carpeta_destino = os.path.join(DESCARGAS, carpeta)
                    os.makedirs(carpeta_destino, exist_ok=True)
                    nuevo_nombre = obtener_nombre_unico(carpeta_destino, archivo)
                    shutil.move(ruta_archivo, os.path.join(carpeta_destino, nuevo_nombre))
                    mensaje = f"Movido: {archivo} → {carpeta} como {nuevo_nombre}"
                    print(mensaje)
                    registrar_log(mensaje)
                    break

if __name__ == "__main__":
    organizar_descargas()
