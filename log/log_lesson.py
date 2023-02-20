from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG
from logging import basicConfig
from logging import critical, error, warning, info, debug


# Forma como o log vai se comportar na aplicação
basicConfig(
    level=DEBUG,
    filename='logs.log',
    filemode='a',
)

# debug('Estou testando')
# critical('Senha do usuário foi exposta')

try:
    x = int(input('Digite um numero'))

    y = 10/x

except ZeroDivisionError:
    warning('Tentou dividir por zero')