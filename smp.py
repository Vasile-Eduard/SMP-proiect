import pygame, sys


pygame.init()
clock = pygame.time.Clock()

screen_width=600  #lungime_ecran
screen_height=360 #inaltime_ecran
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Try to stay calm') #nume joc


#coordonate jucator
player=pygame.Rect(screen_width-55, screen_height-35,20,20)

#coordonate labirint
zid_1=pygame.Rect(screen_width/6, screen_height/3,90,5)
zid_2=pygame.Rect(screen_width/3-10, screen_height/6-55,5,120)
zid_3=pygame.Rect(screen_width/2-200, screen_height*2/3,300,5)
zid_4=pygame.Rect(screen_width/3+200, screen_height/3,100,5)
zid_5=pygame.Rect(screen_width*2/3-5, screen_height/6+60,5,120)
zid_6=pygame.Rect(screen_width*2/3, screen_height/12-25,5,60)
zid_7=pygame.Rect(screen_width*5/6, screen_height/4-25,5,60)
zid_8=pygame.Rect(screen_width*5/6, screen_height*2/3+15,5,100)
zid_9=pygame.Rect(screen_width/2, screen_height/4-20,5,100)

#coordonate margini
border_l=pygame.Rect(0, 0,5,screen_height)
border_d=pygame.Rect(5,355,screen_width-5,5)
border_u=pygame.Rect(5,0,screen_width-10,5)
border_r=pygame.Rect(screen_width-5,0,5,355)

#coordonate obstacole
glont=pygame.Rect(screen_width/2-14, screen_height/2-14,5,5)
glont2=pygame.Rect(screen_width/2-37, screen_height/2-14,5,5)
glont3=pygame.Rect(320,20,5,5)
glont4=pygame.Rect(100,300,5,5)
glont5=pygame.Rect(200,300,5,5)
glont6=pygame.Rect(300,300,5,5)
glont7=pygame.Rect(390,300,5,5)
glont8=pygame.Rect(6,60,5,5)
glont9=pygame.Rect(150,5,5,5)
glont10=pygame.Rect(410,40,5,5)
glont11=pygame.Rect(410,180,5,5)
glont12=pygame.Rect(5,5,5,5)

#coordonate chei
key1=pygame.Rect(150,260,3,3)
key2=pygame.Rect(250,340,3,3)
key3=pygame.Rect(350,300,3,3)
key4=pygame.Rect(350,160,3,3)
key5=pygame.Rect(250,130,3,3)
key6=pygame.Rect(180,220,3,3)
key7=pygame.Rect(30,30,3,3)
key8=pygame.Rect(450,20,3,3)
key9=pygame.Rect(450,160,3,3)
key10=pygame.Rect(300,30,3,3)

final=pygame.Rect(160,90,30,30) #coordonate final

intrebare=pygame.Rect(30,160,30,30) #coordonate intrebare

start=pygame.Rect(screen_width-60, screen_height-40,30,30) #coordonate start

speed=3  #viteza jucator

#viteza gloante
glont_x=1 
glont_y=1
glont2_x=1
glont2_y=1
glont3_y=1
glont4_y=4
glont5_y=3
glont6_y=2
glont7_y=2
glont8_x=3
glont9_y=1
glont10_x=1
glont11_x=1
glont12_x=1
glont12_y=1

#variabile ajutor
playing=True
k=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                player.y+=speed            
            if event.key==pygame.K_UP:
                player.y+=-speed
            if event.key==pygame.K_LEFT:
                player.x+=-speed
            if event.key==pygame.K_RIGHT:
                player.x+=speed
                 

    
    glont.x+=glont_x
    glont.y+=glont_y
    glont2.x+=glont2_x
    glont2.y+=glont2_y
    glont3.y+=glont3_y
    glont4.y+=glont4_y
    glont5.y+=glont5_y
    glont6.y+=glont6_y
    glont7.y+=glont7_y
    glont8.x+=glont8_x
    glont9.y+=glont9_y
    glont10.x+=glont10_x
    glont11.x+=glont11_x
    glont12.x+=glont12_x
    glont12.y+=glont12_y
          
    #interactiune gloante vs ziduri/margini    
    if glont.colliderect(zid_2) or glont.colliderect(zid_3):
        glont_x*=-1
        glont_y*=-1
        
    if glont2.colliderect(zid_2) or glont2.colliderect(zid_3):
        glont2_x*=-1
        glont2_y*=-1

    if glont12.colliderect(border_l) or glont12.colliderect(zid_1):
        glont12_x*=-1
        glont12_y*=-1
        
    if glont3.colliderect(border_u) or glont3.colliderect(zid_3):
        glont3_y*=-1
        
    if glont4.colliderect(border_d) or glont4.colliderect(zid_3):
        glont4_y*=-1
        
    if glont5.colliderect(border_d) or glont5.colliderect(zid_3):
        glont5_y*=-1
        
    if glont6.colliderect(border_d) or glont6.colliderect(zid_3):
        glont6_y*=-1
        
    if glont7.colliderect(border_d) or glont7.colliderect(zid_3):
        glont7_y*=-1
        
    if glont8.colliderect(border_l) or glont8.colliderect(zid_2):
        glont8_x*=-1   
        
    if glont9.colliderect(border_u) or glont9.colliderect(zid_1):
        glont9_y*=-1  
        
    if glont10.colliderect(border_r) or glont10.colliderect(zid_6):
        glont10_x*=-1
        
    if glont11.colliderect(border_r) or glont11.colliderect(zid_5):
        glont11_x*=-1   
     

        
#interactiune jucator vs ziduri      
    if player.colliderect(zid_9):
        if zid_9.x < player.x:
            player.x+=2
        else:
                player.x-=2
    if player.colliderect(zid_8):
        if zid_8.x < player.x:
            player.x+=2
        else:
                player.x-=2
    if player.colliderect(zid_7):
        if zid_7.x < player.x:
            player.x+=2
        else:
                player.x-=2                
    if player.colliderect(zid_6):
        if zid_6.x < player.x:
            player.x+=2
        else:
                player.x-=2
    if player.colliderect(zid_5):
        if zid_2.x < player.x:
            player.x+=2
        else:
                player.x-=2                
    if player.colliderect(zid_2):
        if zid_2.x < player.x:
            player.x+=2
        else:
                player.x-=2                
    if player.colliderect(zid_1):
        if zid_2.y < player.y:
            player.y+=2
        else:
                player.y-=2  
    if player.colliderect(zid_3):
        if zid_2.y < player.y:
            player.y+=2
        else:
                player.y-=2  
    if player.colliderect(zid_4):
        if zid_2.y < player.y:
            player.y+=2
        else:
                player.y-=2  

#interactiune jucator vs margini
    if player.colliderect(border_u):
        if border_u.y < player.y:
            player.y+=2
        else:
                player.y-=2  
                
    if player.colliderect(border_d):
        if border_d.y < player.y:
            player.y+=2
        else:
                player.y-=2  
               
    if player.colliderect(border_l):
        if border_l.y < player.x:
            player.x+=2
        else:
                player.x-=2  

    if player.colliderect(border_r):
        if border_r.x < player.x:
            player.x+=2
        else:
                player.x-=2  

#interactiune jucator vs chei
    if player.colliderect(key1):
        k+=1
        key1.x=-1
        key1.y=-1
    if player.colliderect(key2):
        k+=1
        key2.x=-1
        key2.y=-1
    if player.colliderect(key3):
        k+=1
        key3.x=-1
        key3.y=-1
    if player.colliderect(key4):
        k+=1
        key4.x=-1
        key4.y=-1
    if player.colliderect(key5):
        k+=1
        key5.x=-1
        key5.y=-1
    if player.colliderect(key6):
        k+=1
        key6.x=-1
        key6.y=-1
    if player.colliderect(key7):
        k+=1
        key7.x=-1
        key7.y=-1
    if player.colliderect(key8):
        k+=1
        key8.x=-1
        key8.y=-1
    if player.colliderect(key9):
        k+=1
        key9.x=-1
        key9.y=-1
    if player.colliderect(key10):
        k+=1
        key10.x=-1
        key10.y=-1
    

        
#interactiune jucator vs gloante & desenare obiecte   
    if playing:
        if glont.colliderect(player) or glont2.colliderect(player) or glont3.colliderect(player) or glont4.colliderect(player) or glont5.colliderect(player) or glont6.colliderect(player) or glont7.colliderect(player) or glont8.colliderect(player) or glont9.colliderect(player) or glont10.colliderect(player) or glont11.colliderect(player) or glont12.colliderect(player):
            screen.fill((0,0,0))
            font=pygame.font.SysFont('Time New Roman',60)
            title=font.render('Ai pierdut.',False, (200,200,200))
            titleRect=title.get_rect()
            titleRect.center=(300,160)
            screen.blit(title,titleRect)
            playing=False
        else:
            screen.fill((0,0,0))
            pygame.draw.rect(screen,(200,200,200),start)
            pygame.draw.rect(screen,(0,255,0),intrebare)
            pygame.draw.rect(screen,(255,255,0),final)
            pygame.draw.rect(screen,(128,0,128),player)
            pygame.draw.rect(screen,(200,200,200),glont)
            pygame.draw.rect(screen,(200,200,200),glont2)
            pygame.draw.rect(screen,(200,200,200),glont3)            
            pygame.draw.rect(screen,(200,200,200),glont4)
            pygame.draw.rect(screen,(200,200,200),glont5)
            pygame.draw.rect(screen,(200,200,200),glont6)
            pygame.draw.rect(screen,(200,200,200),glont7)
            pygame.draw.rect(screen,(200,200,200),glont8)
            pygame.draw.rect(screen,(200,200,200),glont9)
            pygame.draw.rect(screen,(200,200,200),glont10)
            pygame.draw.rect(screen,(200,200,200),glont11)            
            pygame.draw.rect(screen,(200,200,200),glont12)              
            
            pygame.draw.rect(screen,(200,200,200),zid_1)
            pygame.draw.rect(screen,(200,200,200),zid_2)
            pygame.draw.rect(screen,(200,200,200),zid_3)
            pygame.draw.rect(screen,(200,200,200),zid_4)
            pygame.draw.rect(screen,(200,200,200),zid_5)
            pygame.draw.rect(screen,(200,200,200),zid_6)
            pygame.draw.rect(screen,(200,200,200),zid_7)
            pygame.draw.rect(screen,(200,200,200),zid_8)
            pygame.draw.rect(screen,(200,200,200),zid_9)
            pygame.draw.rect(screen,(200,200,200),border_l)
            pygame.draw.rect(screen,(200,200,200),border_d)
            pygame.draw.rect(screen,(200,200,200),border_r)
            pygame.draw.rect(screen,(200,200,200),border_u)
            pygame.draw.rect(screen,(255,255,0),key1)
            pygame.draw.rect(screen,(255,255,0),key2)
            pygame.draw.rect(screen,(255,255,0),key3)
            pygame.draw.rect(screen,(255,255,0),key4)
            pygame.draw.rect(screen,(255,255,0),key5)
            pygame.draw.rect(screen,(255,255,0),key6)
            pygame.draw.rect(screen,(255,255,0),key7)
            pygame.draw.rect(screen,(255,255,0),key8)
            pygame.draw.rect(screen,(255,255,0),key9)
            pygame.draw.rect(screen,(255,255,0),key10)
            
            
            
            if player.colliderect(final) and k==10:
                screen.fill((0,0,0))
                font=pygame.font.SysFont('Time New Roman',60)
                final2=font.render('Felicitari. Ai terminat jocul.',False, (200,200,200))
                final2Rect=final2.get_rect()
                final2Rect.center=(300,160)
                screen.blit(final2,final2Rect)
                playing=False
            elif player.colliderect(final) and (k<10 and k>0):
                font=pygame.font.SysFont('Time New Roman',40)
                final3=font.render('Ai nevoie de toate cele 10 chei',False, (0,0,255))
                final3Rect=final3.get_rect()
                final3Rect.center=(300,180)
                screen.blit(final3,final3Rect)
            if player.colliderect(intrebare):
                font=pygame.font.SysFont('Time New Roman',40)
                cf=font.render('Greul acum urmeaza',False, (0,0,255))
                cfRect=cf.get_rect()
                cfRect.center=(300,180)
                screen.blit(cf,cfRect)
            if player.colliderect(start):
                font=pygame.font.SysFont('Time New Roman',30)
                st=font.render('Trebuie sa aduni toate cheile si sa ajungi la zona galbena',False, (0,0,255))
                stRect=st.get_rect()
                stRect.center=(300,200)
                screen.blit(st,stRect)    
            
    else:
        font=pygame.font.SysFont('Time New Roman',30)
        restart=font.render('Apasa tasta space pentru a reincepe.',False, (200,200,200))
        restartRect=restart.get_rect()
        restartRect.center=(300,260)
        screen.blit(restart,restartRect)
        key=pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            playing=True
            player.x=screen_width-55
            player.y=screen_height-35
            key1.x=150
            key1.y=260
            key2.x=250
            key2.y=340
            key3.x=350
            key3.y=300
            key4.x=350
            key4.y=160
            key5.x=250
            key5.y=130
            key6.x=180
            key6.y=220
            key7.x=30
            key7.y=30
            key8.x=450
            key8.y=20
            key9.x=450
            key9.y=160
            key10.x=300
            key10.y=30
            
    pygame.display.flip()
    clock.tick(60)
    
