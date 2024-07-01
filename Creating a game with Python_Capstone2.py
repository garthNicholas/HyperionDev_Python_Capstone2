# In this example.py you will learn how to make a very simple game using the pygame library.
# One of the best ways of learning to program is by writing games.
# Pygame is a collection of modules in one package.
# You will need to install pygame.
# To do so:
# 1) open the command line interface on your computer,
# 2) cd to the directory that this task is located in,
# 3) follow the instructions here: https://www.pygame.org/wiki/GettingStarted
# 4) if you need help using pip, see here: https://projects.raspberrypi.org/en/projects/using-pip-on-windows

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init()

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the the 3 different enemy images + prize Image). 

player = pygame.image.load("Player1.jpg")
enemy = pygame.image.load("Ryu_enemy1.jpg")
enemy2 = pygame.image.load("Ken_enemy2.jpg")
enemy3 = pygame.image.load("Blanka_enemy3.jpg")
prize = pygame.image.load("Prize.jpg")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()

enemy_height = enemy.get_height()
enemy_height2 = enemy2.get_height()
enemy_height3 = enemy3.get_height()

enemy_width = enemy.get_width()
enemy_width2 = enemy2.get_width()
enemy_width3 = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

print("\n This is the height of the player image: " +str(enemy_height))
print("This is the width of the player image: " +str(enemy_width))

print("\n This is the height of the enemy image: " +str(enemy_height))
print("This is the width of the enemy image: " +str(enemy_width))


print("\n This is the height of the enemy2 image: " +str(enemy_height2))
print("This is the width of the enemy2 image: " +str(enemy_width2))


print("\n This is the height of the enemy3 image: " +str(enemy_height3))
print("This is the width of the enemy3 image: " +str(enemy_width3))


print("\n This is the height of the prize image: " +str(prize_height))
print("This is the width of the prize image: " +str(prize_width))


# Store the positions of the player and enemy as variables so that you can change them later. 
# Number allocated to variable must be within screen_width(1040) and screen_height(680) to display on screen during the game

playerXPosition = 100 
playerYPosition = 50 


enemyXPosition = 1100 
enemyYPosition = 400


enemy2XPosition = 900
enemy2YPosition = 500



enemy3XPosition = 800
enemy3YPosition = 400

prizeXPosition = 500
prizeYPosition = 500

# Make the enemy + prize start off screen and at a random y position.

# enemyXPosition =  screen_width
# enemy2XPosition =  screen_width
# enemy3XPosition =  screen_width

# enemyYPosition =  random.randint(0, screen_height - enemy_height)
# enemy2YPosition =  random.randint(0, screen_height - enemy_height2)
# enemy3YPosition =  random.randint(0, screen_height - enemy_height3)

# prizeXPosition =  screen_width
# prizeYPosition =  random.randint(0, screen_height - prize_height)

# This checks if the up, down, left or right key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    
    screen.blit(enemy, (enemyXPosition, enemyYPosition)) # This draws the enemy image to the screen at the postion specfied.
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition)) # This draws the enemy2 image to the screen at the postion specfied.
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition)) # This draws the enemy3 image to the screen at the postion specfied.
    screen.blit(prize, (prizeXPosition, prizeYPosition)) # This draws the prize image to the screen at the postion specfied.
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN: # This should move - player - down the screen
                keyDown = True
            if event.key == pygame.K_LEFT: # This should move - player - left on the screen
                keyLeft = True
            if event.key == pygame.K_RIGHT: # This should move - player - right - on the screen
                keyRight = True
        

        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            # If no directional keys are pressed down - player - should not move on the screen
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
      
        
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyLeft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player too far left of the window.
            playerXPosition -= 1

    if keyRight == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player too far right of the window.
            playerXPosition += 1 


    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition



    enemy2Box = pygame.Rect(enemy.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition



    enemy3Box = pygame.Rect(enemy.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    # Bounding box for the prize:
    
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    

    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)


    if playerBox.colliderect(enemy2Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)


    if playerBox.colliderect(enemy3Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)


        
    # If the enemy is off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width:
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)

    if enemy2XPosition < 0 - enemy_width2:
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)


    if enemy3XPosition < 0 - enemy_width3:
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)


    # If user collides with prizebox the user wins the game:
    
    if playerBox.colliderect(prizeBox):
    
        # Display wining status to the user: 
        
        print("You win!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)
 
    
    # Make enemy approach the player.
    
    enemyXPosition -= 0.15
    enemy2YPosition -= 0.15
    enemy3XPosition -= 0.15
    prizeYPosition -= 0.15
    
    # ================The game loop logic ends here. =============
  
