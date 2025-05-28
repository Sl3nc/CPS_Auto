from pathlib import Path
from docxtpl import DocxTemplate, RichText
from unidecode import unidecode
from tkinter.filedialog import asksaveasfilename

class File:
    """
    Gerencia operações relacionadas a arquivos de contratos, como seleção de modelo,
    alteração e salvamento do documento gerado.
    """
    def __init__(self):
        self.options = ['Pessoa Física', 'Inatividade', 'Lucro Presumido', 'Simples Nacional']
        self.base_caminho = 'src\\CPS\'s\\CPS {0}.docx'
        self.current_option = ''

    def set_option(self, nome: str):
        """
        Define a opção/modelo de contrato a ser utilizado.
        """
        self.current_option = nome if nome in self.options else Exception('Nome de arquivo inválido')

    def alterar(self, base: dict, updt: dict, caminho: str): 
        """
        Renderiza e salva o documento Word com os dados fornecidos.
        """
        self.arquivo = \
            DocxTemplate(
                (Path(__file__).parent).__str__() + \
                    self.base_caminho.format(
                        unidecode(self.current_option)
                    )
            )

        self.arquivo.render(base)
        self.arquivo.save(caminho)
        self.arquivo = DocxTemplate(caminho)
        self.arquivo.render(updt)
        self.arquivo.save(caminho)

    def salvar(self):
        """
        Abre diálogo para o usuário escolher onde salvar o arquivo gerado.
        """
        caminho = asksaveasfilename(title='Defina o nome e o local onde o arquivo será salvo', filetypes=((".docx","*.docx"),))

        if caminho[caminho.rfind('/') + 1:] == '':
            raise Exception('Operação Cancelada')
        
        return caminho + '.docx'