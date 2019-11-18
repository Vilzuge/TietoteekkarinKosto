import pygame
pygame.init()

win = pygame.display.set_mode((800,500))
pygame.display.set_caption("Tietoteekkari Go!")

walkRight = pygame.image.load('R1.png')
walkLeft = pygame.image.load('L1.png')
bg = pygame.image.load('bg.png')
char = pygame.image.load('standing.png')
charup = pygame.image.load('standingback.png')
screenid = "00"
raja1 = -18
raja2 = 782
raja3 = -40
raja4 = 460
text1 = pygame.image.load("text1.png")
text2 = pygame.image.load("text2.png")

class player(object):
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
            win.blit(walkRight,(self.x,self.y))
        elif self.left:
            win.blit(walkLeft,(self.x,self.y))
        elif self.up:
            win.blit(charup,(self.x,self.y))
        elif self.down:
            win.blit(char,(self.x,self.y))
        else:
            win.blit(char,(self.x,self.y))
        
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    if x > 0 and x < 300  and screenid == "00":
        win.blit(text1,(250,420))
    if x > 300 and x < 780 and screenid == "00":
        win.blit(text2,(250,420))
    
    pygame.display.update()    

#mainloop
man = player(250, 250, 64,64)
#for i in range (225):
 #   win.fill((0,0,0))
  #  image = pygame.image.load("start.png")
   # image = image.convert()
    #image.set_alpha(i)
    #logoimage = win.blit(image,(0,0))
    #pygame.display.flip()

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x >= raja1:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
        man.up = False
        man.down = False
    elif keys[pygame.K_RIGHT] and man.x <= raja2:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
        man.up = False
        man.down = False
    elif keys[pygame.K_UP] and man.y >= raja3:
        man.y -= man.vel
        man.right = False
        man.left = False
        man.standing = False
        man.up = True
        man.down = False
    elif keys[pygame.K_DOWN] and man.y <= raja4:
        man.y += man.vel
        man.right = False
        man.left = False
        man.standing = False
        man.up = False
        man.down = True
    else:
        man.standing = True
    
    #Skenen vaihdot
    if man.x > 780 and man.y > 200-man.height and man.y < 400+man.height and screenid == "00":
        bg = pygame.image.load('bg2.png')
        man.x = -16
        screenid = "10"  
    elif man.x < -17 and man.y > 200-man.height and man.y < 400+man.height and screenid == "10":
        bg = pygame.image.load('bg.png')
        man.x = 779
        screenid = "00"
    elif man.y > 459 and screenid == "10":
        bg = pygame.image.load('bg3.png')
        man.y = -39
        screenid = "11"   
    elif man.y < -40 and screenid == "11":
        bg = pygame.image.load('bg2.png')
        man.y = 458
        screenid = "10"



    if man.x > 400 and screenid == "10":
        win = pygame.display.set_mode((400,400))
        pygame.display.set_caption("Thot Patrol!")
        man = player(200,200,32,32)
        walkRight = pygame.image.load('standing.png')
        walkLeft = pygame.image.load('standing.png')
        char = pygame.image.load('standing.png')
        charup = pygame.image.load('standing.png')
        bg = pygame.image.load('bgmini.png')
        raja1 = 0
        raja2 = 400 - man.width
        raja3 = 0
        raja4 = 400 - man.height

    redrawGameWindow()

pygame.quit()




