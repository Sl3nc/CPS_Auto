from PySide6.QtGui import QValidator
from re import compile

class TextOnly(QValidator):
    """
    Validador personalizado para aceitar apenas texto (letras) em campos de entrada.
    """
    def validate(self, string, index):
        if compile("[a-zA-Z]+").fullmatch(string) or string == '':
            return QValidator.State.Acceptable
        return QValidator.State.Invalid