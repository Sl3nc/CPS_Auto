from tkinter import *
from tkinter import messagebox
from docx import Document
import os

window = Tk()

class application:
    def __init__(self):
        self.window = window
        self.tela()
        self.pageMenu()
        window.mainloop()

    def tela(self):
        self.window.configure(background='darkblue')
        self.window.resizable(True,True)
        self.window.minsize(width=860, height=500)
        self.window.maxsize(width=860, height=500)
        self.window.title('Gerador de CPS')

    def pageMenu(self):
        self.menu = Frame(self.window, bd=4, bg='lightblue')
        self.menu.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)

        self.textOrientacao = Label(self.menu, text='Selecione o tipo de CPS que deseja fazer:', background='lightblue', font=('Bold', 15))\
        .place(relx=0.12,rely=0.1,relheight=0.15)

        #Pessoa física
        self.btnPF = Button(self.menu, text='CPS Pessoa Física',\
            command= lambda: self.pagePF())\
                .place(relx=0.15,rely=0.7,relwidth=0.25,relheight=0.15)

        #Inatividade
        self.btnIN = Button(self.menu, text='CPS Inatividade',\
            command= lambda: self.pageIN())\
                .place(relx=0.60,rely=0.4,relwidth=0.25,relheight=0.15)

        #Lucro Presumido
        self.btnLP = Button(self.menu, text='CPS Lucro Presumido',\
            command= lambda: self.pageLP())\
                .place(relx=0.15,rely=0.4,relwidth=0.25,relheight=0.15)

        #Simples Nacional
        self.btnSN = Button(self.menu, text='CPS Simples Nacional',\
            command= lambda: self.pageSN())\
                .place(relx=0.60,rely=0.7,relwidth=0.25,relheight=0.15)

    def pagePF(self):
        self.menu.destroy()
        self.doc = Document('.\code\CPS\'s\CPS PESSOA FISICA.docx')

        self.cpsPF = Frame(self.window, bd=4, bg='lightblue')
        self.cpsPF.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)

        #Titulo
        Label(self.cpsPF, text='Gerador de CPS Pessoa física', background='lightblue', font=('arial',17,'bold'))\
            .place(relx=0.3,rely=0.05)

        #Botão voltar
        Button(self.cpsPF, text='Voltar ao menu',\
            command= lambda: (self.cpsPF.destroy, self.pageMenu()))\
                .place(relx=0,rely=0,relwidth=0.25,relheight=0.06)

        self.referencias = {
            '$nomeContra' : StringVar(), #strValidator
            '$ruaContra' : StringVar(), #strValidator
            '$numContra' : StringVar(), #intValidator
            '$bairroContra' : StringVar(),  #strValidator
            '$cepContra' : StringVar(),  #intValidator
            '$rgContra' : StringVar(),  #rgValidator
            '$sspContra' : StringVar(),  #sspValidator
            '$cpfContra' : StringVar(),  #cpfValidator
            '$estadoContra' : StringVar(), #strValidator
            "$comple" : StringVar(), #strValidator
            "$dtVenc" : StringVar(),  #dateValidator
            "$valPag" : StringVar(), #intValidator
            "$dtInic" : StringVar()  #dateValidator
        }

        #Labels e Entrys
        #Contratante
        Label(self.cpsPF, text='Contratante',\
            background='lightblue', font=('Times New Roman',15,'bold italic'))\
                .place(relx=0.05,rely=0.2)

        ###########nome

        Label(self.cpsPF, text='Nome',\
            background='lightblue', font=(10))\
                .place(relx=0.05,rely=0.3)

        self.nomeEntry = Entry(self.cpsPF,\
            textvariable=self.referencias['$nomeContra'])\
                .place(relx=0.05,rely=0.37,relwidth=0.25,relheight=0.05)

        ###########rua

        Label(self.cpsPF, text='Rua',\
            background='lightblue', font=(10))\
                .place(relx=0.35,rely=0.30)

        self.ruaEntry = Entry(self.cpsPF,\
            textvariable=self.referencias['$ruaContra'])\
                .place(relx=0.35,rely=0.37,relwidth=0.20,relheight=0.05)

        ###########Num

        Label(self.cpsPF, text='Num.',\
            background='lightblue', font=(10))\
                .place(relx=0.6,rely=0.30)

        self.numEntry = Entry(self.cpsPF,\
            textvariable=self.referencias['$numContra'])\
                .place(relx=0.61,rely=0.37,relwidth=0.05,relheight=0.05)

        ###########bairro

        Label(self.cpsPF, text='Bairro',\
            background='lightblue', font=(10))\
                .place(relx=0.7,rely=0.30)

        self.bairroEntry = Entry(self.cpsPF,\
            textvariable=self.referencias['$bairroContra'])\
                .place(relx=0.7,rely=0.37,relwidth=0.25,relheight=0.05)

        ###########CEP

        Label(self.cpsPF, text='CEP',\
            background='lightblue', font=(10))\
                .place(relx=0.05,rely=0.45)

        self.cepEntry = Entry(self.cpsPF,\
            textvariable=self.referencias['$cepContra'])\
                .place(relx=0.05,rely=0.52,relwidth=0.25,relheight=0.05)

        ###########RG

        Label(self.cpsPF, text='RG',\
            background='lightblue', font=(10))\
                .place(relx=0.35,rely=0.45)

        self.rgEntry = Entry(self.cpsPF,\
            textvariable=self.referencias['$rgContra'])\
                .place(relx=0.35,rely=0.52,relwidth=0.20,relheight=0.05)

        ###########Org. Emissor

        Label(self.cpsPF, text='Org.',\
            background='lightblue', font=(10))\
                .place(relx=0.9,rely=0.45)

        self.sspEntry = Entry(self.cpsPF,\
            textvariable=self.referencias['$sspContra'])\
                .place(relx=0.9,rely=0.52,relwidth=0.05,relheight=0.05)

        ###########CPF

        Label(self.cpsPF, text='CPF',\
            background='lightblue', font=(10))\
                .place(relx=0.6,rely=0.45)

        self.cpfEntry = Entry(self.cpsPF,\
            textvariable=self.referencias['$cpfContra'])\
                .place(relx=0.6,rely=0.52,relwidth=0.25,relheight=0.05)

        ###########Estado Civil

        Label(self.cpsPF, text='Estado Civil',\
            background='lightblue', font=(10))\
                .place(relx=0.35,rely=0.60)

        self.estadoEntry = StringVar(self.cpsPF)

        self.estadoEntryOpt = ('solteiro(a)', 'casado(a)','divorsiado(a)','viuvo(a)')

        self.estadoEntry.set('solteiro(a)')

        self.popup = OptionMenu(self.cpsPF, self.estadoEntry, *self.estadoEntryOpt)\
            .place(relx=0.35,rely=0.67,relwidth=0.2,relheight=0.06)

        self.referencias['$estadoContra'] = self.estadoEntry

        ###########Complemento

        Label(self.cpsPF, text='Complemento',\
            background='lightblue', font=(10))\
                .place(relx=0.6,rely=0.6)

        self.complementoEntry = Entry(self.cpsPF,\
            textvariable=self.referencias['$comple'])\
                .place(relx=0.61,rely=0.67,relwidth=0.35,relheight=0.05)

        #Contrato
        Label(self.cpsPF, text='Contrato',\
            background='lightblue', font=('Times New Roman',15,'bold italic'))\
                .place(relx=0.05,rely=0.7)

        ###########Valor pagamento

        Label(self.cpsPF, text='Val. pagamento',\
            background='lightblue', font=(10))\
                .place(relx=0.05,rely=0.8)

        self.valPagEntry = Entry(self.cpsPF,\
            textvariable=self.referencias['$valPag'])\
                .place(relx=0.05,rely=0.87,relwidth=0.15,relheight=0.05)

        ###########Data inicio

        Label(self.cpsPF, text='Dia início',\
            background='lightblue', font=(10))\
                .place(relx=0.25,rely=0.8)

        self.dtInicEntry = Entry(self.cpsPF,\
            textvariable=self.referencias['$dtInic'])\
                .place(relx=0.25,rely=0.87,relwidth=0.1,relheight=0.05)

        ###########Data pagamento

        Label(self.cpsPF, text='Dia vencimento',\
            background='lightblue', font=(10))\
                .place(relx=0.4,rely=0.8)

        self.dtPagEntry = Entry(self.cpsPF,\
            textvariable=self.referencias['$dtVenc'])\
                .place(relx=0.4,rely=0.87,relwidth=0.1,relheight=0.05)

        #Botão enviar
        Button(self.cpsPF, text='Gerar CPS',\
            command= lambda: self.alterar_doc(frame_ativo=self.cpsPF))\
                .place(relx=0.61,rely=0.8,relwidth=0.35,relheight=0.12)

    def pageIN(self):
        self.menu.destroy()
        self.doc = Document('.\code\CPS\'s\CPS INATIVIDADE.docx')

        self.cpsIN = Frame(self.window, bd=4, bg='lightblue')
        self.cpsIN.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)

        #Titulo
        Label(self.cpsIN, text='Gerador de CPS Inatividade', background='lightblue', font=('arial',17,'bold'))\
            .place(relx=0.3,rely=0.02)

        #Botão voltar
        Button(self.cpsIN, text='Voltar ao menu',\
            command= lambda: (self.cpsIN.destroy, self.pageMenu()))\
                .place(relx=0,rely=0,relwidth=0.25,relheight=0.06)

        self.referencias = {
            '$nomeEmp' : StringVar(), #strValidator
            '$ruaEmp' : StringVar(), #strValidator
            '$numEmp' : StringVar(), #intValidator
            '$bairroEmp' : StringVar(),  #strValidator
            '$cepEmp' : StringVar(),  #intValidator
            '$rgEmp' : StringVar(),  #rgValidator
            '$sspEmp' : StringVar(),  #sspValidator
            '$cnpjEmp' : StringVar(),  #cpfValidator
            '$nomeContra' : StringVar(), #strValidator
            '$ruaContra' : StringVar(), #strValidator
            '$numContra' : StringVar(), #intValidator
            '$bairroContra' : StringVar(),  #strValidator
            '$cepContra' : StringVar(),  #intValidator
            '$rgContra' : StringVar(),  #rgValidator
            '$sspContra' : StringVar(),  #sspValidator
            '$cpfContra' : StringVar(),  #cpfValidator
            '$estadoContra' : StringVar(), #strValidator
            "$comple" : StringVar(), #strValidator
            "$dtVenc" : StringVar(),  #dateValidator
            "$valPag" : StringVar(), #intValidator
            "$dtInic" : StringVar()  #dateValidator
        }

        #Labels e Entrys
        #Empresa
        Label(self.cpsIN, text='Empresa',\
            background='lightblue', font=('Times New Roman',15,'bold italic'))\
                .place(relx=0.05,rely=0.11)
                
        ###########nome empresa

        Label(self.cpsIN, text='Nome empresa',\
            background='lightblue', font=(10))\
                .place(relx=0.05,rely=0.18)

        self.nomeEmpEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$nomeEmp'])\
                .place(relx=0.05,rely=0.23,relwidth=0.25,relheight=0.05)

        ###########rua

        Label(self.cpsIN, text='Rua',\
            background='lightblue', font=(10))\
                .place(relx=0.35,rely=0.18)

        self.ruaEmpEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$ruaEmp'])\
                .place(relx=0.35,rely=0.23,relwidth=0.20,relheight=0.05)

        ###########Num

        Label(self.cpsIN, text='Num.',\
            background='lightblue', font=(10))\
                .place(relx=0.6,rely=0.18)

        self.numEmpEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$numEmp'])\
                .place(relx=0.61,rely=0.23,relwidth=0.05,relheight=0.05)

        ###########bairro

        Label(self.cpsIN, text='Bairro',\
            background='lightblue', font=(10))\
                .place(relx=0.7,rely=0.18)

        self.bairroEmpEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$bairroEmp'])\
                .place(relx=0.7,rely=0.23,relwidth=0.25,relheight=0.05)

        ###########CEP

        Label(self.cpsIN, text='CEP',\
            background='lightblue', font=(10))\
                .place(relx=0.05,rely=0.31)

        self.cepEmpEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$cepEmp'])\
                .place(relx=0.05,rely=0.36,relwidth=0.25,relheight=0.05)

        ###########CNPJ

        Label(self.cpsIN, text='CNPJ',\
            background='lightblue', font=(10))\
                .place(relx=0.35,rely=0.31)

        self.cnpjEmpEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$cnpjEmp'])\
                .place(relx=0.35,rely=0.36,relwidth=0.2,relheight=0.05)
                
        ###########Complemento

        Label(self.cpsIN, text='Complemento',\
            background='lightblue', font=(10))\
                .place(relx=0.6,rely=0.31)

        self.complementoEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$comple'])\
                .place(relx=0.61,rely=0.36,relwidth=0.35,relheight=0.05)
        
        #Socio
        Label(self.cpsIN, text='Sócio',\
            background='lightblue', font=('Times New Roman',15,'bold italic'))\
                .place(relx=0.05,rely=0.42)

        ###########nome

        Label(self.cpsIN, text='Nome',\
            background='lightblue', font=(10))\
                .place(relx=0.05,rely=0.48)

        self.nomeEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$nomeContra'])\
                .place(relx=0.05,rely=0.53,relwidth=0.25,relheight=0.05)

        ###########rua

        Label(self.cpsIN, text='Rua',\
            background='lightblue', font=(10))\
                .place(relx=0.35,rely=0.48)

        self.ruaEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$ruaContra'])\
                .place(relx=0.35,rely=0.53,relwidth=0.20,relheight=0.05)

        ###########Num

        Label(self.cpsIN, text='Num.',\
            background='lightblue', font=(10))\
                .place(relx=0.6,rely=0.48)

        self.numEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$numContra'])\
                .place(relx=0.61,rely=0.53,relwidth=0.05,relheight=0.05)

        ###########bairro

        Label(self.cpsIN, text='Bairro',\
            background='lightblue', font=(10))\
                .place(relx=0.7,rely=0.48)

        self.bairroEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$bairroContra'])\
                .place(relx=0.7,rely=0.53,relwidth=0.25,relheight=0.05)

        ###########CEP

        Label(self.cpsIN, text='CEP',\
            background='lightblue', font=(10))\
                .place(relx=0.05,rely=0.61)

        self.cepEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$cepContra'])\
                .place(relx=0.05,rely=0.66,relwidth=0.25,relheight=0.05)

        ###########RG

        Label(self.cpsIN, text='RG',\
            background='lightblue', font=(10))\
                .place(relx=0.35,rely=0.61)

        self.rgEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$rgContra'])\
                .place(relx=0.35,rely=0.66,relwidth=0.20,relheight=0.05)

        ###########Org. Emissor

        Label(self.cpsIN, text='Org.',\
            background='lightblue', font=(10))\
                .place(relx=0.9,rely=0.61)

        self.sspEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$sspContra'])\
                .place(relx=0.9,rely=0.66,relwidth=0.05,relheight=0.05)

        ###########CPF

        Label(self.cpsIN, text='CPF',\
            background='lightblue', font=(10))\
                .place(relx=0.6,rely=0.61)

        self.cpfEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$cpfContra'])\
                .place(relx=0.61,rely=0.66,relwidth=0.25,relheight=0.05)

        ###########Estado Civil

        Label(self.cpsIN, text='Estado Civil',\
            background='lightblue', font=(10))\
                .place(relx=0.35,rely=0.72)

        self.estadoEntry = StringVar(self.cpsIN)

        self.estadoEntryOpt = ('solteiro(a)', 'casado(a)','divorsiado(a)','viuvo(a)')

        self.estadoEntry.set('solteiro(a)')

        self.popup = OptionMenu(self.cpsIN, self.estadoEntry, *self.estadoEntryOpt)\
            .place(relx=0.35,rely=0.77,relwidth=0.2,relheight=0.06)

        self.referencias['$estadoContra'] = self.estadoEntry

        ###########Complemento

        Label(self.cpsIN, text='Complemento',\
            background='lightblue', font=(10))\
                .place(relx=0.6,rely=0.73)

        self.complementoEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$comple'])\
                .place(relx=0.61,rely=0.78,relwidth=0.35,relheight=0.05)

        #Contrato
        Label(self.cpsIN, text='Contrato',\
            background='lightblue', font=('Times New Roman',15,'bold italic'))\
                .place(relx=0.05,rely=0.8)

        ###########Valor pagamento

        Label(self.cpsIN, text='Val. pagamento',\
            background='lightblue', font=(10))\
                .place(relx=0.05,rely=0.88)

        self.valPagEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$valPag'])\
                .place(relx=0.05,rely=0.93,relwidth=0.15,relheight=0.05)

        ###########Data inicio

        Label(self.cpsIN, text='Dia início',\
            background='lightblue', font=(10))\
                .place(relx=0.25,rely=0.88)

        self.dtInicEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$dtInic'])\
                .place(relx=0.25,rely=0.93,relwidth=0.1,relheight=0.05)

        ###########Data pagamento

        Label(self.cpsIN, text='Dia vencimento',\
            background='lightblue', font=(10))\
                .place(relx=0.4,rely=0.88)

        self.dtPagEntry = Entry(self.cpsIN,\
            textvariable=self.referencias['$dtVenc'])\
                .place(relx=0.4,rely=0.93,relwidth=0.1,relheight=0.05)

        #Botão enviar
        Button(self.cpsIN, text='Gerar CPS',\
            command= lambda: self.alterar_doc(frame_ativo=self.cpsIN))\
                .place(relx=0.61,rely=0.865,relwidth=0.35,relheight=0.12)

    def pageLP(self):
        self.menu.destroy()

        self.cpsLP = Frame(self.window, bd=4, bg='lightblue')
        self.cpsLP.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)

        self.textOrientacao = Label(self.cpsLP, text='OI', background='lightblue', font=('Bold', 15))\
            .place(relx=0.22,rely=0.1,relheight=0.15)

        #Botão voltar
        self.btnVoltar = Button(self.cpsLP, text='Voltar ao menu',\
            command= lambda: (self.cpsLP.destroy, self.pageMenu()))\
                .place(relx=0.15,rely=0.7,relwidth=0.25,relheight=0.15)

    def pageSN(self):
        self.menu.destroy()

        self.cpsSN = Frame(self.window, bd=4, bg='lightblue')
        self.cpsSN.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)

        self.textOrientacao = Label(self.cpsSN, text='OI', background='lightblue', font=('Bold', 15))\
            .place(relx=0.22,rely=0.1,relheight=0.15)

        #Botão voltar
        self.btnVoltar = Button(self.cpsSN, text='Voltar ao menu',\
            command= lambda: (self.cpsSN.destroy, self.pageMenu()))\
                .place(relx=0.15,rely=0.7,relwidth=0.25,relheight=0.15)

    def alterar_doc(self, frame_ativo):
        for par in self.doc.paragraphs:
            for itens in self.referencias:
                if par.text.find(itens) != -1:
                    par.text = par.text.replace(itens, self.referencias[itens].get())


        self.doc.save('CPS_testeResult.docx')
        messagebox.showinfo(title='Aviso', message='Abrindo arquivo gerado!')
        os.startfile('C:\pedro\CPS Pessoa Física\Code\CPS_testeResult.docx')

        frame_ativo.destroy()
        self.pageMenu()



application()