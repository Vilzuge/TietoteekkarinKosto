import pygame
import time
import sys
pygame.init()

win = pygame.display.set_mode((800,500))
pygame.display.set_caption("Tietoteekkari Go!")

walkRight = pygame.image.load('R1.png')
walkLeft = pygame.image.load('L1.png')
bg = pygame.image.load('bg.png')
char = pygame.image.load('standing.png')
charup = pygame.image.load('standingback.png')
dodge = pygame.image.load('standing.png')

class bullet(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.standing = False
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
    
    def draw(self, win):
        

        if self.right:
            win.blit(dodge,(self.x,self.y))
        elif self.left:
            win.blit(dodge,(self.x,self.y))
        elif self.up:
            win.blit(dodge,(self.x,self.y))
        elif self.down:
            win.blit(dodge,(self.x,self.y))
        else:
            win.blit(dodge,(self.x,self.y))

#for i in range (225):
 #   win.fill((0,0,0))
  #  image = pygame.image.load("start.png")
   # image = image.convert()
    #image.set_alpha(i)
    #logoimage = win.blit(image,(0,0))
    #pygame.display.flip()
    
x = 200
y = 250
width = 32
height = 64
vel = 2
raja1 = -18
raja2 = 782
raja3 = -40
raja4 = 460
eventid = 0
nopeus = 0
kypara = 0
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
screenid = "00"
text1 = pygame.image.load("text1.png")
text2 = pygame.image.load("text22.png")

left = False
right = False
up = False
down = False

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg,color,cord):
    screen_text = font.render(msg, True, color)
    win.blit(screen_text,(cord))

def redrawGameWindow():


    win.blit(bg, (0,0))


    if x > 0 and x < 300 and eventid == 0 and screenid == "00":
        win.blit(text1,(250,420))
    if x > 300 and x < 780 and eventid == 0 and screenid == "00":
        win.blit(text2,(250,420))
    if screenid == "66":
        win.blit(dodge,(50,nopeus-30))
        win.blit(dodge,(150,nopeus-10))
        win.blit(dodge,(100,nopeus-30))
        win.blit(dodge,(200,nopeus))
        win.blit(dodge,(300,nopeus-30))
        win.blit(dodge,(250,nopeus-10))
        win.blit(dodge,(350,nopeus-30))

    if right:
        win.blit(walkRight,(x,y))
    elif left:
        win.blit(walkLeft,(x,y))
    elif up:
        win.blit(charup,(x,y))
    elif down:
        win.blit(char,(x,y))


    pygame.display.update()


run = True
while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= raja1:
        x -= vel
        left = True
        right = False
        up = False
        down = False       
    if keys[pygame.K_RIGHT] and x <= raja2:
        x += vel
        left = False
        right = True
        up = False
        down = False
    if keys[pygame.K_UP] and y >= raja3:
        y -= vel
        left = False
        right = False
        up = True
        down = False
    if keys[pygame.K_DOWN] and y <= raja4:
        y += vel
        left = False
        right = False
        up = False
        down = True


    if x > 780 and y > 150 and y < 220 and screenid == "00":
        bg = pygame.image.load('bg2.png')
        x = -16
        eventid = 1
        screenid = "10"
   
    elif x < -17 and screenid == "10":
        bg = pygame.image.load('bg.png')
        x = 779
        screenid = "00"

    elif y > 459 and x > 700 and screenid == "10":
        bg = pygame.image.load('bg3.png')
        y = -39
        screenid = "11"
    
    elif y < -40 and screenid == "11":
        bg = pygame.image.load('bg2.png')
        y = 458
        screenid = "10"
    
    if x > 100 and x < 200 and y < 200 and y > 100 and screenid == "00":
        char = pygame.image.load('standing - Copy.png')
        kypara = 1
    if screenid =="11":
        kypara = 0
    if x > 300 and x < 350 and y < 100 and y > 50 and screenid == "10":
        screenid = "66"
        win = pygame.display.set_mode((400,400))
        pygame.display.set_caption("Minigame!")
        pygame.draw.rect(win,(0,0,255),(0,300,400,100),0)
        time.sleep(2)
        message_to_screen("......",green,(150,300))
        pygame.display.update()
        time.sleep(3)
        x = 200
        y = 350
        walkRight = pygame.image.load('standing.png')
        walkLeft = pygame.image.load('standing.png')
        char = pygame.image.load('standing.png')
        charup = pygame.image.load('standing.png')
        bg = pygame.image.load('bgmini.png')
        raja1 = 0
        raja2 = 400 - width
        raja3 = 0
        raja4 = 400 - height
    if screenid == "66":
        nopeus = nopeus + 1
        if nopeus > 500:
            pygame.draw.rect(win,(0,0,255),(0,300,400,100),0)
            pygame.display.update()
            message_to_screen("U dead",red,(150,220))
            pygame.display.update()
            time.sleep(5)
            win = pygame.display.set_mode((800,500))
            pygame.display.set_caption("Tietoteekkari Go!")
            walkRight = pygame.image.load('R1.png')
            walkLeft = pygame.image.load('L1.png')
            bg = pygame.image.load('bg2.png')
            char = pygame.image.load('standing.png')
            charup = pygame.image.load('standingback.png')
            dodge = pygame.image.load('standing.png')
            x = 300
            y = 200
            width = 32
            height = 64
            vel = 2
            raja1 = -18
            raja2 = 782
            raja3 = -40
            raja4 = 460
            eventid = 0
            nopeus = 0
            screenid = "10"
            continue

        
        
        
    
    if x > 700 and kypara == 0 and screenid == "10":
        message_to_screen("Kuolit, ei varmaan kannattais kävellä autotielle",(255,10,0),(220,180))
        pygame.display.update()
        time.sleep(5)
        break
        
        sys.exit(0)
    if x > 700 and kypara == 1 and eventid == 1 and screenid == "10":
        message_to_screen("Ai sulla on kypärä ei siinä sit mitää",(green),(220,180))
        pygame.display.update()
        time.sleep(2)
        eventid = 2
        
        
    
    
    redrawGameWindow()

    

pygame.quit()