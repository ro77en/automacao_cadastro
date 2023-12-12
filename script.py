
from functions import *
import openpyxl

# Bot para fazer lançamento de produtos (planilha) para um sistema
# 1- Abrir planilha e site
# 2- Copiar da planilha e colar no campo correspondente (repetir)
# 3- Proximo
# 4- Finalizar -> OK
# 5- Adicionar mais um e repetir

# pyautogui -> automação click e teclado
# openpyxl -> automatizar e ler planilhas

site = 'https://cadastro-produtos-devaprender.netlify.app/'

bot.hotkey('win', 's')
bot.write('chrome')
bot.press('enter')
bot.sleep(2)
bot.write(site)
bot.press('enter')
bot.sleep(2)
bot.press('tab')

workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']


column_names = [cell.value for cell in sheet_produtos[1]]
for row in sheet_produtos.iter_rows(min_row=2, values_only=True):
    produto = {}
    for index, column in enumerate(column_names):
        produto[column] = row[index]
    preencher_produto(produto)
    bot.press('enter')
    bot.sleep(1)
    bot.press('tab')
    bot.press('enter')
    bot.sleep(1)
    bot.press('tab')        


