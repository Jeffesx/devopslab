from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "My name is MR - Robot"

if __name__ == '__main__':
    app.run()