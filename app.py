import pygame
from pygame.locals import *
from sys import exit

pygame.init()


pygame.mixer.music.set_volume(0.05)
musica_de_fundo = pygame.mixer.music.load('musicafundo.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(0.5)

largura = 640
altura = 480
x = int(largura/2)
y = int(altura/2) #meio da tela

from random import randint
x_azul = randint(40, 600)
y_azul = randint(50, 430) #escolhe um valor entre os declarados

fonte = pygame.font.SysFont('arial', 40, True, True) #negrito e italico
pontos = 0
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(10)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

            
       # if event.type == KEYDOWN: #evento de apertar tecla
        #    if event.key == K_a: #quando aperta a tecla a
         #       x = x - 20
          #  if event.key == K_d:
           #     x = x + 20
            #if event.key == K_w:
             #   y = y - 20
           # if event.key == K_s:
            #    y = y + 20
    
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    ret_vermelho = pygame.draw.rect(tela,(255,0,0), (x, y, 40, 50)) #posicao x y largura altura
    ret_azul = pygame.draw.rect(tela,(0,0,255), (x_azul,y_azul, 40, 50))

    if ret_vermelho.colliderect(ret_azul):
       x_azul = randint(40, 600)
       y__azul = randint(50, 430)
       pontos = pontos + 1
       barulho_colisao.play
    
    #if y >= altura:
    #    y=0 #para voltar ao começo
    #y = y+1
    
    #pygame.draw.circle(tela, (0,0, 255), (300, 260), (40)) #cor posicao raio
    #pygame.draw.line(tela, (255,255,0), (390, 0), (390, 600), 5) #posicao inicial e final, espessura

    tela.blit(texto_formatado,(450, 40))
    pygame.display.update()