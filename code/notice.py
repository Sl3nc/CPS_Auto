class Aviso:
    """
    Responsável por validar se todos os campos obrigatórios foram preenchidos.
    """
    def __init__(self, ref) -> None:
        self.ref = ref
        pass

    def validar(self):
        """
        Verifica se há campos vazios e lança exceção se necessário.
        """
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
