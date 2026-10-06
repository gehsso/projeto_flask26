from dao.base_dao import BaseDAO
from dao.db_config import get_connection

class AlunoDAO(BaseDAO):
    
    sql_select = 'select id, nome, idade, cidade from aluno'

    def salvar(self, id, nome, idade, cidade):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO aluno (nome, idade, cidade) VALUES (%s, %s, %s)', (nome, idade, cidade))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
