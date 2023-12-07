
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

bot.hotkey('win', 's')
bot.write('chrome')
bot.press('enter')
bot.sleep(2)
bot.write('https://cadastro-produtos-devaprender.netlify.app/')
bot.press('enter')
bot.sleep(2)
bot.press('tab')

workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']

produto = {}
for linha in sheet_produtos.iter_rows(min_row=2):
    produto['nome_produto'] = linha[0].value
    produto['descricao'] = linha[1].value
    produto['categoria'] = linha[2].value
    produto['codigo'] = linha[3].value
    produto['peso_kg'] = linha[4].value
    produto['dimensoes'] = linha[5].value
    produto['preco'] = linha[6].value
    produto['qtdade'] = linha[7].value
    produto['validade'] = linha[8].value
    produto['cor'] = linha[9].value
    produto['tamanho'] = linha[10].value
    produto['material'] = linha[11].value
    produto['fabricante'] = linha[12].value
    produto['pais_origem'] = linha[13].value
    produto['obs'] = linha[14].value
    produto['codigo_barras'] = linha[15].value
    produto['loc_estoque'] = linha[16].value

preencher_produto(produto)












