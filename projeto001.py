# criando tela de login
# sg -> cria uma interface

from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('DarkBlue')

layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

#Janela/Tela
janela = sg.Window('Tela de Login', layout)

#ler os eventos
while True:
    eventos, valores =janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'agatha' and valores['senha'] == '123456':
            print('Bem-vindo ao nosso teste!')


