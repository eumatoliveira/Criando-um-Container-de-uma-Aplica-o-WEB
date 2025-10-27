from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_data():
    try:
        connection = mysql.connector.connect(
            host='db',
            user='usuario',
            password='senha',
            database='minha_base'
        )
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS exemplo (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(50))")
        cursor.execute("INSERT INTO exemplo (nome) VALUES ('Hello Web App')")
        connection.commit()

        cursor.execute("SELECT * FROM exemplo")
        rows = cursor.fetchall()
        return rows
    except Error as e:
        return [("Erro", str(e))]
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route("/")
def index():
    data = get_data()
    return "<br>".join([str(row) for row in data])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
