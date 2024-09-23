import cv2
import time
import pygame

# Inicializar el módulo de música de pygame
pygame.mixer.init()

# Cargar la música
music_path = './Temon.mp3'
pygame.mixer.music.load(music_path)

# Iniciar la reproducción de la música en bucle
pygame.mixer.music.play(-1)  # El argumento -1 significa que la música se repetirá infinitamente

# Cargar la imagen usando OpenCV
image_path = './Diseno.png'
image = cv2.imread(image_path)

# Verificar si la imagen se cargó correctamente
# fix by https://github.com/syltr1x
if image is None:
    print(f"Error: No se pudo cargar la imagen en {image_path}")
else:
    while True:
        # Mostrar la imagen en una ventana llamada 'Ventana de Imagen'
        cv2.imshow('Skibidi sigma pomny', image)

        # Esperar 1 segundo entre cada iteración
        time.sleep(1)

        # Presionar la tecla 'q' para salir del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Detener la música al salir del bucle
pygame.mixer.music.stop()

# Cerrar la ventana al salir del bucle
cv2.destroyAllWindows()
# :)