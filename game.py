import pygame
from sys import exit
from os import listdir

from scripts.entities import PhysicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import Tilemap


class Game:
    def __init__(self, WIDTH = 640, HEIGHT = 480, CAPTION = "Ninja Game") -> None:
        pygame.init()

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        
        pygame.display.set_caption(CAPTION)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display = pygame.Surface((self.WIDTH/2, self.HEIGHT/2))


        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'player' : load_image("entities/player.png")
        }

        for folder in listdir("data\images\\tiles"):
            self.assets[folder] = load_images("tiles\\" + folder)

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        self.tilemap = Tilemap(self, 16)
    
    def run(self) -> None:
        while True:
            self.display.fill((14,219,248))

            self.tilemap.render(self.display)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))

            pygame.display.update()
            self.clock.tick(60)




if __name__ == "__main__":
    Game(640, 480, "Ninja Game").run()
