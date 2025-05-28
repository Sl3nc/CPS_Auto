from PySide6.QtCore import QObject, Signal
from file import File

class Worker(QObject):
    """
    Executa a geração do contrato em uma thread separada para não travar a interface.
    """
    inicio = Signal()
    fim = Signal(str)

    def __init__(self, file: File, base: dict, atualizado: dict) -> None:
        super().__init__()
        self.file = file
        self.base = base
        self.atualizado = atualizado
        
        self.addctional_base = [
            'valPorc', 'dtInic', 'dtAss', 'nomeEmp', 'cnpjEmp', 'numEmpre','dtVenc', 'valPag', 'dtCompe', 'diaVenc'
        ]

    def main(self):
        """
        Executa o processo de geração e salvamento do contrato.
        """
        caminho = self.file.salvar() 
        self.inicio.emit()
        for i in self.addctional_base:
            self.base[i] = self.atualizado[i]
        self.file.alterar(self.base, self.atualizado, caminho)
        self.fim.emit(caminho)