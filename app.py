from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fcae8ef56d81f9c154bf882f92f219c8'

import views

if __name__ == "__main__":
    app.run(debug=True)
