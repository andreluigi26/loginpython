import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Login')],
    [sg.Text('',key='mensagem')],
]   

janela = sg.Window('Login', layout=layout)


while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == 'Login':
        senha_correta = '123456'
        usuario_correto = 'andreluigi'
        usuario = values['usuario']
        senha = values ['senha']
        if senha == senha_correta and usuario == usuario_correto:
            janela['mensagem'].update('Login feito com sucesso!')
        else:
            janela['mensagem'].update('Senha ou usuario incorreto!')
