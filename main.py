# Date: 9/31/24
# Name: Gravity Balls (Python)
# Author: Andrea B.
# Contact: baciuandrea04@gmail.com
# Description: This was a visual game I made while learning how to use pygame import
import pygame

# Screen dimensions
width = 1000
height = 700
background_color = (65, 23, 62)

class GravityBall:
    def __init__(self, x, y):
        original_image = pygame.image.load("gravity_ball.png")
        self.image = pygame.transform.scale(original_image, (150, 150))  # Resize image to make smaller balls
        self.speed = [0,1] # variable to make the ball move at a certain speed after initializing display
        self.rect = self.image.get_rect(center = (x,y)) # surface that displays png file
    # function to update command
    def update(self):
        self.movement() #intializes the 'movement' function
    #function to move the ball according to the speed
    def movement(self):
         self.rect = self.rect.move(self.speed)   

# function for the intro screen before game begins
def intro_screen(screen):
     # Font of text
     intro_text_color = (233, 114, 223)  # Pink color for text
     hover_text_color = (255, 255, 255)  # White color for hover effect for the button
     heading_font = pygame.font.Font(None, 100) #Title size
     subheading_font = pygame.font.Font(None, 70) #description size
     button_font = pygame.font.Font(None, 60) #button size
     
     # Text input
     text_surface = heading_font.render("Welcome to Gravity Balls", True, intro_text_color)
     subtext_surface = subheading_font.render("Ready to play?", True, intro_text_color)
     button_surface = button_font.render("Start Game", True, intro_text_color)

     button_rect = button_surface.get_rect(center = (width // 2, height // 2 + 90)) #Centers button

    # to recognize when user clicks screen
     while True:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 return
             if event.type == pygame.MOUSEBUTTONDOWN:
                 #checks if button clicked
                 if button_rect.collidepoint(event.pos):
                    return
                    
         # Creates Display for background
         screen.fill(background_color)
         # Creates pink to white animation when user hovers over button
         cursor_pos = pygame.mouse.get_pos()
         if button_rect.collidepoint(cursor_pos):
             button_surface = button_font.render("START GAME", True, hover_text_color)
         else:
             button_surface = button_font.render("START GAME", True, intro_text_color)
         # Creates Display for text and button
         screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 2 - 150))
         screen.blit(subtext_surface, (width // 2 - subtext_surface.get_width() // 2, height // 2 - 50))
         screen.blit(button_surface, button_rect)
         pygame.display.flip()


def main():
    pygame.init() #initiates game library
    screen = pygame.display.set_mode((width,height)) #sets image of display to output
    fps = pygame.time.Clock() #creates timer when frame animation occurs
    balls = []
    
    # initiates intro screen before game starts
    intro_screen(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 'QUIT' function to stop the game if user exits out
                pygame.quit()
                return
            # checks for cursor clicking events, and when user clicks, creates new ball
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos # postion where user clicks
                new_ball = GravityBall(x, y) # creates new ball at position user clicks
                balls.append(new_ball) #creates new ball result after user input
        screen.fill(background_color) # clear screen  

        # update and draws multiple balls
        for ball in balls:
            ball.update()
            screen.blit(ball.image, ball.rect) #command to display ball into set background

        #add movement and speed aspects (ouside of for loop above to prevent flickering)
        pygame.display.flip() #updating screen
        fps.tick(120) #120 fps (frames per seconds)

if __name__=="__main__": # initiates the main program to run
    main()


        
