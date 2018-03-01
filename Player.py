import pygame

class Player(pygame.sprite.Sprite):
    gif=[]
    gifDelay=0
    gifCounter=0
    def __init__(self,X,Y):
        pygame.sprite.Sprite.__init__(self)
        self.imgSize=(20,20)
        self.image=pygame.image.load("player1.png")
        self.gif.append(pygame.image.load("player1.png"))
        self.gif.append(pygame.image.load("player2.png"))
        self.gif.append(pygame.image.load("player3.png"))
        self.gif.append(pygame.image.load("player4.png"))
        self.gif.append(pygame.image.load("player5.png"))
        self.gif.append(pygame.image.load("player6.png"))
        for i in range(6):
            self.gif[i].set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.x=X
        self.rect.y=Y
        
    def update(self,keys):
        self.gifDelay+=1
        if(self.gifDelay%4==0):
            self.image=self.gif[self.gifCounter]
            self.gifCounter+=1
            self.gifDelay=0
            if self.gifCounter==6:
                self.gifCounter=0
        if keys[pygame.K_UP]:
            if self.rect.y<=600:
                self.rect.y=600
            else:
                self.rect.y-=20
        if keys[pygame.K_DOWN]:
            if self.rect.y>=780:
                self.rect.y=780
            else:
                self.rect.y+=20
        if keys[pygame.K_LEFT]:
            if self.rect.x<=0:
                self.rect.x=0
            else:
                self.rect.x-=20
        if keys[pygame.K_RIGHT]:
            if self.rect.x>=580:
                self.rect.x=580
            else:
                self.rect.x+=20
    
