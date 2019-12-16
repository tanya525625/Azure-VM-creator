from flask import Flask, render_template, request, Response

import logging
from time import sleep
import json
import os

from tools.AzureQueue import QueueWorker


app = Flask(__name__)

logging.basicConfig(filename="sample.log", level=logging.INFO)

is_end = False
is_started = False
res = ''

@app.route("/")
def main():
    return render_template('index.html')


def launch_code_on_vm(data):
    global is_started
    global res
    global is_end
    is_started = True
    # create virtual machine
    os.system("ansible-playbook create_vm.yml")

    # sending user's data to the queue
    client_queue_name = 'client_queue'
    client_queue = QueueWorker(client_queue_name)
    client_queue.create_queue()
    client_queue.send_message(json.dumps(data))
    # sleep(60)
    os.system("sh ./ansible_mkdir.sh")

    server_queue_name = 'server_queue'
    server_queue = QueueWorker(server_queue_name)
    res = server_queue.receive_message()
    is_end = True


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

    if not is_started:
        launch_code_on_vm(user_data)

    if is_end == False:
        return Response(status=200)
    else:
        return render_template('prediction.html', res=res)


if __name__ == "__main__":
    app.run()

