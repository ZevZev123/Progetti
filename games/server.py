from flask import Flask, render_template
import connection

# connection details
db_name = 'Games'
db_password = '250571'

conn = connection.create_connection(db_name, db_password)
if conn is None:
    print("Failed to connect to the database.")
    exit(1)

server = Flask(__name__)
server.config['SECRET_KEY'] = '250571'
server.config['DEBUG'] = True
server.config['TEMPLATES_AUTO_RELOAD'] = True

@server.route('/', methods=['GET'])
def main():
    return render_template('main.html', list=connection.execute_read_query(conn, "SELECT * FROM gioco"))

server.run()

connection.close_connection(conn)