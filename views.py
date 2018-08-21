from app import app

@app.route("/")
def get_input():
    return "Hello world"
