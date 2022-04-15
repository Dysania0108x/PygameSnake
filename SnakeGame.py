from pygame.color import THECOLORS as COLORS
import pygame
import Snake

# draw start screen
def draw_start():
    # fill in background colour #wathet blue--same as the UI I draw
    screen.fill(COLORS['wathet'])
    # draw choice_board
    pygame.draw.rect(screen,COLORS['azure'],(220,304,250,78),0)
    pygame.draw.rect(screen,COLORS['black'],(220,304,250,78),3)
    # set choice_board name
    txt_start = font_start.render('Start',True,COLORS['black'])
    # set title
    txt_title = font_title.render('Perfect Snake',True,COLORS['black'])
    # set and draw with coordinates
    x,y = 290,312
    screen.blit(txt_start,(x,y))
    x,y = 96,110
    screen.blit(txt_title,(x,y))

# draw menu board
def draw_menu():
    # fill in background colour #wathet blue--same as the UI I draw
    screen.fill(COLORS['wathet'])
    # draw choice_board_different levels
    pygame.draw.rect(screen,COLORS['azure'],(128,200,190,90),0)
    pygame.draw.rect(screen,COLORS['black'],(128,200,190,90),3)
    pygame.draw.rect(screen,COLORS['azure'],(128,340,190,90),0)
    pygame.draw.rect(screen,COLORS['black'],(128,340,190,90),3)
    pygame.draw.rect(screen,COLORS['azure'],(372,200,190,90),0)
    pygame.draw.rect(screen,COLORS['black'],(372,200,190,90),3)
    pygame.draw.rect(screen,COLORS['azure'],(372,340,190,90),0)
    pygame.draw.rect(screen,COLORS['black'],(372,340,190,90),3)
    # set title
    txt_title = font_title.render('Levels',True,COLORS['black'])
    # set choice_board name
    txt_easy = font_option.render('Easy',True,COLORS['black'])
    txt_normal = font_option.render('Normal',True,COLORS['black'])
    txt_hard = font_option.render('Hard',True,COLORS['black'])
    txt_crazy = font_option.render('Crazy',True,COLORS['black'])
    # set and draw with coordinates
    x,y = 230,50
    screen.blit(txt_title,(x,y))
    x,y = 181,220
    screen.blit(txt_easy,(x,y))
    x,y = 396,220
    screen.blit(txt_normal,(x,y))
    x,y = 175,360
    screen.blit(txt_hard,(x,y))
    x,y = 410,360
    screen.blit(txt_crazy,(x,y))

# Draw game start screen
def draw_map():
    # easy   4*4
    # normal 8*8
    # hard   12*12
    # crazy  16*16
    # Judging difficulty level of easy
    if level == 1:
        # set detailed size
        size_x = 690
        size_y = 480
        # Initialize a screen for display
        pygame.display.set_mode([size_x, size_y])
        # fill in background colour
        screen.fill(COLORS['wathet'])
        # draw chess board
        pygame.draw.rect(screen,COLORS['black'],(285,200,120,120),3)
        pygame.draw.line(screen,COLORS['black'],(285,230),(405,230))
        pygame.draw.line(screen,COLORS['black'],(285,260),(405,260))
        pygame.draw.line(screen,COLORS['black'],(285,290),(405,290))
        pygame.draw.line(screen,COLORS['black'],(315,200),(315,320))
        pygame.draw.line(screen,COLORS['black'],(345,200),(345,320))
        pygame.draw.line(screen,COLORS['black'],(375,200),(375,320))
    # Judging difficulty level of normal
    elif level == 2:
        size_x = 690
        size_y = 480
        pygame.display.set_mode([size_x, size_y])
        # fill in background colour
        screen.fill(COLORS['wathet'])
        # draw chess board
        pygame.draw.rect(screen,COLORS['black'],(225,120,240,240),3)
        pygame.draw.line(screen,COLORS['black'],(255,120),(255,360))
        pygame.draw.line(screen,COLORS['black'],(285,120),(285,360))
        pygame.draw.line(screen,COLORS['black'],(315,120),(315,360))
        pygame.draw.line(screen,COLORS['black'],(345,120),(345,360))
        pygame.draw.line(screen,COLORS['black'],(375,120),(375,360))
        pygame.draw.line(screen,COLORS['black'],(405,120),(405,360))
        pygame.draw.line(screen,COLORS['black'],(435,120),(435,360))
        pygame.draw.line(screen,COLORS['black'],(225,150),(465,150))
        pygame.draw.line(screen,COLORS['black'],(225,180),(465,180))
        pygame.draw.line(screen,COLORS['black'],(225,210),(465,210))
        pygame.draw.line(screen,COLORS['black'],(225,240),(465,240))
        pygame.draw.line(screen,COLORS['black'],(225,270),(465,270))
        pygame.draw.line(screen,COLORS['black'],(225,300),(465,300))
        pygame.draw.line(screen,COLORS['black'],(225,330),(465,330))
    # level is hard
    elif level == 3:
        size_x = 690
        size_y = 480
        pygame.display.set_mode([size_x, size_y])
        screen.fill(COLORS['wathet'])
        # draw chess board
        pygame.draw.rect(screen,COLORS['black'],(165,80,360,360),3)
        pygame.draw.line(screen,COLORS['black'],(195,80),(195,440))
        pygame.draw.line(screen,COLORS['black'],(225,80),(225,440))
        pygame.draw.line(screen,COLORS['black'],(255,80),(255,440))
        pygame.draw.line(screen,COLORS['black'],(285,80),(285,440))
        pygame.draw.line(screen,COLORS['black'],(315,80),(315,440))
        pygame.draw.line(screen,COLORS['black'],(345,80),(345,440))
        pygame.draw.line(screen,COLORS['black'],(375,80),(375,440))
        pygame.draw.line(screen,COLORS['black'],(405,80),(405,440))
        pygame.draw.line(screen,COLORS['black'],(435,80),(435,440))
        pygame.draw.line(screen,COLORS['black'],(465,80),(465,440))
        pygame.draw.line(screen,COLORS['black'],(495,80),(495,440))
        pygame.draw.line(screen,COLORS['black'],(165,110),(525,110))
        pygame.draw.line(screen,COLORS['black'],(165,140),(525,140))
        pygame.draw.line(screen,COLORS['black'],(165,170),(525,170))
        pygame.draw.line(screen,COLORS['black'],(165,200),(525,200))
        pygame.draw.line(screen,COLORS['black'],(165,230),(525,230))
        pygame.draw.line(screen,COLORS['black'],(165,260),(525,260))
        pygame.draw.line(screen,COLORS['black'],(165,290),(525,290))
        pygame.draw.line(screen,COLORS['black'],(165,320),(525,320))
        pygame.draw.line(screen,COLORS['black'],(165,350),(525,350))
        pygame.draw.line(screen,COLORS['black'],(165,380),(525,380))
        pygame.draw.line(screen,COLORS['black'],(165,410),(525,410))
    # level is crazy
    elif level == 4:
        size_x = 690
        size_y = 550
        pygame.display.set_mode([size_x, size_y])
        screen.fill(COLORS['wathet'])
        # draw chess board 16*16
        pygame.draw.rect(screen,COLORS['black'],(105,60,480,480),3)
        pygame.draw.line(screen,COLORS['black'],(135,60),(135,540))
        pygame.draw.line(screen,COLORS['black'],(165,60),(165,540))
        pygame.draw.line(screen,COLORS['black'],(195,60),(195,540))
        pygame.draw.line(screen,COLORS['black'],(225,60),(225,540))
        pygame.draw.line(screen,COLORS['black'],(255,60),(255,540))
        pygame.draw.line(screen,COLORS['black'],(285,60),(285,540))
        pygame.draw.line(screen,COLORS['black'],(315,60),(315,540))
        pygame.draw.line(screen,COLORS['black'],(345,60),(345,540))
        pygame.draw.line(screen,COLORS['black'],(375,60),(375,540))
        pygame.draw.line(screen,COLORS['black'],(405,60),(405,540))
        pygame.draw.line(screen,COLORS['black'],(435,60),(435,540))
        pygame.draw.line(screen,COLORS['black'],(465,60),(465,540))
        pygame.draw.line(screen,COLORS['black'],(495,60),(495,540))
        pygame.draw.line(screen,COLORS['black'],(525,60),(525,540))
        pygame.draw.line(screen,COLORS['black'],(555,60),(555,540))
        pygame.draw.line(screen,COLORS['black'],(105,90),(585,90))
        pygame.draw.line(screen,COLORS['black'],(105,120),(585,120))
        pygame.draw.line(screen,COLORS['black'],(105,150),(585,150))
        pygame.draw.line(screen,COLORS['black'],(105,180),(585,180))
        pygame.draw.line(screen,COLORS['black'],(105,210),(585,210))
        pygame.draw.line(screen,COLORS['black'],(105,240),(585,240))
        pygame.draw.line(screen,COLORS['black'],(105,270),(585,270))
        pygame.draw.line(screen,COLORS['black'],(105,300),(585,300))
        pygame.draw.line(screen,COLORS['black'],(105,330),(585,330))
        pygame.draw.line(screen,COLORS['black'],(105,360),(585,360))
        pygame.draw.line(screen,COLORS['black'],(105,390),(585,390))
        pygame.draw.line(screen,COLORS['black'],(105,420),(585,420))
        pygame.draw.line(screen,COLORS['black'],(105,450),(585,450))
        pygame.draw.line(screen,COLORS['black'],(105,480),(585,480))
        pygame.draw.line(screen,COLORS['black'],(105,510),(585,510))

# Draw the game running frame; 游戏运行帧
def draw_run():
    # Declare global variable_win
    global win
    # here level 1 is easy
    # Use 12 seconds to run and win
    if level == 1:
        # Determine if the snake eats and fill the entire screen
        # Because here maze**2 is the square value of maze-maze^2; 3 is the body, head and apple
        if snake.score < snake.maze**2-3:
            # If not eating up all the food and fill the screen; 没有吃满屏幕绘制食物
            # set the apple with colour orange; apple's size is 30*30
            pygame.draw.rect(screen, COLORS['orange'], pygame.Rect(snake.food[0]*30 + 286, snake.food[1]*30 + 201, 29, 29))
        else:
            pygame.draw.rect(screen, COLORS['darkblue'], pygame.Rect(snake.food[0]*30 + 286, snake.food[1]*30 + 201, 29, 29))
            # set music
            pygame.mixer.music.load('/Users/daisy/Desktop/PygameSnake/BattleCity.mp3')
            pygame.mixer.music.play()
            # sign that snake eats up and fill the screen
            win = True
        # sign of snake head
        snake_head = False
        for pose in snake.body:
            # whether it is snake head
            if snake_head == False:
                snake_head = True
                # snake head colour is blue
                pygame.draw.rect(screen, COLORS['blue'], pygame.Rect(pose[0]*30 + 286, pose[1]*30 + 201, 29, 29))
                # snake body colour is dark_blue
            else:
                pygame.draw.rect(screen, COLORS['darkblue'], pygame.Rect(pose[0]*30 + 286, pose[1]*30 + 201, 29, 29))
    # here level 2 is normal
    # Use 1'45" minutes to run and win
    elif level == 2:
        if snake.score < snake.maze**2-3:
            pygame.draw.rect(screen, COLORS['orange'], pygame.Rect(snake.food[0]*30 + 226, snake.food[1]*30 + 121, 29, 29))
        else:
            pygame.draw.rect(screen, COLORS['darkblue'], pygame.Rect(snake.food[0]*30 + 226, snake.food[1]*30 + 121, 29, 29))
            pygame.mixer.music.load('/Users/daisy/Desktop/PygameSnake/BattleCity.mp3')
            pygame.mixer.music.play()
            win = True
        snake_head = False
        for pose in snake.body:
            if snake_head == False:
                snake_head = True
                pygame.draw.rect(screen, COLORS['blue'], pygame.Rect(pose[0]*30 + 226, pose[1]*30 + 121, 29, 29))
            else:
                pygame.draw.rect(screen, COLORS['darkblue'], pygame.Rect(pose[0]*30 + 226, pose[1]*30 + 121, 29, 29))
    # here level 3 is hard
    # Use 10 minutes to run and win
    elif level == 3:
        if snake.score < snake.maze**2-3:
            pygame.draw.rect(screen, COLORS['orange'], pygame.Rect(snake.food[0]*30 + 166, snake.food[1]*30 + 81, 29, 29))
        else:
            pygame.draw.rect(screen, COLORS['darkblue'], pygame.Rect(snake.food[0]*30 + 166, snake.food[1]*30 + 81, 29, 29))
            pygame.mixer.music.load('/Users/daisy/Desktop/PygameSnake/BattleCity.mp3')
            pygame.mixer.music.play()
            win = True
        snake_head = False
        for pose in snake.body:
            if snake_head == False:
                snake_head = True
                pygame.draw.rect(screen, COLORS['blue'], pygame.Rect(pose[0]*30 + 166, pose[1]*30 + 81, 29, 29))
            else:
                pygame.draw.rect(screen, COLORS['darkblue'], pygame.Rect(pose[0]*30 + 166, pose[1]*30 + 81, 29, 29))
    # here level 4 is crazy
    elif level == 4:
        if snake.score < snake.maze**2-3:
            pygame.draw.rect(screen, COLORS['orange'], pygame.Rect(snake.food[0]*30 + 106, snake.food[1]*30 + 61, 29, 29))
        else:
            pygame.draw.rect(screen, COLORS['darkblue'], pygame.Rect(snake.food[0]*30 + 106, snake.food[1]*30 + 61, 29, 29))
            pygame.mixer.music.load('/Users/daisy/Desktop/PygameSnake/BattleCity.mp3')
            pygame.mixer.music.play()
            win = True
        snake_head = False
        for pose in snake.body:
            if snake_head == False:
                snake_head = True
                pygame.draw.rect(screen, COLORS['blue'], pygame.Rect(pose[0]*30 + 106, pose[1]*30 + 61, 29, 29))
            else:
                pygame.draw.rect(screen, COLORS['darkblue'], pygame.Rect(pose[0]*30 + 106, pose[1]*30 + 61, 29, 29))

# draw scores and time used
def draw_score():
    # declare global variable tick
    global tick
    # get the time in milliseconds
    tick = pygame.time.get_ticks()-start_time-pause_time
    # round(number, digits) get 2 digits after "."
    txt_time = font_option.render('Time:' + str(round(tick/60000%24*60,2)),True,COLORS['black'])
    txt_score = font_option.render('Score:' + str(snake.score),True,COLORS['black'])
    # set and draw with coordinates
    x,y = 100,10
    screen.blit(txt_time,(x,y))
    x,y = 440,10
    screen.blit(txt_score,(x,y))
    pygame.draw.rect(screen,COLORS['azure'],(326,18,90,32),0)
    pygame.draw.rect(screen,COLORS['black'],(326,18,90,32),2)
    txt_pause = font_pause.render('Pause',True,COLORS['black'])
    x,y = 344,22
    screen.blit(txt_pause,(x,y))

# draw win screen
def draw_win():
    screen.fill(COLORS['wathet'])
    txt_win1 = font_win.render('Congratulations!',True,COLORS['black'])
    txt_win2 = font_win.render('You win.',True,COLORS['black'])
    txt_score = font_option.render('Total time:' + str(round(tick/60000%24*60,2)),True,COLORS['black'])
    txt_time = font_option.render('Total score:' + str(snake.score),True,COLORS['black'])
    txt_back = font_stop.render('Back', True, COLORS['black'])
    # draw rectangles
    pygame.draw.rect(screen, COLORS['azure'], (240, 240, 200, 60), 0)
    pygame.draw.rect(screen, COLORS['black'], (240, 240, 200, 60), 3)
    # set and draw with coordinates
    x,y = 110,100
    screen.blit(txt_win1,(x,y))
    x,y = 222,168
    screen.blit(txt_win2,(x,y))
    x,y = 110,390
    screen.blit(txt_time,(x,y))
    x,y = 110,330
    screen.blit(txt_score,(x,y))
    x,y = 300,250
    screen.blit(txt_back,(x,y))
    
# draw pause screen
def draw_pause():
    screen.fill(COLORS['wathet'])
    # draw rectangle choice_boards
    pygame.draw.rect(screen,COLORS['azure'],(220,90,250,78),0)
    pygame.draw.rect(screen,COLORS['black'],(220,90,250,78),3)
    pygame.draw.rect(screen,COLORS['azure'],(220,210,250,78),0)
    pygame.draw.rect(screen,COLORS['black'],(220,210,250,78),3)
    pygame.draw.rect(screen,COLORS['azure'],(220,330,250,78),0)
    pygame.draw.rect(screen,COLORS['black'],(220,330,250,78),3)
    # set choice_board names
    txt_new = font_stop.render('New Game',True,COLORS['black'])
    txt_back = font_stop.render('Back to Game',True,COLORS['black'])
    txt_home = font_stop.render('Home Page',True,COLORS['black'])
    # set and draw with coordinates
    x,y = 252,108
    screen.blit(txt_new,(x,y))
    x,y = 231,227
    screen.blit(txt_back,(x,y))
    x,y = 250,345
    screen.blit(txt_home,(x,y))

# main function entrance
if __name__ == "__main__":
    # Initialize the mixer
    pygame.mixer.init()
    # load the background music
    pygame.mixer.music.load('/Users/daisy/Desktop/PygameSnake/Snake.wav')
    # play the music
    # The music repeats indefinitely if this argument is set to -1.
    pygame.mixer.music.play(-1)
    # First initialize a Snake object
    snake = Snake.Snake(4)
    # Initialize all the colors required by the game
    COLORS['black'] = (34,34,34)
    COLORS['azure'] = (172,207,234)
    COLORS['wathet'] = (235,245,253)
    COLORS['darkblue'] = (36,48,70)
    COLORS['orange'] = (235,56,2)
    COLORS['gray'] = (217,217,217)
    COLORS['blue'] = (0, 47, 167)
    # Initialize pygame-- initialize all imported pygame modules
    pygame.init()
    # create an object to help track time-- game start time
    clock = pygame.time.Clock()
    # screen width and height
    SIZE = [690,480]
    # initialize the fonts
    font_title = pygame.font.Font('/Users/daisy/Desktop/PygameSnake/mtbaskervilleetw15-roma.ttf', 80)
    font_pause = pygame.font.Font('/Users/daisy/Desktop/PygameSnake/mtbaskervilleetw15-roma.ttf', 20)
    font_start = pygame.font.Font('/Users/daisy/Desktop/PygameSnake/mtbaskervilleetw15-roma.ttf', 50)
    font_option = pygame.font.Font('/Users/daisy/Desktop/PygameSnake/mtbaskervilleetw15-roma.ttf', 40)
    font_stop = pygame.font.Font('/Users/daisy/Desktop/PygameSnake/mtbaskervilleetw15-roma.ttf', 36)
    font_win = pygame.font.Font('/Users/daisy/Desktop/PygameSnake/BaskervilleSemiBold.ttf', 60, bold=True)
    # create screen and caption
    # Set the current window caption
    # set_caption(title, icon_title = None) -> None
    pygame.display.set_caption('Perfect Snake')
    # Initialize a window or screen for display
    screen = pygame.display.set_mode(SIZE)
    # Initialize game variable
    level = 0
    # timer
    ticks = 0
    # game's start time
    start_time = 0
    # time
    tick = 0
    # pause time 暂停时间
    pause_time = 0
    # pause tick 暂停时刻
    pause_tick = 0
    # pause sign 暂停标志
    pause = False
    # the game is running
    running = True
    # Difficulty level selection sign
    choice = False
    # sign of play
    play = False
    # sign of win
    win = False
    # sign of level
    difficulty = 5
    # game main loop
    while running:
        # User input event acquisition; 用户输入事件获取
        for event in pygame.event.get():
            # The user clicks the close button and the program ends
            if event.type == pygame.QUIT:
                # end main loop and stop running
                running = False
                break
            # The event is a mouse click event
            elif event.type == pygame.MOUSEBUTTONUP:
                # Determine whether the coordinates of the user's click are
                # within the button Play
                if play == False and choice == False:
                    # User clicks the start button
                    # pos is a tuple that stores the position that was clicked
                    if 220 < event.pos[0] < 470 and 304 < event.pos[1] < 382:
                        choice = True
                elif play == False and choice == True:
                    # User chooses level easy
                    if 128 < event.pos[0] < 318 and 200 < event.pos[1] < 290:
                        level = 1
                        play = True
                        if 'snake' in globals():
                            del snake
                        snake = Snake.Snake(4)
                        start_time = pygame.time.get_ticks()
                        pause_time = 0
                    # User chooses level normal
                    elif 372 < event.pos[0] < 562 and 200 < event.pos[1] < 290:
                        level = 2
                        play = True
                        if 'snake' in globals():
                            del snake
                        snake = Snake.Snake(8)
                        start_time = pygame.time.get_ticks()
                        pause_time = 0
                    # User chooses level hard
                    elif 128 < event.pos[0] < 318 and 340 < event.pos[1] < 430:   
                        level = 3
                        play = True
                        if 'snake' in globals():
                            del snake
                        snake = Snake.Snake(12)
                        start_time = pygame.time.get_ticks()
                        pause_time = 0
                    # User chooses level crazy
                    elif 372 < event.pos[0] < 562 and 340 < event.pos[1] < 430:
                        level = 4
                        play = True
                        if 'snake' in globals():
                            del snake
                        snake = Snake.Snake(16)
                        start_time = pygame.time.get_ticks()
                        pause_time = 0
                # User clicks game to pause
                elif play == True and choice == True and win == False and pause == False:
                    if 326 < event.pos[0] < 416 and 18 < event.pos[1] < 50:
                        pause = True
                        pause_tick = pygame.time.get_ticks()

                # Game pause menu
                elif pause:
                    if 220 < event.pos[0] < 470 and 90 < event.pos[1] < 168:
                        play = False
                        pause = False
                    elif 220 < event.pos[0] < 470 and 210 < event.pos[1] < 288:
                        pause = False
                        pause_time += pygame.time.get_ticks() - pause_tick
                    elif 220 < event.pos[0] < 470 and 330 < event.pos[1] < 408:
                        play = False
                        choice = False
                        pause = False
                # Game win menu
                elif win:
                    play = False
                    choice = False
                    pause = False
                    win = False
                    pygame.mixer.music.load('/Users/daisy/Desktop/PygameSnake/Snake.wav')
                    pygame.mixer.music.play(-1)
        if win:
            # draw win screen
            draw_win()
        elif pause == False:
            if play == False and choice == False:
                # game start menu
                draw_start() 
            elif play == False and choice == True:   
                # home_page menu
                draw_menu() 
            elif play == True and choice == True:
                # draw game map
                draw_map()
                # game run
                draw_run()
                # draw score
                draw_score()
                if snake and snake.score < snake.maze**2-3:
                    snake.move()
        else:
            # the game pause
            draw_pause()
        # refresh game screen
        pygame.display.flip()
    # game exit function
    pygame.quit()
