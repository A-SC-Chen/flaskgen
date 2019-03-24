from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from chatheads import chatheads
from flask_socketio import SocketIO
# from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key= 'fds312312is not important'

"""
# Configure MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'lorem'
app.config['MYSQL_PASSWORD'] = 'lorem'
app.config['MYSQL_DB'] = 'lorem'
app.config['MYSQL_CURSORCLASS'] = 'DistCursor'

# initiate MySQL

mysql = MySQL(app)
"""
chatheads = chatheads()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/trial')
def trial():
    return render_template('trial.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html', chatheads = chatheads)

@app.route('/about')
def about():
    return render_template('about.html', chatheads = chatheads)

@app.route('/shortcuts')
def articles():
    return render_template('articles.html')

@app.route('/confirmed')
def confirmed():
    return render_template('confirmed.html')

@app.route('/chat/<string:name>')
def chat(name):
    return render_template('chat.html', name=name)

class RegisterForm(Form):
    name = StringField('Name', [validators.length(min=1, max=20)])
    username = StringField('Username', [validators.length(min=4, max=25)])
    email = StringField('Email', [validators.length(min=6, max=50)])
    # password requires PasswordField instead
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        """ #create cursor
        # cur = mysql.connection.cursor()
        
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, 
        %s, %s, %s)"), (name, email, username, password)
        
        mysql.connect.commit()
        
        cur.close()
        
        """
        return redirect(url_for('home') + 'confirmed')

    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)