from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from abc import ABCMeta, abstractmethod
from num2words import num2words
from docxtpl import DocxTemplate, RichText
from datetime import datetime
from itertools import cycle
import unicodedata
import decimal
import copy
import keyboard
import re
import sys
import os
import locale
import traceback

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

class IFormater:
    def cpf_formater(self, text, var, index, mode):
        #Só recebe valor que passa pelo validador
        valor = text.get()
        if len(valor) == 11:
           valor = valor[:3] + "." + valor[3:6] + "." + valor[6:9] + "-" + valor[9:]
        else:
            valor = valor.replace('.','').replace('-','')
        text.set(valor)

    def cnpj_formater(self, text, var, index, mode): 
        #Só recebe valor que passa pelo validador
        valor = text.get()
        if len(valor) == 14:
           valor = valor[:2] + "." + valor[2:5] + "." + valor[5:8] + "/" + valor[8:12] + "-" + valor[12:]
        else:
            valor = valor.replace('.','').replace('-','').replace('/','')
        text.set(valor)
    

    def cep_formater(self, text, var, index, mode): 
        #Só recebe valor que passa pelo validador
        valor = text.get()
        if len(valor) == 8 and '-' not in valor:
           valor = valor[:5] + "-" + valor[5:]
        else:
            valor = valor.replace('-','')
        text.set(valor)

    def rg_formater(self, text, var, index, mode): 
        #Só recebe valor que passa pelo validador
        valor = text.get()
        if len(valor) == 10:
           valor = valor[:2] + "-" + valor[2:4] + "." + valor[4:7] + "." + valor[7:]
        else:
            valor = valor.replace('.','').replace('-','').replace(' ','')
        text.set(valor)
    
    def date_formater(self, text, var, index, mode): 
        #Só recebe valor que passa pelo validador
        valor = text.get()
        if len(valor) == 8:
           valor = valor[:2] + "/" + valor[2:4] + "/" + valor[4:]
        else:
            valor = valor.replace('/','')
        text.set(valor)

    def comp_formater(self, text, var, index, mode): 
        #Só recebe valor que passa pelo validador
        valor = text.get()
        if len(valor) == 6 and '/' not in valor:
           valor = valor[:2] + "/" + valor[2:]
        else:
            valor = valor.replace('/','')
        text.set(valor)

    def valor_formater(self, text, var, index, mode): 
        #Só recebe valor que passa pelo validador
        valor = text.get()
        if ',' not in valor:
            valor = valor + ',00'
        
        text.set(valor)      

class SpecialOnly(QValidator):
    def validate(self, string, index):
        if re.compile("[./0-9-]+").fullmatch(string) or string == '':
            return QValidator.State.Acceptable
        return QValidator.State.Invalid

class TextOnly(QValidator):
    def validate(self, string, index):
        if re.compile("[a-zA-Z]+").fullmatch(string) or string == '':
            return QValidator.State.Acceptable
        return QValidator.State.Invalid

class IValidator:    
    def str_validator(self, text):
        return not text.isdecimal()
    
    def num_validator(self, text):
        return text.isdecimal()
    
    def valor_validator(self, text):
        padrao = r"^[-\d.,/]+$"  # Permite dígitos, ponto, vírgula, hífen e barra
        if len(text) == 0:
            return True
        return re.match(padrao, text) is not None

    def operacao_cpf(self, text):
        numeros = [int(digito) for digito in text if digito.isdigit()]
  
        for i in range(9,11):
            soma_produtos = sum(a*b for a, b in zip (numeros[0:i], range (i + 1, 1, -1)))
            digito_esperado = (soma_produtos * 10 % 11) % 10
            if numeros[i] != digito_esperado:
                return False
        return True
        
    def cpf_validator(self, text):
        padrao = r"^[-\d.,/]+$"  # Permite dígitos, ponto, vírgula, hífen e barra
        if len(text) < 15:
            if len(text) >= 12:
                if len(text) == 14 and self.operacao_cpf(text) == False:
                    messagebox.showwarning(title='Aviso', message='O CPF digitado é inválido')
                return re.match(padrao, text) is not None
            elif len(text) == 0 or text.isdecimal():
                return True
        return False
    
    def operacao_cnpj(self, text):
        cnpj = ''.join([digito for digito in text if digito.isdigit()])
        if cnpj in (c * 14 for c in "1234567890"):
            return False

        cnpj_r = cnpj[::-1]
        for i in range(2, 0, -1):
            cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
            dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False
        return True
        
    def cnpj_validator(self, text):
        padrao = r"^[-\d.,/]+$"  # Permite dígitos, ponto, vírgula, hífen e barra
        if len(text) < 19:
            if len(text) >= 15:
                if len(text) == 18 and self.operacao_cnpj(text) == False:
                    messagebox.showwarning(title='Aviso', message='O CNPJ digitado é inválido')
                return re.match(padrao, text) is not None
            elif len(text) == 0 or text.isdecimal():
                return True
        return False
    
    def cep_validator(self, text):
        padrao = r"^[-\d.,/]+$"  # Permite dígitos, ponto, vírgula, hífen e barra
        if len(text) < 10:
            if len(text) >= 9:
                return re.match(padrao, text) is not None
            elif len(text) in [0,8] or text.isdecimal():
                return True
        return False
    
    def rg_validator(self, text):
        if len(text) < 14:
            return True
        return False
    
    def date_validator(self, text):
        padrao = r"^[-\d.,/]+$"  # Permite dígitos, ponto, vírgula, hífen e barra
        if len(text) < 11:
            if len(text) >= 9:
                return re.match(padrao, text) is not None
            elif len(text) == 0 or text.isdecimal():
                return True
        return False
    
    def comp_validator(self, text):
        padrao = r"^[-\d.,/]+$"  # Permite dígitos, ponto, vírgula, hífen e barra
        if len(text) < 8:
            if len(text) >= 7:
                return re.match(padrao, text) is not None
            elif len(text) in [0,6] or text.isdecimal():
                return True
        return False

class File:
    def __init__(self):
        self.options = ['Pessoa Física', 'Inatividade', 'Lucro Presumido', 'Simples Nacional']
        self.base_caminho = 'src\\CPS\'s\\CPS {0}.docx'

#Falta usarmos o set quando se escolhe uma opção do menu
    def set_option(self, nome: str):
        self.arquivo = \
            DocxTemplate(
                resource_path(self.base_caminho.format(
                    {unicodedata.normalize("NFKD", nome.upper())}
                ).encode('ascii', 'ignore').decode('ascii'))) \
                    if nome in self.options else None

    def alterar(self, base, updt): 
        caminho = self.salvar() 

        self.arquivo.render(base)
        self.arquivo.save(caminho)
        self.arquivo = DocxTemplate(caminho)
        self.arquivo.render(updt)
        self.arquivo.save(caminho)

        self.abrir(caminho)

    def salvar(self):
        caminho = asksaveasfilename(title='Defina o nome e o local onde o arquivo será salvo', filetypes=((".docx","*.docx"),))

        if caminho[caminho.rfind('/') + 1:] == '':
            raise Exception('Operação Cancelada')
        
        return caminho + '.docx'
    
    def abrir(self, caminho: str):
        messagebox.showinfo(title='Aviso', message='Abrindo o arquivo gerado!')
        os.startfile(caminho)

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
    def __init__(self, referencias):
        self.dictonary = copy.deepcopy(referencias)
        
        self.SAL_MINIMO = 1412.00
        self.CUSTO_CORREIO = 0.02

        self.cabecalho = '{{r nomeEmp }}, estabelecida na rua {{ ruaEmp }}, nº {{ numEmp }}, {{ compleEmp }}, bairro {{ bairroEmp }}, CEP {{ cepEmp }}, CNPJ {{r cnpjEmp }}, neste ato representada por ',

        self.conteudo_base = {
            0: [
                '{{r nomeContra1 }}, {{ nacionalidadeContra1 }}, {{ empregoContra1 }}, {{ estadoCivilContra1 }}, residente e domiciliado(a) na rua {{ ruaContra1 }}, nº {{ numContra1 }}, {{ compleContra1 }} bairro {{ bairroContra1 }} , CEP {{ cepContra1 }}, {{ cidadeContra1 }}, {{ estadoContra1 }}, portador(a) do documento de identidade sob o nº {{ rgContra1 }} {{ emissorContra1 }}, CPF {{r cpfContra1 }}',

                '''_______________________________                                                  ____________________________________
                    Deltaprice Serviços Contábeis Ltda.                                                        {{r nomeContra1 }}
                '''
                ],
            1: [
                '{{r nomeContra1 }}, brasileiro(a), empresário(a), {{ estadoCivilContra1 }}, residente e domiciliado(a) na rua {{ ruaContra1 }}, nº {{ numContra1 }}, {{ compleContra1 }} bairro {{ bairroContra1 }} , CEP {{ cepContra1 }}, {{ cidadeContra }}, {{ estadoContra1 }}, portador(a) do documento de identidade sob o nº {{ rgContra1 }} {{ emissorContra1 }}, CPF {{r cpfContra1 }} e {{r nomeContra2 }}, brasileiro(a), empresário(a), {{ estadoCivilContra2 }}, residente e domiciliado(a) na rua {{ ruaContra2 }}, nº {{ numContra2 }}, {{ compleContra2 }} bairro {{ bairroContra2 }} , CEP {{ cepContra2 }}, {{ cidadeContra2 }}, {{ estadoContra2 }}, portador(a) do documento de identidade sob o nº {{ rgContra2 }} {{ emissorContra }}, CPF {{r cpfContra2 }} denominados(a) daqui por diante de Contratante;',

                '''_______________________________                                                  ____________________________________
                    Deltaprice Serviços Contábeis Ltda.                                                        {{r nomeContra1 }}
                ''']
        }

    def base(self, index_atual: int):
        return {
            'cabecalho_emp' : self.cabecalho[0],
            'honorarios' : self.conteudo_base[index_atual][0],
            'assinatura' : self.conteudo_base[index_atual][1]
        }

    #TODO UPDT DICT
    def update_dict(self, qnt_repre):
        ref = {
            'valorPagamento': self.__set_valor(),
            'numEmp': self.__set_num(self.dictonary['numEmp']),
            'diaVenc': self.__set_num(self.dictonary['diaVencimento']),
            'dataComple': lambda: self.dictonary['dataInicio'][2:],
            # 'dataAssinatura': self.__set_data(self.dictonary['dataAssinatura']),
            # 'dataInicio': self.__set_data(self.dictonary['dataInicio']),
        }

        self.dictonary['valPorc'] = self.__calc_porc()
        
        for key, func in ref.items():
            self.dictonary[key] = func

        self.__set_IJuridica()
        self.__update_repre(qnt_repre)

        return self.dictonary
    
    def __update_repre(self, qnt_repre):
        ref_estado = {
            'STB': 'Casado em Separação Total de Bens',
            'CPB': 'Casado em Comunhão Parcial de Bens',
            'CUB': 'Casado em Comunhão Universal de Bens'
        }

        for i in range(1, qnt_repre + 1):
            i = str(i)
            ref = {
                'nomeContra': RichText(self.dictonary['nomeContra' + i].upper(), bold = True),
                'ruaContra': self.dictonary['ruaContra'+ i].title(), 
                'bairroContra':self.dictonary['bairroContra'+ i].title(),
                'cpfContra' : RichText(self.dictonary['cpfContra'+ i].upper(), bold = True),
                'compleContra': self.dictonary['compleContra'+ i].title()
            }

            regime = self.dictonary['estadoCivilContra' + i]
            if regime in ref_estado:
                self.dictonary['estadoCivilContra' + i] = ref_estado[regime]

            for index, value in ref.items():
                self.dictonary[index + i] = value

    def __set_IJuridica(self):
        if 'nomeEmp' in self.dictonary:

            ref = {
                'nomeEmp': RichText(self.dictonary['nomeEmp'].upper(), bold = True),
                'ruaEmp': self.dictonary['ruaEmp'].title(), 
                'bairroEmp':self.dictonary['bairroEmp'].title(),
                'cnpjEmp' : RichText(self.dictonary['cnpjEmp'].upper(), bold = True),
                'compleEmp': self.dictonary['bairroEmp'].title()
            }

            for index, value in ref.items():
                self.dictonary[index] = value

            # if "LTDA" in self.dictonary['nomeEmp']:
            #     self.dictonary['nomeEmp'] = self.dictonary['nomeEmp'].replace('LTDA',' LTDA.')

    def __set_valor(self):
        valor = self.dictonary['valorPagamento'].replace(',','.')
        valorExtenso = num2words(valor, lang='pt_BR', to='currency')\
            .replace('reais e','reais,')
        return f'R$ {float(valor):,.2f} ({valorExtenso})'.replace('.',',')
    
    def __set_num(self, num):
        valorExtenso = num2words(num,lang='pt_BR')
        return f'{num} ({valorExtenso})'

    def __set_data(self, data):
        data_format = datetime.strptime(data, '%d/%m/%Y')
        return data_format.strftime("%d de %B de %Y")
        
    def __calc_porc(self):
        valor = self.dictonary['valorPagamento'].replace(',','.')
        custo_envio = self.SAL_MINIMO * self.CUSTO_CORREIO
        return f'{((custo_envio / float(valor)) * 100):,.2f}%'
    
        # subLista.add_command(label='Comunhão Parcial de Bens', \
        #     command= lambda: estadoEntry.set('casado(a) em CPB'))
        
        # subLista.add_command(label='Comunhão Universal de Bens',\
        #     command= lambda: estadoEntry.set('casado(a) em CUB'))
        
        # subLista.add_command(label='Separação Total de Bens',\
        #     command= lambda: estadoEntry.set('casado(a) em STB'))

class IExececao(metaclass=ABCMeta):
    @abstractmethod
    def aplicacao(self):
        pass

    @abstractmethod
    def remocao(self):
        pass

#TODO MAIN
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.vez = 1

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
            'empregoContra': self.lineEdit_cargo
        }
        #Colocar aqui seu lineEdit da janela, se este estiver vazio, fica como "brasileiro"
        
        self.init_reference()

        self.relacoes_validator ={
            self.lineEdit_cnpj_empresa: SpecialOnly(),
            self.lineEdit_cep_empresa: SpecialOnly(),
            self.lineEdit_cpf_repre: SpecialOnly(),
            self.lineEdit_cep_repre: SpecialOnly(),
            self.lineEdit_dt_inicio_contrato: SpecialOnly(),
            self.lineEdit_dt_assinatura_contrato: SpecialOnly(),
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

        self.ID_MENU = 0
        self.ID_FORM = 1
        
        self.max_repre = 3
      
        self.file = File()
        self.excecao = None

        self.setWindowTitle('Gerador de CPS')

        self.setWindowIcon(QIcon(
            resource_path('src\\imgs\\cps-icon.ico'))
        )

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
        for index in range(1, 3):
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

        #TODO TESTE EXECUTAR
        teste.preencher_teste(self)

    def executar(self):
        try:    
            Aviso(self.filtro()).validar()
            conteudo = Conteudo(self.referencias)
            print(self.referencias)

            qnt_repre = self.comboBox_repre.currentIndex()
            base = conteudo.base(qnt_repre)
            atualizado = conteudo.update_dict(qnt_repre)

            self.file.alterar(base, atualizado)
        # except decimal.InvalidOperation:
        #     messagebox.showwarning(title='Aviso', message= 'Insira um número válido')
        # except ValueError:
        #     messagebox.showwarning(title='Aviso', message= 'Insira datas válidas')
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

    def filtro(self):
        ref_temp = copy.deepcopy(self.referencias)
        ref_temp.pop('compleEmp')

        if type(self.excecao) == IFisica:
            for key in ref_temp.keys:
                ref_temp.pop(key, None) if 'emp' in key else None

        for i in range(1, self.comboBox_repre.currentIndex() +2):
            ref_temp.pop('emissorContra' + str(i))
            ref_temp.pop('compleContra' + str(i))
            if ref_temp['nacionalidadeContra' + str(i)] != 'brasileiro(a)':
                ref_temp.pop('rgContra' + str(i))

        for i in range(self.comboBox_repre.currentIndex() + 2, 4):
            for j in self.valores_contratante:
                ref_temp.pop(j + str(i),None)

        return ref_temp
    
    def convert_id(self, id) -> str:
        for key, index in self.relacao_ids.items():
            if id == key:
                return str(index)

    def absorve_preenche(self, id):
        for key, widget in self.relacoes.items():
            if f'Contra{id}' in key and type(widget) == QLineEdit:
                self.referencias[key] = widget.text()
                print(f'Contra{id}')
                print(f'chave - {key}')
            elif f'Contra{id}' in key and type(widget) == QComboBox:
                self.referencias[key] = widget.currentText()

        for key, widget in self.relacoes_label_cliente.items():
            if f'Contra{id}' in key:
                widget.setText(self.referencias[key])

        print(f'---------------------------------------{self.vez}')
        self.vez = self.vez + 1

    def items_checkbox(self, check_box: QCheckBox):
        for key, list in self.relacoes_checkbox.items():
            if key == check_box:
                lineEdit, button = list
        return lineEdit,button

#TODO TESTE
class teste:
    def preencher_teste(self: MainWindow):
        for index, chave in enumerate(self.referencias.keys()):
            self.referencias[chave] = str(index)

class ILucroPresumido(IExececao):
    def aplicacao(self: MainWindow):
        self.grid_contrato.removeWidget(self.pushButton_executar)
        self.grid_contrato.addWidget(self.label_EFD,0,5)
        self.grid_contrato.addWidget(self.lineEdit_EFD, 1,5)
        self.grid_contrato.addWidget(self.pushButton_executar, 0,6, 2, 1)
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