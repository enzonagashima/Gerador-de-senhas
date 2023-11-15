import PySimpleGUI as sg
import random
import string

def gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    caracteres = ''

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        sg.popup_error("Você deve escolher pelo menos um tipo de caractere para a senha.")
        return None

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

layout = [
    [sg.Text("Comprimento da Senha:"), sg.InputText(size=(10, 1), key='-COMPRIMENTO-')],
    [sg.Checkbox("Letras Maiúsculas", default=True, key='-MAIUSCULAS-'),
     sg.Checkbox("Letras Minúsculas", default=True, key='-MINUSCULAS-')],
    [sg.Checkbox("Números", default=True, key='-NUMEROS-'),
     sg.Checkbox("Símbolos Especiais", default=True, key='-SIMBOLOS-')],
    [sg.Button("Gerar Senha"), sg.Button("Sair")],
    [sg.Text("", size=(20, 1), key='-SENHA-')]
]

window = sg.Window("Gerador de Senhas", layout)

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, 'Sair'):
        break
    elif event == "Gerar Senha":
        comprimento = int(values['-COMPRIMENTO-'])
        incluir_maiusculas = values['-MAIUSCULAS-']
        incluir_minusculas = values['-MINUSCULAS-']
        incluir_numeros = values['-NUMEROS-']
        incluir_simbolos = values['-SIMBOLOS-']

        senha_gerada = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)

        if senha_gerada:
            window['-SENHA-'].update(senha_gerada)

window.close()

