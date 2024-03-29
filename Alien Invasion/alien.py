import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class of Alien"""
    
    def __init__(self, ai_settings, screen):
        """Initialize the alien and it starting position"""
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        
        # Load the Alien image and set it rec attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien on top left screen position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the aliens exact position
        self.x = float(self.rect.x)
    
    
    
        
    def blitme(self):
        """Draw the Alien and its current location"""
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        """Return True if alien is at age of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """Move the alien right or left"""
        self.x += ( self.ai_settings.alien_speed_factor *
                    self.ai_settings.fleet_direction )
        self.rect.x = self.x