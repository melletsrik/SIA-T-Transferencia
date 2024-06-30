import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
            dbname="db_transferencia",
            user="postgres",
            password="root",
            host="localhost",  # O el host donde está corriendo tu servidor PostgreSQL
            port="5432"  # Puerto por defecto de PostgreSQL
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error al conectar a PostgreSQL: {e}")
        return None
