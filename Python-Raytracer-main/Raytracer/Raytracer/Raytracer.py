import pygame
from pygame.locals import *
from rt import Raytracer
from figures import *
from lights import *
from materials import *


width = 512
height = 512

pygame.init()

# Creacion de la pantalla de pygame
screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

# Instanciar el raytracer
raytracer = Raytracer(screen)
raytracer.rtClearColor(0.081, 0.21, 0.25)

# Creacion de materiales
brick = Material(diffuse=(1, 0.4, 0.4))

# Figuras en la escena
raytracer.scene.append(Sphere(position=(0, 0.95, -5), radius=0.3, material=Material(diffuse=(1, 1, 1))))  # Esfera superior
raytracer.scene.append(Sphere(position=(0, 0.3, -5), radius=0.4, material=Material(diffuse=(1, 1, 1))))  # Esfera del medio
raytracer.scene.append(Sphere(position=(0, -0.5, -5), radius=0.5, material=Material(diffuse=(1, 1, 1))))  # Esfera inferior
raytracer.scene.append(Sphere(position=(0, 0.0, -5), radius=0.09, material=Material(diffuse=(0, 0, 0))))  # Botones
raytracer.scene.append(Sphere(position=(0, -0.3, -5), radius=0.09, material=Material(diffuse=(0, 0, 0))))  # Botones
raytracer.scene.append(Sphere(position=(0, 0.3, -5), radius=0.09, material=Material(diffuse=(0, 0, 0))))  # Botones
raytracer.scene.append(Sphere(position=(0.1, 1.05, -5), radius=0.05, material=Material(diffuse=(0, 0, 0))))  # Ojo izquierdo
raytracer.scene.append(Sphere(position=(-0.1, 1.05, -5), radius=0.05, material=Material(diffuse=(0, 0, 0))))  # Ojo derecho
raytracer.scene.append(Sphere(position=(0, 0.95, -5), radius=0.05, material=Material(diffuse=(0.25, 0.25, 0.008))))  # nariz (zanahoria)
raytracer.scene.append(Sphere(position=(0.15, 0.88, -5), radius=0.04, material=Material(diffuse=(0, 0, 0))))  # boca
raytracer.scene.append(Sphere(position=(0.06, 0.83, -5), radius=0.04, material=Material(diffuse=(0, 0, 0))))  # boca
raytracer.scene.append(Sphere(position=(-0.06, 0.83, -5), radius=0.04, material=Material(diffuse=(0, 0, 0))))  # boca
raytracer.scene.append(Sphere(position=(-0.15, 0.88, -5), radius=0.04, material=Material(diffuse=(0, 0, 0))))  # boca

# Luces de la escena
raytracer.lights.append(AmbientLight(intensity=0.1))
raytracer.lights.append(DirectionalLight(direction = (0,-1,-1), intensity = 0.7))


isRunning = True
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                isRunning = False

    raytracer.rtClear()
    raytracer.rtRender()

    pygame.display.flip()

pygame.quit()