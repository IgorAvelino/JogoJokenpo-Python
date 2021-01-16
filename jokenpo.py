from random import randint
from time import sleep
from resultados import player_vence, cpu_vence, empate

print('========= JOKENPÔ =========')

pedra = 'Pedra'
papel = 'Papel'
tesoura = 'Tesoura'

cpu = ['']
num = randint(1, 3)
if num == 1:
    cpu = pedra
elif num == 2:
    cpu = papel
elif num == 3:
    cpu = tesoura

print('Você jogara Jokenpô com a máquina, escolha uma das opções...')
esc = int(input('Escolha:\n\033[35m[ 1 ] Pedra\033[0;0m\n\033[36m[ 2 ] Papel\033[0;0m\n\033[33m[ 3 ] Tesoura\033[0;0m\nDigite sua Escolha: '))

player = ['']
if esc == 1:
    player = pedra
elif esc == 2:
    player = papel
elif esc == 3:
    player = tesoura

# ANIMAÇÃO "COMPUTANDO..."
print('Escolhendo a melhor opção para te derrotar',end='')
for i in range(1, 4):
    print('.',end='')
    sleep(.7)

print()
# PLAYER VENCE
if (player == pedra and cpu == tesoura) or (player == papel and cpu == pedra) or (player == tesoura and cpu == papel):
    player_vence()

# CPU VENCE
elif (player == pedra and cpu == papel) or (player == papel and cpu == tesoura) or (player == tesoura and cpu == pedra):
    cpu_vence()

# EMPATE
elif (player == cpu):
    empate()
    
print(f'A Máquina Escolheu {cpu}!!!\033[0;0m')
print('\n\033[32mFim de Jogo...\033[0;0m')
