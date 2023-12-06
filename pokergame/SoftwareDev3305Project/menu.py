import pygame
import hello

pygame.init()
WIDTH, HEIGHT = 900, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Poker")
clock = pygame.time.Clock()
FPS = 30


def text(msg, size, color):
    font = pygame.font.Font('assets/gluegun.ttf', size)
    newText = font.render(msg, True, color)

    return newText


def menu():
    run = True
    select = "start"
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    select = "start"
                elif event.key == pygame.K_DOWN:
                    select = "quit"
                if event.key == pygame.K_RETURN:
                    if select == "start":
                        hello.main()
                    if select == "quit":
                        pygame.quit()
                        quit()
        # menu UI
        window.fill((0, 155, 0))
        title = text("Poker", 90, (255, 255, 255))
        if select == "start":
            text_start = text("START", 50, (255, 255, 255))
        else:
            text_start = text("START", 50, (0, 0, 0))
        if select == "quit":
            text_quit = text("QUIT", 50, (255, 255, 255))
        else:
            text_quit = text("QUIT", 50, (0, 0, 0))

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # menu text
        window.blit(title, (WIDTH / 2 - (title_rect[2] / 2), 80))
        window.blit(text_start, (WIDTH / 2 - (start_rect[2] / 2), 300))
        window.blit(text_quit, (WIDTH / 2 - (quit_rect[2] / 2), 360))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    menu()
