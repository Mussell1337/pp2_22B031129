import pygame


pygame.init()
FPS=pygame.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
sc=pygame.display.set_mode((800, 600))
pygame.display.set_caption("music player")

Playlist=['first.mp3', 'second.mp3', 'third.mp3']
curm=0
curs=pygame.mixer.music.load(Playlist[curm])
pygame.mixer.music.play()
pygame.mixer.music.pause()
m1 = m2 = m3 = False

FONT_SIZE = 32
font = pygame.font.Font(None, FONT_SIZE)

text1 = font.render("tap SPACE to start a song", True, (255, 255, 255))
text2 = font.render("tap K_RIGHT to select next song", True, (255, 255, 255))
text3 = font.render("tap K_LEFT to select previous song", True, (255, 255, 255))

# Get text surface dimensions
text1_width, text1_height = text1.get_size()
text2_width, text2_height = text2.get_size()
text3_width, text3_height = text3.get_size()

# Calculate center coordinates
text1_x = (SCREEN_WIDTH - text1_width) // 2
text1_y = (SCREEN_HEIGHT // 2) - (text1_height + text2_height + text3_height) + 12
text2_x = (SCREEN_WIDTH - text2_width) // 2
text2_y = (SCREEN_HEIGHT // 2) - (text2_height + text3_height) // 2
text3_x = (SCREEN_WIDTH - text3_width) // 2
text3_y = (SCREEN_HEIGHT // 2) + text2_height // 2

# Draw text surfaces onto the screen
screen.blit(text1, (text1_x, text1_y))
screen.blit(text2, (text2_x, text2_y))
screen.blit(text3, (text3_x, text3_y))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if(m1):
                    pygame.mixer.music.pause()
                    m1=0
                else:
                    pygame.mixer.music.unpause()
                    m1=1
            if event.key==pygame.K_RIGHT:
                curm=(curm+1)%3
                pygame.mixer.music.stop()
                pygame.mixer.music.load(Playlist[curm])
                pygame.mixer.music.play()
                m2=True
                if not m1 :
                    pygame.mixer.music.pause()
            if event.key==pygame.K_LEFT:
                curm=(curm-1+3)%3
                pygame.mixer.music.stop()
                pygame.mixer.music.load(Playlist[curm])
                pygame.mixer.music.play()
                m3=True
                if not m1 :
                    pygame.mixer.music.pause()
                   

    pygame.display.update()
    FPS.tick(60)