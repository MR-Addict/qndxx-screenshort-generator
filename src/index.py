import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=os.path.join(os.getcwd(), 'public'))


@app.route('/<path:filename>', methods=["GET"])
def route_static_files(filename):
    return send_from_directory(app.static_folder, filename)


@app.route('/', methods=["GET"])
def route_home_get():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
