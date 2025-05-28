from PySide6.QtWidgets import QCheckBox
from main import MainWindow

class ICheckBox:
    """
    Gerencia exibição de campos alternativos ativados por checkbox.
    """
    def aplicacao(self: MainWindow, check_box: QCheckBox):
        lineEdit, button = self.items_checkbox(check_box)

        if check_box.isChecked() == True:
            check_box.hide()
            lineEdit.show()
            lineEdit.setFocus()
            button.show()

    def remocao(self: MainWindow, check_box: QCheckBox):
        lineEdit, button = self.items_checkbox(check_box)
        
        lineEdit.setText('')
        check_box.setChecked(False)
        check_box.show()
        lineEdit.hide()
        button.hide()