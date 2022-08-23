import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from alien import Alien
from ship import Ship
import game_functions as gf


def run_game():
    
    pygame.init()  # initialize game
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
        
    pygame.display.set_caption("Alien Invasion")
    
    #Create an instance to store game stats
    stats = GameStats(ai_settings)
    
    #Make a ship, groups of bullets and aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    #Make an alien
    alien = Alien(ai_settings, screen)
    
    # Make a fleet of Aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
                
        pygame.display.flip() #make screen visible
        
run_game() 