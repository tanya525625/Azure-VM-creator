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
    subscription_id = 'c40abeec-914c-4d18-a980-5634a2ee2e4b'
    client_id = 'da5e2b36-ab65-499a-8849-a4d21e198dd7'
    secret = 'b4f8e8a6-bb62-4d47-bc38-b48d26a179df'
    tenant = '213f50d2-073b-4146-bbee-7a25fd629183'

    credentials = CreadentialsParser(subscription_id, client_id, secret, tenant)
    credentials.make_credentials()

    app.run()
    # subscription_id = os.environ['subscription_id']
    # client_id = os.environ['client_id']
    # secret = os.environ['secret']
    # tenant = os.environ['tenant']

