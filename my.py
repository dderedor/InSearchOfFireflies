# venv\Scripts\Activate.ps1 активация
# https://www.iconfinder.com сайт с иконками





import pygame

pygame.init() #инициализация
screen = pygame.display.set_mode((1000, 600)) #размер экрана , flags=pygame.NOFRAME
pygame.display.set_caption('Ежик')
icon = pygame.image.load('image/icon.webp') #иконка
pygame.display.set_icon(icon)

squere = pygame.Surface((50,200)) #квадрат размер квадрата#squere.fill((80, 100, 100))
squere.fill('Blue')#отрисовка

tekst = pygame.font.Font('fonts.ttf', 40) #шрифт и размер шрифта
tekst_surface = tekst.render('hello!', True, 'Red' ) #надпись,сглаживание,цвет,задний фон


run = True
while run:
#   screen.fill((8, 25, 59)) # цвет заднего фона rgb

    pygame.draw.circle(screen, (1, 100, 100),( 100, 100), 30)
    screen.blit(squere, (100,100)) #отрисовка квадрата, координаты
    screen.blit(tekst_surface, (200,100)) #отрисовка текста, координаты



    pygame.display.update()
    for event in pygame.event.get():#список событий
        if event.type == pygame.QUIT:
            run = False
            pygame.quit() # выход
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_1: # если нажатие на определенную клавишу то..
                screen.fill((78, 127, 2)) #меняем цвет экрана









import pygame

pygame.init() #инициализация
screen = pygame.display.set_mode((960, 768)) #размер экрана , flags=pygame.NOFRAME
pygame.display.set_caption('Ежик')
icon = pygame.image.load('image/icon.webp') #иконка
pygame.display.set_icon(icon)

hedgehog_down_img = pygame.image.load('image/hedgehog_down.png') #изображение ежика
hedgehog_up_img = pygame.image.load('image/hedgehog_up.png')
hedgehog_left_img = pygame.image.load('image/hedgehog_left.png')
hedgehog_right_img = pygame.image.load('image/hedgehog_right.png')
#начальный спрайт
current_hedgehog_img = hedgehog_down_img # Начинаем с вида вниз

hedgehog_x = 430  # начальные координаты и скорость
hedgehog_y = 600  #
hedgehog_speed = 5  #скорость

# размеры экрана
screen_width = screen.get_width()
screen_height = screen.get_height()
#трава
grass_img = pygame.image.load('image/trava.png')
tile_size = grass_img.get_width()
#Определяем размеры карты
map_w = 10 #ширина
map_h = 41 #высота
mpw = map_w * tile_size
mph = map_h * tile_size
#карта, заполнение травой
karta_grass = [[0 for _ in range(map_w)] for _ in range(map_h)]
#создание камеры
camera_x = 0
camera_y = 0



run = True
while run:
    #Отрисовываем карту
    for tile_y in range(map_h): # Перебираем все тайлы по высоте
        for tile_x in range(map_w): # Перебираем все тайлы по ширине
            tile_rect = pygame.Rect(tile_x * tile_size - camera_x, tile_y * tile_size - camera_y, tile_size, tile_size)#Вычисляем координаты тайла на карте (в пикселях)
            #находится ли тайл в пределах экрана
            if screen.get_rect().colliderect(tile_rect):
                #отрисовывка тайтла
                screen.blit(grass_img, tile_rect)

    screen.blit(current_hedgehog_img,(hedgehog_x,hedgehog_y))#рисуем ежа по координатам

    # Получаем информацию о нажатых клавишах
    keys = pygame.key.get_pressed()
    # Изменяем координаты ёжика в зависимости от нажатых клавиш
    if keys[pygame.K_LEFT]:
        if hedgehog_x > 0:
            hedgehog_x -= hedgehog_speed
        current_hedgehog_img = hedgehog_left_img
        # Меняем спрайт на вид слева
        current_hedgehog_img = hedgehog_left_img
    if keys[pygame.K_RIGHT]:
        if hedgehog_x < screen_width - current_hedgehog_img.get_width():
            hedgehog_x += hedgehog_speed
        current_hedgehog_img = hedgehog_right_img
        # Меняем спрайт на вид справа
        current_hedgehog_img = hedgehog_right_img
    if keys[pygame.K_UP]:
        if hedgehog_y > 0:
            hedgehog_y -= hedgehog_speed
        current_hedgehog_img = hedgehog_up_img
        # Меняем спрайт на вид спереди
        current_hedgehog_img = hedgehog_up_img

    if keys[pygame.K_DOWN]:
        if hedgehog_y < screen_height - current_hedgehog_img.get_height():
            hedgehog_y += hedgehog_speed
        current_hedgehog_img = hedgehog_down_img
        # Меняем спрайт на вид сзади
        current_hedgehog_img = hedgehog_down_img  






    pygame.display.update()
    for event in pygame.event.get():#список событий
        if event.type == pygame.QUIT:
            run = False
            pygame.quit() # выход