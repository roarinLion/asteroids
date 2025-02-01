import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    """
    Initialize Pygame and print a starting message for the game.
    This function sets up the necessary initializations for Pygame modules and
    outputs a single message to the console, indicating the start of the game.
    """
    # Initialize all imported Pygame modules
    pygame.init()

    # Print the starting message
    print("Starting asteroids!")
    print("Screen Width:", SCREEN_WIDTH)
    print("Screen Height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
