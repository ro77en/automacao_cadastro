import pyperclip
import pyautogui as bot

def preencher_produto(produto):
    bot.sleep(0.5)
    for chave, valor in produto.items():
        pyperclip.copy(valor)
        bot.hotkey('ctrl', 'v')
        bot.press('tab')
        bot.press('enter')

    