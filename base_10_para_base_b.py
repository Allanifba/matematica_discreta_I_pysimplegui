import PySimpleGUI as sg

def f_base_10_para_base_b():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################

    def base_10_para_base_b(n, b):
        base_n = ""
        n1 = int(n)
        b = int(b)
        print('____________________________________________RESPOSTA_____________________________________________')
        while n > 0:
            dig = int(n % b)
            if dig < 10:
                base_n += str(dig)
            else:
                base_n += chr(ord('A') + dig - 10)
            n //= b
        base_n = base_n[::-1]
        return print(f'O valor correspondente ao número decimal {n1} na base {b} é {base_n}.')

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Base 10 para base b (max 36)')],
        [sg.Output(size=(100, 20), font='Times 10 bold')],
        [sg.Text('Digite o número decimal:')],
        [sg.Input(key='-n-', do_not_clear=True,size=(30,1))],
        [sg.Text('Digite a base:')],
        [sg.Input(key='-b-', do_not_clear=True,size=(10,1))],
        [sg.Button('Calcular', bind_return_key=True),
         sg.Button('Tutorial', bind_return_key=True)],
        [sg.Button('Voltar', bind_return_key=True)]

    ]

    window = sg.Window('Matemática Discreta I - youtube: @prof_allanIFBA', layout)


    event = 0

    while event != 'Voltar':

        event, values = window.read()
        n = values['-n-']
        b = values['-b-']

        if event == 'Calcular':
            try:
                n = int(n)
            except:
                print("Digite um valor válido.\n")
                continue
            try:
                b = int(b)
                if (b < 2) or (b > 36):
                    raise ValueError()
            except:
                print("Digite uma base inteira positiva válida (de 2 a 36).\n")
                continue


            base_10_para_base_b(n,b)

        if event == 'Tutorial':
            print('____________________________________________TUTORIAL_____________________________________________\n'
                  'Por exemplo, para converter o número decimal 12 para a base 7, digite 12 na primeira entrada e 7'
                  'na segunda. A resposta esperada é:\n'
                  '____________________________________________RESPOSTA_____________________________________________\n'
                  'O valor correspondente ao número decimal 12 na base 7 é 15.\n'
                  '____________________________________________________________________________________________________\n')

    window.close()

