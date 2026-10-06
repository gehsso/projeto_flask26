from dao.base_dao import BaseDAO
from dao.db_config import get_connection

class AlunoDAO(BaseDAO):
    
    sql_select = 'select id, nome, idade, cidade from aluno'

