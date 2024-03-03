import pygame


class PhysicsEntity:
    def __init__(self, game, entityType, pos,  size) -> None:
        self.game = game
        self.type = entityType
        self.pos = list(pos) 
        self.size = size
        self.velocity = [0, 0]

        self.collisions = {i : False for i in ["up","down","right","left"]}

        self.terminalVel = 5
        self.gravity = 0.1
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement = (0, 0)):
        self.collisions = {i : False for i in ["up","down","right","left"]}

        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y

        self.velocity[1] = min(self.terminalVel, self.velocity[1] + self.gravity)

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
    
    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)