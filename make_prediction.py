from azure.servicebus import Message, ServiceBusService

import json
import random


key_name = 'RootManageSharedAccessKey'
key_value = 'Pyh1POvpagtuCZlth3mFiburtkEYQr9M/hJd5Z+JKSA='
service_namespace = 'appForGrid'


class QueueWorker:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.sbs = ServiceBusService(service_namespace,
                                     shared_access_key_name=key_name,
                                     shared_access_key_value=key_value)

    def create_queue(self):
        self.sbs.create_queue(self.queue_name)

    def send_message(self, message):
        # Send a message to the queue
        msg = Message(message)
        self.sbs.send_queue_message(self.queue_name, msg)

    def receive_message(self):
        # Receive the message from the queue
        msg = self.sbs.receive_queue_message(self.queue_name, peek_lock=False)
        return msg.body.decode("utf-8").replace("'", '"')


def make_prediction(user_data):
    days_to_success = int(random.uniform(0, 1000))
    forecast = f'{user_data["name"]}, '
    if days_to_success == 0:
        forecast += "you are an extremely successful person. Congratulations!"
    else:
        forecast += f'stars predict you success in {days_to_success} days'

    return forecast


if __name__ == "__main__":
    client_queue_name = 'client_queue'
    client_queue = QueueWorker(client_queue_name)
    messages = client_queue.receive_message()

    user_data_dict = json.loads(messages)
    prediction = make_prediction(user_data_dict)

    server_queue_name = 'server_queue'
    server_queue = QueueWorker(server_queue_name)
    server_queue.create_queue()
    server_queue.send_message(prediction)


