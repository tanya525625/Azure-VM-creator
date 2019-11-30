from flask import Flask, render_template, request
import subprocess
import logging

app = Flask(__name__)

logging.basicConfig(filename="sample.log", level=logging.INFO)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/get_the_prediction/', methods=['POST'])
def script():
    # name = request.form.get('name')
    # logging.debug(name)
    return str(subprocess.call("sh ./launch_yaml.sh", shell=True))


if __name__ == "__main__":
    app.run()
