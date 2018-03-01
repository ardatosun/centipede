import pygame,random

class Explode(pygame.sprite.Sprite):
    gifDelay=0
    gifCounter=0
    gif=[]
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.imgSize=(20,20)
        self.image=pygame.image.load("expo1.png")
        self.gif.append(pygame.image.load("expo1.png"))
        self.gif.append(pygame.image.load("expo2.png"))
        self.gif.append(pygame.image.load("expo3.png"))
        self.gif.append(pygame.image.load("expo4.png"))
        self.gif.append(pygame.image.load("expo5.png"))
        self.gif.append(pygame.image.load("expo6.png"))
        self.gif.append(pygame.image.load("expo5.png"))
        self.gif.append(pygame.image.load("expo4.png"))
        self.gif.append(pygame.image.load("expo3.png"))
        self.gif.append(pygame.image.load("expo2.png"))
        self.gif.append(pygame.image.load("expo1.png"))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        for i in range(11):
            self.gif[i].set_colorkey((0,0,0))
    def update(self):
        #Gif
        self.gifDelay+=1
        if(self.gifDelay%1==0):
            self.image=self.gif[self.gifCounter]
            self.gifCounter+=1
            self.gifDelay=0
            if self.gifCounter==11:
                self.kill()
