from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

data = '02/02/2014'
data_format = datetime.strptime(data, '%d/%m/%Y')
print( data_format.strftime("%d de %B de %Y"))