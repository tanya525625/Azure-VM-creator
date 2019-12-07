from flask import Flask, render_template, request
import subprocess
import logging
import os

from tools.credentials_parser import CreadentialsParser


app = Flask(__name__)

logging.basicConfig(filename="sample.log", level=logging.INFO)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/get_the_prediction/', methods=['POST'])
def script():
    name = request.form["user_name"]
    age = request.form["user_age"]
    city = request.form["user_city"]

    # data = {
    #     "name": name,
    #     "age": age,
    #     "city": city
    # }
    # C = cookies.SimpleCookie()
    # C["fig"] = "newton"
    # C["sugar"] = "wafer"
    #
    # # C = cookies.SimpleCookie()
    # # C["name"] = "newton"
    # #
    # #
    # url = 'http://127.0.0.1:5000'
    # # r = requests.get(url, headers=)
    # #
    # # session = requests.Session()
    # # cookies = {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}
    #
    # # r = requests.post(url, cookies=cookies)

    return str(subprocess.call("sh ./launch_yaml.sh", shell=True))


if __name__ == "__main__":
    app.run()
    # subscription_id = os.environ['subscription_id']
    # client_id = os.environ['client_id']
    # secret = os.environ['secret']
    # tenant = os.environ['tenant']

