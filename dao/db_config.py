import psycopg2

DB_PATH = "postgresql://neondb_owner:npg_MDElQSzfU2i6@ep-summer-violet-acwc2vxb-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
     conn = psycopg2.connect(DB_PATH) # Cria/conecta ao BD
     return conn
















"""
import psycopg2
DB_PATH = "postgresql://neondb_owner:npg_MDElQSzfU2i6@ep-summer-violet-acwc2vxb-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

"""