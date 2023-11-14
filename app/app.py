from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # replace with your MySQL username
app.config['MYSQL_PASSWORD'] = ''  # replace with your MySQL password
app.config['MYSQL_DB'] = 'CineStar'

mysql = MySQL(app)

# Example: Call stored procedure sp_getCines()
@app.route('/cines', methods=['GET'])
def get_cines():
    cur = mysql.connection.cursor()
    cur.callproc('sp_getCines')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

# Example: Call stored procedure sp_getCine(3)
@app.route('/cine/<int:cine_id>', methods=['GET'])
def get_cine(cine_id):
    cur = mysql.connection.cursor()
    cur.callproc('sp_getCine', (cine_id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

# Example: Call stored procedure sp_getCineTarifas(1)
@app.route('/cine/<int:cine_id>/tarifas', methods=['GET'])
def get_cine_tarifas(cine_id):
    cur = mysql.connection.cursor()
    cur.callproc('sp_getCineTarifas', (cine_id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

# Example: Call stored procedure sp_getCinePeliculas(1)
@app.route('/cine/<int:cine_id>/peliculas', methods=['GET'])
def get_cine_peliculas(cine_id):
    cur = mysql.connection.cursor()
    cur.callproc('sp_getCinePeliculas', (cine_id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

# Example: Call stored procedure sp_getPeliculas(1)
@app.route('/peliculas', methods=['GET'])
def get_peliculas():
    cur = mysql.connection.cursor()
    cur.callproc('sp_getPeliculas')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

# Example: Call stored procedure sp_getPelicula(1)
@app.route('/pelicula/<int:pelicula_id>', methods=['GET'])
def get_pelicula(pelicula_id):
    cur = mysql.connection.cursor()
    cur.callproc('sp_getPelicula', (pelicula_id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
