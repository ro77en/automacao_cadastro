import pyperclip
import pyautogui as bot

def preencher_produto(produto):
    '''
    Preenche os campos do sistema web com as informações do produto passado
    A função verifica sempre o primeiro item de cada página, esperando com que a página carregue totalmente para preencher as informações corretamente

    Parameters:
        produto (dict): dicionário contendo as informações do produto

    '''
    for chave, valor in produto.items():
        bot.sleep(0.5)
        if chave == 'Descrição':
            pyperclip.copy(valor)
            bot.hotkey('ctrl', 'v')
            bot.press('tab')
        elif chave == 'Preço':
            bot.sleep(1)
            bot.press('tab')
            pyperclip.copy(valor)
            bot.hotkey('ctrl', 'v')
            bot.press('tab')
        elif chave == 'Fabricante':
            bot.sleep(1)
            bot.press('tab')
            pyperclip.copy(valor)
            bot.hotkey('ctrl', 'v')
            bot.press('tab')
        elif chave == 'Tamanho':
            bot.press('enter')
            if valor == 'Grande':
                bot.press('g')
                bot.press('enter')
            elif valor == 'Médio':
                bot.press('m')
                bot.press('enter')
            else:
                bot.press('p')
                bot.press('enter')
            bot.press('enter')
            bot.press('tab')
        else:
            pyperclip.copy(valor)
            bot.hotkey('ctrl', 'v')
            bot.press('tab')
            bot.press('enter')


        

    