import psycopg2

def create_connection(dbname, password, user='postgres', host='localhost', port='5432'):
    """Create a database connection to a PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Connection to the database was successful.")
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def close_connection(conn):
    """Close the database connection."""
    if conn:
        conn.close()
        print("Connection closed.")
    else:
        print("No connection to close.")

def execute_query(conn, query, params=None):
    """Execute a single query."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            print("Query executed successfully.")
    except Exception as e:
        print(f"Error executing query: {e}")
        conn.rollback()

def execute_read_query(conn, query):
    """Execute a read query and return the results."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            print("Query executed successfully.")
            return result
    except Exception as e:
        print(f"Error executing read query: {e}")
        return None
    
if (__name__ == "__main__"):
    conn = create_connection('Games', '250571')
    execute_query(conn, "INSERT INTO gioco (nome, descrizione, numgiocatorimassimi, immagine, link) VALUES (%s, %s, %s, %s, %s)", ('In Sound Mind', 'In Sound Mind is an imaginative first-person psychological horror with frenetic puzzles, unique boss fights, and original music by The Living Tombstone. Journey within the inner workings of the one place you can’t seem to escape—your own mind.', 1, 'inSoundMind.jpg', 'https://store.steampowered.com/app/1119980/In_Sound_Mind/'))

    close_connection(conn)


# Example SQL Queries:

# DELETE FROM <tabella> WHERE <condizione>
# INSERT INTO <tabella> (<colonna1>, <colonna2>, ...) VALUES (%s, %s, ...)
# UPDATE <tabella> SET <colonna1> = %s, <colonna2> = %s WHERE <condizione>
# SELECT * FROM <tabella> WHERE <condizione>