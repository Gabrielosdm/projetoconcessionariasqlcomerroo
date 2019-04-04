from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *


# Instanciando a app Flask
app = Flask(__name__)
# Instanciar o objeto MySQL
mysql = MySQL()
# Ligar o MYSQL ao Flask
mysql.init_app(app)

# Configurando o acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'concessionaria'

#rota para (/)
@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/patio', methods=['GET','POST'])
def carros():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        # Obtendo o cursor para acessar o BD
        cursor = mysql.get_db().cursor()

        # Obtendo o idlogin
        idfuncionarios = get_idfuncionarios(cursor, login, senha)

        # Verificar a senha
        if idfuncionarios is None:
            return render_template('login.html', erro='Login/senha incorretos!')
        else:
            # Obtendo o cursor para acessar o BD
            cursor = mysql.get_db().cursor()

            return render_template('patio.html')

    else:
        return render_template('login.html', erro='Método incorreto. Use POST!')


# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)


