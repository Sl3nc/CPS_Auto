from docxtpl import DocxTemplate, RichText
import os

def oi(base, updt, arquivo, caminho):
    arquivo.render(base)
    arquivo.save(caminho)
    arquivo = DocxTemplate(caminho)
    arquivo.render(updt)
    arquivo.save(caminho)

arquivo = DocxTemplate('code/CPS\'s/CPS PESSOA FISICA.docx')

nome = input('Nome do arquivo: ')
caminho = f'c:/Users/DELTAASUS/Downloads/{nome}.docx'
a = RichText('oooi', bold=True)
b = RichText('Sesas', italic=True)
oi(
    {'cabecalho': '{{r oi }} {{r sese }}'},
     
    {'oi': a, 'sese': 'oi'},
    arquivo,
    caminho)

os.startfile(caminho)

