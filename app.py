from flask import Flask, render_template
# Flask-MySQLdb ---> package nme to be used with mysql and we had installed it with the help of pip
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Ebrahimmm@17"
app.config['MYSQL_DB'] = "flaskdbprac"

mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

# Route for inserting the record in database
@app.route('/insert_record')
def insert():
    cur = mysql.connection.cursor()
    query = "INSERT INTO users (id, name) VALUES (%s, %s)"
    values = (5, 'abc')
    cur.execute(query, values)
    mysql.connection.commit()
    cur.close()
    return render_template('index.html')

# Route for updating the record in database
@app.route('/update_record')
def update():
    new_name = "xyz"  # Change the name of ID 5 from abc to xyz
    cur = mysql.connection.cursor()
    update_query = "UPDATE users SET name = %s WHERE id = %s"
    select_query = "SELECT * FROM users"
    cur.execute(select_query)
    data = cur.fetchall()
    values = (new_name, 5)
    cur.execute(update_query, values)
    mysql.connection.commit()
    cur.close()
    return render_template("index.html", data=data)

# Route for deleting the record from database
@app.route('/delete_record')
def delete():
    cur = mysql.connection.cursor()
    delete_query = "DELETE FROM users WHERE id = %s"
    user_id = 5
    # This comma (,) after user_id in values tuple below is important without it, it will throw error
    values = (user_id,)
    cur.execute(delete_query, values)
    mysql.connection.commit()
    select_query = "SELECT * FROM users"
    cur.execute(select_query)
    data = cur.fetchall()
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)