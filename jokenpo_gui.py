from random import choice
from time import sleep
import PySimpleGUI as sg

class Jokenpo():

    sg.theme('DarkGrey13')
    
    def iniciar(self):
        self.layout = [
            [sg.Text('============== JOKENPÔ ==============')],
            [sg.Text('Você jogara Jokenpô com a máquina, escolha uma das opções...')],
            [sg.Button('Pedra'), sg.Button('Papel'), sg.Button('Tesoura'), sg.Button('Sair')],
            [sg.Output(size=(40, 10))]
        ]

        self.janela = sg.Window('Jokenpô!!', layout=self.layout)

        escolhas = ['Pedra', 'Papel', 'Tesoura']

        while True:

            self.evento, self.valores = self.janela.Read()
            if self.evento == 'Sair':
                break

            self.player = self.evento

            self.cpu = choice(escolhas)

            # ANIMAÇÃO "COMPUTANDO..."
            if self.evento != 'Sair':
                print('------------------------------------------------------------------')
                print('Escolhendo',end='')
                for i in range(1, 4):
                    print('.',end='')
                    sleep(.7)
                print()

                # PLAYER VENCE
                if (self.player == 'Pedra' and self.cpu == 'Tesoura') or (self.player == 'Papel' and self.cpu == 'Pedra') or (self.player == 'Tesoura' and self.cpu == 'Papel'):
                    print('O PLAYER VENCEU!!!')
                    

                # CPU VENCE
                elif (self.player == 'Pedra' and self.cpu == 'Papel') or (self.player == 'Papel' and self.cpu == 'Tesoura') or (self.player == 'Tesoura' and self.cpu == 'Pedra'):
                    print('A MÁQUINA VENCEU!!!')

                # EMPATE
                elif (self.player == self.cpu):
                    print('HOUVE UM EMPATE!!!')

                print(f'Você Escolheu {self.player}')
                print(f'A Máquina Escolheu {self.cpu}\n\n')

# programa
j = Jokenpo()
j.iniciar()
