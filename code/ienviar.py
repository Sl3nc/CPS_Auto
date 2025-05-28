from PySide6.QtWidgets import QLineEdit, QComboBox
from iexception import IExececao
from main import MainWindow

class IEnviar(IExececao):
    """
    Exceção para envio de dados de representantes.
    """
    def aplicacao(self: MainWindow, id: str):
        self.titulo_repre.setText(f'Representante {id}')

        id = self.convert_id(id)
        for key, widget in self.relacoes.items():
            if f'Contra{id}' in key and type(widget) == QLineEdit:
                widget.setText(self.referencias[key])
            elif f'Contra{id}' in key and type(widget) == QComboBox:
                widget.setCurrentText(self.referencias[key])

        self.stackedWidget_2.setCurrentIndex(0)
        self.titulo_quantidade.hide()
        self.comboBox_repre.hide()
        self.grid_repre.addWidget(self.cb_enviar_repre, 0,6)
        self.cb_enviar_repre.show()
        self.pushButton_executar.setDisabled(True)

        self.cb_enviar_repre.clicked.connect(
            lambda: IEnviar.remocao(self, id)
        )

    def remocao(self: MainWindow, id: str):
        self.absorve_preenche(id)
        self.cb_enviar_repre.clicked.disconnect()
        self.grid_repre.removeWidget(self.cb_enviar_repre)
        self.cb_enviar_repre.hide()
        self.titulo_quantidade.show()
        self.comboBox_repre.show()
        self.titulo_repre.setText('Representante')
        self.pushButton_executar.setDisabled(False)
        self.stackedWidget_2.setCurrentIndex(1)