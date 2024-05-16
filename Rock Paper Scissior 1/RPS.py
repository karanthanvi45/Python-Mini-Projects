import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define options for rock, paper, scissors (text and images)
options = {
    "rock": {"text": "Rock", "image": "/home/karan/Downloads/Rock.jpeg"},
    "paper": {"text": "Paper", "image": "/home/karan/Downloads/Paper.jpeg"},
    "scissors": {"text": "Scissors", "image": "/home/karan/Downloads/Scissor.jpeg"},
}

# Initialize Pygame
pygame.init()

# Set the screen size
width = 1020
height = 1000
screen = pygame.display.set_mode((width, height))

# Set the window title
pygame.display.set_caption("Rock Paper Scissors")

# Load images for options
def load_image(name):
    image = pygame.image.load(name)
    image = pygame.transform.scale(image, (100, 100))  # Scale images to a manageable size
    return image.convert_alpha()

images = {key: load_image(options[key]["image"]) for key in options.keys()}

# Font for displaying text
font = pygame.font.Font(None, 36)

# Function to display text on screen
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to display an option (text and image)
def display_option(option, x, y):
    draw_text(options[option]["text"], BLACK, x + 50, y - 40)
    screen.blit(images[option], (x, y))

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You Win!"
    else:
        return "You Lose!"

# Game loop
running = True
player_choice = None
computer_choice = None
result = None

while running:
    screen.fill(WHITE)  # Clear the screen

    # Display options
    display_option("rock", width // 3 - 50, height // 2)
    display_option("paper", width // 2 - 50, height // 2)
    display_option("scissors", width // 3 * 2 - 50, height // 2)

    # Display result and choices
    if result:
        draw_text(f"Result: {result}", RED, width // 2 - 100, height // 2 -100)
        draw_text(f"Your choice: {player_choice}", BLACK, width // 4, height // 3)
        draw_text(f"Computer's choice: {computer_choice}", BLACK, width // 4, height // 4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # Define regions for clicking images
            rock_rect = images["rock"].get_rect(topleft=(width // 3 - 50, height // 2))
            paper_rect = images["paper"].get_rect(topleft=(width // 2 - 50, height // 2))
            scissors_rect = images["scissors"].get_rect(topleft=(width // 3 * 2 - 50, height // 2))

            if rock_rect.collidepoint(mouse_x, mouse_y):
                player_choice = "rock"
            elif paper_rect.collidepoint(mouse_x, mouse_y):
                player_choice = "paper"
            elif scissors_rect.collidepoint(mouse_x, mouse_y):
                player_choice = "scissors"

            if player_choice:
                computer_choice = random.choice(list(options.keys()))
                result = determine_winner(player_choice, computer_choice)

    pygame.display.flip()  # Update the display

pygame.quit()
