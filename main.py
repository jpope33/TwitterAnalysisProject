from flask import Flask, send_from_directory, jsonify
app = Flask(__name__, static_url_path='', static_folder='client/public')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/data/<path:username>')
def data(username):
    return jsonify(username=username,chartData=[57, 13, 10, 20])

if __name__ == '__main__':
    app.run()
