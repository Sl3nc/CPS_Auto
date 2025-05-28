from PySide6.QtWidgets import (
    QMainWindow, QApplication, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton, QSpinBox, QDoubleSpinBox
)
from PySide6.QtGui import QPixmap, QIcon, QMovie
from ilucro_presumido import ILucroPresumido
from PySide6.QtCore import QThread, QSize
from src.window_cps import Ui_MainWindow
from locale import setlocale, LC_ALL
from iexception import IExececao
from icheckbox import ICheckBox
from traceback import print_exc
from tkinter import messagebox
from text_only import TextOnly
from postman import Correios
from content import Conteudo
from ienviar import IEnviar
from Ifisica import IFisica
from worker import Worker
from copy import deepcopy
from notice import Aviso
from pathlib import Path
from os import startfile
from file import File

setlocale(LC_ALL, 'pt_BR.UTF-8')

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Classe principal da interface gráfica. Gerencia eventos, widgets e fluxo do programa.
    """
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        # self.vez = 1

        #1 a mais do criado pois é o máximo (n<max), não os disponíveis
        self.max_repre = 4

        self.ID_MENU = 0
        self.ID_FORM = 1
        self.ID_LOAD = 2
          
        self.file = File()
        self.excecao = None

        self.setWindowTitle('Gerador de CPS')

        self.setWindowIcon(QIcon(
            (Path(__file__).parent / 'src'/'imgs'/'cps-icon.ico').__str__())
        )

        self.movie = QMovie(
            (Path(__file__).parent / 'src'/'imgs'/'loadgif').__str__()
        )
        self.gif_load.setMovie(self.movie)

        self.atual_stacked_2 = 0

        self.label_EFD = QLabel('Valor EFD')
        self.lineEdit_EFD = QLineEdit()

        self.cb_enviar_repre = QPushButton()
        self.cb_enviar_repre.setText('Enviar')

        self.referencias = {}

        self.relacoes = {
            'nomeEmp': self.lineEdit_nome_empresa,
            'cnpjEmp': self.lineEdit_cnpj_empresa,
            'cepEmp': self.lineEdit_cep_empresa,
            'ruaEmp': self.lineEdit_endereco_empresa,
            'numEmpre': self.lineEdit_numero_empresa,
            'bairroEmp': self.lineEdit_bairro_empresa,
            'compleEmp': self.lineEdit_complemento_empresa,
            'valPag': self.lineEdit_valor_contrato,
            'dtInic': self.lineEdit_dt_inicio_contrato,
            'dtAss': self.lineEdit_dt_assinatura_contrato,
            'dtVenc': self.lineEdit_dia_vencimento_contrato,
            'numEmpre': self.lineEdit_num_empreg_contrato,
            'valorEFD': self.lineEdit_EFD
        }

        self.valores_contratante = {
            'funcaoContra': self.comboBox_funcao_repre,
            'nomeContra': self.lineEdit_nome_repre,
            'rgContra': self.lineEdit_rg_repre,  
            'cpfContra': self.lineEdit_cpf_repre, 
            'emissorContra': self.lineEdit_orgao_repre, 
            'estadoCivilContra': self.comboBox_estado_civil_repre,
            'cepContra': self.lineEdit_cep_repre,  
            'ruaContra': self.lineEdit_endereco_repre, 
            'numContra': self.lineEdit_numero_repre, 
            'bairroContra': self.lineEdit_bairro_repre,  
            'cidadeContra': self.lineEdit_cidade_repre, 
            'estadoContra': self.lineEdit_estado_repre, 
            'compleContra': self.lineEdit_complemento_repre,
            'nacionalidadeContra': self.lineEdit_nacio, 
            'empregoContra': self.lineEdit_cargo,
        }
        #Colocar aqui seu lineEdit da janela, se este estiver vazio, fica como "brasileiro"
        
        self.init_reference()

        self.widgets_especials = {
            'cnpjEmp': self.lineEdit_cnpj_empresa,
            'cepEmp': self.lineEdit_cep_empresa,
            'dtInic': self.lineEdit_dt_inicio_contrato,
            'dtAss': self.lineEdit_dt_assinatura_contrato
        }

        self.widgets_especials_contra = {
            'rgContra': self.lineEdit_rg_repre,
            'cpfContra': self.lineEdit_cpf_repre,
            'cepContra': self.lineEdit_cep_repre,
        }

        self.relacoes_validator ={
            self.lineEdit_nome_repre: TextOnly(),
            self.lineEdit_orgao_repre: TextOnly(),
            self.lineEdit_nacio: TextOnly(),
            self.lineEdit_cargo: TextOnly(),
            self.lineEdit_cidade_repre: TextOnly(),
            self.lineEdit_estado_repre: TextOnly()
        }

        for widget, validator in self.relacoes_validator.items():
            widget.setValidator(validator)

        self.relacao_ids = {'A':1,'B':2,'C':3}
        self.relacoes_label_cliente = {
            'nomeContra1': self.label_nome_input_clienteA,
            'nomeContra2': self.label_nome_input_clienteB,
            'nomeContra3': self.label_nome_input_clienteC,
            'cpfContra1': self.label_cpf_input_clienteA,
            'cpfContra2': self.label_cpf_input_clienteB,
            'cpfContra3': self.label_cpf_input_clienteC,
        }

        self.relacoes_checkbox = {
            self.checkBox_nacio_repre : [self.lineEdit_nacio, self.pushButton_nacio],
            self.checkBox_cargo_repre: [self.lineEdit_cargo, self.pushButton_cargo]
        }

        for i in [self.lineEdit_nacio, self.pushButton_nacio, self.lineEdit_cargo, self.pushButton_cargo]:
            i.hide()

        self.relacoes_nacio_emprego = {
            'nacionalidadeContra': 'Brasileiro(a)', 'empregoContra':'Empresário(a)'
        }

        self.relacao_numeros = {
            self.radioButton_numero_empresa: 'numEmpre',
            self.radioButton_numero_repre: 'numContra{0}'
        }

        self.correio_empresa = [
            self.lineEdit_cep_empresa, self.lineEdit_endereco_empresa, self.lineEdit_bairro_empresa
        ]
        
        self.correio_repre = [
            self.lineEdit_cep_repre, self.lineEdit_endereco_repre, self.lineEdit_bairro_repre, self.lineEdit_cidade_repre, self.lineEdit_estado_repre
        ]

        for i in [self.pushButton_clienteA, self.pushButton_clienteB, self.pushButton_clienteC]:
            icon = QIcon()
            icon.addFile(
                (Path(__file__).parent / 'src'/'imgs'/'engine.png').__str__(),
                QSize(),
                QIcon.Mode.Normal,
                QIcon.State.Off
            )
            i.setIcon(icon)

        self.logo_menu.setPixmap(QPixmap(
            (Path(__file__).parent / 'src'/'imgs'/'cps_horizontal.png').__str__())
        )

        self.logo_form.setPixmap(QPixmap(
            (Path(__file__).parent / 'src'/'imgs'/'cps_logo.png').__str__())
        )

        self.pushButton_executar.clicked.connect(
            self.executar
        )

        self.back_button.clicked.connect(
            self.return_menu
        )

        self.comboBox_repre.currentTextChanged.connect(
            self.change_repre
        )

        self.radioButton_numero_repre.clicked.connect(
            lambda: self.lineEdit_numero_repre.setDisabled(True) if self.radioButton_numero_repre.isChecked() == True else self.lineEdit_numero_repre.setDisabled(False)
        )

        self.radioButton_numero_empresa.clicked.connect(
            lambda: self.lineEdit_numero_empresa.setDisabled(True) if self.radioButton_numero_empresa.isChecked() == True else self.lineEdit_numero_empresa.setDisabled(False)
        )

        self.lineEdit_cep_empresa.textChanged.connect(
            lambda: self.consultar_correio(self.correio_empresa)
        )

        self.lineEdit_cep_repre.textChanged.connect(
            lambda: self.consultar_correio(self.correio_repre)
        )

        self.checkBox_nacio_repre.checkStateChanged.connect(
            lambda: ICheckBox.aplicacao(self, self.checkBox_nacio_repre)
        )

        self.checkBox_cargo_repre.checkStateChanged.connect(
            lambda: ICheckBox.aplicacao(self, self.checkBox_cargo_repre)
        )

        self.pushButton_nacio.clicked.connect(
            lambda: ICheckBox.remocao(self, self.checkBox_nacio_repre)
        )

        self.pushButton_cargo.clicked.connect(
            lambda: ICheckBox.remocao(self, self.checkBox_cargo_repre)
        )

        self.pb_inatividade.clicked.connect(
             lambda: self.acess_form('Inatividade', None)
        )

        self.pb_simples.clicked.connect(
             lambda: self.acess_form('Simples Nacional', None)
        )

        self.pb_pessoa.clicked.connect(
             lambda: self.acess_form('Pessoa Física', IFisica)
        )

        self.pb_lucro.clicked.connect(
             lambda: self.acess_form('Lucro Presumido', ILucroPresumido)
        )

        self.pushButton_clienteA.clicked.connect(
            lambda: IEnviar.aplicacao(self, 'A')
        )

        self.pushButton_clienteB.clicked.connect(
            lambda: IEnviar.aplicacao(self, 'B')
        )

        self.pushButton_clienteC.clicked.connect(
            lambda: IEnviar.aplicacao(self, 'C')
        )

    def init_reference(self):
        """
        Inicializa o dicionário de referências com os widgets da interface.
        """
        for index in range(1, self.max_repre):
            for nome, widget in self.valores_contratante.items():
                self.relacoes[nome + str(index)] = widget

        self.referencias = {
                chave: '' 
                for chave, widget in self.relacoes.items() if type(widget) == QLineEdit
            } | {
                chave: widget.currentText()
                for chave, widget in self.relacoes.items() if type(widget) == QComboBox
            } | {
                chave: widget.text()
                for chave, widget in self.relacoes.items() if type(widget) == QSpinBox or type(widget) == QDoubleSpinBox
        }

    def executar(self):
        """
        Inicia o processo de validação e geração do contrato.
        """
        try:    
            self.pushButton_executar.setEnabled(False)
            if self.comboBox_repre.currentIndex() == 0:
                self.absorve_preenche(1)
            self.slim_absorve_preenche()

            Aviso(self.filtro()).validar()
            conteudo = Conteudo(self.referencias)

            qnt_repre = self.comboBox_repre.currentIndex() + 1
            base = conteudo.base(qnt_repre)
            atualizado = conteudo.update_dict(qnt_repre)

            self._worker = Worker(
                self.file,
                base,
                atualizado
            )

            self._thread = QThread()
            worker = self._worker
            thread = self._thread

            worker.moveToThread(thread)
            thread.started.connect(worker.main)
            worker.fim.connect(thread.quit)
            worker.fim.connect(thread.deleteLater)
            thread.finished.connect(worker.deleteLater)
            worker.inicio.connect(self.start_load) 
            worker.fim.connect(self.end_load) 
            thread.start() 
        except ValueError:
            messagebox.showwarning(title='Aviso', message= 'Insira datas válidas')
        except ZeroDivisionError:
            messagebox.showwarning(title='Aviso', message= 'Insira um valor de contrato diferente de R$ 0.00')
        except Exception as e:
            print_exc()
            messagebox.showwarning(title='Aviso', message= e)
        finally:
            self.pushButton_executar.setEnabled(True)

    def start_load(self):
        """
        Exibe animação de carregamento.
        """
        self.movie.start()
        self.stackedWidget.setCurrentIndex(self.ID_LOAD)

    def end_load(self, caminho: str):
        """
        Finaliza animação de carregamento e abre o arquivo gerado.
        """
        self.pushButton_executar.setEnabled(True)
        self.movie.stop()
        self.stackedWidget.setCurrentIndex(self.ID_FORM)

        messagebox.showinfo(title='Aviso', message='Abrindo o arquivo gerado!')
        startfile(caminho)

    def consultar_correio(self, lineEdit: list[QLineEdit]):
        """
        Consulta endereço pelo CEP e preenche os campos automaticamente.
        """
        try:
            cep = lineEdit[0].text()
            if len(cep) == 9:
                resp = Correios().pesquisar_cep(cep)

                for i in range(1, len(lineEdit)):
                    lineEdit[i].setText(resp[i - 1])

        except Exception as e:
            print_exc()
            messagebox.showwarning(title='Aviso', message= e)

    def acess_form(self, titulo: str, excecao: IExececao|None):
        """
        Acessa o formulário de acordo com o tipo de contrato selecionado.
        """
        self.stackedWidget.setCurrentIndex(self.ID_FORM)

        self.file.set_option(titulo)
        self.titulo_id1.setText(titulo)

        self.excecao = excecao
        if self.excecao != None:
            self.excecao.aplicacao(self)

    def change_repre(self):
        """
        Altera a quantidade de representantes exibidos no formulário.
        """
        if self.atual_stacked_2 == 0:
            self.absorve_preenche(1)
        self.atual_stacked_2 = self.comboBox_repre.currentIndex()
        index = 0
        if self.atual_stacked_2 != 0:
            count = 0
            for count in range(self.max_repre):
                visivel = True if self.atual_stacked_2 - count >= 0 else False
                self.tabWidget.setTabVisible(count, visivel)
            index = 1
        else: #Se está voltando para o 0, necessáriamente deve ter Contra1
            for key, widget in self.relacoes.items():
                if f'Contra1' in key and type(widget) == QLineEdit:
                    widget.setText(self.referencias[key])
                elif f'Contra1' in key and type(widget) == QComboBox:
                    widget.setCurrentText(self.referencias[key])

        self.stackedWidget_2.setCurrentIndex(index)

    def return_menu(self):
        """
        Retorna à tela inicial do menu.
        """
        self.stackedWidget.setCurrentIndex(self.ID_MENU)
        if self.excecao != None:
            self.excecao.remocao(self)

    def filtro(self):
        """
        Filtra e prepara os dados para validação e geração do contrato.
        """
        ref_temp = deepcopy(self.referencias)
        ref_temp.pop('compleEmp')

        for key, widget in self.widgets_especials.items():
            value = widget.text()
            ref_temp[key] = value.replace('.','').replace('-','').replace('/','').replace(' ','')

        for i in range(1, self.comboBox_repre.currentIndex() + 2):
            for key, widget in self.widgets_especials_contra.items():
                value = widget.text()
                ref_temp[key+str(i)] = value.replace('.','').replace('-','').replace('/','').replace(' ','') 

        if self.excecao != None:
            if self.excecao.__qualname__ != ILucroPresumido.__qualname__:
                ref_temp.pop('valorEFD')

            if self.excecao.__qualname__ == IFisica.__qualname__:
                for key in self.relacoes.keys():
                    ref_temp.pop(key, None) if 'Emp' in key else None
        else:
            ref_temp.pop('valorEFD')

        for i in range(1, self.max_repre):
            ref_temp.pop('emissorContra' + str(i))
            ref_temp.pop('compleContra' + str(i))
            if ref_temp['nacionalidadeContra' + str(i)] != 'Brasileiro(a)':
                ref_temp.pop('rgContra' + str(i))

        #Desconsiderar do atual pra frente
        for i in range(self.comboBox_repre.currentIndex() + 2, self.max_repre):
            for j in self.valores_contratante:
                ref_temp.pop(j + str(i),None)

        return ref_temp
    
    def convert_id(self, id) -> str:
        """
        Converte identificador de representante para string numérica.
        """
        for key, index in self.relacao_ids.items():
            if id == key:
                return str(index)
            
    def slim_absorve_preenche(self):
        """
        Absorve dados dos campos não relacionados a representantes.
        """
        for key, widget in self.relacoes.items():
            if 'Contra' not in key:
                self.referencias[key] = widget.text()

        for widget, key in self.relacao_numeros.items():
            if widget.isChecked() == True and 'Contra' not in key:
                self.referencias[key] = 'S/N'
            
    def absorve_preenche(self, id):
        """
        Absorve e preenche dados dos campos de um representante específico.
        """
        for key, widget in self.relacoes.items():
            if f'Contra{id}' in key:
                if type(widget) == QLineEdit:
                    self.referencias[key] = widget.text()
                elif f'Contra{id}' in key and type(widget) == QComboBox:
                    self.referencias[key] = widget.currentText()

            elif 'Contra' not in key:
                self.referencias[key] = widget.text()

        for key, value in self.relacoes_nacio_emprego.items():
            if self.relacoes[f'{key}{id}'].text() == '':
                self.referencias[f'{key}{id}'] = value

        for widget, key in self.relacao_numeros.items():
            if widget.isChecked() == True:
                self.referencias[key.format(id)] = 'S/N'

        for key, widget in self.relacoes_label_cliente.items():
            if f'Contra{id}' in key:
                widget.setText(self.referencias[key])

    def items_checkbox(self, check_box: QCheckBox):
        """
        Retorna widgets relacionados a um checkbox específico.
        """
        for key, list in self.relacoes_checkbox.items():
            if key == check_box:
                lineEdit, button = list
        return lineEdit,button
            

if __name__ == '__main__':
    """
    Ponto de entrada do programa. Inicializa a aplicação Qt.
    """
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()