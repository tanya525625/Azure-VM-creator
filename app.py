from flask import Flask, render_template, request

import json
import os

from tools.AzureQueue import QueueWorker


app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


def launch_code_on_vm(data):
    # create virtual machine
    os.system("./configs/ansible-playbook create_vm.yml")

    # sending user's data to the queue
    client_queue_name = 'client_queue'
    client_queue = QueueWorker(client_queue_name)
    client_queue.create_queue()
    client_queue.send_message(json.dumps(data))
    os.system("sh ./scripts/ansible_mkdir.sh")

    # receiving response from the server
    server_queue_name = 'server_queue'
    server_queue = QueueWorker(server_queue_name)
    return server_queue.receive_message()


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
    res = launch_code_on_vm(user_data)
    return render_template('prediction.html', res=res)


if __name__ == "__main__":
    app.run()

