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

from PySide6.QtWidgets import (
    QMainWindow, QApplication, QRadioButton, QVBoxLayout, QWidget
)
from PySide6.QtGui import QPixmap, QIcon, QMovie
from PySide6.QtCore import QThread, QObject, Signal, QSize
from src.window_cps import Ui_MainWindow

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def resource_path(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def enter_press(event):
    if event.keysym == 'Return':
        keyboard.send('tab')

def alter_estado(self, event):
    if event.keysym == 'Down' or event.keysym == 'Up':
        self.popup.focus()
        keyboard.send('space')
        
window = Tk()
window.bind('<Key>', enter_press)


class IFormater: #TODO Formaters
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

class IValidator:    #TODO Validators
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
#sdas
#Arquivo

class File:
    def __init__(self):
        self.options = ['Pessoa Física', 'Inatividade', 'Lucro Presumido', 'Simples Nacional']
        self.base_caminho = 'src\\CPS\'s\\CPS {0}.docx'

    def set_option(self, nome: str):
        self.arquivo = \
            DocxTemplate(
                resource_path(self.base_caminho.format(
                    {unicodedata.normalize("NFKD", nome.upper())}
                ).encode('ascii', 'ignore').decode('ascii'))) \
                    if nome in self.options else None

    def alterar(self, base, updt):  
        self.arquivo.render(base)
        self.arquivo.save(self.caminho)
        self.arquivo = DocxTemplate(self.caminho)
        self.arquivo.render(updt)
        self.arquivo.save(self.caminho)

    def salvar(self):
        self.caminho = asksaveasfilename(title='Defina o nome e o local onde o arquivo será salvo', filetypes=((".docx","*.docx"),))

        if self.caminho[self.caminho.rfind('/') + 1:] == '':
            raise Exception('Operação Cancelada')
        
        self.caminho = self.caminho + '.docx'
        
    
    def abrir(self):
        messagebox.showinfo(title='Aviso', message='Abrindo o arquivo gerado!')
        os.startfile(self.caminho)

class IValido:
    def __init__(self) -> None:
        pass

    def validar(self, ref):
        resp_final = self.__textos_vazios(self.__add_vazios(ref))

        if len(resp_final) != 0:
            raise Exception (f'Estão vazios as seguintes dados:\n{resp_final}\nfavor preencher TODOS')
        
    def __add_vazios(self, ref):
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

        for key, valor in ref.items():
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

class Conteudo:
    def __init__(self, referencias):
        self.dictonary = {chave: copy.deepcopy(valor.get()) for chave, valor in referencias.items()}
        
        self.SAL_MINIMO = 1412.00
        self.CUSTO_CORREIO = 0.02

        self.cabecalho = '{{r nomeEmp }}, estabelecida na rua {{ ruaEmp }}, nº {{ numEmp }}, {{ compleEmp }}, bairro {{ bairroEmp }}, CEP {{ cepEmp }}, CNPJ {{r cnpjEmp }}, neste ato representada por ',

        self.conteudo = {
            1: [
                '{{r nomeContra1 }}, {{ nacionalidadeContra1 }}, {{ empregoContra1 }}, {{ estadoCivilContra1 }}, residente e domiciliado(a) na rua {{ ruaContra1 }}, nº {{ numContra1 }}, {{ compleContra1 }} bairro {{ bairroContra1 }} , CEP {{ cepContra1 }}, {{ cidadeContra1 }}, {{ estadoContra1 }}, portador(a) do documento de identidade sob o nº {{ rgContra1 }} {{ emissorContra1 }}, CPF {{r cpfContra1 }}',

                '''_______________________________                                                  ____________________________________
                    Deltaprice Serviços Contábeis Ltda.                                                        {{r nomeContra1 }}
                '''
                ],
            2: [
                '{{r nomeContra1 }}, brasileiro(a), empresário(a), {{ estadoCivilContra1 }}, residente e domiciliado(a) na rua {{ ruaContra1 }}, nº {{ numContra1 }}, {{ compleContra1 }} bairro {{ bairroContra1 }} , CEP {{ cepContra1 }}, {{ cidadeContra }}, {{ estadoContra1 }}, portador(a) do documento de identidade sob o nº {{ rgContra1 }} {{ emissorContra1 }}, CPF {{r cpfContra1 }} e {{r nomeContra2 }}, brasileiro(a), empresário(a), {{ estadoCivilContra2 }}, residente e domiciliado(a) na rua {{ ruaContra2 }}, nº {{ numContra2 }}, {{ compleContra2 }} bairro {{ bairroContra2 }} , CEP {{ cepContra2 }}, {{ cidadeContra2 }}, {{ estadoContra2 }}, portador(a) do documento de identidade sob o nº {{ rgContra2 }} {{ emissorContra }}, CPF {{r cpfContra2 }} denominados(a) daqui por diante de Contratante;',

                '''_______________________________                                                  ____________________________________
                    Deltaprice Serviços Contábeis Ltda.                                                        {{r nomeContra1 }}
                ''']
        }

    def base(self):
        return {
            'cabecalho_emp' : self.cabecalho[0],
            'honorarios' : self.conteudo[self.qnt][0],
            'assinatura' : self.conteudo[self.qnt][1]
        }

    def update_dict(self, qnt_repre):

        ref = {
            'valorPagamento': self.__set_valor(),
            'numeroRuaEmp': self.__set_num(self.dictonary['numeroRuaEmp']),
            'diaVenc': self.__set_num(self.dictonary['diaVencimento']),
            'dataComple': lambda: self.dictonary['dataInicio'].get()[2:],
            'dataAssinatura': self.__set_data(self.dictonary['dataAssinatura']),
            'dataInicio': self.__set_data(self.dictonary['dataInicio']),
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
    
class Opcionais:
    def __init__(self, frame):
        self.janela = Toplevel(frame, bd=4, bg='darkblue' )
        self.janela.resizable(False,False)
        self.janela.iconbitmap(resource_path('imgs\\cps-icon.ico'))
        self.janela.transient(window)
        self.janela.focus_force()
        self.janela.grab_set()
        self.janela.protocol("WM_DELETE_WINDOW", self.__disable_x)

        self.janela_frame = Frame(self.janela, bd=4, bg='lightblue')
        self.janela_frame.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
        self.janela.geometry('300x70')
        self.janela.title('Complemento')
        
    def __disable_x(self):
        pass

    def exibir(self, title, ref):
        #Titulo
        Label(self.janela_frame, text= title,\
            background='lightblue', font=('Times New Roman',15,'bold italic'))\
                .place(relx=0,rely=0)
                
        self.canvas = Canvas(self.janela_frame, width=625, height=10, background='darkblue',border=-5)
        self.canvas.place(relx=0.55,rely=0.05)
                
        self.canvas.create_line(-5,0,625,0, fill="darkblue", width=10)

        ###########Valor Competência
        valComp = StringVar()

        self.entryVal = Entry(
            self.janela_frame, 
            textvariable = valComp,
            validate='key', 
            validatecommand=(
                self.janela.register(lambda text: not text.isdecimal()), '%S'
                )
            ).place(relx=0,rely=0.65,relwidth=0.7,relheight=0.3)
                
        ref[f'val{title}'] = valComp

        Button(self.janela_frame, text='OK',\
            command= lambda: self.janela.destroy())\
                .place(relx=0.75,rely=0.6,relwidth=0.15,relheight=0.4)
        
class Layout():
    def __init__(self) -> None:
        pass

    def  janela(self, obj, id, frame):
        self.janela = Toplevel(frame, bd=4, bg='darkblue' )
        self.janela.resizable(False,False)
        self.janela.iconbitmap(resource_path('imgs\\cps-icon.ico'))
        self.janela.transient(window)
        self.janela.focus_force()
        self.janela.grab_set()
        self.janela.geometry('880x190')
        self.janela.title(f'Entrada Sócio {id}')
        self.janela.protocol("WM_DELETE_WINDOW", self.__disable_x)

        obj.frame_ativo = Frame(self.janela, bd=4, bg='lightblue')
        obj.frame_ativo.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)

        obj.base(id)

        obj.compleEntry.place(relx=0.65,rely=0.85,relwidth=0.225,relheight=0.15)

        Button(obj.frame_ativo, text='OK',\
            command= lambda: self.__fechar_janela(obj))\
                .place(relx=0.9,rely=0.75,relwidth=0.1,relheight=0.25)
        
    def __fechar_janela(self, obj):
        self.janela.destroy()
        obj.exibir()

    def __disable_x(self):
        pass
        
        # Opcionais(self.frame_ativo).exibir('Emprego', self.referencias)if empreg_var.get() else self.referencias['empregoContra' + id].set('empresário(a)'))\

        # subLista.add_command(label='Comunhão Parcial de Bens', \
        #     command= lambda: estadoEntry.set('casado(a) em CPB'))
        
        # subLista.add_command(label='Comunhão Universal de Bens',\
        #     command= lambda: estadoEntry.set('casado(a) em CUB'))
        
        # subLista.add_command(label='Separação Total de Bens',\
        #     command= lambda: estadoEntry.set('casado(a) em STB'))
        ...


class IExececao(metaclass=ABCMeta):
    @abstractmethod
    def index(self):
        pass

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        #TODO Referencias
        self.referencias = {}

        self.valores_gerais = [
            'valorPagamento',
            'dataInicio',
            'dataAssinatura',
            'diaVencimento',
            'numeroRuaEmp',
            'nomeEmp',
            'ruaEmp',
            'numEmp',
            'bairroEmp',
            'cepEmp',
            'cnpjEmp',
            'compleEmp',
            'valCompe'
            ]

        self.valores_contratante = [
            'nomeContra',
            'rgContra',  
            'emissorContra', 
            'cpfContra', 
            'estadoCivilContra',
            'nacionalidadeContra', 
            'empregoContra',
            'tipoRua',
            'tipoRepre',
            'ruaContra', 
            'numContra', 
            'bairroContra',  
            'cepContra',  
            'cidadeContra', 
            'estadoContra', 
            'compleContra'
            ]
        
        self.status_contratante = {
            'nacionalidadeContra': 'brasileiro(a)',
            'empregoContra': 'empresário(a)'
        }

        
        self.init_reference()

        self.ID_MENU = 0
        self.ID_FORM = 1

        self.file = File()
        self.excecao = None

        self.setWindowTitle('Gerador de CPS')

        self.setWindowIcon(QIcon(
            resource_path('src\\imgs\\cps-icon.ico'))
        )

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
            lambda: self.stackedWidget.setCurrentIndex(0)
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

    def init_reference(self):
        for i in self.valores_gerais:
            self.referencias[i] = ''
        
        for index in range(1, 3):
            for nome in self.valores_contratante:
                self.referencias[nome + str(index)] = ''

            for nome, valor in self.status_contratante.items():
                self.referencias[nome + str(index)] = valor

    def executar(self):
        #TODO EXECUTAR
        try:
            IValido.validar(self.filtro())

            conteudo = Conteudo(self.referencias)

            base = conteudo.base()
            atualizado = conteudo.update_dict(self.comboBox_repre.currentData())

            self.file.salvar()
            self.file.alterar(base, atualizado)
            self.file.abrir()
        except decimal.InvalidOperation:
            messagebox.showwarning(title='Aviso', message= 'Insira um número válido')
        except ValueError:
            messagebox.showwarning(title='Aviso', message= 'Insira datas válidas')
        except Exception as e:
            messagebox.showwarning(title='Aviso', message= e)

    def acess_form(self, titulo: str, excecao: IExececao|None):
        self.stackedWidget.setCurrentIndex(self.ID_FORM)

        self.excecao = excecao
        self.file.set_option(titulo)

        if self.excecao != None:
            self.excecao.index(self)

    def filtro(self):
        ref_temp = {
            chave: copy.deepcopy(valor.get()) for chave, valor in self.referencias.items()
        }

        ref_temp.pop('compleEmp')

        if type(self.excecao) == IFisica:
            for i in self.itens_juri:
                ref_temp.pop(i,None)

        for i in range(1, self.comboBox_repre.currentData() +1):
            ref_temp.pop('emissorContra' + str(i))
            ref_temp.pop('compleContra' + str(i))
            if ref_temp['nacionalidadeContra' + str(i)] != 'brasileiro(a)':
                ref_temp.pop('rgContra' + str(i))

        for i in range(self.comboBox_repre.currentData() + 1, 4):
            for j in self.itens_repre:
                ref_temp.pop(j + str(i),None)

        return ref_temp

class ILucroPresumido(IExececao):
    def index(self: MainWindow):
        print('oi')

class IFisica(IExececao):
    def index(self: MainWindow):
        print('oi')

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()