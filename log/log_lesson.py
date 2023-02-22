from logging import (CRITICAL, DEBUG, ERROR, INFO, WARNING, FileHandler,
                     Filter, StreamHandler, basicConfig, critical, debug,
                     error, info, warning)


# Criando filtros para os logs
class Filtro(Filter):
    def filter(self, record):
        if 'cartão' in record.msg:
            record.msg = 'Vazou a senha do cartão!!! ATENÇÃO'
            return True
        return False 

file_handler = FileHandler('logs.log', 'a')
# Setando Warning no file_handler para que sejam salvos 
# logs a partir do Warning 
file_handler.setLevel(WARNING)
# Adicionndo o filtro em file_handler 
file_handler.addFilter(Filtro())


# Da para criar níveis de gravidade para os handlers
stream_handler = StreamHandler()


# Forma como o log vai se comportar na aplicação
basicConfig(
    level=DEBUG,
    format='%(levelname)s:%(asctime)s:%(message)s',
    #Para cada handler especifico vai ter um level diferente
    handlers=[file_handler, stream_handler]
)

# debug('Estou testando')
# critical('Senha do usuário foi exposta')

critical('cartão 12345')
