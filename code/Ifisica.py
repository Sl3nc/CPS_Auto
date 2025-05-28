from iexception import IExececao
from main import MainWindow

class IFisica(IExececao):
    """
    Exceção para contratos do tipo Pessoa Física, ocultando campos de empresa.
    """
    def aplicacao(self: MainWindow):
        for layout in [self.grid_empresa, self.intro_empresa]:
            for i in range(layout.count()):
                layout.itemAt(i).widget().hide()

    def remocao(self: MainWindow):
        for layout in [self.grid_empresa, self.intro_empresa]:
            for i in range(layout.count()):
                layout.itemAt(i).widget().show()