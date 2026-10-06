from dao.db_config import get_connection

class BaseDAO:
    
    def listar(self):
        conn = get_connection() # Cria/conecta ao BD
        cursor = conn.cursor() # Cursor - "caneta" para escrever SQL
        cursor.execute(self.sql_select) #Executa consulta SQL
        lista = cursor.fetchall() # Retorna lista de tuplas
        conn.close
        print('listar de BaseDAO')
        return lista      