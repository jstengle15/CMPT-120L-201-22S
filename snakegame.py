# import the pygame module, so you can use it
from turtle import left
import pygame

colors = {"white" : pygame.Color(255, 255, 255),
          "red" :  pygame.Color(255, 0, 0)}


# main function creates the window and handles events that 
# happen in game
def main():
    pygame.init()

    # Set window name and window size
    pygame.display.set_caption("Snake Game")
    window = pygame.display.set_mode((1280,960))
    
    # Initialize snake position 
    snake_position = [300, 300]
    new_x_position = 0
    new_y_position = 0

    # Initialize the clock
    clock = pygame.time.Clock()
    
    # Set running equal to true
    running = True
     
    while running:
        for event in pygame.event.get():
            # brainstorming events here
            # For each event losing event, set running to false
            # if event.type == keyboard press: move snake accordingly
            # if event.type == get food: increase length of snake by 1
            # if event.type == snake collision with wall, end game
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
        
        # Check if player hits the edges of the screen, if so they lose
        if snake_position[0] < 0 or snake_position[0] > 1280:
            running = False
        if snake_position[1] < 0 or snake_position[1] > 960:
            running = False


        # Fill color after each new position as to not leave trailing rectangles
        window.fill(colors["white"])

        # Continuously update the position of the head of the snake
        snake_position[1] += new_y_position
        snake_position[0] += new_x_position 
        pygame.draw.rect(window, colors["red"], [snake_position[0], snake_position[1], 10, 10])

        # Start of logic for score display
        display_score = pygame.font.SysFont('roboto', 40).render('Score : ' + '1000', True, colors["red"])
        window.blit(display_score, (0,0))

        pygame.display.update()
        clock.tick(40)
     
main()

