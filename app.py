from flask import Flask, render_template, request
import subprocess
import logging

app = Flask(__name__)

logging.basicConfig(filename="sample.log", level=logging.INFO, filemode="w")


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/launch_vm/', methods=['POST'])
def script():
    try:
        return str(subprocess.call("sh ./launch_yaml.sh", shell=True))
    except:
        logging.exception('')


if __name__ == "__main__":
    app.run()
