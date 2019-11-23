from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/process_data/', methods=['POST'])
def script():
    return str(subprocess.call("sh ./process_data.sh", shell=True))


if __name__ == "__main__":
    app.run()
