from logging import (CRITICAL, DEBUG, ERROR, INFO, WARNING, FileHandler,
                     StreamHandler, basicConfig, critical, debug, error, info,
                     warning)

# Forma como o log vai se comportar na aplicação
basicConfig(
    level=DEBUG,
    format='%(levelname)s:%(asctime)s:%(message)s',
    handlers=[StreamHandler(), FileHandler('logs.log', 'a')]
)

# debug('Estou testando')
# critical('Senha do usuário foi exposta')

try:
    x = int(input('Digite um numero'))

    y = 10/x

except ZeroDivisionError:
    warning('Tentou dividir por zero')