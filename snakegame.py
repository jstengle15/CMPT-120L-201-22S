# import the pygame module, so you can use it
import pygame
 
# main function creates the window and handles events that 
# happen in game
colors = {"white" : pygame.Color(255, 255, 255),
          "red" :  pygame.Color(255, 0, 0)}

def main():
    pygame.init()

    # Set window name and window size
    pygame.display.set_caption("Snake Game")
    window = pygame.display.set_mode((1280,960))
    window.fill(colors["white"])
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
            # initialize the head of the snake
            pygame.draw.rect(window,colors["red"],[200,150,10,10])
            pygame.display.update()
    
     
if __name__=="__main__":
    main()
    
