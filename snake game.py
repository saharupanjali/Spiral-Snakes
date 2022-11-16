import pygame
import random
pygame.mixer.init()
pygame.init()
#Creating Game Window
window_width = 700
window_height = 600
gameWindow = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("First Snake Game")
pygame.display.update()
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
violet = (176, 38, 255)
purple = (120,81,169)
cream = (246,225,220)
crimson = (184,15,10)
silver = (66,63,64)
snake = (161,165,140)
dark_grey = (169,169,169)
golden = (212,175,55)
bg = pygame.image.load("back.jpg")
field = pygame.image.load("wall.jpg")
snakes = pygame.image.load("snake image.jpg")
cobra = pygame.image.load("snake_image.jpg")
anaconda = pygame.image.load("snake pic.jpg")
game_over = pygame.image.load("game over.jpg")
gamefield = pygame.image.load("field.jpg")
bgimg = pygame.image.load("background.jpg")
#game_field = pygame.image.load("background.jpg")
#Game Specific Variables
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
coverfont = pygame.font.SysFont(None, 40)
scorefont = pygame.font.SysFont(None, 34)
goldenfont = pygame.font.SysFont(None,36)
warningfont = pygame.font.SysFont(None,48) 
#Font functions
def screen_text (text,color,x,y):
    text_style = font.render(text,True,blue)
    gameWindow.blit(text_style,[x,y])
def warning (text,color,x,y):
    warning_style = warningfont.render(text,True,red)
    gameWindow.blit(warning_style,[x,y])
def text_screen (text,color,x,y):
    text_type = coverfont.render(text,True,crimson)
    gameWindow.blit(text_type,[x,y])
def game_score (text,color,x,y):
    text_font = scorefont.render(text,True,cream)
    gameWindow.blit(text_font,[x,y])
def black_font (text,color,x,y):
    font_style = scorefont.render(text,True,dark_grey)
    gameWindow.blit(font_style,[x,y])
#Snake Controlling Function
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

#Game Levels
def welcome():
    exit_game = False
    while exit_game != True:
        gameWindow.fill(violet)
        gameWindow.blit(snakes, (0,-30))
        text_screen("Press Space Bar To Enter",black,200,5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('theme.mp3')
                    pygame.mixer.music.play(-1)
                    firstlevel()
        pygame.display.update()
        clock.tick(60)

def firstlevel():
    exit_game = False
    while exit_game != True:
        gameWindow.fill(violet)
        gameWindow.blit(bg, (0,-10))
        text_screen("Press The Right Key To Play",red,180,560)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pygame.mixer.music.load('theme.mp3')
                    pygame.mixer.music.play(-1)
                    gameloop()
        pygame.display.update()
        clock.tick(60)

def secondlevel(score):
    exit_game = False
    while exit_game != True:
        gameWindow.fill(black)
        gameWindow.blit(cobra,(0,-20))
        black_font("Press The Right Key To Play",black,190,5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pygame.mixer.music.load('back.wav')
                    pygame.mixer.music.play(-1)
                    nextlevel(score)
        pygame.display.update()
        clock.tick(60)
def nextlevel(score):
    exit_game = False
    snake_x = 0
    snake_y = 250
    snake_size = 10
    #body_parts = 3
    food_x = random.randint(30,window_width)
    food_y = random.randint(30,window_height)
    obs_x = random.randint(100,window_width/2)
    obs_y = random.randint(100,window_height/2)
    obs_size = 20
    obstacle1_x = 480
    obstacle1_y = 450
    obstacle2_x = 80
    obstacle2_y = 50
    obstacle3_x = 80
    obstacle3_y = 450
    obstacle4_x = 480
    obstacle4_y = 50
    obstacle_size = 25
    #food_radius = 4
    fps = 40
    velocity_x = 4
    velocity_y = 0
    init_velocity = 4
    new_score = int(score)
    food_size = 8
    snake_list = []
    snake_length = 2
    game_over = False
    with open("highscore.txt", "r") as f:
        new_highscore = f.read()
#Game Loop
    while exit_game !=True:
        if game_over == True:
            with open("highscore.txt", "w") as f:
             f.write(str(new_highscore))
            gameWindow.fill(black)
            #gameWindow.blit(game_over,(0,0))
            game_score("Press Enter To Play Again", red, 100, 300)
            game_score("Final Score: "+str(new_score),red,50,50)
            if new_score>int(new_highscore):
                game_score("Congratulations for the highest score!", red, 150, 350)
                new_highscore = new_score
            game_score("Highest Score: "+str(new_highscore),red,450,50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            if new_score<650:
                game_score("Enjoyed the game huh!", red, 150, 270)
            else:
                game_score("Senior Player!", red, 150, 350)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
            snake_x +=velocity_x
            snake_y +=velocity_y
            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                new_score +=5
                food_x = random.randint(30, window_width-100)
                food_y = random.randint(30, window_height-100)
                obs_x = random.randint(100,window_width/2)
                obs_y = random.randint(100,window_height/2)
                snake_length +=5
                if new_score > 1000:
                    thirdlevel(new_score)
            gameWindow.fill(cream)
            gameWindow.blit(bgimg,(0,0))
            screen_text("Score: " + str(new_score), blue, 50, 10)
            screen_text("Highest Score: " + new_highscore, blue, 500, 10)
            screen_text("Level:2", blue, 270, 10)
            warning("*Be careful from the red and blue squares", red, 50, 550)
            screen_text("Score above 1000 to reach the final level", red, 150, 500)
            #if score > int(highscore) :
                #highscore = score
            if abs(food_x - obstacle1_x)>25 and abs(food_y-obstacle1_y)>25 or abs(food_x-obstacle2_x)>25 and abs(food_y-obstacle2_y)>25 or abs(food_x - obstacle3_x)>25 and abs(food_y-obstacle3_y)>25 or abs(food_x-obstacle4_x)>25 and abs(food_y-obstacle4_y)>25:
                pygame.draw.rect(gameWindow,golden,[food_x,food_y,food_size,food_size])
            if abs(obs_x - food_x)>12 and abs(obs_y - food_y)>12 or abs(obs_x - obstacle1_x) >10 and abs(obs_y - obstacle1_y) >10 or abs(obs_x - obstacle2_x) >10 and abs(obs_y - obstacle2_y)>10 or abs(obs_x - obstacle3_x)>10 and abs(obs_y - obstacle3_y)>10 or abs(obs_x - obstacle4_x)>10 and abs(obs_y - obstacle4_y)>10:
                pygame.draw.rect(gameWindow,red,[obs_x,obs_y,obs_size,obs_size])
            #pygame.draw.line(gameWindow, black, (obs_x,0),(obs_x,obs_y),10)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                warning("Crashed! Game Over",red,250,200)
                game_over = True
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
            if abs(snake_x - obs_x)<15 and abs(snake_y - obs_y)<15 or abs(snake_x - obstacle1_x)<20 and abs(snake_y - obstacle1_y)<20 :
                warning("Oh no! Crashed! Game Over",red,250,200)
                game_over = True
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
            if abs(snake_x - obstacle2_x)<20 and abs(snake_y - obstacle2_y)<20 or abs(snake_x - obstacle3_x)<20 and abs(snake_y - obstacle3_y)<20:
                warning("Oh no! Crashed! Game Over",red,250,200)
                game_over = True
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
            if abs(snake_x - obstacle4_x)<20 and abs(snake_y - obstacle4_y)<20: 
                warning("Oh no! Crashed! Game Over",red,250,200)
                game_over = True
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>window_width or snake_y<0 or snake_y>window_height:
                warning("Crashed! Game Over",red,250,200)
                game_over = True
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
            plot_snake(gameWindow, silver, snake_list, snake_size)
            pygame.draw.rect(gameWindow,blue,[obstacle1_x,obstacle1_y,obstacle_size,obstacle_size])
            pygame.draw.rect(gameWindow,blue,[obstacle2_x,obstacle2_y,obstacle_size,obstacle_size])
            pygame.draw.rect(gameWindow,blue,[obstacle3_x,obstacle3_y,obstacle_size,obstacle_size])
            pygame.draw.rect(gameWindow,blue,[obstacle4_x,obstacle4_y,obstacle_size,obstacle_size])
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
def thirdlevel(new_score):
    exit_game = False
    while exit_game != True:
        gameWindow.fill(black)
        gameWindow.blit(anaconda,(0,-20))
        text_screen("Now Press The Right Key To Play",black,50,5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pygame.mixer.music.load('Game.mp3')
                    pygame.mixer.music.play(-1)
                    finallevel(new_score)
        pygame.display.update()
        clock.tick(60)
def finallevel(new_score):
    exit_game = False
    snake_x = 440
    snake_y = 0
    snake_size = 12
    #body_parts = 3
    food_1_x = random.randint(30,window_width/2)
    food_1_y = random.randint(30,window_height/2)
    food_2_x = random.randint(50,window_width/2)
    food_2_y = random.randint(50,window_height/2)
    obs1_x = random.randint(50,window_width/2)
    obs1_y = random.randint(50,window_height/2)
    obs2_x = random.randint(250,window_width)
    obs2_y = random.randint(250,window_height)
    obs_size = 40
    obstacle1_x = 480
    obstacle1_y = 450
    obstacle2_x = 80
    obstacle2_y = 50
    obstacle3_x = 80
    obstacle3_y = 450
    obstacle4_x = 480
    obstacle4_y = 50
    obstacle_size = 25
    #food_radius = 4
    fps = 40
    velocity_x = 0
    velocity_y = 5
    init_velocity = 5
    final_score = int(new_score)
    food_1_size = 8
    snake_list = []
    snake_length = 3
    game_over = False
    with open("highscore.txt", "r") as f:
        final_highscore = f.read()
#Game Loop
    while exit_game !=True:
        if game_over == True:
            with open("highscore.txt", "w") as f:
             f.write(str(final_highscore))
            gameWindow.fill(black)
            #gameWindow.blit(game_over,(0,0))
            game_score("Press Enter To Play Again", red, 200, 300)
            game_score("Final Score: "+str(final_score),red,50,50)
            if final_score>int(final_highscore):
                game_score("Congratulations for the highest score!", red, 150, 350)
                final_highscore = final_score
            game_score("Highest Score: "+str(final_highscore),red,450,50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            if new_score<1250:
                game_score("Masterstroke!", red, 250, 270)
            else:
                game_score("Incredible!", red, 250, 350)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
            snake_x +=velocity_x
            snake_y +=velocity_y
            if abs(snake_x - food_1_x)<5 and abs(snake_y - food_1_y)<5:
                final_score +=5
                food_1_x = random.randint(30,window_width/2)
                food_1_y = random.randint(30,window_height/2)
                obs1_x = random.randint(100,window_width/2)
                obs1_y = random.randint(100,window_height/2)
                snake_length +=5
            if abs(snake_x - food_2_x)<7 and abs(snake_y - food_2_y)<7:
                final_score +=10
                food_2_x = random.randint(50,window_width/2)
                food_2_y = random.randint(50,window_height/2)
                obs2_x = random.randint(250,window_width)
                obs2_y = random.randint(250,window_height)
                snake_length +=7
            gameWindow.fill(cream)
            gameWindow.blit(gamefield,(0,0))
            screen_text("Score: " + str(final_score), blue, 50, 10)
            screen_text("Highest Score: " + final_highscore, blue, 500, 10)
            screen_text("Level:2", blue, 270, 10)
            warning("Be careful from the squares!", red, 150, 550)
            #if score > int(highscore) :
                #highscore = score
            if abs(food_1_x - obstacle1_x)>20 and abs(food_1_y-obstacle1_y)>20 or abs(food_1_x-obstacle2_x)>20 and abs(food_1_y-obstacle2_y)>20 or abs(food_1_x - obstacle3_x)>20 and abs(food_1_y-obstacle3_y)>20 or abs(food_1_x-obstacle4_x)>20 and abs(food_1_y-obstacle4_y)>20 or food_1_x!=food_2_x and food_1_y!=food_2_y:
                pygame.draw.rect(gameWindow,white,[food_1_x,food_1_y,food_1_size,food_1_size])
            if abs(food_2_x - obstacle1_x)>20 and abs(food_2_y-obstacle1_y)>20 or abs(food_2_x-obstacle2_x)>20 and abs(food_2_y-obstacle2_y)>20 or abs(food_2_x - obstacle3_x)>20 and abs(food_2_y-obstacle3_y)>20 or abs(food_2_x-obstacle4_x)>20 and abs(food_2_y-obstacle4_y)>20 or food_2_x!= food_1_x and food_2_y!=food_1_y:
                pygame.draw.circle(gameWindow,black,(food_2_x,food_2_y),10)
            if abs(obs1_x - food_1_x)>12 and abs(obs1_y - food_1_y)>12 or obs1_x!=obs2_x and obs1_y!=obs2_y or obs1_x != obstacle1_x and obs1_y != obstacle1_y or obs1_x != obstacle2_x and obs1_y != obstacle2_y or obs1_x != obstacle3_x and obs1_y != obstacle3_y or obs1_x != obstacle4_x and obs1_y != obstacle4_y:
                pygame.draw.rect(gameWindow,cream,[obs1_x,obs1_y,obs_size,obs_size])
            if abs(obs2_x - food_1_x)>12 and abs(obs2_y - food_1_y)>12 or obs2_x!=obs1_x and obs2_y!=obs1_y or obs2_x != obstacle1_x and obs2_y != obstacle1_y or obs2_x != obstacle2_x and obs2_y != obstacle2_y or obs2_x != obstacle3_x and obs2_y != obstacle3_y or obs2_x != obstacle4_x and obs2_y != obstacle4_y:
                pygame.draw.rect(gameWindow,cream,[obs2_x,obs2_y,obs_size,obs_size])
            #pygame.draw.line(gameWindow, black, (obs_x,0),(obs_x,obs_y),10)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                warning("Crashed! Game Over",red,250,200)
                game_over = True
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
            if abs(snake_x - obs1_x)<15 and abs(snake_y - obs1_y)<15 or abs(snake_x - obstacle1_x)<20 and abs(snake_y - obstacle1_y)<20 :
                warning("Oh no! Crashed! Game Over",red,250,200)
                game_over = True
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
            if abs(snake_x - obs2_x)<15 and abs(snake_y-obs2_y)<15:
                warning("Oh no! Crashed! Game Over",red,250,200)
                game_over = True
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
            if abs(snake_x - obstacle2_x)<20 and abs(snake_y - obstacle2_y)<20 or abs(snake_x - obstacle3_x)<20 and abs(snake_y - obstacle3_y)<20:
                warning("Oh no! Crashed! Game Over",red,250,200)
                game_over = True
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
            if abs(snake_x - obstacle4_x)<20 and abs(snake_y - obstacle4_y)<20: 
                warning("Oh no! Crashed! Game Over",red,250,200)
                game_over = True
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>window_width or snake_y<0 or snake_y>window_height:
                warning("Crashed! Game Over",red,250,200)
                game_over = True
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
            plot_snake(gameWindow, snake, snake_list, snake_size)
            pygame.draw.rect(gameWindow,golden,[obstacle1_x,obstacle1_y,obstacle_size,obstacle_size])
            pygame.draw.rect(gameWindow,golden,[obstacle2_x,obstacle2_y,obstacle_size,obstacle_size])
            pygame.draw.rect(gameWindow,golden,[obstacle3_x,obstacle3_y,obstacle_size,obstacle_size])
            pygame.draw.rect(gameWindow,golden,[obstacle4_x,obstacle4_y,obstacle_size,obstacle_size])
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
def gameloop():
    exit_game = False
    score = 0
    snake_x = 0
    snake_y = 50
    snake_size = 10
    obstacle_x1 = 300
    obstacle_y1 = 0
    obstacle_size1 = 30
    obstacle_x2 = 0
    obstacle_y2 = 300
    obstacle_size2 = 40
    #body_parts = 3
    food_x = random.randint(30,window_width/2)
    food_y = random.randint(30,window_height/2)
    obs_x = random.randint(100,window_width/2)
    obs_y = random.randint(100,window_height/2)
    obs_size = 25
    #food_radius = 4
    fps = 30
    velocity_x = 3
    velocity_y = 0
    init_velocity = 3
    init_velocity_1 = 30
    init_velocity_2 = 20
    food_size = 6
    snake_list = []
    snake_length = 1
    game_over = False
    with open("highscore.txt", "r") as f:
        highscore = f.read()
#Game loop 
    while exit_game != True:
        if game_over == True:
            with open("highscore.txt", "w") as f:
             f.write(str(highscore))
            gameWindow.fill(black)
            game_score("Game Over. Press Enter To Restart", red, 150, 300)
            game_score("Final Score: "+str(score),red,50,50)
            if score>int(highscore):
                game_score("Congratulations for the highest score!", red, 150, 350)
                highscore = score
            game_score("Highest Score: "+str(highscore),red,450,50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            if score<500:
                game_score("Oops! Better Luck Next Time", red, 150, 270)
            else:
                game_score("Well played!", red, 150, 350)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    obstacle_x1 +=0
                    obstacle_y1 +=init_velocity_1
                    obstacle_y2 +=0
                    obstacle_x2 +=init_velocity_2
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
            snake_x +=velocity_x
            snake_y +=velocity_y
            if obstacle_y1 >= window_height:
                obstacle_y1 = 0
            if obstacle_x2 >= window_width:
                obstacle_x2 = 0
            if abs(snake_x - food_x)<5 and abs(snake_y - food_y)<5:
                score +=10
                food_x = random.randint(30, window_width/2)
                food_y = random.randint(30, window_height/2)
                obs_x = random.randint(100,window_width/2)
                obs_y = random.randint(100,window_height/2)
                snake_length +=2
                if score>500:
                   secondlevel(score)
            gameWindow.blit(field,(0,0))
            screen_text("Score: " + str(score), blue, 50, 10)
            screen_text("Highest Score: " + highscore, blue, 500, 10)
            screen_text("Level:1", blue, 270, 10)
            #warning("*Avoid the silver box to be safe.", blue, 150, 500)
            screen_text("Score above 500 to reach the next level", blue, 150, 550)
            #if score > int(highscore) :
                #highscore = score
            pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size,food_size])
            pygame.draw.rect(gameWindow,silver,[obstacle_x1,obstacle_y1,obstacle_size1,obstacle_size1])
            pygame.draw.rect(gameWindow,golden,[obstacle_x2,obstacle_y2,obstacle_size2,obstacle_size2])
            #if abs(obs_x - food_x)>25 and abs(obs_y - food_y)>25:
            #pygame.draw.rect(gameWindow,silver,[obs_x,obs_y,obs_size,obs_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
                warning("Oh no! Crashed! Game Over",red,250,200)
                game_over = True
            if snake_x<0 or snake_x>window_width or snake_y<0 or snake_y>window_height:
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
                warning("Oh no! Crashed! Game Over",red,250,200)
                game_over = True
            if abs(snake_x - obstacle_x1)<10 and abs(snake_y - obstacle_y1)<10:
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
                warning("Oh no! Crashed! Game Over",red,250,200)
                game_over = True
            if abs(snake_x - obstacle_x2)<30 and abs(snake_y - obstacle_y2)<30:
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
                warning("Oh no! Crashed! Game Over",red,250,200)
                game_over = True
            #if abs(snake_x - obs_x)<15 and abs(snake_y - obs_y)<15:
                #pygame.mixer.music.load('collision.wav')
                #pygame.mixer.music.play()
                #warning("Oh no! Crashed! Game Over",red,250,200)
                #game_over = True
            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)                
    pygame.quit()
    quit()
welcome()
firstlevel()
gameloop()
secondlevel()
nextlevel()
