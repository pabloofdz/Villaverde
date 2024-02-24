import pygame
import os

from settings import LAYERS

class NPC(pygame.sprite.Sprite):
    def __init__(self, pos, group, sprite_directory, inventory, dialogue, personaje):
        super().__init__(group)
        self.sprite_directory = sprite_directory
        self.dialogue = dialogue
        self.inventory = inventory
        self.personaje = personaje
        self.load_sprites()

        # Configuración inicial
        self.image = self.sprites[0]  # Use the first sprite as the initial image
        self.rect = self.image.get_rect(center=pos)
        self.z = LAYERS['main']

        # Animation variables
        self.current_frame = 0
        self.animation_delay = 40
        self.animation_counter = 0

        self.dialogo_abierto = False

    def load_sprites(self):
        self.sprites = []
        for filename in sorted(os.listdir(self.sprite_directory)):
            path = os.path.join(self.sprite_directory, filename)
            self.sprites.append(pygame.image.load(path).convert_alpha())

    def update_animation(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.sprites)
            self.image = self.sprites[self.current_frame]

    def talk(self, dialogue, inventory, personaje):
            if personaje == "don diego":
                dialogue.set_opcion_dialogo(True)
                dialogue.dibujar_dialogo(inventory, "don diego")
            elif personaje == "butanero":
                
                dialogue.set_opcion_dialogo(True)
                dialogue.dibujar_dialogo(inventory, "butanero")
                if inventory.get_dinero():
                    dialogue.set_opcion_escogida(True)
                else:
                    dialogue.set_opcion_escogida(True)
                    
    def update(self, dt):
        self.update_animation()
