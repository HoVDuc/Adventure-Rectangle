import pygame
from math import sin


class Entity(pygame.sprite.Sprite):
    
    def __init__(self, groups):
        super().__init__(groups)
        self.direction = pygame.math.Vector2()
        self.finished = False
        
    def move(self, speed, flag):
        if flag:
            if self.direction.magnitude() != 0:  # Trả về độ lớn Euclid của vector
                self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacles_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacles_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom 
                    if sprite.sprite_type == 'finish_line':
                        self.finished = True
    
    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        return 255 if value >= 0 else 0  
        