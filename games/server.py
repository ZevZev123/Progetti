from flask import Flask, render_template
from flask import request, redirect, url_for, session, flash
import connection

# connection details
db_name = 'Games'
db_password = ''

session = {'username': None}

# conn = connection.create_connection(db_name, db_password)
# if conn is None:
#     print("Failed to connect to the database.")
#     exit(1)

listaGiochi = [('In Sound Mind', 'In Sound Mind is an imaginative first-person psychological horror with frenetic puzzles, unique boss fights, and original music by The Living Tombstone. Journey within the inner workings of the one place you can’t seem to escape—your own mind.', 1, '/static/gameImages/inSoundMind.jpg', 'https://store.steampowered.com/app/1119980/In_Sound_Mind/'),
               ('The Dark Pictures Anthology: the devil in me', 'La troupe di un documentario riceve un misterioso invito a visitare la riproduzione del "Castello della morte" del serial killer H.H. Holmes. Presto scopriranno che qualcuno li sta osservando, e persino manipolando, e che le visualizzazioni dei loro video non sono l\'unica cosa di cui preoccuparsi!', 5, '/static/gameImages/theDevilInMe.jpg', 'https://store.steampowered.com/app/1567020/The_Dark_Pictures_Anthology_The_Devil_in_Me/'),]

listaUtenti = [('admin', 'admin'), ('zev', 'a')]

server = Flask(__name__)
server.secret_key = 'abcdadmin'
server.config['DEBUG'] = True
server.config['TEMPLATES_AUTO_RELOAD'] = True

@server.route('/home', methods=['GET'])
def main():
    return render_template('main.html', list=listaGiochi, username=session['username'])

@server.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (username, password) in listaUtenti:
            session['username'] = username  # Salva l'utente nella sessione
            return redirect(url_for('main'))
        else:
            return render_template('login.html', error="Invalid username or password.")
    return render_template('login.html')

@server.route('/logout', methods=['GET'])
def logout():
    session['username'] = None
    flash('Logout effettuato con successo.', 'success')
    return redirect(url_for('main'))

@server.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return render_template('register_success.html', username=session['username'])
    return render_template('register.html')

server.run()

# connection.close_connection(conn)