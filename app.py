from flask import Flask, render_template, request

import logging
import json
import os

from tools.AzureQueue import QueueWorker


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
    zodiac_sign = request.form["zodiac_sign"]

    user_data = {
        "name": name,
        "age": age,
        "city": city,
        "zodiac_sign": zodiac_sign
    }
    #
    # # create virtual machine
    os.system("sh ./launch_yaml.sh")

    # sending user's data to the queue
    client_queue_name = 'client_queue'
    client_queue = QueueWorker(client_queue_name)
    client_queue.create_queue()
    client_queue.send_message(json.dumps(user_data))

    os.system("sh ./ansible_mkdir.sh")

    server_queue_name = 'server_queue'
    server_queue = QueueWorker(server_queue_name)
    result = server_queue.receive_message()
    print(result)
    return render_template('prediction.html', res=result)


if __name__ == "__main__":
    app.run()
