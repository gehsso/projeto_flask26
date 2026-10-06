from dao.base_dao import BaseDAO

class ProfessorDAO(BaseDAO):
    
    sql_select = 'select id, nome, disciplina from professor'
    
