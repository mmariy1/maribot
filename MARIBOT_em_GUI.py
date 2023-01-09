import PySimpleGUI as sg
import datetime
import requests
import random

nome_usuario = 'jjj'
numero_usuario = 2

#Janelas ja feitas: INICIAL, PREVISAO DO TEMPO, JOGOS, JOKENPO
#Falta: Adivinhe o Numero em JOGOS, jogo da velha em JOGOS, conversao de numeros em INICIAL

#para a randomizacao do pedra papel e tesoura
escolhaBot = ['Pedra', 'Papel', 'Tesoura']
jogadaBot = 'batata'

#para a randomizacao do adivinhe o numero
resultado_vitoria_derrota = 'banana'
numerobot = 2

chave_api = 'b8fb07b4b2009b78d41f0757dcf97423'
cidade = 'São Paulo'
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br'
requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
temp_max = requisicao_dic['main']['temp_max'] - 273.15
temp_min = requisicao_dic['main']['temp_min'] - 273.15

#Layout das telas
def telaNome():
    sg.theme('LightBrown11')
    layout = [
        [sg.Text('Como voce se chama?')],
        [sg.Input(key= 'usuario', size=(20,1))],
        [sg.Button('Entrar')]
        ]
    return(sg.Window('Entrada', layout= layout, finalize= True))

def telaJokenpo():
    sg.theme('LightBrown11')
    layout = [
        [sg.Text('Escolha um', font=(80), size=(21), justification='center')],
        [sg.Text('', size = 1), sg.Button('Pedra'), sg.Button('Papel'), sg.Button('Tesoura'), sg.Text('', size = 1)],
        [sg.Text('')],
        [sg.Text('', size = 8), sg.Button('Voltar')]
    ]
    return sg.Window('JoKenPo', layout=layout, finalize=True)

def telaResultado():
    sg.theme('LightBrown11')
    layout = [
        [sg.Text(txtResultado)],
        [sg.Text('Escolha do bot: '), sg.Text(jogadaBot)],
        [sg.Button('Jogar denovo'), sg.Button('Voltar ao inicio')]
    ]
    return sg.Window(txtResultado, layout=layout, finalize=True)

def telaInicial():
    sg.theme('LightBrown11')
    layout = [
        [sg.Text('Ola, '), sg.Text(nome_usuario)],
        [sg.Button('Jogos'), sg.Button('Previsao do Tempo')],
        [sg.Button('Conversao de Numeros')]
    ]
    return(sg.Window('MARIBOT', layout= layout, finalize= True))

def telaJogos():
    sg.theme('LightBrown11')
    layout = [
        [sg.Button('Adivinhe o Numero'), sg.Button('Jokenpo'), sg.Button('Jogo da Velha')],
        [sg.Button('Voltar')]
    ]
    return(sg.Window('Jogos', layout= layout, finalize= True))

def telaPrevisaoDoTempo():
    sg.theme('LightBrown11')
    layout = [
        [sg.Text('Clima hoje em SP:'), sg.Text(descricao.title())],
        [sg.Text('Temperatura atual:'), sg.Text(int(temperatura)), sg.Text('°C')],
        [sg.Text('Temperatura máxima:'), sg.Text(int(temp_max)), sg.Text('°C')],
        [sg.Text('Temperatura mínima:'), sg.Text(int(temp_min)), sg.Text('°C')],
        [sg.Button('Voltar')]
    ]
    return(sg.Window('Clima', layout= layout, finalize= True))

def telaAdivinheONumero():
    sg.theme('LightBrown11')
    layout = [
        [sg.Text('Em qual numero estou pensando?')],
        [sg.Text('Dica: Entre 1 a 10')],
        [sg.Input(key = 'numero', size = (20, 1)), sg.Button('É Este!')]
    ]

    return(sg.Window('Adivinhe o Numero', layout = layout, finalize = True))

def telaResultadoNumero():
    sg.theme('LightBrown11')
    layout = [
        [sg.Text(resultado_vitoria_derrota)],
        [sg.Text('Escolha do bot:'), sg.Text(numerobot)],
        [sg.Button('Jogar de novo'), sg.Button('Voltar ao inicio')]
    ]
    return(sg.Window(resultado_vitoria_derrota, layout= layout, finalize = True))
#Criando as janelas

janelaLogin, janelaInicial, janelaJogos, janelaJokenpo, janelaPrevisao, janelaResultado, janelaAdivinheoNumero, janelaResultadoNumero = telaNome(), None, None, None, None, None, None, None

#Criando um Loop para que as janelas abram
while True:
    janela, evento, valor = sg.read_all_windows()
#Caso a aba seja fechada
    if evento == sg.WINDOW_CLOSED:
        break
#Indo da aba de nome para a aba inicial de MARIBOT
    if janela == janelaLogin and evento == 'Entrar':
        if valor['usuario'] != '':
            nome_usuario = valor['usuario']
            janelaInicial = telaInicial()
            janelaLogin.hide()
        else:
            break

    if janela == janelaInicial and evento == 'Jogos':
        janelaJogos = telaJogos()
        janelaInicial.hide()
    if janela == janelaJogos and evento == 'Jokenpo':
        janelaJokenpo = telaJokenpo()
        janelaJogos.hide()
        jogadaBot = random.choice(escolhaBot)
    if janela == janelaJogos and evento == 'Voltar':
        janelaInicial.un_hide()
        janelaJogos.hide()
    if janela == janelaResultado and evento == 'Voltar ao inicio':
        janelaResultado.hide()
        janelaInicial.un_hide()
    if janela == janelaResultado and evento == 'Jogar denovo':
        janelaResultado.hide()
        janelaJokenpo.un_hide()
        jogadaBot = random.choice(escolhaBot)
    if janela == janelaInicial and evento == 'Previsao do Tempo':
        janelaPrevisao = telaPrevisaoDoTempo()
        janelaInicial.hide()
    if janela == janelaPrevisao and evento == 'Voltar':
        janelaInicial.un_hide()
        janelaPrevisao.hide()
    if janela == janelaJokenpo and evento == 'Voltar':
        janelaJokenpo.hide()
        janelaJogos.un_hide()
    if janela == janelaJogos and evento == 'Adivinhe o Numero':
        janelaJogos.hide()
        janelaAdivinheoNumero = telaAdivinheONumero()
        numerobot = random.randint(1, 10)

    if evento == 'É Este!':
        if valor['numero'] == str(numerobot):
            resultado_vitoria_derrota = 'Vitoria'
        else:
            resultado_vitoria_derrota = 'Derrota'

        janelaAdivinheoNumero.hide()
        janelaResultadoNumero = telaResultadoNumero()


    if janela == janelaResultadoNumero and evento == 'Jogar de novo':
        janelaAdivinheoNumero.un_hide()
        janelaResultadoNumero.hide()
        numerobot = random.randint(1, 10)
    if janela == janelaResultadoNumero and evento == 'Voltar ao inicio':
        janelaInicial.un_hide()
        janelaResultadoNumero.hide()

    if evento == 'Pedra':
        if jogadaBot == 'Pedra':
            txtResultado = 'Empate'
            janelaJokenpo.hide()
            janelaResultado = telaResultado()

        elif jogadaBot == 'Tesoura':
            txtResultado = 'Vitoria'
            janelaJokenpo.hide()
            janelaResultado = telaResultado()

        else:
            txtResultado = 'Derrota'
            janelaJokenpo.hide()
            janelaResultado = telaResultado()

#JOKENPO escolhas
    if evento == 'Papel':
        if jogadaBot == 'Papel':
            txtResultado = 'Empate'
            janelaJokenpo.hide()
            janelaResultado = telaResultado()

        elif jogadaBot == 'Pedra':
            txtResultado = 'Vitoria'
            janelaJokenpo.hide()
            janelaResultado = telaResultado()

        else:
            txtResultado = 'Derrota'
            janelaJokenpo.hide()
            janelaResultado = telaResultado()

    if evento == 'Tesoura':
        if jogadaBot == 'Tesoura':
            txtResultado = 'Empate'
            janelaJokenpo.hide()
            janelaResultado = telaResultado()

        elif jogadaBot == 'Papel':
            txtResultado = 'Vitoria'
            janelaJokenpo.hide()
            janelaResultado = telaResultado()

        else:
            txtResultado = 'Derrota'
            janelaJokenpo.hide()
            janelaResultado = telaResultado()