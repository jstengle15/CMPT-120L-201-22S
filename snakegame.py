# import the pygame module, so you can use it
import pygame
import time
from random import randrange

colors = {"white" : pygame.Color(255, 255, 255),
          "red" :  pygame.Color(255, 0, 0),
          "black" :  pygame.Color(0, 0, 0)
         }


# main function creates the window and handles events that 
# happen in game
def main():
    pygame.init()

    # Set window name and window size
    display_intro = pygame.font.SysFont('roboto', 40).render("Welcome to Snake Game!", True, colors["red"])
    pygame.display.set_caption("Snake Game")
    test = pygame.display.set_mode((1024,576))
    test.blit(display_intro, (350,250))
    pygame.display.update()
    time.sleep(2)
    pygame.display.set_caption("Snake Game")
    window = pygame.display.set_mode((1024,576))

    # Initialize snake position 
    snake_position = [350, 250]
    new_x_position = 0
    new_y_position = 0

    # Initialize the clock
    clock = pygame.time.Clock()
    
    # Set running equal to true
    running = True

    # Spawn in food
    food_x_coordinate = round(randrange(0, 1024 - 15) / 10.0) * 10.0
    food_y_coordinate = round(randrange(0, 576 - 15) / 10.0) * 10.0
    
     
    while running:
        for event in pygame.event.get():
            # brainstorming events here
            # if event.type == get food: increase length of snake by 1
            # if event.type == snake collision with itself end game
            if event.type == pygame.QUIT:
                running = False
            # Get user input and move snake in according direction
            # Need position = 0 values so that snake won't move diagonally 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_x_position = -10
                    new_y_position = 0
                elif event.key == pygame.K_RIGHT:
                    new_x_position = 10
                    new_y_position = 0
                elif event.key == pygame.K_UP:
                    new_y_position = -10
                    new_x_position = 0
                elif event.key == pygame.K_DOWN:
                    new_y_position = 10
                    new_x_position = 0
        
        # Check if player hits the edges of the screen, if so display message: you lose!
        display_loss_screen = pygame.font.SysFont('roboto', 40).render("You lose!", True, colors["red"])
        if snake_position[0] < 0 or snake_position[0] > 1024:
            window.blit(display_loss_screen, (350, 250))
            pygame.display.update()
            time.sleep(3)
            running = False
        if snake_position[1] < 0 or snake_position[1] > 576:
            window.blit(display_loss_screen, (350, 250))
            pygame.display.update()
            time.sleep(3)
            running = False

        # Fill color after each new position as to not leave trailing rectangles
        window.fill(colors["white"])

        # Continuously update the position of the head of the snake
        snake_position[1] += new_y_position
        snake_position[0] += new_x_position 
        # Draw snake position
        pygame.draw.rect(window, colors["red"], [snake_position[0], snake_position[1], 15, 15])
        # Draw food position
        pygame.draw.rect(window, colors["black"], [food_x_coordinate, food_y_coordinate, 10, 10])
        # if player position is the same as food position
        if snake_position[0] == food_x_coordinate and snake_position[1] == food_y_coordinate:
            # Spawn new food
            food_x_coordinate = round(randrange(0, 1024 - 10) / 10.0) * 10.0
            food_y_coordinate = round(randrange(0, 576 - 10) / 10.0) * 10.0
            
        # Start of logic for score display
        display_score = pygame.font.SysFont('roboto', 40).render('Score : ' + '1000', True, colors["red"])
        window.blit(display_score, (0,0))

        pygame.display.update()
        clock.tick(20)
     
main()

