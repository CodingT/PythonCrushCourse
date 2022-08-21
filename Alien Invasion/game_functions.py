import sys
import pygame
from bullet import Bullet

def check_keyDown_events(event, ai_settings, screen, ship, bullets):
    """Respond to key press"""
    if event.key == pygame.K_RIGHT:
         ship.moving_right = True
    elif event.key == pygame.K_LEFT:
         ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bul9let(ai_settings, screen, ship, bullets)
    elif event.key ==pygame.K_q:
        sys.exit()
    
def fire_bullet(ai_settings, screen,ship, bullets):
    """Fire a bullet if limit not reached yet"""    
    #Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet) 

def check_keyUp_events(event, ship):
    """Respond to key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypress and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keyDown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyUp_events(event, ship)
               
        
def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    #Update bullet position
    bullets.update()       
    
    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  
            
def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen"""
    screen.fill(ai_settings.bg_color) # fill background screen with color
    #Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    
    
