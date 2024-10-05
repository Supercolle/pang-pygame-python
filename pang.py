import pygame


pygame.init()

width = 800
height = 600



root = pygame.display.set_mode((width,height))
pygame.display.set_caption('Pang')

clock = pygame.time.Clock()

score_a = 0 
score_b = 0 


font = pygame.font.Font(None,20)

class Paddle():
    def __init__(self,x,y,paddle_width,paddle_height,vel):
        self.x = x
        self.y = y
        self.paddle_width = paddle_width 
        self.paddle_height = paddle_height
        self.vel = vel

########################################################################
#----> DRAW RETTANGLE

    def paddle (self,root):
        pygame.draw.rect(root,'white',(self.x,self.y,self.paddle_width,self.paddle_height))

##########################################################################
#----> MOOVE PADDLE

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key]:
            self.y -= self.vel
        if keys[down_key]:
            self.y += self.vel
##########################################################################
# ----> CONTROL PADDLE COLLISION WINDOW            
        if self.y < 0:
            self.y = 0
        if self.y + self.paddle_height > height:
            self.y = height - self.paddle_height
##########################################################################
# ----> CREATE A RECT FOR CONTROLL COLDIRECT FROM BALL AND PADDLE
    def get_rect (self):
        return pygame.Rect(self.x,self.y,self.paddle_width,self.paddle_height)


class Ball:
    def __init__(self,ball_x,ball_y,radius,vel):
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.radius = radius
        self.vel = vel

    def draw_ball (self,root):
        pygame.draw.circle(root,'white',(self.ball_x,self.ball_y),self.radius)

    def moove(self):
        self.ball_x += self.vel[0]
        self.ball_y += self.vel[1]
###############################################################################
# ---->   CONTROLL BALL COLLISION ON WINDOW AND CHANGE DIRECTION
        # if self.ball_x - self.radius <= 0 or self.ball_x + self.radius >= width:
        #     self.vel = (-self.vel[0],self.vel[1])
        if self.ball_y -self.radius <= 0 or self.ball_y +self.radius >= height:
            self.vel = (self.vel[0],-self.vel[1])
        
    def get_ball_rect(self):
        return pygame.Rect(self.ball_x - self.radius, self.ball_y - self.radius, self.radius * 2, self.radius * 2)


    def ball_reset(self):
        self.ball_x = width//2
        self.ball_y = height //2
        self.vel = (3,3)

paddle_a = Paddle(10,(height//2),15,90,5)
paddle_b = Paddle(770,(height//2),15,90,5)



ball = Ball(width//2,height//2,7,(3,3))

running = True







while running :

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    

   

    root.fill('black')

    pygame.draw.line(root,'white',(width//2,0),(width//2,height-1),5)

    paddle_a.move(pygame.K_w, pygame.K_s)
    paddle_b.move(pygame.K_UP, pygame.K_DOWN)

    paddle_a.paddle(root)
    paddle_b.paddle(root)

    ball.moove()
    ball.draw_ball(root)
#########################################################################
# ----> CONTROLL COLLISION WHIT PADDLE AND CHANGE DIRECTIO BALL
    if ball.get_ball_rect().colliderect(paddle_a.get_rect()) or ball.get_ball_rect().colliderect(paddle_b.get_rect()):
        ball.vel = (-ball.vel[0],ball.vel[1])

    if ball.ball_x < 0:
        score_b +=1
        ball.ball_reset()
    elif ball.ball_x > (width)-1:
        score_a += 1
        ball.ball_reset()

    text = font.render(f'Player A : {score_a} - Player B : {score_b}', True, (255,255,255))   
    text_rect = text.get_rect()    
    text_rect.center = (width // 2, 10)  

    
    root.blit(text, text_rect)
   
   
    pygame.display.update()

pygame.quit()
