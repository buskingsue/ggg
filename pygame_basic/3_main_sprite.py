import pygame

pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")

background = pygame.image.load("C:/Users/a/desktop/code/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/a/desktop/code/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width /2)
character_y_pos = screen_height - character_height

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0,0)) #배경 그리기
    
    screen.blit(character, (character_x_pos, character_y_pos))
   
    pygame.display.update() #게임 화면을 다시 그리기
# pygame 종료
pygame.quit()