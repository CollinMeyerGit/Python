import pygame

WIDTH = 1920
HEIGHT = 1020
WHITE = (255, 255, 255)
    



def startup():
    game_display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PONG")
    clock = pygame.time.Clock()
    return game_display, clock

def createEnvironment(game_display, WHITE):
    game_display.fill((255, 255, 255))
    pygame.display.update()

def main():
    game_display, clock = startup()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            createEnvironment(game_display, (255, 255, 255))
            clock.tick(60)

if __name__ == "__main__":
    main()

