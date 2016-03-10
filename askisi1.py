import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
TURQUOISE=(64,224,208)


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 35
HEIGHT = 35
 
# This sets the margin between each cell
MARGIN = 4
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell
 
# Set row 0, cell 0 to one. (Remember rows and
# column numbers start at zero.)
grid[0][0] = 1
grid[5][7] = 2
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [400, 400]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("to paixnidi tou 8isaurou")
 
# Loop until the user clicks the close button.
done = False
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10

# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 25)
 

display_instructions = True
instruction_page = 1

# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 2:
                display_instructions = False
 
    # Set the screen background
    screen.fill(TURQUOISE)
 
    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
 
        text = font.render("To paixnidi tou 8isaurou", True, WHITE)
        screen.blit(text, [10, 10])
 
        text = font.render(" ", True, WHITE)
        screen.blit(text, [10, 40])
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
            # User pressed down on a key

        elif event.type == pygame.KEYDOWN:
         # User clicks the mouse. Get the position
            
            pos = pygame.mouse.get_pos()
            if event.key== pygame.K_LEFT:
                x_speed = -1
            elif  event.key== pygame.K_RIGHT:
                x_speed = 1
            elif  event.key== pygame.K_UP:
                y_speed = -1
            elif event.key== pygame.K_DOWN:
                y_speed = 1
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key== pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[0] // (HEIGHT + MARGIN)
            # Set that location to zero
            grid[row][column] = 1
            print("Grid coordinates: ", row, column)

 # --- Game Logic

    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] ==1:
                color = TURQUOISE
            elif grid[row][column]==2:
                    color=RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
