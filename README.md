# Gerador de Contratos CPS

Este projeto é uma aplicação desktop para geração automatizada de contratos de prestação de serviços contábeis (CPS), utilizando interface gráfica baseada em PySide6 (Qt for Python) e integração com modelos de documentos Word (.docx).

## Funcionalidades

- **Geração automática de contratos**: Preencha os dados do cliente, empresa e representantes e gere contratos personalizados em formato Word.
- **Modelos de contrato**: Suporte a diferentes tipos de contratos (Pessoa Física, Inatividade, Lucro Presumido, Simples Nacional).
- **Validação de campos**: O sistema verifica se todos os campos obrigatórios foram preenchidos antes de gerar o contrato.
- **Consulta automática de endereço**: Preenchimento automático de endereço a partir do CEP usando a API ViaCEP.
- **Cálculo automático de valores**: Conversão de valores para extenso, cálculo de porcentagens e formatação de datas.
- **Interface intuitiva**: Interface gráfica amigável, com navegação por abas e animação de carregamento durante a geração do contrato.
- **Suporte a múltiplos representantes**: Permite adicionar até três representantes para o contratante.
- **Personalização de campos**: Possibilidade de adicionar nacionalidade e cargo personalizados para representantes.

## Tecnologias Utilizadas

- **Python 3**
- **PySide6** (Qt for Python)
- **docxtpl** (para manipulação de arquivos .docx)
- **num2words** (para conversão de números em texto)
- **requests** (para integração com a API ViaCEP)
- **unidecode, copy, re, json, etc.**

## Estrutura do Projeto

- `code/index.py`: Arquivo principal da aplicação, contendo toda a lógica de interface, validação, geração de contratos e integração com modelos.
- `src/window_cps.py`: Arquivo gerado pelo Qt Designer, contendo a definição da interface gráfica.
- `src/CPS's/`: Pasta com os modelos de contratos em formato `.docx`.
- `src/imgs/`: Imagens utilizadas na interface (logos, ícones, animações).

## Como Usar

1. **Instale as dependências**:
    ```
    pip install -r requirements.txt
    ```
    (Certifique-se de incluir as bibliotecas: PySide6, docxtpl, num2words, requests, unidecode.)

2. **Execute o programa**:
    ```
    python code/index.py
    ```

3. **Preencha os campos** conforme o tipo de contrato desejado.

4. **Gere o contrato** clicando no botão "Executar". O arquivo será salvo no local escolhido e aberto automaticamente.

## Observações

- Os modelos de contrato devem estar na pasta `src/CPS's/` com os nomes correspondentes às opções do menu.
- O sistema utiliza locale `pt_BR.UTF-8` para formatação de valores e datas.
- Para funcionamento correto da consulta de CEP, é necessário acesso à internet.

## Licença

Este projeto é de uso interno e não possui licença aberta.