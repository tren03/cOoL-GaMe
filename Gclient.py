import pygame

width = 500
height = 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("client")

clientNumber = 0

class Player():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (self.x,self.y,self.width,self.height)
        self.vel = 0.3 # how much to move when we press arrow keys


    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)

    def move(self):
        keys = pygame.key.get_pressed() # returns dict of all of keys with 0 and 1 to see which key is pressed
        if keys[pygame.K_LEFT]:
            self.x-=self.vel


        if keys[pygame.K_RIGHT]:
            self.x+=self.vel

        if keys[pygame.K_UP]:
            self.y-=self.vel

        if keys[pygame.K_DOWN]:
            self.y+=self.vel

        if(self.x < 0):
            self.x=0

        if(self.y < 0):
            self.y=0

        if(self.x > width-self.width):
            self.x=400

        if(self.y > height-self.height):
            self.y=400
        
        self.rect = (self.x,self.y,self.width,self.height)


def redrawWindow(win,player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()


def main():
    p = Player(50,50,100,100,(255,0,0))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win,p)


main()