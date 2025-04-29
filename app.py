from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola Mundo con Flask!'

@app.route('/index')
def hola_adso():
    return '¡Hola - asdfasdfsafsd'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000) 