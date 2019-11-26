from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route("/")
def main():
    return "test" # render_template('index.html')

"""
@app.route('/launch_vm/', methods=['POST'])
def script():
    return str(subprocess.call("sh ./launch_yaml.sh", shell=True))
"""

if __name__ == "__main__":
    app.run()
