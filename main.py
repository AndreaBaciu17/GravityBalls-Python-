# Date: 9/31/24
# Name: Gravity Balls (Python)
# Author: Andrea B.
# Contact: baciuandrea04@gmail.com
# Description: This was a visual game I made while learning how to use pygame import
import pygame

# Screen dimensions
width = 700
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

def main():
        pygame.init() #initiates game library
        screen = pygame.display.set_mode((width,height)) #sets image of display to output
        fps = pygame.time.Clock() #creates timer when frame animation occurs
        balls = []
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
                #add movement and speed aspects
            pygame.display.flip() #updating screen
            fps.tick(120) #120 fps (frames per seconds)

if __name__=="__main__": #the main program that runs
    main()


        
