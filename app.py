from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/globe')
def globe():
    return render_template('globe.html')


@app.route('/cronus')
def cronus():
    return render_template('cronus.html')


@app.route('/cronus_flipside')
def cronus_flipside():
    return render_template('cronus_flipside.html')


if __name__ == '__main__':
    app.run(debug=True)
