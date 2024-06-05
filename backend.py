from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

# Configurar a conexão com o banco de dados MySQL
app.config['MYSQL_DATABASE_USER'] = 'seu_usuario'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sua_senha'
app.config['MYSQL_DATABASE_DB'] = 'seu_banco_de_dados'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)

@app.route('/dados', methods=['GET'])
def get_dados():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sua_tabela")
    rows = cursor.fetchall()
    conn.close()

    # Convertendo os dados em um formato JSON-friendly
    results = []
    for row in rows:
        results.append({
            'coluna1': row[0],  # substitua pelos nomes reais das colunas
            'coluna2': row[1],  # substitua pelos nomes reais das colunas
            # adicione mais colunas conforme necessário
        })
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
