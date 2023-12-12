import pandas as pd
from ..common import DefaultConfiguration, Layout, DataFrameColumns, TipoPessoa, Converter

config: DefaultConfiguration = {
    "codigo_banco": "033",
    "tipo_inscricao": "2",
    "numero_inscricao_empresa": "123456456",
    "codigo_convenio": "10123123132",
    "agencia_mantenedora_conta": "0002",
    "numero_conta_corrente": "1234562",
    "digito_verificador_conta": "5",
    "nome_empresa": "ADAN EINSTEIN SA",
    "nome_banco": "BANCO SANTANDER",
    "endereco": "RUA A",
    "numero": "10",
    "cidade": "SUZANO",
    "cep": "11012",
    "complemento_cep": "000",
    "uf": "SP",
    "g010": "1",
    "g011": "0",
    "g012": "00",
    "g013a": "99",
    "g013b": "99999",
    "g013c": "CC",
    "g015": "20",
    "g016": "",
    "g002": "45",
    "g005": "BRL",
    "g014": "009",
    "g018": "0",
    "g032": "05",
    "versao_header_arquivo": "060",
    "versao_header_lote": "031"
}

class Columns(DataFrameColumns):
    AGENCIA = 'ag'
    TIPO_PESSOA = 'tp'
    CODIGO_BANCO = 'cp'
    NOME_FAVORECIDO = 'nm'
    DATA_PAGAMENTO = 'dp'
    CPFJ_FAVORECIDO = 'nd'
    CONTA_CORRENTE = 'cc'
    VALOR_PAGAMENTO = 'vp'

df = pd.DataFrame({
    'ag': ['123', '456'],
    'tp': [TipoPessoa.FISICA, TipoPessoa.JURIDICA],
    'cp': ['033', '140'],
    'nm': ['ADAN', 'EINSTEIN'],
    'dp': ['01/01/01', '26/08/01'],
    'nd': ['12345612345', '78945612345'],
    'cc': ['1231212', '12324545'],
    'vp': ['100,00', '100.00'],
})

layout = Layout(data_frame=df, default_options=config, df_columns=Columns)

build = Converter(layout).build()

with open('result.txt', 'w') as file:
    file.write(build.read().decode('utf8'))