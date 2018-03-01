import pygame, math, random
class Spider(pygame.sprite.Sprite):
    left_right=1
    isActive=0
    gifDelay=0
    gifCounter=0
    gif=[]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgSize=(40,20)
        self.image=pygame.image.load("spider1.png")
        self.gif.append(pygame.image.load("spider1.png"))
        self.gif.append(pygame.image.load("spider2.png"))
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        self.rect=self.image.get_rect()
        self.rect.y=700
        self.time=0
        for i in range(2):
            self.gif[i].set_colorkey((0,0,0))
        startpos = random.randint(1,2)
        #self.left_right=startpos
        if startpos == 1:
            self.rect.x=-40
            self.left_right=1
        else:
            self.left_right=0
            self.rect.x = 600
    def update(self):
        if(self.isActive):
            if(self.gifDelay%8==0):
                self.image=self.gif[self.gifCounter]
                self.gifCounter+=1
                self.gifDelay=0
                if self.gifCounter==2:
                    self.gifCounter=0
            if self.time == 0:
                self.time = random.randint(5,10)
                self.direction = random.randint(1,4)
            #diagonal down
            if self.direction == 1:
                if self.left_right == 1:
                    self.rect.x = self.rect.x + 10
                else:
                    self.rect.x = self.rect.x-10
                self.rect.y = self.rect.y+5
            #diagonal up
            if self.direction == 2:
                if self.left_right == 1:
                    self.rect.x = self.rect.x + 10
                else:
                    self.rect.x = self.rect.x-10
                self.rect.y = self.rect.y-5
            #up
            if self.direction == 3:
                self.rect.y = self.rect.y-5
            #down
            if self.direction == 4:
                self.rect.y = self.rect.y+5
            if self.rect.y >= 780:
                if self.direction == 1:
                    self.direction = 2
                else:
                    self.direction =3
            if self.rect.y <= 600:
                if self.direction == 2:
                    self.direction = 1
                else:
                    self.direction = 4
            if self.rect.x<-40 or self.rect.x>600:
                self.deactivate()
            self.time-=1
    def activate(self):
        self.isActive=1
        startpos = random.randint(1,2)
        self.left_right=startpos
        if startpos == 1:
            self.rect.x=-40
            self.left_right=1
        else:
            self.rect.x = 600

    def deactivate(self):
        self.rect.x=-40
        self.isActive=0
    
            
