from flask import Flask

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return '<h1>ola mundo!</h1>'

if __name__ == '__main__':
    app.run()