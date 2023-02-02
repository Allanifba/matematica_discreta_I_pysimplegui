'''
RODANDO A PRIMEIRA VEZ (PyCharm)
[1] No terminal instale as bibliotecas, PySimpleGUI, webbrowser, os, numpy (e mais alguma se eu esqueci - aparecerá como
erro acusando a falta do módulo)
[2] Rode o arquivo mestre.py

GERANDO UM EXECUTÁVEL .EXE (PyCharm)
[1] Para gerar um arquivo executável coloque todos os arquivos em um mesmo diretório.
[2] No terminal digite
   [2.1] pip install pyinstaller
   [2.2] pyinstaller --onefile mestre.py
[3] O arquivo exe encontra-se na pasta dist
'''


import PySimpleGUI as sg
import webbrowser
import os


def f_mestre():
    layout = [
        [sg.Text('                                   Funcionalidade Disponíveis')],
        [sg.Text('----------------------------------------------Bases Numéricas---------------------------------------------\n'
                 '1 - Conversão da base 10 pra a base b (max 36)\n',
                 font='defalut 9')],
        [sg.Output(visible=False)],
        [sg.Text('Digite uma das opções acima e aperte seguir:',font='defalut 9')],
        [sg.Input(key='-escolha-', size=(10,1)),
         sg.Button('Seguir', bind_return_key=True)],
        [sg.Text('Autoria: Allan de Sousa Soares, professor do Instituto Federal de Educação, \n'
                 'Ciência e Tecnologia da Bahia - Campus Vitória da Conquista - IFBAVDC',font='defalut 9')],
        [sg.Text('Clique nos botões para navegar nas minhas páginas!',font='defalut 9')],
        [sg.Text('Acesse o Código Completo:',font='defalut 9'),
         sg.Button('Código', bind_return_key=True,font='defalut 9')],
        [sg.Text('Links Úteis:', font='defalut 9'),
         sg.Button('+Links', bind_return_key=True, font='defalut 9')],
    ]

    window = sg.Window('Matemática Discreta I - youtube: @prof_allanIFBA', layout)


    event = 0

    while True:

        event, values = window.read()


        escolha = values['-escolha-']

        if event == 'Seguir' and escolha == '1':
            from base_10_para_base_b import f_base_10_para_base_b
            f_base_10_para_base_b()



        if event == 'Código':
            os.system("start \"\" https://github.com/Allanifba/calculo_numerico_pysimplegui")

        if event == '+Links':
            from links import f_links
            f_links()

while True:

    f_mestre()

