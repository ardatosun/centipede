import pygame,random

class Bomb(pygame.sprite.Sprite):
    drop=0
    ax=0
    ay=0
    isActive=0
    gifDelay=0
    gifCounter=0
    gif=[]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgSize=(20,20)
        self.image=pygame.image.load("bomb1.png")
        self.gif.append(pygame.image.load("bomb1.png"))
        self.gif.append(pygame.image.load("bomb2.png"))
        self.gif.append(pygame.image.load("bomb3.png"))
        self.gif.append(pygame.image.load("bomb4.png"))
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        self.rect=self.image.get_rect()
        self.rect.y=-20
        self.ax=self.rect.x
        self.ay=self.rect.y
        for i in range(4):
            self.gif[i].set_colorkey((0,0,0))
    def update(self):
        if(self.isActive):
            self.gifDelay+=1
            if(self.gifDelay%4==0):
                self.image=self.gif[self.gifCounter]
                self.gifCounter+=1
                self.gifDelay=0
                if self.gifCounter==4:
                    self.gifCounter=0
            rnd=random.randint(1,5)
            if(rnd==1 and self.rect.y%20==0):
                self.drop=1
                self.ax=self.rect.x
                self.ay=self.rect.y
            self.rect.y+=10
            if(self.rect.y>=780):
                self.drop=0
                self.deactivate()
    def activate(self):
        self.isActive=1
        startpos = random.randint(0,29)
        self.rect.x=startpos*20

    def deactivate(self):
        self.rect.y=-40
        self.isActive=0
        
