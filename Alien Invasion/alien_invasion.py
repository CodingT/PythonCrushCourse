import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    
    pygame.init()  # initialize game
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
        
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(ai_settings, screen)  #Make a ship
    #Make a group to store bullets
    bullets = Group()
    
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        
        

                
        pygame.display.flip() #make screen visible
        
run_game() 