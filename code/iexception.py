from abc import ABCMeta, abstractmethod

class IExececao(metaclass=ABCMeta):
    """
    Interface para exceções de comportamento na interface gráfica.
    """
    @abstractmethod
    def aplicacao(self):
        pass

    @abstractmethod
    def remocao(self):
        pass
