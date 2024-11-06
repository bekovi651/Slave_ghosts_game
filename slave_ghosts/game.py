import pygame
import time, random
#nessasary
pygame.init()

bullets_count = 5
games_count = 1
record = 0
result = 0
def load():
    global games_count,record
    file = open('statistic.txt','r+')
    statictic = file.read().split(",")
    file.close()
    record = int(statictic[0])
    games_count = int(statictic[1])
def save():
    global games_count,record
    file = open('statistic.txt','w+')
    file.write(f'{record},{games_count}')
    file.close()
load()


#frames
clock = pygame.time.Clock()

#display settings
screen = pygame.display.set_mode((618,359),vsync=1)
class Ghost:
    def __init__(self,x):
        self.ghost_x = x
        self.ghost = pygame.transform.scale(pygame.image.load('images/ghost.png').convert_alpha(), (45, 35))
        self.ghost1 = pygame.transform.flip(self.ghost,True,False)
class Ghost1:
    def __init__(self,x):
        self.ghost_x = x
        self.ghost = pygame.transform.scale(pygame.image.load('images/ghost1.png').convert_alpha(), (40, 35))
    
        self.ghost1 = pygame.transform.flip(self.ghost,True,False)
ghost1 = Ghost1(620)
ghost = Ghost(-10)

#title
pygame.display.set_caption('game')

#icon
icon = pygame.image.load('images/icon0.png').convert_alpha()
dead_label = pygame.image.load('images/death.png').convert_alpha()
magic = pygame.transform.scale(pygame.image.load('images/magic.png').convert_alpha(), (360, 640))
magics = []
bullet = pygame.transform.scale(pygame.image.load('images/bullet.png').convert_alpha(), (30, 40))
bullet1 =  pygame.transform.rotate(bullet, 180)
show_bullet_img = pygame.transform.rotate(bullet, 90)
bullets = []
bullets1=[]


pygame.display.set_icon(icon)

#bg
bg = pygame.image.load('images/image.png').convert_alpha()


#loop the game
running = True
right = [pygame.image.load('images/r1.png').convert_alpha(),
pygame.image.load('images/r2.png').convert_alpha(),
pygame.image.load('images/r3.png').convert_alpha(),
pygame.image.load('images/r4.png').convert_alpha(),

]
left = [
pygame.image.load('images/s1.png').convert_alpha(),
pygame.image.load('images/s2.png').convert_alpha(),
pygame.image.load('images/s3.png').convert_alpha(),
pygame.image.load('images/s4.png').convert_alpha(),
]
#sound
step = pygame.mixer.Sound('sound0.mp3')

"""анимация"""
player_count = 0

jump = False
jump_hight = 8

#move screen
#координаты 
bg_x = 0

player_x = 300
player_y = 250


way = [right, left]


way_count = 0
gameplay = True
ghost_list1 = []
ghost_list = [] 

def show_bullet():
    global bullets_count
    for i in range(bullets_count):
        screen.blit(show_bullet_img,(600-(40*(i+1)-15*i),20))

def update_all():
    global screen, bg,way,bg_x, way_count,player_count, player_x,player_y, ghost,gameplay,bullets,bullet,bullets1,record,result,games_count
    screen.blit(bg,(-618+bg_x,0))
    screen.blit(bg,(bg_x,0))
    screen.blit(bg,(618 + bg_x,0))
    screen.blit(way[way_count][player_count],(player_x,player_y))
    show_bullet()
    
    
    
    
    if ghost_list:
        for el in ghost_list:
            if el[1] == 0:
                screen.blit(ghost1.ghost, el[0])
            else:
                screen.blit(ghost.ghost, el[0])
            
            player_rect = left[0].get_rect(topleft = (player_x,player_y))
            
            if player_rect.colliderect(el[0]):
                gameplay = False
                
            
                if record < result:
                    record = result
                    save()
    if ghost_list1:
        for el in ghost_list1:
            if el[1] == 0:
                screen.blit(ghost1.ghost1, el[0])
            else:
                screen.blit(ghost.ghost1, el[0])
            
            player_rect = left[0].get_rect(topleft = (player_x,player_y))
            
            if player_rect.colliderect(el[0]):
                gameplay = False
                
            
                if record < result:
                    record = result
                    save()
    if bullets:
        for el in bullets:
            screen.blit(bullet1,(el.x,el.y))
    if bullets1:
        for el in bullets1:
            screen.blit(bullet,(el.x,el.y))
            
    text_result1 = pygame.font.SysFont('sand', 50).render(f'Очки: {result}', 0, (100,0,0))
    screen.blit(text_result1, (20, 20))
    text_result2 = pygame.font.SysFont('sand', 50).render(f'Рекорд: {record}', 0, (100,0,0))
    screen.blit(text_result2, (240, 20))
    text_result3 = pygame.font.SysFont('sand', 50).render(f'Игр сыгранно: {games_count}', 0, (100,0,0))
    screen.blit(text_result3, (300,310 ))
    
    pygame.display.flip()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer,5000)
ghost_timer1 = pygame.USEREVENT + 2
pygame.time.set_timer(ghost_timer1,8500)
bullet_timer = pygame.USEREVENT + 3
pygame.time.set_timer(bullet_timer,14000)



def ghosts(x):
    global ghost_list, ghost,screen, player_x, player_y, update_all, gameplay, ghost1,ghost_list1,result,record,games_count
    
    
    if ghost_list:
        for (i,el) in enumerate(ghost_list):
            if el[1] == 0:
                screen.blit(ghost1.ghost, el[0])
            else:
                screen.blit(ghost.ghost, el[0])
            el[0].x += x
            player_rect = left[0].get_rect(topleft = (player_x,player_y))
            if el[0].x < -10:
                ghost_list.pop(i)
                result += 1
            
                if record < result:
                    record = result
                    save()
            if player_rect.colliderect(el[0]):
                gameplay = False
                
                
            
                if record < result:
                    record = result
                    save()
    if bullets:
        for (i,el) in enumerate(bullets):
            screen.blit(bullet1,(el.x,el.y))
            if x > 0:
                el.x += x+3
            else:
                el.x += x-3
            if el.x < -10:
                bullets.pop(i)
    if ghost_list1 and bullets:
        for (i,el) in enumerate(bullets):
            for (i1,el1) in enumerate(ghost_list1):
                if el1[0].colliderect(el):
                    
                    bullets.pop(i)
                    ghost_list1.pop(i1)
                    result += 1
            
                    if record < result:
                        record = result
                        save()
    if ghost_list and bullets:
        for (i,el) in enumerate(bullets):
            for (i1,el1) in enumerate(ghost_list):
                if el1[0].colliderect(el):
                    
                    bullets.pop(i)
                    ghost_list.pop(i1)
                    result += 1
            
                    if record < result:
                        record = result
                        save()
    
def ghosts1(x):
    global ghost_list, ghost,screen, player_x, player_y, update_all, gameplay, ghost1,ghost_list1,bullet,bullets1,bullets,result,record,games_count
    
    
    if ghost_list1:
        for (i,el) in enumerate(ghost_list1):
            if el[1] == 0:
                screen.blit(ghost1.ghost1, el[0])
            else:
                screen.blit(ghost.ghost1, el[0])
            el[0].x -= x
            player_rect = left[0].get_rect(topleft = (player_x,player_y))
            if el[0].x > 630:
                ghost_list1.pop(i)
                result += 1
            
                if record < result:
                    record = result
                    save()
            if player_rect.colliderect(el[0]):
                gameplay = False
                
                
            
                if record < result:
                    record = result
                    save()
    if bullets1:
        for (i,el) in enumerate(bullets1):
            screen.blit(bullet,(el.x,el.y))
            
            
        
            if x > 0:
                el.x -= x+3
            else:
                el.x -= x-3
    
            if el.x > 630:
                bullets1.pop(i)
                
    if ghost_list1 and bullets1:
        for (i,el) in enumerate(bullets1):
            for (i1,el1) in enumerate(ghost_list1):
                if el1[0].colliderect(el):
                    
                    bullets1.pop(i)
                    ghost_list1.pop(i1)
                    result += 1
            
                    if record < result:
                        record = result
                        save()
    if ghost_list and bullets1:
        for (i,el) in enumerate(bullets1):
            for (i1,el1) in enumerate(ghost_list):
                if el1[0].colliderect(el):
                    
                    bullets1.pop(i)
                    ghost_list.pop(i1)
                    result += 1
            
                    if record < result:
                        record = result
                        save()
    

while running:
    load()
    
    
    if gameplay:
        while gameplay:
            screen.blit(icon,(0,0))
            
            update_all()

            
            ghosts(-6)
            ghosts1(-6)
            if not gameplay:
                break
            

            #rects
            

            keys = pygame.key.get_pressed()
            if not jump:
                
                if keys[pygame.K_UP]:
                    jump = True

                    
            else:
                
                if jump_hight >= -8:
                    if jump_hight>0:
                        player_y -= (jump_hight**2)/2
                    else:
                        player_y += (jump_hight**2)/2
                    jump_hight -= 1
                    
                
                else:
                    jump = False
                    jump_hight = 8
                    step.play(maxtime = 150)
                
                if keys[pygame.K_a]:
                    if way_count == 0:
                        way_count = 1
                        player_count = 0
                    else:
                            
                        if jump_hight >= -8:
                            ghosts(4)
                            ghosts1(-4)
                            bg_x += 4
                            if bg_x >= 618:
                                bg_x = 0
                        else:
                            jump = False
                            jump_hight = 8
                            step.play(maxtime = 150)
                            
                        
                        if not gameplay:
                            break
                        
                    
                if keys[pygame.K_d]:
                        
                    if way_count == 1:
                            
                        way_count = 0
                        player_count = 0
                    else:

                            
                        if jump_hight >= -8:
                            ghosts(-4)
                            ghosts1(4)
                            bg_x -= 4
                            if bg_x >= 618:
                                bg_x = 0
                        else:
                            jump = False
                            jump_hight = 8
                            step.play(maxtime = 150)
                        if not gameplay:
                            break
                        
                    
                if keys[pygame.K_LEFT]:
                    if way_count == 0:
                        way_count = 1
                        player_count = 0
                        
                    if player_x >= 100:
                            player_x -= 3
                    else:
                        ghosts(3)
                        ghosts1(-3)
                        if not gameplay:
                            break
                        bg_x += 3
                        if bg_x >= 618:
                            bg_x = 0
                    
                if keys[pygame.K_RIGHT]:
                        
                    if way_count == 1:
                        way_count = 0
                        player_count = 0
                        
                        
                    if player_x <= 500:
                        player_x += 3
                            
                    else:
                            
                        bg_x -= 3
                        ghosts(-3)
                        ghosts1(3)
                        if not gameplay:
                            break
                        if bg_x <= -618:
                            bg_x = 0
                    
            if True:
                    
                    if keys[pygame.K_d] and jump == False:
                        
                        if way_count == 1:
                            
                            way_count = 0
                            player_count = 0
                        else:

                            if random.random()>0.5:
                                step.play(maxtime = 150)
                            if player_count == 3:
                                player_count = 0
                            else:
                                
                                player_count+= 1
                            ghosts(-5)
                            ghosts1(5)
                            if not gameplay:
                                break
                            bg_x -= 5
                            if bg_x <= -618:
                                bg_x = 0
                        
                    
                        

                    elif keys[pygame.K_a] and jump == False:
                        
                        if way_count == 0:
                            way_count = 1
                            player_count = 0
                            
                        else:
                            if random.random()>0.5:
                                step.play(maxtime = 150)
                            if player_count == 3:
                                player_count = 0
                            else:
                                player_count+= 1
                            
                            bg_x += 5
                            
                            ghosts(5)
                            ghosts1(-5)
                            if not gameplay:
                                break
                            if bg_x >= 618:
                                bg_x = 0
                        
                    
                    elif keys[pygame.K_RIGHT] and jump == False:
                        
                        if way_count == 1:
                            way_count = 0
                            player_count = 0
                        else:
                            if random.random()>0.5:
                                step.play(maxtime = 150)
                            if player_count == 3:
                                player_count = 0
                            else:
                                player_count+= 1
                        if player_x <= 500:
                            player_x += 3
                            
                        else:
                            
                            bg_x -= 3
                            ghosts(-3)
                            ghosts1(3)
                            if not gameplay:
                                break
                            if bg_x <= -618:
                                bg_x = 0
                        
                    elif keys[pygame.K_LEFT] and jump == False:
                        if way_count == 0:
                            way_count = 1
                            player_count = 0
                        else:
                            if random.random()>0.5:
                                
                                step.play(maxtime = 150)
                            if player_count == 3:
                                player_count = 0
                            else:
                                player_count+= 1
                        
                        if player_x >= 100:
                            player_x -= 3
                        else:
                            ghosts(+3)
                            ghosts1(-3)
                            if not gameplay:
                                break
                            bg_x += 3
                            if bg_x >= 618:
                                bg_x = 0
                    
                    
                        
            #correct qiut if the window is closed
            #check all the events
            
            for event in pygame.event.get():
                #if event is quit
                if event.type == pygame.QUIT:
                    gameplay = False
                    running=False 
                    pygame.quit() 
                if event.type == bullet_timer:
                    if bullets_count<5:
                        bullets_count += 1
                if event.type == ghost_timer:
                    if random.randint(0,2) == 1:
                        ghost_list.append((ghost.ghost.get_rect(topleft =    (620,250)),0))
                    else:
                        ghost_list.append((ghost1.ghost.get_rect(topleft =    (620,250)),1))
                if event.type == ghost_timer1:
                    if random.randint(0,2) == 1:
                        ghost_list1.append((ghost1.ghost1.get_rect(topleft =    (-10,250)),1))
                    else:
                        ghost_list1.append((ghost.ghost1.get_rect(topleft =    (-10,250)),0))
                if event.type == pygame.KEYUP and event.key == pygame.K_w and jump == False and way_count == 0 and bullets_count >= 1:
                    bullets1.append(bullet.get_rect(topleft=(player_x+40,player_y+15)))
                    bullets_count -= 1
                if event.type == pygame.KEYUP and event.key == pygame.K_w and jump == False and way_count == 1 and bullets_count >= 1:
                    bullets.append(bullet.get_rect(topleft=(player_x-20,player_y+15)))
                    bullets_count -= 1
            
                
                    
                
                    
                    
                #chech keys
            
            
            
            
            
                        

                    
                    



            clock.tick(20)
    else:
        mouse = pygame.mouse.get_pos() 
        
        font = pygame.font.SysFont('sand',60)
        text = font.render(f"Ещё раз", 0, (0,0,0))
        screen.fill((0,0,0))
        screen.blit(dead_label,(70,40))
        screen.blit(text,(220,220))
        pygame.display.update()
        for event in pygame.event.get():
            #if event is quit
            if event.type == pygame.QUIT:
                running=False 
                pygame.quit() 
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                
                #if the mouse is clicked on the 
                # button the game is terminated 
                if 220 <= mouse[0] <= 390 and 220 <= mouse[1] <= 260: 
                    gameplay = True
                    ghost_list1 = []
                    ghost_list = []
                    player_count = 0
                    games_count +=1
                    save()
                    bullets_count = 5
                    bullets1 = []
                    bullets = []
                    result = 0

                    jump = False
                    

                    #move screen
                    #координаты 
                    bg_x = 0
                    jump_hight = 8
                    player_x = 300
                    player_y = 250


                    way = [right, left]


                    way_count = 0
                    pygame.time.set_timer(ghost_timer,5000)
                    
                    pygame.time.set_timer(ghost_timer1,8500)

                    pygame.time.set_timer(bullet_timer,14000)
        if running == False:
            pygame.quit() 