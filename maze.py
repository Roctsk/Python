from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed =player_speed
        self.rect =self.image.get_rect()
        self.rect.x =player_x  
        self.rect.y =player_y 

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -=self.speed
        if keys[K_RIGHT] and self.rect.x <(win_widht - 80):
            self.rect.x +=self.speed
        if keys[K_UP] and self.rect.y > 5 :
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y <(win_height - 80):
            self.rect.y +=self.speed

class Enemy(GameSprite):
    direction = 'left'

    def update(self): 
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= (win_widht - 85):
            self.direction = 'left'
        
        if self.direction =='left':
            self.rect.x -=self.speed
        else:
            self.rect.x +=self.speed
class Wall(sprite.Sprite):
    def __init__(self,color1,color2,color3,wall_x,wall_y,wall_wight,wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.wight= wall_wight
        self.height = wall_height
        self.image = Surface((self.wight,self.height))
        self.image.fill((self.color1,self.color2,self.color2))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


win_widht = 700
win_height= 500
window = display.set_mode((win_widht,win_height))
display.set_caption("MAZE")
background =transform.scale(image.load("background.jpg"),(win_widht,win_height))

wall1 = Wall(154, 205, 50, 100, 20, 450, 10)
wall2 = Wall(154, 205, 50, 100, 480, 360, 10)
wall3 = Wall(154, 205, 50, 100, 20, 10, 380)
wall4 = Wall(154, 205, 50,450,200,10,300)
wall5 = Wall(154, 205, 50,210,20,10,300)
wall6 = Wall(154, 205, 50,325,300,10,200)

player=Player('hero.png',5,win_height - 80,4)
monster=Enemy('cyborg.png',win_height - 80,280,2)
treasure = GameSprite('treasure.png',win_widht - 120,win_height - 80,0)

game = True
finish = False
clock = time.Clock()
FPS = 120

font.init()
font = font.Font(None, 70)
win = font.render('YOU WON!', 1, (255, 215, 0))
lose = font.render('YOU LOST!', 1, (180, 0, 0))
 
 
 
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.set_volume(0.1)
mixer.music.play()
 
money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")


while game:
 
    for e in event.get():
        if e.type == QUIT:
            game = False
 
    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update()
 
        player.reset()
        monster.reset()
        treasure.reset()
 
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(
            player, wall1
        ) or sprite.collide_rect(player, wall2) or sprite.collide_rect(
            player, wall3
        ) or sprite.collide_rect(player, wall4):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
 
        if sprite.collide_rect(player, treasure):
            finish = True
            window.blit(win, (200, 200))
            money.play()
 
    display.update()
    clock.tick(FPS)
    


       

