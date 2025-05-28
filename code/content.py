from docxtpl import RichText
from datetime import datetime
from copy import deepcopy
from num2words import num2words

class Conteudo:
    """
    Manipula e prepara os dados que serão inseridos no contrato, incluindo
    formatação, cálculos e textos em extenso.
    """
    def __init__(self, referencias: dict[str:str]):
        self.dictonary = deepcopy(referencias)
        
        self.SAL_MINIMO = 1518.00
        self.CUSTO_CORREIO = 0.02

        self.cabecalho = RichText('{{r nomeEmp }}, estabelecida na rua {{r ruaEmp }}, nº {{r numEmpre }}, {{r compleEmp }}, bairro {{r bairroEmp }}, CEP {{r cepEmp }}, CNPJ {{r cnpjEmp }}, neste ato representado(a) por ', size= 20, font= 'Calibri'),

        self.honorario_base = {
            1: 
                RichText('{{r nomeContra1 }}, {{r nacionalidadeContra1 }}, {{r empregoContra1 }}, {{r estadoCivilContra1 }}, residente e domiciliado(a) na {{r ruaContra1 }}, nº {{r numContra1 }}, {{r compleContra1 }} bairro {{r bairroContra1 }} , CEP {{r cepContra1 }}, {{r cidadeContra1 }}, {{r estadoContra1 }}, portador(a) do documento de identidade sob o nº {{r rgContra1 }} {{r emissorContra1 }}, CPF {{r cpfContra1 }}', size= 20, font= 'Calibri'),
               
            2:
                RichText('{{r nomeContra1 }}, {{r nacionalidadeContra1 }}, {{ empregoContra1 }}, {{r estadoCivilContra1 }}, residente e domiciliado(a) na rua {{r ruaContra1 }}, nº {{r numContra1 }}, {{r compleContra1 }} bairro {{r bairroContra1 }} , CEP {{r cepContra1 }}, {{r cidadeContra }}, {{r estadoContra1 }}, portador(a) do documento de identidade sob o nº {{r rgContra1 }} {{r emissorContra1 }}, CPF {{r cpfContra1 }} e {{r nomeContra2 }}, {{r nacionalidadeContra2 }}, {{r empregoContra2 }}, {{r estadoCivilContra2 }}, residente e domiciliado(a) na rua {{r ruaContra2 }}, nº {{r numContra2 }}, {{r compleContra2 }} bairro {{r bairroContra2 }} , CEP {{r cepContra2 }}, {{r cidadeContra2 }}, {{r estadoContra2 }}, portador(a) do documento de identidade sob o nº {{r rgContra2 }} {{r emissorContra }}, CPF {{r cpfContra2 }} denominados(a) daqui por diante de Contratante;', size= 20, font= 'Calibri'),

            3: 
                RichText('{{r nomeContra1 }}, {{r nacionalidadeContra1 }}, {{r empregoContra1 }}, {{r estadoCivilContra1 }}, residente e domiciliado(a) na rua {{r ruaContra1 }}, nº {{r numContra1 }}, {{r compleContra1 }} bairro {{r bairroContra1 }} , CEP {{r cepContra1 }}, {{r cidadeContra }}, {{r estadoContra1 }}, portador(a) do documento de identidade sob o nº {{r rgContra1 }} {{r emissorContra1 }}, CPF {{r cpfContra1 }}, {{r nomeContra2 }}, {{r nacionalidadeContra2 }}, {{r empregoContra2 }}, {{r estadoCivilContra2 }}, residente e domiciliado(a) na rua {{r ruaContra2 }}, nº {{r numContra2 }}, {{r compleContra2 }} bairro {{r bairroContra2 }} , CEP {{r cepContra2 }}, {{r cidadeContra2 }}, {{r estadoContra2 }}, portador(a) do documento de identidade sob o nº {{r rgContra2 }} {{r emissorContra2 }}, CPF {{r cpfContra2 }} e {{r nomeContra3 }}, {{r nacionalidadeContra3 }}, {{r empregoContra3 }}, {{r estadoCivilContra3 }}, residente e domiciliado(a) na rua {{r ruaContra3 }}, nº {{r numContra3 }}, {{r compleContra3 }} bairro {{r bairroContra3 }} , CEP {{r cepContra3 }}, {{r cidadeContra3 }}, {{r estadoContra3 }}, portador(a) do documento de identidade sob o nº {{r rgContra3 }} {{r emissorContra3 }}, CPF {{r cpfContra3 }} denominados(as) daqui por diante de Contratante;', size= 20, font= 'Calibri')
        }

        self.assinatura_base = {
            1:  
                RichText('''_______________________________     
                
                
                ______________________________
                Deltaprice Serviços Contábeis Ltda.                                                        {{r nomeContra1 }}
                ''', size= 20, font= 'Calibri'),
            2: 
                RichText('''_______________________________                                                  ____________________________________
                    Deltaprice Serviços Contábeis Ltda.                                                        {{r nomeContra1 }}
                    {{r nomeContra2 }}
                ''', size= 20, font= 'Calibri'),
            3: 
                RichText('''_______________________________                                                  ____________________________________
                    Deltaprice Serviços Contábeis Ltda.                                                        {{r nomeContra1 }}
                    {{r nomeContra2 }}
                    {{r nomeContra3 }}
                ''', size= 20, font= 'Calibri')
        }

        self.rodape = {
            1: RichText(
                '''
                    {{r nomeContra1 }}
                ''', bold = True, size= 20, font= 'Calibri'),
            2: RichText(
                '''
                    {{r nomeContra1 }}
                    {{r nomeContra2 }}
                ''', bold = True, size= 20, font= 'Calibri'),
            3: RichText(
                '''
                    {{r nomeContra1 }}
                    {{r nomeContra2 }}
                    {{r nomeContra3 }}
                ''', bold = True, size= 20, font= 'Calibri'),
        }

    def base(self, index_atual: int):
        """
        Retorna o dicionário base para renderização do contrato.
        """
        return {
            'cabecalho_emp' : self.cabecalho[0],
            'honorarios' : self.honorario_base[index_atual],
            'assinatura' : self.assinatura_base[index_atual],
            'rodape': self.rodape[index_atual]
        }

    def update_dict(self, qnt_repre):
        """
        Atualiza o dicionário de referências com valores calculados e formatados.
        """
        ref = {
            'valPag': self.__set_valor(),
            'diaVenc': self.__set_num(self.dictonary['dtVenc']),
            'dtCompe': lambda: self.dictonary['dtInic'][2:],
            'dtAss': self.__set_data(self.dictonary['dtAss']),
            'dtInic': self.__set_data(self.dictonary['dtInic']),
        }

        self.dictonary['valPorc'] = self.__calc_porc()
        
        for key, func in ref.items():
            self.dictonary[key] = func

        self.__set_empresa()
        self.__update_repre(qnt_repre)
        for key, value in self.dictonary.items():
            if type(self.dictonary[key]) != RichText:
                self.dictonary[key] = RichText(value, size= 20, font='Calibri')

        return self.dictonary
    
    def __update_repre(self, qnt_repre):
        """
        Atualiza os dados dos representantes no dicionário de referências.
        """
        for i in range(1, qnt_repre + 1):
            i = str(i)
            ref = {
                'nomeContra': RichText(self.dictonary['nomeContra' + i].upper(), bold = True, size= 20, font= 'Calibri'),
                'ruaContra': self.dictonary['ruaContra'+ i].title().replace('Rua ',''), 
                'bairroContra':self.dictonary['bairroContra'+ i].title(),
                'cpfContra' : RichText(self.dictonary['cpfContra'+ i].upper(), bold = True, size= 20, font= 'Calibri'),
                'compleContra': self.dictonary['compleContra'+ i].title()
            }

            for index, value in ref.items():
                self.dictonary[index + i] = value

    def __set_empresa(self):
        """
        Define os dados da empresa no dicionário de referências.
        """
        if self.dictonary.get('nomeEmp') != None:

            ref = {
                'nomeEmp': RichText(self.dictonary['nomeEmp'].upper(), bold = True, size= 20, font= 'Calibri'),
                'ruaEmp': self.dictonary['ruaEmp'].title().replace('Rua ',''), 
                'bairroEmp':self.dictonary['bairroEmp'].title(),
                'cnpjEmp' : RichText(self.dictonary['cnpjEmp'].upper(), bold = True, size= 20, font= 'Calibri'),
                'compleEmp': self.dictonary['compleEmp'].title()
            }

            for index, value in ref.items():
                self.dictonary[index] = value

    def __set_valor(self):
        """
        Formata o valor do pagamento em moeda e por extenso.
        """
        valor = self.dictonary['valPag'].replace(',','.').replace('R$','')
        valorExtenso = num2words(valor, lang='pt_BR', to='currency')\
            .replace('reais e','reais,')
        return f'R$ {float(valor):_.2f} ({valorExtenso})'.replace('.',',').replace('_','.')
    
    def __set_num(self, num: str):
        """
        Formata números para exibição no contrato, incluindo por extenso.
        """
        if num.isdigit() == True:
            valorExtenso = num2words(num,lang='pt_BR')
            return f'{num} ({valorExtenso})'
        return 'S/N'

    def __set_data(self, data):
        """
        Converte e formata datas para o padrão do contrato.
        """
        data_format = datetime.strptime(data, '%d/%m/%Y')
        return data_format.strftime("%d de %B de %Y")
        
    def __calc_porc(self):
        """
        Calcula a porcentagem do valor do contrato que corresponde ao custo de envio.
        """
        valor = self.dictonary['valPag'].replace(',','.').replace('R$','')
        custo_envio = self.SAL_MINIMO * self.CUSTO_CORREIO
        return f'{((custo_envio / float(valor)) * 100):,.2f}%'