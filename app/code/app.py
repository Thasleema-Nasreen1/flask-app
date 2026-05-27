from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/db')
def db_test():
    conn = psycopg2.connect(
        host="db",
        database="mydb",
        user="postgres",
        password="postgres"
    )

    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()

    cur.close()
    conn.close()

    return f"Connected to: {version}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
