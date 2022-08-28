import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from alien import Alien
from ship import Ship
import game_functions as gf


def run_game():
    
    pygame.init()  # initialize game
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
        
    pygame.display.set_caption("Alien Invasion")
    
    #Make the Play button
    play_button = Button(ai_settings, screen, "Play")
    
    
    #Create an instance to store game stats and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
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
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
        #Make screen visible        
        pygame.display.flip() 
        
run_game() 