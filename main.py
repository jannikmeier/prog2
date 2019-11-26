from flask import Flask

app = Flask("hello")

@app.route('/hello/<name>')
@app.route('/')
def hello(name='World'):
    return "Hallo " + name.capitalize() + "!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)