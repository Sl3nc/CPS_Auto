from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from abc import ABCMeta, abstractmethod
from num2words import num2words
from docxtpl import DocxTemplate, RichText
from datetime import datetime
from itertools import cycle
from unidecode import unidecode
import copy
import re
import sys
import os
import locale
import traceback
import requests
import json

from PySide6.QtWidgets import (
    QMainWindow, QApplication, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton, QSpinBox, QDoubleSpinBox
)
from PySide6.QtGui import QPixmap, QIcon, QMovie, QValidator
from PySide6.QtCore import QThread, QObject, Signal, QSize
from src.window_cps import Ui_MainWindow

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def resource_path(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class TextOnly(QValidator):
    def validate(self, string, index):
        if re.compile("[a-zA-Z]+").fullmatch(string) or string == '':
            return QValidator.State.Acceptable
        return QValidator.State.Invalid

    # def operacao_cpf(self, text):
    #     numeros = [int(digito) for digito in text if digito.isdigit()]
  
    #     for i in range(9,11):
    #         soma_produtos = sum(a*b for a, b in zip (numeros[0:i], range (i + 1, 1, -1)))
    #         digito_esperado = (soma_produtos * 10 % 11) % 10
    #         if numeros[i] != digito_esperado:
    #             return False
    #     return True
    
    # def operacao_cnpj(self, text):
    #     cnpj = ''.join([digito for digito in text if digito.isdigit()])
    #     if cnpj in (c * 14 for c in "1234567890"):
    #         return False

    #     cnpj_r = cnpj[::-1]
    #     for i in range(2, 0, -1):
    #         cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
    #         dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
    #     if cnpj_r[i - 1:i] != str(dv % 10):
    #         return False
    #     return True
        
class File:
    def __init__(self):
        self.options = ['Pessoa Física', 'Inatividade', 'Lucro Presumido', 'Simples Nacional']
        self.base_caminho = 'src\\CPS\'s\\CPS {0}.docx'
        self.current_option = ''

#Falta usarmos o set quando se escolhe uma opção do menu
    def set_option(self, nome: str):
        self.current_option = nome if nome in self.options else Exception('Nome de arquivo inválido')

    def alterar(self, base: dict, updt: dict, caminho: str): 
        self.arquivo = \
            DocxTemplate(
                resource_path(self.base_caminho.format(
                        unidecode(self.current_option)
                    )
                )
            )

        self.arquivo.render(base)
        self.arquivo.save(caminho)
        self.arquivo = DocxTemplate(caminho)
        self.arquivo.render(updt)
        self.arquivo.save(caminho)

    def salvar(self):
        caminho = asksaveasfilename(title='Defina o nome e o local onde o arquivo será salvo', filetypes=((".docx","*.docx"),))

        if caminho[caminho.rfind('/') + 1:] == '':
            raise Exception('Operação Cancelada')
        
        return caminho + '.docx'

class Aviso:
    def __init__(self, ref) -> None:
        self.ref = ref
        pass

    def validar(self):
        resp_final = self.__textos_vazios(self.__add_vazios())

        if len(resp_final) != 0:
            raise Exception (f'Estão vazios as seguintes dados:\n{resp_final}\nfavor preencher TODOS')
        
    def __add_vazios(self):
        vazios_contrato = []
        vazios_emp = []
        vazios_repre1 = []
        vazios_repre2 = []
        vazios_repre3 = []
    
        vazios_repre = {
            1: vazios_repre1,
            2: vazios_repre2,
            3: vazios_repre3
        }

        for key, valor in self.ref.items():
            if valor == '':
                if 'Contra' in key:
                    for index, lista in vazios_repre.items():
                        if str(index) in key:
                            lista.append(key.replace('Contra'+ str(index), ''))
                elif 'Emp' in key:
                    vazios_emp.append(key.replace('Emp',''))
                else:
                    vazios_contrato.append(key)

        return [vazios_emp, vazios_repre, vazios_contrato]

    def __textos_vazios(self, lista):
        resp_final = ''

        text_void = {
            'Empresa: ': lista[0],
            'Representante 1: ': lista[1][1],
            'Representante 2: ': lista[1][2],
            'Representante 3: ': lista[1][3],
            'Contrato: ': lista[2]
        }
         
        for titulo, vet in text_void.items():
            if len(vet) != 0:
                resp_final = f'{resp_final}\n{titulo.upper()}\n{' - '.join(str(x) for x in vet)}\n'

        return resp_final

#TODO CONTEUDO
class Conteudo:
    def __init__(self, referencias: dict[str:str]):
        self.dictonary = copy.deepcopy(referencias)
        
        self.SAL_MINIMO = 1412.00
        self.CUSTO_CORREIO = 0.02

        self.cabecalho = '{{r nomeEmp }}, estabelecida na rua {{ ruaEmp }}, nº {{ numEmp }}, {{ compleEmp }}, bairro {{ bairroEmp }}, CEP {{ cepEmp }}, CNPJ {{r cnpjEmp }}, neste ato representada por ',

        self.conteudo_base = {
            1: [
                '{{r nomeContra1 }}, {{ nacionalidadeContra1 }}, {{ empregoContra1 }}, {{ estadoCivilContra1 }}, residente e domiciliado(a) na rua {{ ruaContra1 }}, nº {{ numContra1 }}, {{ compleContra1 }} bairro {{ bairroContra1 }} , CEP {{ cepContra1 }}, {{ cidadeContra1 }}, {{ estadoContra1 }}, portador(a) do documento de identidade sob o nº {{ rgContra1 }} {{ emissorContra1 }}, CPF {{r cpfContra1 }}',

                '''_______________________________     
                
                
______________________________
Deltaprice Serviços Contábeis Ltda.                                                        {{r nomeContra1 }}
                '''
                ],
            2: [
                '{{r nomeContra1 }}, {{ nacionalidadeContra1 }}, {{ empregoContra1 }}, {{ estadoCivilContra1 }}, residente e domiciliado(a) na rua {{ ruaContra1 }}, nº {{ numContra1 }}, {{ compleContra1 }} bairro {{ bairroContra1 }} , CEP {{ cepContra1 }}, {{ cidadeContra }}, {{ estadoContra1 }}, portador(a) do documento de identidade sob o nº {{ rgContra1 }} {{ emissorContra1 }}, CPF {{r cpfContra1 }} e {{r nomeContra2 }}, {{ nacionalidadeContra2 }}, {{ empregoContra2 }}, {{ estadoCivilContra2 }}, residente e domiciliado(a) na rua {{ ruaContra2 }}, nº {{ numContra2 }}, {{ compleContra2 }} bairro {{ bairroContra2 }} , CEP {{ cepContra2 }}, {{ cidadeContra2 }}, {{ estadoContra2 }}, portador(a) do documento de identidade sob o nº {{ rgContra2 }} {{ emissorContra }}, CPF {{r cpfContra2 }} denominados(a) daqui por diante de Contratante;',

                '''_______________________________                                                  ____________________________________
                    Deltaprice Serviços Contábeis Ltda.                                                        {{r nomeContra1 }}
                    {{r nomeContra2 }}
                '''],
            3: [
                '{{r nomeContra1 }}, {{ nacionalidadeContra1 }}, {{ empregoContra1 }}, {{ estadoCivilContra1 }}, residente e domiciliado(a) na rua {{ ruaContra1 }}, nº {{ numContra1 }}, {{ compleContra1 }} bairro {{ bairroContra1 }} , CEP {{ cepContra1 }}, {{ cidadeContra }}, {{ estadoContra1 }}, portador(a) do documento de identidade sob o nº {{ rgContra1 }} {{ emissorContra1 }}, CPF {{r cpfContra1 }}, {{r nomeContra2 }}, {{ nacionalidadeContra2 }}, {{ empregoContra2 }}, {{ estadoCivilContra2 }}, residente e domiciliado(a) na rua {{ ruaContra2 }}, nº {{ numContra2 }}, {{ compleContra2 }} bairro {{ bairroContra2 }} , CEP {{ cepContra2 }}, {{ cidadeContra2 }}, {{ estadoContra2 }}, portador(a) do documento de identidade sob o nº {{ rgContra2 }} {{ emissorContra2 }}, CPF {{r cpfContra2 }} e {{r nomeContra3 }}, {{ nacionalidadeContra3 }}, {{ empregoContra3 }}, {{ estadoCivilContra3 }}, residente e domiciliado(a) na rua {{ ruaContra3 }}, nº {{ numContra3 }}, {{ compleContra3 }} bairro {{ bairroContra3 }} , CEP {{ cepContra3 }}, {{ cidadeContra3 }}, {{ estadoContra3 }}, portador(a) do documento de identidade sob o nº {{ rgContra3 }} {{ emissorContra3 }}, CPF {{r cpfContra3 }} denominados(as) daqui por diante de Contratante;',

                '''_______________________________                                                  ____________________________________
                    Deltaprice Serviços Contábeis Ltda.                                                        {{r nomeContra1 }}
                    {{r nomeContra2 }}
                    {{r nomeContra3 }}
                ''']
        }

    def base(self, index_atual: int):
        conteudo_base = self.conteudo_base[index_atual]
        return {
            'cabecalho_emp' : self.cabecalho[0],
            'honorarios' : conteudo_base[0],
            'assinatura' : conteudo_base[1]
        }

    #TODO UPDT DICT
    def update_dict(self, qnt_repre):
        ref = {
            'valorPagamento': self.__set_valor(),
            'numEmp': self.__set_num(self.dictonary['numEmp']),
            'diaVenc': self.__set_num(self.dictonary['diaVencimento']),
            'dataComple': lambda: self.dictonary['dataInicio'][2:],
            'dataAssinatura': self.__set_data(self.dictonary['dataAssinatura']),
            'dataInicio': self.__set_data(self.dictonary['dataInicio']),
        }

        self.dictonary['valPorc'] = self.__calc_porc()
        
        for key, func in ref.items():
            self.dictonary[key] = func

        self.__set_empresa()
        self.__update_repre(qnt_repre)

        return self.dictonary
    
    #TODO UPDT REPRE
    def __update_repre(self, qnt_repre):
        for i in range(1, qnt_repre + 1):
            i = str(i)
            ref = {
                'nomeContra': RichText(self.dictonary['nomeContra' + i].upper(), bold = True),
                'ruaContra': self.dictonary['ruaContra'+ i].title(), 
                'bairroContra':self.dictonary['bairroContra'+ i].title(),
                'cpfContra' : RichText(self.dictonary['cpfContra'+ i].upper(), bold = True),
                'compleContra': self.dictonary['compleContra'+ i].title()
            }

            for index, value in ref.items():
                self.dictonary[index + i] = value

    def __set_empresa(self):
        if self.dictonary.get('nomeEmp') != None:

            ref = {
                'nomeEmp': RichText(self.dictonary['nomeEmp'].upper(), bold = True),
                'ruaEmp': self.dictonary['ruaEmp'].title(), 
                'bairroEmp':self.dictonary['bairroEmp'].title(),
                'cnpjEmp' : RichText(self.dictonary['cnpjEmp'].upper(), bold = True),
                'compleEmp': self.dictonary['bairroEmp'].title()
            }

            for index, value in ref.items():
                self.dictonary[index] = value

    def __set_valor(self):
        valor = self.dictonary['valorPagamento'].replace(',','.').replace('R$','')
        valorExtenso = num2words(valor, lang='pt_BR', to='currency')\
            .replace('reais e','reais,')
        return f'R$ {float(valor):_.2f} ({valorExtenso})'.replace('.',',').replace('_','.')
    
    def __set_num(self, num: str):
        if num.isdigit() == True:
            valorExtenso = num2words(num,lang='pt_BR')
            return f'{num} ({valorExtenso})'
        return 'S/N'

    def __set_data(self, data):
        data_format = datetime.strptime(data, '%d/%m/%Y')
        return data_format.strftime("%d de %B de %Y")
        
    def __calc_porc(self):
        valor = self.dictonary['valorPagamento'].replace(',','.').replace('R$','')
        custo_envio = self.SAL_MINIMO * self.CUSTO_CORREIO
        return f'{((custo_envio / float(valor)) * 100):,.2f}%'

class IExececao(metaclass=ABCMeta):
    @abstractmethod
    def aplicacao(self):
        pass

    @abstractmethod
    def remocao(self):
        pass

class Correios:
    URL = 'https://viacep.com.br/ws/{0}/json/'

    def __init__(self) -> None:
        pass

    def pesquisar_cep(self, endereco):
        try:
            url = requests.get(self.URL.format(endereco)).content
            dic = json.loads(url)
            return [dic["logradouro"], dic["bairro"], dic["localidade"], dic["estado"]]
        except:
            raise Exception('Verifique se o cep foi digitado corretamente e tente novamente') 

class Worker(QObject):
    inicio = Signal()
    fim = Signal(str)


    def __init__(self, file: File, base: dict, atualizado: dict) -> None:
        super().__init__()
        self.file = file
        self.base = base
        self.atualizado = atualizado

    def main(self):
        caminho = self.file.salvar() 
        self.inicio.emit()
        self.file.alterar(self.base, self.atualizado, caminho)
        self.fim.emit(caminho)

#TODO MAIN
class MainWindow(QMainWindow, Ui_MainWindow):
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
            resource_path('src\\imgs\\cps-icon.ico'))
        )

        self.movie = QMovie(resource_path("src\\imgs\\load.gif"))
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
            'numEmp': self.lineEdit_numero_empresa,
            'bairroEmp': self.lineEdit_bairro_empresa,
            'compleEmp': self.lineEdit_complemento_empresa,
            'valorPagamento': self.lineEdit_valor_contrato,
            'dataInicio': self.lineEdit_dt_inicio_contrato,
            'dataAssinatura': self.lineEdit_dt_assinatura_contrato,
            'diaVencimento': self.lineEdit_dia_vencimento_contrato,
            'numFuncionario': self.lineEdit_num_empreg_contrato,
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
            'dataInicio': self.lineEdit_dt_inicio_contrato,
            'dataAssinatura': self.lineEdit_dt_assinatura_contrato
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
            self.radioButton_numero_empresa: 'numEmp',
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
            icon.addFile(resource_path("src\\imgs\\engine.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            i.setIcon(icon)

        self.logo_menu.setPixmap(QPixmap(
            resource_path('src\\imgs\\cps_horizontal.png'))
        )

        self.logo_form.setPixmap(QPixmap(
            resource_path('src\\imgs\\cps_logo.png'))
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

    #TODO EXECUTAR
    def executar(self):
        try:    
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
            traceback.print_exc()
            messagebox.showwarning(title='Aviso', message= e)

    def start_load(self):
         self.movie.start()
         self.stackedWidget.setCurrentIndex(self.ID_LOAD)

    def end_load(self, caminho: str):
        self.movie.stop()
        self.stackedWidget.setCurrentIndex(self.ID_FORM)

        messagebox.showinfo(title='Aviso', message='Abrindo o arquivo gerado!')
        os.startfile(caminho)

    def consultar_correio(self, lineEdit: list[QLineEdit]):
        try:
            cep = lineEdit[0].text()
            if len(cep) == 9:
                resp = Correios().pesquisar_cep(cep)

                for i in range(1, len(lineEdit)):
                    lineEdit[i].setText(resp[i - 1])

        except Exception as e:
            traceback.print_exc()
            messagebox.showwarning(title='Aviso', message= e)

    def acess_form(self, titulo: str, excecao: IExececao|None):
        self.stackedWidget.setCurrentIndex(self.ID_FORM)

        self.file.set_option(titulo)
        self.titulo_id1.setText(titulo)

        self.excecao = excecao
        if self.excecao != None:
            self.excecao.aplicacao(self)

    def change_repre(self):
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
        self.stackedWidget.setCurrentIndex(self.ID_MENU)
        if self.excecao != None:
            self.excecao.remocao(self)

    #TODO FILTRO
    def filtro(self):
        ref_temp = copy.deepcopy(self.referencias)
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
        for key, index in self.relacao_ids.items():
            if id == key:
                return str(index)
            
    def slim_absorve_preenche(self):
        for key, widget in self.relacoes.items():
            if 'Contra' not in key:
                self.referencias[key] = widget.text()

        for widget, key in self.relacao_numeros.items():
            if widget.isChecked() == True and 'Contra' not in key:
                self.referencias[key] = 'S/N'
            
#TODO ABS_PRE
    def absorve_preenche(self, id):
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
        for key, list in self.relacoes_checkbox.items():
            if key == check_box:
                lineEdit, button = list
        return lineEdit,button

class ILucroPresumido(IExececao):
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
            
class IFisica(IExececao):
    def aplicacao(self: MainWindow):
        for layout in [self.grid_empresa, self.intro_empresa]:
            for i in range(layout.count()):
                layout.itemAt(i).widget().hide()

    def remocao(self: MainWindow):
        for layout in [self.grid_empresa, self.intro_empresa]:
            for i in range(layout.count()):
                layout.itemAt(i).widget().show()

class IEnviar(IExececao):
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

class ICheckBox:
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

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()