from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки')

#задай фон сцены
background = transform.scale(
    image.load('background.png'),
    (700, 500)
)
game = True

#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(
    image.load('images.jpg'),
    (100, 100)
)

sprite2 = transform.scale(
    image.load('sprite2.png'),
    (100, 100)
)

x1 = 300
x2 = 500
y1 = 360
y2 = 350

clock = time.Clock()
FPS = 60

while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP] and y1 > 0:
        y1 -= 10
    elif keys_pressed[K_DOWN] and y1 < 395:
        y1 += 10
    elif keys_pressed[K_RIGHT] and x1 < 600:
        x1 += 10
    elif keys_pressed[K_LEFT] and x1 > 0:
        x1 -= 10
    elif keys_pressed[K_w] and y2 > 0:
        y2 -= 10
    elif keys_pressed[K_s] and y2 < 395:
        y2 += 10
    elif keys_pressed[K_d] and x2 < 600:
        x2 += 10
    elif keys_pressed[K_a] and x2 > 0:
        x2 -= 10

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)



#обработай событие «клик по кнопке "Закрыть окно"»