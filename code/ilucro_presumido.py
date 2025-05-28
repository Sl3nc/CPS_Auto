from iexception import IExececao
from main import MainWindow

class ILucroPresumido(IExececao):
    """
    Exceção para contratos do tipo Lucro Presumido, exibindo campo EFD.
    """
    def aplicacao(self: MainWindow):
        self.grid_contrato.removeWidget(self.pushButton_executar)
        self.grid_contrato.addWidget(self.label_EFD,1,5)
        self.grid_contrato.addWidget(self.lineEdit_EFD, 2,5)
        self.grid_contrato.addWidget(self.pushButton_executar, 1,6, 2, 1)
        self.lineEdit_EFD.show()
        self.label_EFD.show()

    def remocao(self: MainWindow):
        self.grid_contrato.removeWidget(self.lineEdit_EFD)
        self.grid_contrato.removeWidget(self.label_EFD)
        self.lineEdit_EFD.hide()
        self.label_EFD.hide()