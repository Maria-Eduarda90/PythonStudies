import pyautogui as pg
import pyperclip as pyc
import time

emojis='❤️💕🥰😍😻💗🦋🌸💐🌹'

def destribuir_coracao(e):
    c = [
        [0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0],
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    ]

    coracao = '\u200e'

    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] == 1:
                coracao += e
            else:
                coracao += '   '
        coracao += '\n'
    
    pyc.copy(coracao)

mensagem = int(input('Número de mensagens: '))
time.sleep(5)

for i in range(mensagem):
    destribuir_coracao(emojis[i%10])
    pg.hotkey('ctrl', 'v')
    pg.press('enter')