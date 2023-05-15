from flask import Flask, request

app = Flask(__name__)
app.debug = True

@app.route('/logar', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        return 'Recebeu post! fazer login'
    else:
        return 'Recebeu get! Exibir FORM de login'

if __name__ == '__main__':
    app.run()