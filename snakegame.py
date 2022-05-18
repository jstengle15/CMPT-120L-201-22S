import pygame
import time
from random import randrange

colors = {"white" : pygame.Color(255, 255, 255),
          "red" :  pygame.Color(255, 0, 0),
          "black" :  pygame.Color(0, 0, 0)
         }


def get_new_snake_position(current_position, new_y_position, new_x_position):
    current_position[1] += new_y_position
    current_position[0] += new_x_position 
    return current_position

def display_intro_screen():
    display_intro = pygame.font.SysFont('roboto', 40).render("Welcome to Snake Game!", True, colors["red"])
    pygame.display.set_caption("Snake Game")
    intro_screen = pygame.display.set_mode((1024,576))
    intro_screen.blit(display_intro, (350,250))
    pygame.display.update()
    time.sleep(2)

def display_loss_screen(window, current_position):
    display_loss_screen = pygame.font.SysFont('roboto', 40).render("You lose!", True, colors["red"])
    window.blit(display_loss_screen, (450, 250))
    pygame.display.update()
    time.sleep(3)
    running = False
    return running 

def display_score(window, score):
    display_score = pygame.font.SysFont('roboto', 40).render('Score : ' + str(score), True, colors["red"])
    window.blit(display_score, (0,0))

def spawn_food():
    food_x_coordinate = round(randrange(0, 1024 - 15) / 10.0) * 10.0
    food_y_coordinate = round(randrange(0, 576 - 15) / 10.0) * 10.0
    return food_x_coordinate, food_y_coordinate

def initialize_snake_body(current_position, snake_body):
    snake_head = []
    snake_head.append(current_position[0])
    snake_head.append(current_position[1])
    snake_body.append(snake_head)
    return snake_head

def build_snake(window, snake_list):
    for rect in snake_list:
        pygame.draw.rect(window, colors["red"], [rect[0], rect[1], 15, 15])

# Main function creates the window and handles events that happen in game
def main():
    pygame.init()

    # Display intro window
    display_intro_screen()

    # Set window name and window size
    pygame.display.set_caption("Snake Game")
    window = pygame.display.set_mode((1024,576))

    # Initialize snake position 
    snake_position = [350, 250]
    new_x_position = 0
    new_y_position = 0

    # Initialize the clock
    clock = pygame.time.Clock()

    # Initialize score
    score = 0
    
    # Set running equal to true
    running = True

    # Spawn in food 
    food_x_coordinate, food_y_coordinate = spawn_food()

    # Initialize snake body list and length
    snake_body = []
    snake_length = 1

    while running:
        for event in pygame.event.get():
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
        
        # Continuously update the position of the head of the snake
        current_position = get_new_snake_position(snake_position, new_y_position, new_x_position)

        # Keep track of the snake's head/body
        snake_head = initialize_snake_body(current_position, snake_body)

        # Check if player hits the edges of the screen, if so display message: you lose!
        if current_position[0] < 0 or current_position[0] > 1024:
            running = display_loss_screen(window)
        if current_position[1] < 0 or current_position[1] > 576:
            running = display_loss_screen(window)

        # Fill color after each new position as to not leave trailing rectangles
        window.fill(colors["white"])
        
        # Draw snake position
        pygame.draw.rect(window, colors["red"], [current_position[0], current_position[1], 15, 15])
        
        # Draw food position
        pygame.draw.rect(window, colors["black"], [food_x_coordinate, food_y_coordinate, 10, 10])
        
        # If player position is the same as food position spawn new food
        if current_position[0] == food_x_coordinate and current_position[1] == food_y_coordinate:
            score += 1
            food_x_coordinate, food_y_coordinate = spawn_food()
            snake_length += 1

       

        # Upon initialization of game snake gets a body length of two
        # Since it's head is in the same position of it's body the game will exit
        # This is needed to prevent the game from not starting
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Draw the snakes body
        build_snake(window, snake_body)
 
        # If head of snake touches the snakes body end the game
        for rect in snake_body[:-1]:
            if rect == snake_head:
                running = False

        
            
        # Start of logic for score display
        display_score(window, score)

        # Update the display
        pygame.display.update()
        
        # Sets FPS to 20 
        clock.tick(20)
     
main()

